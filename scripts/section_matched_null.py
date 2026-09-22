#!/usr/bin/env python3
"""Gauntlet 4: is the label prefix register a section-mix effect?

Gauntlet 3 left open: L0 is zodiac-heavy / L1 is pharma-heavy, so section and
page-type are confounded. This cycle holds page-type fixed (page-matched pages
only) and asks whether L vs same-section P still shows the register inside
each sufficiently large section.

Inputs (not republished; download from voynich.nu/data/):
    IT2a-n.txt   primary (Takahashi, IVTFF 2.0)
    ZL3b-n.txt   control (Zandbergen-Landini, IVTFF 2.0)

Usage:
    python3 scripts/section_matched_null.py /path/to/IT2a-n.txt [/path/to/ZL3b-n.txt]

Tokenisation: series default (passes 2-8 / gauntlets 2-3).
Output: JSON on stdout. Nothing here is a reading of any token.
"""
from __future__ import annotations

import json
import os
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np

from line_position_null import (  # noqa: E402
    SEED,
    build_tables,
    prefix_block,
    read_loci,
)

N_PERM = 100_000
# Pre-registered load-bearing floors (written before scoring).
MIN_L = 50
MIN_P = 200
MIN_PAGES = 5


def page_sets(recs):
    has_p, has_l = set(), set()
    for r in recs:
        if r["band"] == "P":
            has_p.add(r["page"])
        elif r["band"] == "L":
            has_l.add(r["page"])
    return has_p & has_l, has_l - has_p


def fisher_two_sided(k1, n1, k2, n2):
    from math import comb

    if min(n1, n2) == 0:
        return 1.0
    k_tot = k1 + k2
    n_tot = n1 + n2
    lo = max(0, k_tot - n2)
    hi = min(n1, k_tot)

    def pmf(k):
        return comb(n1, k) * comb(n2, k_tot - k) / comb(n_tot, k_tot)

    p_obs = pmf(k1)
    p = 0.0
    for k in range(lo, hi + 1):
        pk = pmf(k)
        if pk <= p_obs + 1e-15:
            p += pk
    return min(1.0, p)


def page_matched_perm(l_recs, p_recs, n_perm=N_PERM, seed=SEED):
    by_page_l = defaultdict(list)
    by_page_p = defaultdict(list)
    for r in l_recs:
        by_page_l[r["page"]].append(r["tok"])
    for r in p_recs:
        by_page_p[r["page"]].append(r["tok"])
    pages = sorted(set(by_page_l) & set(by_page_p))

    def hits(toks, kind):
        if kind == "qo":
            return sum(1 for t in toks if t.startswith("qo"))
        return sum(1 for t in toks if t.startswith("ok") or t.startswith("ot"))

    obs_qo = sum(hits(by_page_l[p], "qo") for p in pages)
    obs_ok = sum(hits(by_page_l[p], "okot") for p in pages)
    n_l = sum(len(by_page_l[p]) for p in pages)

    page_data = []
    for pg in pages:
        pool = by_page_l[pg] + by_page_p[pg]
        k = len(by_page_l[pg])
        qo = np.fromiter((t.startswith("qo") for t in pool), dtype=np.int8, count=len(pool))
        ok = np.fromiter(
            (t.startswith("ok") or t.startswith("ot") for t in pool),
            dtype=np.int8,
            count=len(pool),
        )
        page_data.append((len(pool), k, qo, ok))

    rng = np.random.default_rng(seed)
    null_qo = np.zeros(n_perm, dtype=np.int32)
    null_ok = np.zeros(n_perm, dtype=np.int32)
    for i in range(n_perm):
        q = o = 0
        for n_pool, k, qo, ok in page_data:
            idx = rng.choice(n_pool, size=k, replace=False)
            q += int(qo[idx].sum())
            o += int(ok[idx].sum())
        null_qo[i] = q
        null_ok[i] = o

    return {
        "pages": len(pages),
        "n_l": n_l,
        "obs_qo": int(obs_qo),
        "obs_okot": int(obs_ok),
        "null_qo_mean": float(null_qo.mean()),
        "null_okot_mean": float(null_ok.mean()),
        "null_qo_min": int(null_qo.min()) if n_perm else None,
        "null_qo_max": int(null_qo.max()) if n_perm else None,
        "null_okot_min": int(null_ok.min()) if n_perm else None,
        "null_okot_max": int(null_ok.max()) if n_perm else None,
        "p_le_qo": float((int((null_qo <= obs_qo).sum()) + 1) / (n_perm + 1)),
        "p_ge_okot": float((int((null_ok >= obs_ok).sum()) + 1) / (n_perm + 1)),
    }


def section_verdict(l_block, p_block, perm):
    """Pre-registered per-section rule (gauntlet-4 note §2).

    NULL (register survives inside section):
        L qo- <= 3.0% AND L ok+ot >= 22.0% AND both perm p < 0.001
    HIT (section confound kills the law here):
        L qo- >= 5.0% OR L ok+ot <= 18.0% OR either perm p > 0.01
    PARTIAL: anything else.
    SKIP: floors not met.
    """
    lq = l_block["qo"]["rate"]
    lo = l_block["ok+ot"]["rate"]
    if lq is None or lo is None:
        return "SKIP"
    null_ok = (
        lq <= 0.03
        and lo >= 0.22
        and perm["p_le_qo"] < 0.001
        and perm["p_ge_okot"] < 0.001
    )
    hit = lq >= 0.05 or lo <= 0.18 or perm["p_le_qo"] > 0.01 or perm["p_ge_okot"] > 0.01
    if null_ok:
        return "NULL"
    if hit:
        return "HIT"
    return "PARTIAL"


def score(path, zl=False):
    loci = read_loci(path, zl=zl)
    recs = build_tables(loci)
    both, label_only = page_sets(recs)

    p_all = [r for r in recs if r["band"] == "P"]
    l_all = [r for r in recs if r["band"] == "L"]
    l1 = [r for r in l_all if r["page"] in both]
    p1 = [r for r in p_all if r["page"] in both]

    calib = {
        "n_p": len(p_all),
        "n_l": len(l_all),
        "n_types_p": len({r["tok"] for r in p_all}),
        "n_types_l": len({r["tok"] for r in l_all}),
        "n_pages_both": len(both),
        "n_pages_label_only": len(label_only),
        "n_l1": len(l1),
        "n_p1": len(p1),
        "sect_L_all": dict(Counter(r["sect"] for r in l_all)),
        "sect_P_all": dict(Counter(r["sect"] for r in p_all)),
        "sect_L1": dict(Counter(r["sect"] for r in l1)),
    }

    # Candidate sections = those with any L1. Load-bearing decided by floors.
    sections = sorted({r["sect"] for r in l1})
    by_section = {}
    load_bearing = []
    secondary = []

    for sect in sections:
        l_s = [r for r in l1 if r["sect"] == sect]
        # Same-section P on the same pages that carry those L tokens.
        pages_s = {r["page"] for r in l_s}
        p_s = [r for r in p1 if r["page"] in pages_s and r["sect"] == sect]
        # Also record same-page P regardless of sect (sanity; pages are mono-sect).
        p_page = [r for r in p1 if r["page"] in pages_s]

        l_tok = [r["tok"] for r in l_s]
        p_tok = [r["tok"] for r in p_s]
        l_block = prefix_block(l_tok)
        p_block = prefix_block(p_tok)

        floors_met = (
            len(l_s) >= MIN_L
            and len(p_s) >= MIN_P
            and len(pages_s) >= MIN_PAGES
        )
        role = "load_bearing" if floors_met else "secondary"
        if floors_met:
            load_bearing.append(sect)
        else:
            secondary.append(sect)

        if len(l_s) == 0 or len(p_s) == 0:
            perm = {
                "pages": 0,
                "n_l": len(l_s),
                "obs_qo": 0,
                "obs_okot": 0,
                "null_qo_mean": None,
                "null_okot_mean": None,
                "null_qo_min": None,
                "null_qo_max": None,
                "null_okot_min": None,
                "null_okot_max": None,
                "p_le_qo": 1.0,
                "p_ge_okot": 1.0,
                "skipped": True,
            }
            verdict = "SKIP"
        else:
            # Distinct seed per section so sections are independent draws.
            seed = SEED + 17 * (ord(sect[0]) if sect else 0)
            perm = page_matched_perm(l_s, p_s, n_perm=N_PERM, seed=seed)
            perm["skipped"] = False
            verdict = section_verdict(l_block, p_block, perm) if floors_met else "SECONDARY"

        # Fisher L vs P rates (descriptive).
        lq_k = l_block["qo"]["k"]
        lo_k = l_block["ok+ot"]["k"]
        pq_k = p_block["qo"]["k"]
        po_k = p_block["ok+ot"]["k"]
        fisher = {
            "qo": fisher_two_sided(lq_k, len(l_tok), pq_k, len(p_tok)) if p_tok else None,
            "ok+ot": fisher_two_sided(lo_k, len(l_tok), po_k, len(p_tok)) if p_tok else None,
        }

        by_section[sect] = {
            "role": role,
            "floors_met": floors_met,
            "n_pages": len(pages_s),
            "pages": sorted(pages_s),
            "n_l": len(l_tok),
            "n_p_same_sect": len(p_tok),
            "n_p_same_pages_any_sect": len(p_page),
            "L": l_block,
            "P": p_block,
            "perm": perm,
            "fisher_L_vs_P": fisher,
            "verdict": verdict,
        }

    # Overall gauntlet verdict from load-bearing sections only.
    lb_verdicts = [by_section[s]["verdict"] for s in load_bearing]
    if not load_bearing:
        overall = "VOID_NO_LOAD_BEARING"
    elif any(v == "HIT" for v in lb_verdicts):
        overall = "HIT"
    elif all(v == "NULL" for v in lb_verdicts):
        overall = "NULL"
    else:
        overall = "PARTIAL"

    # Negative control: odd/even L1 tokens (should NOT show a P-to-L sized gap).
    l1_tok = [r["tok"] for r in l1]
    odd = l1_tok[0::2]
    even = l1_tok[1::2]
    odd_b = prefix_block(odd)
    even_b = prefix_block(even)

    return {
        "file": os.path.basename(path),
        "zl": zl,
        "calibration": calib,
        "floors": {"MIN_L": MIN_L, "MIN_P": MIN_P, "MIN_PAGES": MIN_PAGES},
        "load_bearing_sections": load_bearing,
        "secondary_sections": secondary,
        "by_section": by_section,
        "odd_even_L1_control": {"odd": odd_b, "even": even_b},
        "overall_verdict": overall,
        "n_perm": N_PERM,
        "seed_base": SEED,
    }


def main():
    if len(sys.argv) < 2:
        print("usage: section_matched_null.py IT2a-n.txt [ZL3b-n.txt]", file=sys.stderr)
        sys.exit(2)
    it_path = sys.argv[1]
    zl_path = sys.argv[2] if len(sys.argv) > 2 else None
    out = {"IT": score(it_path, zl=False)}
    if zl_path:
        out["ZL"] = score(zl_path, zl=True)
    # Compound: HIT if either is HIT; NULL only if both NULL on their load-bearing sets.
    it_v = out["IT"]["overall_verdict"]
    zl_v = out.get("ZL", {}).get("overall_verdict")
    if zl_v is None:
        compound = it_v
    elif "HIT" in (it_v, zl_v):
        compound = "HIT"
    elif it_v == "NULL" and zl_v == "NULL":
        compound = "NULL"
    else:
        compound = "PARTIAL"
    out["compound_verdict"] = compound
    json.dump(out, sys.stdout, indent=2, sort_keys=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
