#!/usr/bin/env python3
"""Gauntlet 6: does section T HIT-shape survive a pre-registered word-like length floor?

Gauntlet 4 recorded section T as HIT-shaped (qo- 6.8%, ok+ot 1.7%) but secondary
only (2 both-band pages; floors unmet). This cycle does NOT promote T to
load-bearing. It asks whether the HIT shape is single-glyph / short-token noise
or survives among word-like L tokens under an explicit tiny-n rule.

Inputs (not republished; download from voynich.nu/data/):
    IT2a-n.txt   primary
    ZL3b-n.txt   control

Usage:
    python3 scripts/section_t_tiny_null.py /path/to/IT2a-n.txt [/path/to/ZL3b-n.txt]

Tokenisation: series default. Output: JSON on stdout. Not a reading.
"""
from __future__ import annotations

import json
import os
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from line_position_null import (  # noqa: E402
    build_tables,
    prefix_block,
    read_loci,
)

# Pre-registered (written before scoring).
SECT = "T"
MIN_LEN_PRIMARY = 3          # word-like floor
MIN_LEN_SENSITIVITY = 4      # reported, not verdict-bearing
MIN_N_FILTERED = 10          # tiny-n floor; below -> TINY_UNDERPOWERED
# T never becomes load-bearing here (gauntlet-4 floors: pages>=5 unmet).


def page_sets(recs):
    has_p, has_l = set(), set()
    for r in recs:
        if r["band"] == "P":
            has_p.add(r["page"])
        elif r["band"] == "L":
            has_l.add(r["page"])
    return has_p & has_l, has_l - has_p


def tiny_verdict(l_block):
    """Explicit tiny-n rule for section T after length filter.

    TINY_HIT:   qo- >= 5.0% AND ok+ot <= 18.0%  (HIT shape survives word-like)
    TINY_NULL:  qo- <= 3.0% AND ok+ot >= 22.0%  (word-like T looks like register)
    TINY_NOISE: n < MIN_N_FILTERED
    TINY_PARTIAL: anything else
    """
    n = l_block["n"]
    if n < MIN_N_FILTERED:
        return "TINY_UNDERPOWERED"
    lq = l_block["qo"]["rate"]
    lo = l_block["ok+ot"]["rate"]
    if lq is None or lo is None:
        return "TINY_UNDERPOWERED"
    if lq >= 0.05 and lo <= 0.18:
        return "TINY_HIT"
    if lq <= 0.03 and lo >= 0.22:
        return "TINY_NULL"
    return "TINY_PARTIAL"


def score_slice(recs, both, min_len):
    l_all = [r for r in recs if r["band"] == "L" and r["sect"] == SECT]
    # page-matched both-band pages only (same scope as gauntlet 4 secondary T)
    l1 = [r for r in l_all if r["page"] in both]
    p1 = [
        r
        for r in recs
        if r["band"] == "P" and r["sect"] == SECT and r["page"] in {x["page"] for x in l1}
    ]
    l_f = [r for r in l1 if len(r["tok"]) >= min_len]
    p_f = [r for r in p1 if len(r["tok"]) >= min_len]  # descriptive only
    l_tok = [r["tok"] for r in l_f]
    p_tok = [r["tok"] for r in p_f]
    l_block = prefix_block(l_tok)
    p_block = prefix_block(p_tok) if p_tok else prefix_block([])
    pages = sorted({r["page"] for r in l_f})
    by_page = {}
    for pg in pages:
        toks = [r["tok"] for r in l_f if r["page"] == pg]
        by_page[pg] = {
            "n": len(toks),
            "tokens": toks,
            "ltypes": dict(Counter(r["ltype"] for r in l_f if r["page"] == pg)),
            "L": prefix_block(toks),
        }
    return {
        "min_len": min_len,
        "n_l_raw_page_matched": len(l1),
        "n_l_filtered": len(l_f),
        "n_p_same_pages_filtered": len(p_f),
        "n_pages": len(pages),
        "pages": pages,
        "ltypes": dict(Counter(r["ltype"] for r in l_f)),
        "pos": dict(Counter(r["pos"] for r in l_f)),
        "mean_len": round(sum(len(t) for t in l_tok) / len(l_tok), 3) if l_tok else None,
        "qo_tokens": [t for t in l_tok if t.startswith("qo")],
        "okot_tokens": [t for t in l_tok if t.startswith("ok") or t.startswith("ot")],
        "all_l_tokens": l_tok,
        "L": l_block,
        "P_descriptive": p_block,
        "by_page": by_page,
        "verdict": tiny_verdict(l_block),
    }


def score(path, zl=False):
    loci = read_loci(path, zl=zl)
    recs = build_tables(loci)
    both, label_only = page_sets(recs)

    # Unfiltered calibration (matches gauntlet-4 secondary T scope).
    l_raw = [r for r in recs if r["band"] == "L" and r["sect"] == SECT and r["page"] in both]
    p_raw = [
        r
        for r in recs
        if r["band"] == "P"
        and r["sect"] == SECT
        and r["page"] in {x["page"] for x in l_raw}
    ]
    calib = {
        "n_p_corpus": sum(1 for r in recs if r["band"] == "P"),
        "n_l_corpus": sum(1 for r in recs if r["band"] == "L"),
        "n_pages_both": len(both),
        "sect_T_pages_all": sorted({r["page"] for r in recs if r["sect"] == SECT}),
        "sect_T_L_raw_page_matched": prefix_block([r["tok"] for r in l_raw]),
        "sect_T_P_raw_page_matched": prefix_block([r["tok"] for r in p_raw]),
        "sect_T_n_pages_with_L": len({r["page"] for r in l_raw}),
        "sect_T_pages_with_L": sorted({r["page"] for r in l_raw}),
        "sect_T_ltypes_raw": dict(Counter(r["ltype"] for r in l_raw)),
        "sect_T_len_hist_raw": dict(Counter(len(r["tok"]) for r in l_raw)),
        "note": "Section T remains secondary; pages < 5. Not load-bearing.",
    }

    primary = score_slice(recs, both, MIN_LEN_PRIMARY)
    sensitivity = score_slice(recs, both, MIN_LEN_SENSITIVITY)
    # Also report discarded short tokens (noise inventory).
    short = [r for r in l_raw if len(r["tok"]) < MIN_LEN_PRIMARY]
    short_inv = {
        "n": len(short),
        "tokens": [r["tok"] for r in short],
        "pages": dict(Counter(r["page"] for r in short)),
        "L": prefix_block([r["tok"] for r in short]) if short else None,
    }

    return {
        "file": os.path.basename(path),
        "zl": zl,
        "calibration": calib,
        "pre_registered": {
            "section": SECT,
            "min_len_primary": MIN_LEN_PRIMARY,
            "min_len_sensitivity": MIN_LEN_SENSITIVITY,
            "min_n_filtered": MIN_N_FILTERED,
            "load_bearing": False,
            "decision_rule": {
                "TINY_HIT": "qo>=5% AND ok+ot<=18% after len>=3",
                "TINY_NULL": "qo<=3% AND ok+ot>=22% after len>=3",
                "TINY_UNDERPOWERED": f"n_filtered < {MIN_N_FILTERED}",
                "TINY_PARTIAL": "else",
            },
        },
        "short_discarded": short_inv,
        "primary_len_ge_3": primary,
        "sensitivity_len_ge_4": sensitivity,
        "overall_verdict": primary["verdict"],
    }


def main():
    if len(sys.argv) < 2:
        print("usage: section_t_tiny_null.py IT2a-n.txt [ZL3b-n.txt]", file=sys.stderr)
        sys.exit(2)
    it_path = sys.argv[1]
    zl_path = sys.argv[2] if len(sys.argv) > 2 else None
    out = {"IT": score(it_path, zl=False)}
    if zl_path:
        out["ZL"] = score(zl_path, zl=True)
    it_v = out["IT"]["overall_verdict"]
    zl_v = out.get("ZL", {}).get("overall_verdict")
    if zl_v is None:
        compound = it_v
    elif it_v == "TINY_HIT" or zl_v == "TINY_HIT":
        # HIT if either shows surviving HIT shape (conservative for attack success)
        compound = "TINY_HIT"
    elif it_v == "TINY_NULL" and zl_v == "TINY_NULL":
        compound = "TINY_NULL"
    elif "UNDERPOWERED" in (it_v, zl_v):
        compound = "TINY_UNDERPOWERED" if it_v == zl_v else "TINY_PARTIAL"
    else:
        compound = "TINY_PARTIAL"
    out["compound_verdict"] = compound
    json.dump(out, sys.stdout, indent=2, sort_keys=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
