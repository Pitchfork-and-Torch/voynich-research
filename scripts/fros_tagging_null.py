#!/usr/bin/env python3
"""Gauntlet 9: does ZL-only page fRos explain the g8 IT/ZL length disagreement?

Gauntlet 8: IT STILL_WOUNDED (L0 sole len>=3 ok+ot 12.5%) vs ZL LENGTH_EXPLAINS
(24.7%). Inventory showed ZL page `fRos` (rosette foldout aggregate) carries 126
wordlike sole L0 tokens that IT does not have as L at all. This cycle
pre-registers excluding that ZL-only page and re-scores the g8 contrast.

Inputs (not republished; download from voynich.nu/data/):
    IT2a-n.txt   primary
    ZL3b-n.txt   control

Usage:
    python3 scripts/fros_tagging_null.py /path/to/IT2a-n.txt [/path/to/ZL3b-n.txt]

Tokenisation: series default. Output: JSON on stdout. Not a reading of fRos.
"""
from __future__ import annotations

import json
import os
import sys
from collections import Counter
from math import comb

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from line_position_null import (  # noqa: E402
    build_tables,
    prefix_block,
    read_loci,
)

NAME_TYPES = ("Lf", "Lc", "Lp")
MIN_LEN = 3
MIN_N = 30
ZL_ONLY_PAGE = "fRos"


def fisher_two_sided(k1, n1, k2, n2):
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


def block_for(recs):
    toks = [r["tok"] for r in recs]
    b = prefix_block(toks)
    b["mean_len"] = round(sum(len(t) for t in toks) / len(toks), 3) if toks else None
    b["qo_tokens"] = sorted({t for t in toks if t.startswith("qo")})
    return b


def g8_verdict(l0_b, name_b, fisher_okot):
    """Same numeric rule as gauntlet 8."""
    if l0_b["n"] < MIN_N or name_b["n"] < MIN_N:
        return "UNDERPOWERED"
    lo = l0_b["ok+ot"]["rate"]
    no = name_b["ok+ot"]["rate"]
    if lo <= 0.15 and no >= 0.25 and fisher_okot < 0.01:
        return "STILL_WOUNDED"
    if lo >= 0.22:
        return "LENGTH_EXPLAINS"
    return "PARTIAL"


def arms(recs, exclude_pages=frozenset()):
    l0 = [
        r
        for r in recs
        if r["band"] == "L"
        and r["ltype"] == "L0"
        and r["pos"] == "sole"
        and len(r["tok"]) >= MIN_LEN
        and r["page"] not in exclude_pages
    ]
    name = [
        r
        for r in recs
        if r["band"] == "L"
        and r["ltype"] in NAME_TYPES
        and r["pos"] == "sole"
        and len(r["tok"]) >= MIN_LEN
        and r["page"] not in exclude_pages
    ]
    return l0, name


def score_pair(recs, exclude_pages=frozenset()):
    l0, name = arms(recs, exclude_pages)
    l0_b = block_for(l0)
    name_b = block_for(name)
    fisher = {
        "ok+ot": fisher_two_sided(
            l0_b["ok+ot"]["k"], l0_b["n"], name_b["ok+ot"]["k"], name_b["n"]
        ),
        "qo": fisher_two_sided(l0_b["qo"]["k"], l0_b["n"], name_b["qo"]["k"], name_b["n"]),
    }
    return {
        "exclude_pages": sorted(exclude_pages),
        "L0_sole_wordlike": l0_b,
        "NAME_sole_wordlike": name_b,
        "fisher_L0_vs_NAME": fisher,
        "l0_pages": Counter(r["page"] for r in l0).most_common(12),
        "verdict": g8_verdict(l0_b, name_b, fisher["ok+ot"]),
    }


def score(path, zl=False):
    loci = read_loci(path, zl=zl)
    recs = build_tables(loci)
    pages = sorted({r["page"] for r in recs})
    has_fros = ZL_ONLY_PAGE in pages
    fros = [r for r in recs if r["page"] == ZL_ONLY_PAGE]
    fros_inv = None
    if fros:
        fros_l0 = [
            r
            for r in fros
            if r["band"] == "L"
            and r["ltype"] == "L0"
            and r["pos"] == "sole"
            and len(r["tok"]) >= MIN_LEN
        ]
        fros_inv = {
            "n_tokens": len(fros),
            "bands": dict(Counter(r["band"] for r in fros)),
            "ltypes": dict(Counter(r["ltype"] for r in fros)),
            "sect": dict(Counter(r["sect"] for r in fros)),
            "L0_sole_wordlike": block_for(fros_l0),
            "note": "ZL aggregate rosette page; absent from IT page list.",
        }

    baseline = score_pair(recs, exclude_pages=frozenset())
    excl = score_pair(recs, exclude_pages=frozenset({ZL_ONLY_PAGE}))

    return {
        "file": os.path.basename(path),
        "zl": zl,
        "has_fRos_page": has_fros,
        "fRos_inventory": fros_inv,
        "pre_registered": {
            "zl_only_page": ZL_ONLY_PAGE,
            "min_len": MIN_LEN,
            "min_n": MIN_N,
            "g8_rule_reused": True,
            "decision_rule": {
                "TAGGING_EXPLAINS_DISAGREE": (
                    "IT unchanged STILL_WOUNDED; ZL flips from LENGTH_EXPLAINS "
                    "to STILL_WOUNDED after excluding fRos"
                ),
                "DISAGREE_REMAINS": "ZL still not STILL_WOUNDED after exclusion",
                "VOID": "IT lacks fRos and ZL lacks fRos (nothing to test)",
            },
        },
        "baseline_all_pages": baseline,
        "exclude_fRos": excl,
    }


def main():
    if len(sys.argv) < 2:
        print("usage: fros_tagging_null.py IT2a-n.txt [ZL3b-n.txt]", file=sys.stderr)
        sys.exit(2)
    it_path = sys.argv[1]
    zl_path = sys.argv[2] if len(sys.argv) > 2 else None
    out = {"IT": score(it_path, zl=False)}
    if zl_path:
        out["ZL"] = score(zl_path, zl=True)

    it_base = out["IT"]["baseline_all_pages"]["verdict"]
    it_excl = out["IT"]["exclude_fRos"]["verdict"]
    zl = out.get("ZL")
    if zl is None or not zl["has_fRos_page"]:
        compound = "VOID"
    else:
        zl_base = zl["baseline_all_pages"]["verdict"]
        zl_excl = zl["exclude_fRos"]["verdict"]
        # Pre-registered: tagging explains iff IT stays STILL_WOUNDED and
        # ZL moves from LENGTH_EXPLAINS -> STILL_WOUNDED when fRos dropped.
        if (
            it_base == "STILL_WOUNDED"
            and it_excl == "STILL_WOUNDED"
            and zl_base == "LENGTH_EXPLAINS"
            and zl_excl == "STILL_WOUNDED"
        ):
            compound = "TAGGING_EXPLAINS_DISAGREE"
        else:
            compound = "DISAGREE_REMAINS"
    out["compound_verdict"] = compound
    json.dump(out, sys.stdout, indent=2, sort_keys=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
