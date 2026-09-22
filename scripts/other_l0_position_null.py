#!/usr/bin/env python3
"""Gauntlet 7: is OTHER/L0 weak ok+ot a sole/short confound or uniform?

Gauntlet 2 §5 recorded: inside multi-word labels ok+ot sits on the first token;
later tokens are L0-heavy — type and position confounded, not separated.
Gauntlet 5 wounded ok+ot enrichment for OTHER/L0 (~10%). This cycle separates
sole vs initial vs later inside L0/OTHER, and short vs word-like inside sole.

Inputs (not republished; download from voynich.nu/data/):
    IT2a-n.txt   primary
    ZL3b-n.txt   control

Usage:
    python3 scripts/other_l0_position_null.py /path/to/IT2a-n.txt [/path/to/ZL3b-n.txt]

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

# Pre-registered families / floors (written before scoring).
OTHER_TYPES = ("L0", "La", "Lx")
NAME_TYPES = ("Lf", "Lc", "Lp")
MIN_SOLE = 50
MIN_INITIAL = 20
SHORT_MAX = 2          # len <= 2 = glyph-ish
WORDLIKE_MIN = 3       # len >= 3


def block_for(recs):
    toks = [r["tok"] for r in recs]
    b = prefix_block(toks)
    b["mean_len"] = round(sum(len(t) for t in toks) / len(toks), 3) if toks else None
    b["qo_tokens"] = [t for t in toks if t.startswith("qo")]
    return b


def split_pos(recs):
    sole = [r for r in recs if r["pos"] == "sole"]
    initial = [r for r in recs if r["pos"] == "initial"]
    later = [r for r in recs if r["pos"] in ("medial", "final")]
    return sole, initial, later


def confound_verdict(sole_b, init_b, sole_n, init_n):
    """Pre-registered OTHER/L0 position confound rule.

    Floors: sole n>=50, initial n>=20; else UNDERPOWERED.

    CONFOUND_SUPPORTED:
        L0/OTHER initial ok+ot >= 18% AND sole ok+ot <= 12%
        (weakness is not uniform; first-token of multi-word is richer)

    UNIFORM_WEAK:
        initial ok+ot <= 12% AND sole ok+ot <= 12%
        (OTHER lacks enrichment even at label-initial)

    CONFOUND_PARTIAL: anything else with floors met.

    Does NOT touch the NAME law.
    """
    if sole_n < MIN_SOLE or init_n < MIN_INITIAL:
        return "UNDERPOWERED"
    so = sole_b["ok+ot"]["rate"]
    io = init_b["ok+ot"]["rate"]
    if so is None or io is None:
        return "UNDERPOWERED"
    if io >= 0.18 and so <= 0.12:
        return "CONFOUND_SUPPORTED"
    if io <= 0.12 and so <= 0.12:
        return "UNIFORM_WEAK"
    return "CONFOUND_PARTIAL"


def length_verdict(short_b, word_b, short_n, word_n):
    """Inside L0 sole: is weakness short-glyph noise?

    LENGTH_CONFOUND: wordlike (len>=3) ok+ot >= 18% AND short (len<=2) ok+ot <= 5%
    SOLE_STILL_WEAK: wordlike ok+ot <= 12% (even word-like soles lack enrichment)
    LENGTH_PARTIAL: else (need short_n>=20 and word_n>=20)
    """
    if short_n < 20 or word_n < 20:
        return "LENGTH_UNDERPOWERED"
    swo = short_b["ok+ot"]["rate"]
    wwo = word_b["ok+ot"]["rate"]
    if swo is None or wwo is None:
        return "LENGTH_UNDERPOWERED"
    if wwo >= 0.18 and swo <= 0.05:
        return "LENGTH_CONFOUND"
    if wwo <= 0.12:
        return "SOLE_STILL_WEAK"
    return "LENGTH_PARTIAL"


def score(path, zl=False):
    loci = read_loci(path, zl=zl)
    recs = build_tables(loci)
    L = [r for r in recs if r["band"] == "L"]
    other = [r for r in L if r["ltype"] in OTHER_TYPES]
    l0 = [r for r in L if r["ltype"] == "L0"]
    name = [r for r in L if r["ltype"] in NAME_TYPES]

    o_sole, o_init, o_later = split_pos(other)
    l0_sole, l0_init, l0_later = split_pos(l0)
    n_sole, n_init, n_later = split_pos(name)

    l0_short = [r for r in l0_sole if len(r["tok"]) <= SHORT_MAX]
    l0_word = [r for r in l0_sole if len(r["tok"]) >= WORDLIKE_MIN]

    blocks = {
        "OTHER_all": block_for(other),
        "OTHER_sole": block_for(o_sole),
        "OTHER_initial": block_for(o_init),
        "OTHER_later": block_for(o_later),
        "L0_all": block_for(l0),
        "L0_sole": block_for(l0_sole),
        "L0_initial": block_for(l0_init),
        "L0_later": block_for(l0_later),
        "L0_sole_short_len_le_2": block_for(l0_short),
        "L0_sole_wordlike_len_ge_3": block_for(l0_word),
        "NAME_sole_contrast": block_for(n_sole),
        "NAME_initial_contrast": block_for(n_init),
        "NAME_later_contrast": block_for(n_later),
    }

    # Primary confound test uses L0 (bulk of OTHER); OTHER family reported too.
    v_l0 = confound_verdict(blocks["L0_sole"], blocks["L0_initial"], len(l0_sole), len(l0_init))
    v_other = confound_verdict(
        blocks["OTHER_sole"], blocks["OTHER_initial"], len(o_sole), len(o_init)
    )
    v_len = length_verdict(
        blocks["L0_sole_short_len_le_2"],
        blocks["L0_sole_wordlike_len_ge_3"],
        len(l0_short),
        len(l0_word),
    )

    # Compound within file: position confound is the named leftover.
    # Length is secondary diagnostic.
    return {
        "file": os.path.basename(path),
        "zl": zl,
        "calibration": {
            "n_l": len(L),
            "n_other": len(other),
            "n_l0": len(l0),
            "n_name": len(name),
            "other_ltypes": dict(Counter(r["ltype"] for r in other)),
            "l0_sects": dict(Counter(r["sect"] for r in l0)),
            "l0_pos": dict(Counter(r["pos"] for r in l0)),
            "l0_sole_len_hist": dict(Counter(len(r["tok"]) for r in l0_sole)),
        },
        "pre_registered": {
            "other_types": list(OTHER_TYPES),
            "min_sole": MIN_SOLE,
            "min_initial": MIN_INITIAL,
            "short_max": SHORT_MAX,
            "wordlike_min": WORDLIKE_MIN,
            "decision_rule_position": {
                "CONFOUND_SUPPORTED": "initial ok+ot>=18% AND sole ok+ot<=12%",
                "UNIFORM_WEAK": "initial ok+ot<=12% AND sole ok+ot<=12%",
                "CONFOUND_PARTIAL": "else (floors met)",
                "UNDERPOWERED": f"sole n<{MIN_SOLE} or initial n<{MIN_INITIAL}",
            },
            "decision_rule_length_inside_sole": {
                "LENGTH_CONFOUND": "wordlike ok+ot>=18% AND short ok+ot<=5%",
                "SOLE_STILL_WEAK": "wordlike ok+ot<=12%",
                "LENGTH_PARTIAL": "else",
            },
        },
        "blocks": blocks,
        "ns": {
            "OTHER_sole": len(o_sole),
            "OTHER_initial": len(o_init),
            "OTHER_later": len(o_later),
            "L0_sole": len(l0_sole),
            "L0_initial": len(l0_init),
            "L0_later": len(l0_later),
            "L0_sole_short": len(l0_short),
            "L0_sole_wordlike": len(l0_word),
            "NAME_sole": len(n_sole),
            "NAME_initial": len(n_init),
        },
        "verdict_L0_position": v_l0,
        "verdict_OTHER_position": v_other,
        "verdict_L0_sole_length": v_len,
        "overall_verdict": v_l0,  # named leftover = L0 position split
    }


def main():
    if len(sys.argv) < 2:
        print("usage: other_l0_position_null.py IT2a-n.txt [ZL3b-n.txt]", file=sys.stderr)
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
    elif "UNIFORM_WEAK" in (it_v, zl_v) and "CONFOUND_SUPPORTED" in (it_v, zl_v):
        compound = "CONFOUND_PARTIAL"
    else:
        compound = "CONFOUND_PARTIAL"
    out["compound_verdict"] = compound
    # Also compound length diagnostic
    it_l = out["IT"]["verdict_L0_sole_length"]
    zl_l = out.get("ZL", {}).get("verdict_L0_sole_length")
    out["compound_length_verdict"] = it_l if zl_l is None or it_l == zl_l else "LENGTH_PARTIAL"
    json.dump(out, sys.stdout, indent=2, sort_keys=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
