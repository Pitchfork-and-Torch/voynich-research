#!/usr/bin/env python3
"""Gauntlet 5: is the qo- ban / ok+ot enrichment uniform across label locus types?

The series holds "qo- banned on labels" at corpus level, but the rollup already
inventories that all clean Lf/Lc/Lp tokens are qo- = 0 while the nine known
qo- labels sit on L0 / Ls / Lz / Ln / Lt. This cycle pre-registers that split
and asks whether ok+ot enrichment also survives inside the herbal/pharma
name-like family alone, and whether the soft "any L" ban should be narrowed.

Inputs (not republished; download from voynich.nu/data/):
    IT2a-n.txt   primary
    ZL3b-n.txt   control

Usage:
    python3 scripts/label_locus_type_null.py /path/to/IT2a-n.txt [/path/to/ZL3b-n.txt]

Tokenisation: series default. Output: JSON on stdout. Not a reading.
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

# Pre-registered families (written before scoring). IVTFF locus-type letter 2.
FAMILIES = {
    "NAME": ("Lf", "Lc", "Lp"),          # plant / container / plant-caption
    "FIGURE": ("Ln", "Lt"),              # nymph / tub-tube (balneo)
    "ZODIAC": ("Lz",),                   # zodiac labels
    "STARISH": ("Ls",),                  # star / circular diagram labels
    "OTHER": ("L0", "La", "Lx"),         # stand-alone / rare / unknown
}


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


def page_sets(recs):
    has_p, has_l = set(), set()
    for r in recs:
        if r["band"] == "P":
            has_p.add(r["page"])
        elif r["band"] == "L":
            has_l.add(r["page"])
    return has_p & has_l, has_l - has_p


def page_matched_perm(l_recs, p_recs, n_perm=N_PERM, seed=SEED):
    by_page_l = defaultdict(list)
    by_page_p = defaultdict(list)
    for r in l_recs:
        by_page_l[r["page"]].append(r["tok"])
    for r in p_recs:
        by_page_p[r["page"]].append(r["tok"])
    pages = sorted(set(by_page_l) & set(by_page_p))
    if not pages:
        return {
            "pages": 0,
            "n_l": 0,
            "obs_qo": 0,
            "obs_okot": 0,
            "null_qo_mean": None,
            "null_okot_mean": None,
            "p_le_qo": 1.0,
            "p_ge_okot": 1.0,
        }

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
        "null_qo_min": int(null_qo.min()),
        "null_qo_max": int(null_qo.max()),
        "null_okot_min": int(null_ok.min()),
        "null_okot_max": int(null_ok.max()),
        "p_le_qo": float((int((null_qo <= obs_qo).sum()) + 1) / (n_perm + 1)),
        "p_ge_okot": float((int((null_ok >= obs_ok).sum()) + 1) / (n_perm + 1)),
    }


def family_of(ltype: str) -> str:
    for fam, types in FAMILIES.items():
        if ltype in types:
            return fam
    return "UNMAPPED"


def score(path, zl=False):
    loci = read_loci(path, zl=zl)
    recs = build_tables(loci)
    both, label_only = page_sets(recs)

    p_all = [r for r in recs if r["band"] == "P"]
    l_all = [r for r in recs if r["band"] == "L"]
    p_tok = [r["tok"] for r in p_all]
    p_block = prefix_block(p_tok)

    by_ltype = {}
    for lt, n in Counter(r["ltype"] for r in l_all).most_common():
        toks = [r["tok"] for r in l_all if r["ltype"] == lt]
        by_ltype[lt] = {
            "family": family_of(lt),
            **prefix_block(toks),
            "qo_tokens": sorted({t for t in toks if t.startswith("qo")}),
        }

    by_family = {}
    for fam, types in FAMILIES.items():
        recs_f = [r for r in l_all if r["ltype"] in types]
        toks = [r["tok"] for r in recs_f]
        # Page-matched subset vs same-page P (where possible).
        l1 = [r for r in recs_f if r["page"] in both]
        pages = {r["page"] for r in l1}
        p1 = [r for r in p_all if r["page"] in pages]
        seed = SEED + 31 * sum(ord(c) for c in fam)
        perm = page_matched_perm(l1, p1, n_perm=N_PERM, seed=seed) if l1 and p1 else {
            "pages": 0, "n_l": len(l1), "obs_qo": 0, "obs_okot": 0,
            "null_qo_mean": None, "null_okot_mean": None,
            "p_le_qo": 1.0, "p_ge_okot": 1.0,
        }
        block = prefix_block(toks)
        by_family[fam] = {
            "ltypes": list(types),
            "n": len(toks),
            "n_page_matched": len(l1),
            "n_pages_matched": len(pages),
            "prefix": block,
            "perm_vs_same_page_P": perm,
            "fisher_qo_vs_P": fisher_two_sided(
                block["qo"]["k"], len(toks), p_block["qo"]["k"], len(p_tok)
            )
            if toks
            else None,
            "fisher_okot_vs_P": fisher_two_sided(
                block["ok+ot"]["k"], len(toks), p_block["ok+ot"]["k"], len(p_tok)
            )
            if toks
            else None,
            "qo_tokens": sorted({t for t in toks if t.startswith("qo")}),
            "sect_mix": dict(Counter(r["sect"] for r in recs_f)),
        }

    # Pre-registered decision (gauntlet-5 note §2):
    # NAME family is the load-bearing claim for the *strict* ban.
    name = by_family["NAME"]["prefix"]
    name_perm = by_family["NAME"]["perm_vs_same_page_P"]
    # STRICT_NULL: NAME qo- == 0 AND NAME ok+ot >= 22% AND (if page-matched n>=50)
    #   perm p_le_qo < 0.001 and p_ge_okot < 0.001
    # STRICT_HIT: NAME qo- >= 1% OR NAME ok+ot <= 18% OR perm p > 0.01 when n_pm >= 50
    n_pm = by_family["NAME"]["n_page_matched"]
    qo_rate = name["qo"]["rate"] or 0.0
    ok_rate = name["ok+ot"]["rate"] or 0.0
    if n_pm >= 50:
        strict_null = (
            qo_rate == 0.0
            and ok_rate >= 0.22
            and name_perm["p_le_qo"] < 0.001
            and name_perm["p_ge_okot"] < 0.001
        )
        strict_hit = (
            qo_rate >= 0.01
            or ok_rate <= 0.18
            or name_perm["p_le_qo"] > 0.01
            or name_perm["p_ge_okot"] > 0.01
        )
    else:
        strict_null = qo_rate == 0.0 and ok_rate >= 0.22
        strict_hit = qo_rate >= 0.01 or ok_rate <= 0.18

    if strict_null:
        name_verdict = "STRICT_NULL"
    elif strict_hit:
        name_verdict = "STRICT_HIT"
    else:
        name_verdict = "STRICT_PARTIAL"

    # Soft-ban status: any non-NAME qo- exists?
    non_name_qo = []
    for fam in ("FIGURE", "ZODIAC", "STARISH", "OTHER"):
        non_name_qo.extend(by_family[fam]["qo_tokens"])
    soft_ban_status = {
        "corpus_L_qo_tokens": sorted(
            {t for r in l_all for t in [r["tok"]] if t.startswith("qo")}
        ),
        "non_NAME_qo_tokens": sorted(set(non_name_qo)),
        "NAME_qo_tokens": by_family["NAME"]["qo_tokens"],
        "narrowing_supported": len(by_family["NAME"]["qo_tokens"]) == 0
        and len(set(non_name_qo)) > 0,
    }

    return {
        "file": os.path.basename(path),
        "zl": zl,
        "calibration": {
            "n_p": len(p_all),
            "n_l": len(l_all),
            "n_types_p": len({r["tok"] for r in p_all}),
            "n_types_l": len({r["tok"] for r in l_all}),
            "P_prefix": p_block,
        },
        "families_pre_registered": {k: list(v) for k, v in FAMILIES.items()},
        "by_ltype": by_ltype,
        "by_family": by_family,
        "NAME_verdict": name_verdict,
        "soft_ban_status": soft_ban_status,
        "n_perm": N_PERM,
        "seed_base": SEED,
    }


def main():
    if len(sys.argv) < 2:
        print("usage: label_locus_type_null.py IT2a-n.txt [ZL3b-n.txt]", file=sys.stderr)
        sys.exit(2)
    it_path = sys.argv[1]
    zl_path = sys.argv[2] if len(sys.argv) > 2 else None
    out = {"IT": score(it_path, zl=False)}
    if zl_path:
        out["ZL"] = score(zl_path, zl=True)
    it_v = out["IT"]["NAME_verdict"]
    zl_v = out.get("ZL", {}).get("NAME_verdict")
    if zl_v is None:
        compound = it_v
    elif "HIT" in (it_v, zl_v):
        compound = "STRICT_HIT"
    elif it_v == "STRICT_NULL" and zl_v == "STRICT_NULL":
        compound = "STRICT_NULL"
    else:
        compound = "STRICT_PARTIAL"
    out["compound_NAME_verdict"] = compound
    # Narrowing is supported only if BOTH files agree NAME has 0 qo- and some
    # non-NAME qo- exists in IT (primary inventory).
    out["compound_narrowing_supported"] = (
        out["IT"]["soft_ban_status"]["narrowing_supported"]
        and len(out["IT"]["soft_ban_status"]["NAME_qo_tokens"]) == 0
        and (
            zl_v is None
            or len(out["ZL"]["soft_ban_status"]["NAME_qo_tokens"]) == 0
        )
    )
    json.dump(out, sys.stdout, indent=2, sort_keys=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
