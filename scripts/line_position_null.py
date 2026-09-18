#!/usr/bin/env python3
"""Gauntlet 2: is the label prefix register a line-position effect?

Scores the surviving "label register" law (qo- suppressed, ok-/ot- enriched
on labels) against a positional null: labels are one-word text units, so
compare them with the first word of every paragraph line, page-matched.

Inputs (not republished; download from voynich.nu/data/):
    IT2a-n.txt   primary running text (Takahashi, IVTFF 2.0)
    ZL3b-n.txt   control (Zandbergen-Landini, IVTFF 2.0)

Usage:
    python3 scripts/line_position_null.py /path/to/IT2a-n.txt [/path/to/ZL3b-n.txt]

Tokenisation is the series default (passes 2-8):
    '.' is a word break; '<->' is a word space; all other <...> markup is
    stripped; a token must contain at least one letter; '?' is kept.
    P = loci whose type contains 'P'; L = loci whose type contains 'L'.
    ZL only: uncertain commas are joined; [a:b] takes the first reading;
    {..} ligature braces expand to their contents.

Output is JSON on stdout. Nothing here is a reading of any token.
"""
import json
import math
import re
import sys

import numpy as np
from collections import Counter, defaultdict

PREFIXES = ("qo", "ok", "ot")
SEED = 408
N_PERM = 100000


# ----------------------------------------------------------------------------
# parsing
# ----------------------------------------------------------------------------
def read_loci(path, zl=False):
    """Yield dicts: page, locus, locator, ltype, header, tokens, para_start."""
    page, hdr = None, {}
    out = []
    for raw in open(path, encoding="latin-1"):
        line = raw.rstrip("\n")
        if not line or line.startswith("#"):
            continue
        if line.startswith("/"):
            # Orphan continuations (before any locus) used to IndexError on out[-1].
            if out:
                out[-1]["raw"] += line[1:]
            continue
        head, _, rest = line.partition(">")
        head = head + ">"
        m = re.match(r"<(f[^,>]+)>$", head)
        if m:
            page = m.group(1)
            hm = re.search(r"<!\s*([^>]*)>", rest)
            hdr = {}
            if hm:
                for kv in hm.group(1).split():
                    if "=" in kv:
                        k, v = kv.split("=", 1)
                        hdr[k.lstrip("$")] = v
            continue
        m = re.match(r"<([^,>]+),(.)(..)>$", head)
        if not m:
            continue
        out.append(
            {
                "page": page,
                "locus": m.group(1),
                "locator": m.group(2),
                "ltype": m.group(3),
                "hdr": dict(hdr),
                "raw": rest.strip(),
            }
        )
    for loc in out:
        raw = loc["raw"]
        loc["para_start"] = "<%>" in raw
        loc["para_end"] = "<$>" in raw
        loc["tokens"] = tokenise(raw, zl=zl)
    return out


def tokenise(raw, zl=False):
    s = raw.replace("<->", " ")
    s = re.sub(r"<[^>]*>", "", s)
    if zl:
        s = re.sub(r"\[([^\]:]*)(?::[^\]]*)+\]", r"\1", s)
        s = re.sub(r"\{([^}]*)\}", r"\1", s)
        s = s.replace(",", "")
    s = s.replace(".", " ")
    toks = [t for t in s.split() if re.search(r"[A-Za-z]", t)]
    return toks


# ----------------------------------------------------------------------------
# token tables
# ----------------------------------------------------------------------------
def build_tables(loci):
    """Return list of token records with position class."""
    recs = []
    for loc in loci:
        band = "P" if "P" in loc["ltype"] else ("L" if "L" in loc["ltype"] else None)
        if band is None:
            continue
        toks = loc["tokens"]
        n = len(toks)
        for i, t in enumerate(toks):
            if n == 1:
                pos = "sole"
            elif i == 0:
                pos = "initial"
            elif i == n - 1:
                pos = "final"
            else:
                pos = "medial"
            recs.append(
                {
                    "band": band,
                    "page": loc["page"],
                    "locus": loc["locus"],
                    "ltype": loc["ltype"],
                    "lang": loc["hdr"].get("L", "?"),
                    "sect": loc["hdr"].get("I", "?"),
                    "tok": t,
                    "pos": pos,
                    "para_start": loc["para_start"],
                    "nline": n,
                }
            )
    return recs


def rate(tokens, prefix):
    n = len(tokens)
    k = sum(1 for t in tokens if t.startswith(prefix))
    return k, n


def wilson(k, n, z=1.96):
    if n == 0:
        return (None, None)
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (round(c - h, 4), round(c + h, 4))


def prefix_block(tokens):
    n = len(tokens)
    out = {"n": n, "types": len(set(tokens))}
    for pfx in PREFIXES:
        k, _ = rate(tokens, pfx)
        out[pfx] = {"k": k, "rate": round(k / n, 4) if n else None, "ci95": wilson(k, n)}
    k = out["ok"]["k"] + out["ot"]["k"]
    out["ok+ot"] = {"k": k, "rate": round(k / n, 4) if n else None, "ci95": wilson(k, n)}
    if n:
        out["mean_len"] = round(sum(len(t) for t in tokens) / n, 3)
    return out


def first_glyph_dist(tokens):
    c = Counter()
    for t in tokens:
        c[t[0]] += 1
    n = len(tokens)
    return {g: round(v / n, 4) for g, v in sorted(c.items(), key=lambda x: -x[1])} if n else {}


def last_glyph_dist(tokens):
    c = Counter(t[-1] for t in tokens)
    n = len(tokens)
    return {g: round(v / n, 4) for g, v in sorted(c.items(), key=lambda x: -x[1])} if n else {}


# ----------------------------------------------------------------------------
# matched nulls
# ----------------------------------------------------------------------------
def page_matched_expectation(l_recs, p_pool_by_page, prefix):
    """Expected prefix rate if each L token were a random draw from the
    P pool on its own page. Pages with an empty pool are skipped and counted."""
    num = 0.0
    used = 0
    skipped = 0
    for r in l_recs:
        pool = p_pool_by_page.get(r["page"], [])
        if not pool:
            skipped += 1
            continue
        k, n = rate(pool, prefix)
        num += k / n
        used += 1
    return (round(num / used, 4) if used else None), used, skipped


def page_permutation(l_recs, p_pool_by_page, hit, n_perm, rng):
    """Within-page relabelling null. For each page the pool is the L tokens
    plus the chosen P tokens on that page; |L| tokens are drawn without
    replacement. The hit count per page is hypergeometric, so the null is
    sampled exactly with numpy rather than by shuffling."""
    by_page = defaultdict(list)
    for r in l_recs:
        by_page[r["page"]].append(r["tok"])
    total = np.zeros(n_perm, dtype=np.int64)
    for pg, ltoks in by_page.items():
        pool = ltoks + list(p_pool_by_page.get(pg, []))
        n_good = sum(1 for t in pool if hit(t))
        n_bad = len(pool) - n_good
        total += rng.hypergeometric(n_good, n_bad, len(ltoks), size=n_perm)
    obs_k = sum(1 for r in l_recs if hit(r["tok"]))
    n_l = len(l_recs)
    ge = int((total >= obs_k).sum())
    le = int((total <= obs_k).sum())
    return {
        "obs_k": obs_k,
        "n_L": n_l,
        "obs_rate": round(obs_k / n_l, 4),
        "null_mean_rate": round(float(total.mean()) / n_l, 4),
        "null_sd_rate": round(float(total.std()) / n_l, 4),
        "null_min_k": int(total.min()),
        "null_max_k": int(total.max()),
        "p_ge": round((ge + 1) / (n_perm + 1), 6),
        "p_le": round((le + 1) / (n_perm + 1), 6),
        "n_perm": n_perm,
    }


def length_matched_expectation(l_tokens, p_tokens, prefix):
    by_len = defaultdict(list)
    for t in p_tokens:
        by_len[len(t)].append(t)
    num, used, skipped = 0.0, 0, 0
    for t in l_tokens:
        pool = by_len.get(len(t))
        if not pool:
            skipped += 1
            continue
        k, n = rate(pool, prefix)
        num += k / n
        used += 1
    return (round(num / used, 4) if used else None), used, skipped


# ----------------------------------------------------------------------------
# main
# ----------------------------------------------------------------------------
def analyse(path, zl=False, label=""):
    loci = read_loci(path, zl=zl)
    recs = build_tables(loci)
    P = [r for r in recs if r["band"] == "P"]
    L = [r for r in recs if r["band"] == "L"]
    ptok = [r["tok"] for r in P]
    ltok = [r["tok"] for r in L]

    res = {"file": path, "corpus": {"P": prefix_block(ptok), "L": prefix_block(ltok)}}

    # position classes in P
    pos = {}
    for cls in ("initial", "medial", "final", "sole"):
        pos[cls] = prefix_block([r["tok"] for r in P if r["pos"] == cls])
    pos["initial_para_start"] = prefix_block(
        [r["tok"] for r in P if r["pos"] in ("initial", "sole") and r["para_start"]]
    )
    pos["initial_not_para_start"] = prefix_block(
        [r["tok"] for r in P if r["pos"] in ("initial", "sole") and not r["para_start"]]
    )
    pos["initial_or_sole"] = prefix_block([r["tok"] for r in P if r["pos"] in ("initial", "sole")])
    pos["not_initial"] = prefix_block([r["tok"] for r in P if r["pos"] in ("medial", "final")])
    res["P_by_position"] = pos

    # labels: locus-initial vs all
    res["L_by_position"] = {
        "sole": prefix_block([r["tok"] for r in L if r["pos"] == "sole"]),
        "initial_or_sole": prefix_block([r["tok"] for r in L if r["pos"] in ("initial", "sole")]),
        "not_initial": prefix_block([r["tok"] for r in L if r["pos"] in ("medial", "final")]),
    }
    res["L_by_type"] = {
        lt: prefix_block([r["tok"] for r in L if r["ltype"] == lt])
        for lt in sorted(set(r["ltype"] for r in L))
    }

    # calibration: known line effects must reproduce
    res["calibration"] = {
        "first_glyph_P_initial": first_glyph_dist([r["tok"] for r in P if r["pos"] in ("initial", "sole")]),
        "first_glyph_P_not_initial": first_glyph_dist([r["tok"] for r in P if r["pos"] in ("medial", "final")]),
        "first_glyph_L": first_glyph_dist(ltok),
        "last_glyph_P_final": last_glyph_dist([r["tok"] for r in P if r["pos"] in ("final", "sole")]),
        "last_glyph_P_not_final": last_glyph_dist([r["tok"] for r in P if r["pos"] in ("initial", "medial")]),
        "last_glyph_L": last_glyph_dist(ltok),
    }
    # negative control: split P by locus parity; should show no prefix gap
    even = [r["tok"] for i, r in enumerate(P) if int(re.sub(r"\D", "", r["locus"].split(".")[-1]) or 0) % 2 == 0]
    odd = [r["tok"] for i, r in enumerate(P) if int(re.sub(r"\D", "", r["locus"].split(".")[-1]) or 0) % 2 == 1]
    res["calibration"]["negative_control_even_lines"] = prefix_block(even)
    res["calibration"]["negative_control_odd_lines"] = prefix_block(odd)

    # by language
    res["P_by_lang"] = {}
    for lang in sorted(set(r["lang"] for r in P)):
        sub = [r for r in P if r["lang"] == lang]
        res["P_by_lang"][lang] = {
            "all": prefix_block([r["tok"] for r in sub]),
            "initial_or_sole": prefix_block([r["tok"] for r in sub if r["pos"] in ("initial", "sole")]),
            "not_initial": prefix_block([r["tok"] for r in sub if r["pos"] in ("medial", "final")]),
        }
    res["L_by_lang"] = {
        lang: prefix_block([r["tok"] for r in L if r["lang"] == lang])
        for lang in sorted(set(r["lang"] for r in L))
    }

    # page-matched pools
    pool_all = defaultdict(list)
    pool_init = defaultdict(list)
    pool_noninit = defaultdict(list)
    for r in P:
        pool_all[r["page"]].append(r["tok"])
        if r["pos"] in ("initial", "sole"):
            pool_init[r["page"]].append(r["tok"])
        else:
            pool_noninit[r["page"]].append(r["tok"])

    label_pages = sorted(set(r["page"] for r in L))
    res["label_pages"] = {
        "n_pages_with_L": len(label_pages),
        "n_pages_with_L_and_P": sum(1 for pg in label_pages if pool_all.get(pg)),
        "L_tokens_on_pages_with_P": sum(1 for r in L if pool_all.get(r["page"])),
        "L_tokens_on_pages_with_line_initial_P": sum(1 for r in L if pool_init.get(r["page"])),
    }
    L_matched = [r for r in L if pool_init.get(r["page"])]
    res["page_matched"] = {
        "L_used": prefix_block([r["tok"] for r in L_matched]),
        "P_all_same_pages": prefix_block([t for pg in label_pages for t in pool_all.get(pg, [])]),
        "P_initial_same_pages": prefix_block([t for pg in label_pages for t in pool_init.get(pg, [])]),
        "P_not_initial_same_pages": prefix_block([t for pg in label_pages for t in pool_noninit.get(pg, [])]),
    }
    exp = {}
    for pfx in ("qo", "ok", "ot"):
        e_all = page_matched_expectation(L_matched, pool_all, pfx)
        e_init = page_matched_expectation(L_matched, pool_init, pfx)
        e_non = page_matched_expectation(L_matched, pool_noninit, pfx)
        exp[pfx] = {
            "L_obs_rate": round(rate([r["tok"] for r in L_matched], pfx)[0] / len(L_matched), 4),
            "exp_if_random_P_same_page": e_all[0],
            "exp_if_random_line_initial_P_same_page": e_init[0],
            "exp_if_random_non_initial_P_same_page": e_non[0],
        }
    res["page_matched"]["expectations"] = exp

    # permutation tests: L vs line-initial P, L vs all P, L vs non-initial P
    nrng = np.random.default_rng(SEED)
    hits = {
        "qo": lambda t: t.startswith("qo"),
        "ok": lambda t: t.startswith("ok"),
        "ot": lambda t: t.startswith("ot"),
        "ok+ot": lambda t: t.startswith("ok") or t.startswith("ot"),
    }
    perm = {}
    for name, hit in hits.items():
        perm[name] = {
            "vs_line_initial_P": page_permutation(L_matched, pool_init, hit, N_PERM, nrng),
            "vs_all_P": page_permutation(L_matched, pool_all, hit, N_PERM, nrng),
            "vs_non_initial_P": page_permutation(L_matched, pool_noninit, hit, N_PERM, nrng),
        }
    res["permutation"] = perm

    # length-matched expectation (corpus-wide P; and line-initial P)
    p_init_tokens = [r["tok"] for r in P if r["pos"] in ("initial", "sole")]
    lm = {}
    for pfx in ("qo", "ok", "ot"):
        lm[pfx] = {
            "L_obs_rate": round(rate(ltok, pfx)[0] / len(ltok), 4),
            "exp_length_matched_all_P": length_matched_expectation(ltok, ptok, pfx)[0],
            "exp_length_matched_line_initial_P": length_matched_expectation(ltok, p_init_tokens, pfx)[0],
        }
    res["length_matched"] = lm

    # sanity
    res["sanity"] = {
        "P_tokens": len(ptok),
        "P_types": len(set(ptok)),
        "L_tokens": len(ltok),
        "L_types": len(set(ltok)),
        "n_P_loci": len([l for l in loci if "P" in l["ltype"]]),
        "n_L_loci": len([l for l in loci if "L" in l["ltype"]]),
    }
    return res


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    out = {"IT": analyse(sys.argv[1], zl=False)}
    if len(sys.argv) > 2:
        out["ZL"] = analyse(sys.argv[2], zl=True)
    json.dump(out, sys.stdout, indent=1)
    print()


if __name__ == "__main__":
    main()
