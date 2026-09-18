#!/usr/bin/env python3
"""Gauntlet 3: is the label prefix register a label-only-page effect?

Scores the surviving label register (qo- suppressed, ok-/ot- enriched) against
the section confound left open by gauntlet 2: 406 of 1,038 L tokens sit on
pages with no P text at all (mostly zodiac). If the register collapses when
those pages are removed, the law is a page-type effect, not a label lexicon.

Inputs (not republished; download from voynich.nu/data/):
    IT2a-n.txt   primary running text (Takahashi, IVTFF 2.0)
    ZL3b-n.txt   control (Zandbergen-Landini, IVTFF 2.0)

Usage:
    python3 scripts/label_only_page_null.py /path/to/IT2a-n.txt [/path/to/ZL3b-n.txt]

Tokenisation is the series default (passes 2-8), same as line_position_null.py.
Output is JSON on stdout. Nothing here is a reading of any token.
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
    first_glyph_dist,
    prefix_block,
    read_loci,
)

N_PERM = 100_000
N_BOOT = 20_000


def tokens_of(recs, pred):
    return [r["tok"] for r in recs if pred(r)]


def page_sets(recs):
    has_p = set()
    has_l = set()
    for r in recs:
        if r["band"] == "P":
            has_p.add(r["page"])
        elif r["band"] == "L":
            has_l.add(r["page"])
    both = has_p & has_l
    label_only = has_l - has_p
    return both, label_only, has_p, has_l


def fisher_two_sided(k1, n1, k2, n2):
    """Exact Fisher 2x2 two-sided p via hypergeometric enumeration."""
    # table: [[k1, n1-k1], [k2, n2-k2]]
    # Fix margins: row1=n1, row2=n2, col1=k1+k2
    from math import comb

    if min(n1, n2) == 0:
        return 1.0
    k_tot = k1 + k2
    n_tot = n1 + n2
    lo = max(0, k_tot - n2)
    hi = min(n1, k_tot)
    # probability mass for each k in row1
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
    """Within-page hypergeometric draws: |L| from (L∪P) per page, sum prefix hits."""
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

    # Precompute prefix flags per page pool for speed.
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
        "null_qo_min": int(null_qo.min()),
        "null_qo_max": int(null_qo.max()),
        "null_okot_min": int(null_ok.min()),
        "null_okot_max": int(null_ok.max()),
        "p_le_qo": float(np.mean(null_qo <= obs_qo)),
        "p_ge_okot": float(np.mean(null_ok >= obs_ok)),
    }


def pooled_perm_rate_diff(toks_a, toks_b, kind, n_perm=N_BOOT, seed=SEED):
    """Pooled permutation two-sided p for rate_a - rate_b under exchangeability."""
    def rate(toks):
        if not toks:
            return 0.0
        if kind == "qo":
            return sum(t.startswith("qo") for t in toks) / len(toks)
        return sum(t.startswith("ok") or t.startswith("ot") for t in toks) / len(toks)

    a = list(toks_a)
    b = list(toks_b)
    na, nb = len(a), len(b)
    obs = rate(a) - rate(b)
    pool = np.array(a + b, dtype=object)
    rng = np.random.default_rng(seed + 1)
    diffs = np.empty(n_perm)
    for i in range(n_perm):
        rng.shuffle(pool)
        diffs[i] = rate(pool[:na].tolist()) - rate(pool[na:].tolist())
    p = float(np.mean(np.abs(diffs) >= abs(obs) - 1e-15)) if n_perm else 1.0
    return {
        "obs_diff": round(obs, 4),
        "perm_mean": round(float(diffs.mean()), 4),
        "perm_p_two_sided": p,
        "ci95_under_null": [
            round(float(np.quantile(diffs, 0.025)), 4),
            round(float(np.quantile(diffs, 0.975)), 4),
        ],
    }


def score(path, zl=False):
    loci = read_loci(path, zl=zl)
    recs = build_tables(loci)
    both, label_only, has_p, has_l = page_sets(recs)

    p_all = tokens_of(recs, lambda r: r["band"] == "P")
    l_all = tokens_of(recs, lambda r: r["band"] == "L")
    l0_recs = [r for r in recs if r["band"] == "L" and r["page"] in label_only]
    l1_recs = [r for r in recs if r["band"] == "L" and r["page"] in both]
    p1_recs = [r for r in recs if r["band"] == "P" and r["page"] in both]
    l0 = [r["tok"] for r in l0_recs]
    l1 = [r["tok"] for r in l1_recs]
    p1 = [r["tok"] for r in p1_recs]

    sect_l0 = Counter(r["sect"] for r in l0_recs)
    sect_l1 = Counter(r["sect"] for r in l1_recs)

    # Calibration: parse totals (IT known)
    calib = {
        "n_p": len(p_all),
        "n_l": len(l_all),
        "n_types_p": len(set(p_all)),
        "n_types_l": len(set(l_all)),
        "n_pages_both": len(both),
        "n_pages_label_only": len(label_only),
        "n_l0": len(l0),
        "n_l1": len(l1),
    }

    # C2: odd/even negative control on all L (stable index, not hash())
    l_toks_ordered = [r["tok"] for r in recs if r["band"] == "L"]
    odd = l_toks_ordered[1::2]
    even = l_toks_ordered[0::2]

    perm = page_matched_perm(l1_recs, p1_recs)
    perm_ok = pooled_perm_rate_diff(l0, l1, "okot")
    perm_qo = pooled_perm_rate_diff(l0, l1, "qo")

    def okot_k(toks):
        return sum(1 for t in toks if t.startswith("ok") or t.startswith("ot"))

    def qo_k(toks):
        return sum(1 for t in toks if t.startswith("qo"))

    fisher_ok = fisher_two_sided(okot_k(l0), len(l0), okot_k(l1), len(l1))
    fisher_qo = fisher_two_sided(qo_k(l0), len(l0), qo_k(l1), len(l1))

    # Pre-registered verdict on L1 (page-matched) vs same-page P.
    l1_block = prefix_block(l1)
    p1_block = prefix_block(p1)
    l0_block = prefix_block(l0)
    l_all_block = prefix_block(l_all)
    p_all_block = prefix_block(p_all)

    l1_qo = l1_block["qo"]["rate"]
    l1_ok = l1_block["ok+ot"]["rate"]
    p_le = perm["p_le_qo"]
    p_ge = perm["p_ge_okot"]

    # HIT (confound absorbs law): page-matched L no longer label-shaped
    hit = (l1_qo is not None and l1_qo >= 0.05) or (
        l1_ok is not None and l1_ok <= 0.18
    ) or (p_le > 0.01) or (p_ge > 0.01)
    # NULL (confound rejected): L1 still label-shaped vs same-page P
    null = (
        l1_qo is not None
        and l1_qo <= 0.03
        and l1_ok is not None
        and l1_ok >= 0.22
        and p_le < 0.001
        and p_ge < 0.001
    )
    if null and not hit:
        verdict = "NULL"
    elif hit and not null:
        verdict = "HIT"
    else:
        verdict = "PARTIAL"

    return {
        "source": path,
        "zl": zl,
        "calibration": calib,
        "section_counts_l0": dict(sect_l0),
        "section_counts_l1": dict(sect_l1),
        "bands": {
            "P_all": p_all_block,
            "L_all": l_all_block,
            "L0_label_only_pages": l0_block,
            "L1_page_matched": l1_block,
            "P_page_matched": p1_block,
        },
        "l0_vs_l1": {
            "fisher_p_qo": fisher_qo,
            "fisher_p_okot": fisher_ok,
            "perm_qo": perm_qo,
            "perm_okot": perm_ok,
        },
        "page_matched_perm": perm,
        "verdict": verdict,
        "verdict_inputs": {
            "l1_qo_rate": l1_qo,
            "l1_okot_rate": l1_ok,
            "perm_p_le_qo": p_le,
            "perm_p_ge_okot": p_ge,
            "hit_clause": hit,
            "null_clause": null,
        },
        "odd_even_L_control": {
            "odd": prefix_block(odd),
            "even": prefix_block(even),
        },
        "first_glyph_l0": first_glyph_dist(l0),
        "first_glyph_l1": first_glyph_dist(l1),
    }


def main(argv):
    if len(argv) < 2:
        print("usage: label_only_page_null.py IT2a-n.txt [ZL3b-n.txt]", file=sys.stderr)
        return 2
    it_path = argv[1]
    out = {"IT": score(it_path, zl=False)}
    if len(argv) >= 3:
        out["ZL"] = score(argv[2], zl=True)
    # IT calibration gates for series lock
    cal = out["IT"]["calibration"]
    out["gates"] = {
        "C1_totals": cal["n_p"] == 34486 and cal["n_l"] == 1038,
        "C1_split": cal["n_l0"] == 406 and cal["n_l1"] == 632,
        "C1_pages": cal["n_pages_both"] == 36 and cal["n_pages_label_only"] == 16,
    }
    json.dump(out, sys.stdout, indent=2, sort_keys=True)
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
