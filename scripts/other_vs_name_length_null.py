#!/usr/bin/env python3
"""Gauntlet 8: after length floor, does OTHER/L0 sole still lack ok+ot vs NAME sole?

Gauntlet 7 left LENGTH_PARTIAL on IT (wordlike L0 sole ok+ot 12.5%) and
LENGTH_CONFOUND on ZL (wordlike 24.7%). This cycle asks the direct contrast:
word-like (len>=3) L0 sole vs word-like NAME sole. If OTHER remains poor when
length-matched against NAME, the gauntlet-5 wound is not just short-glyph noise.

Inputs (not republished; download from voynich.nu/data/):
    IT2a-n.txt   primary
    ZL3b-n.txt   control

Usage:
    python3 scripts/other_vs_name_length_null.py /path/to/IT2a-n.txt [/path/to/ZL3b-n.txt]

Tokenisation: series default. Output: JSON on stdout. Not a reading.
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
MIN_N = 30  # per arm


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


def verdict(l0_b, name_b, n_l0, n_name, fisher_okot):
    """Pre-registered length-matched contrast.

    Floors: both arms n >= 30.

    STILL_WOUNDED (OTHER lacks enrichment even length-matched):
        L0_sole_wordlike ok+ot <= 15% AND NAME_sole_wordlike ok+ot >= 25%
        AND fisher two-sided p < 0.01

    LENGTH_EXPLAINS (wound was short-glyph / length):
        L0_sole_wordlike ok+ot >= 22%

    PARTIAL: else / floors unmet -> UNDERPOWERED
    """
    if n_l0 < MIN_N or n_name < MIN_N:
        return "UNDERPOWERED"
    lo = l0_b["ok+ot"]["rate"]
    no = name_b["ok+ot"]["rate"]
    if lo is None or no is None:
        return "UNDERPOWERED"
    if lo <= 0.15 and no >= 0.25 and fisher_okot < 0.01:
        return "STILL_WOUNDED"
    if lo >= 0.22:
        return "LENGTH_EXPLAINS"
    return "PARTIAL"


def score(path, zl=False):
    loci = read_loci(path, zl=zl)
    recs = build_tables(loci)
    L = [r for r in recs if r["band"] == "L"]
    l0_sole = [
        r
        for r in L
        if r["ltype"] == "L0" and r["pos"] == "sole" and len(r["tok"]) >= MIN_LEN
    ]
    name_sole = [
        r
        for r in L
        if r["ltype"] in NAME_TYPES and r["pos"] == "sole" and len(r["tok"]) >= MIN_LEN
    ]
    # also all-pos wordlike for descriptive
    l0_word = [r for r in L if r["ltype"] == "L0" and len(r["tok"]) >= MIN_LEN]
    name_word = [r for r in L if r["ltype"] in NAME_TYPES and len(r["tok"]) >= MIN_LEN]

    l0_b = block_for(l0_sole)
    name_b = block_for(name_sole)
    fisher = {
        "ok+ot": fisher_two_sided(
            l0_b["ok+ot"]["k"], l0_b["n"], name_b["ok+ot"]["k"], name_b["n"]
        ),
        "qo": fisher_two_sided(l0_b["qo"]["k"], l0_b["n"], name_b["qo"]["k"], name_b["n"]),
    }
    v = verdict(l0_b, name_b, l0_b["n"], name_b["n"], fisher["ok+ot"])

    return {
        "file": os.path.basename(path),
        "zl": zl,
        "pre_registered": {
            "min_len": MIN_LEN,
            "min_n_per_arm": MIN_N,
            "arms": "L0 sole len>=3 vs NAME (Lf/Lc/Lp) sole len>=3",
            "decision_rule": {
                "STILL_WOUNDED": "L0 ok+ot<=15% AND NAME ok+ot>=25% AND fisher p<0.01",
                "LENGTH_EXPLAINS": "L0 ok+ot>=22%",
                "PARTIAL": "else",
                "UNDERPOWERED": f"either arm n<{MIN_N}",
            },
        },
        "calibration": {
            "n_l": len(L),
            "l0_sole_wordlike_pages_top": Counter(r["page"] for r in l0_sole).most_common(12),
            "l0_sole_wordlike_sects": dict(Counter(r["sect"] for r in l0_sole)),
            "name_sole_wordlike_sects": dict(Counter(r["sect"] for r in name_sole)),
            "l0_all_wordlike": block_for(l0_word),
            "name_all_wordlike": block_for(name_word),
        },
        "L0_sole_wordlike": l0_b,
        "NAME_sole_wordlike": name_b,
        "fisher_L0_vs_NAME": fisher,
        "overall_verdict": v,
    }


def main():
    if len(sys.argv) < 2:
        print("usage: other_vs_name_length_null.py IT2a-n.txt [ZL3b-n.txt]", file=sys.stderr)
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
    elif it_v == zl_v:
        compound = it_v
    else:
        # Disagree across transliterations -> PARTIAL (do not overclaim wound)
        compound = "PARTIAL"
    out["compound_verdict"] = compound
    json.dump(out, sys.stdout, indent=2, sort_keys=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
