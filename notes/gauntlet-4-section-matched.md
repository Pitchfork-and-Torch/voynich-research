# Voynich gauntlet 4 - label prefix register vs section-matched null (not a translation)

**For:** Pitchfork-and-Torch
**Date:** 22 Sep 2026 (ET)
**Status:** corpus-wide structural test. No folio opened. **NULL** for the attack on the two load-bearing sections (pharma `P`, balneo `B`). **No verified full translation of Beinecke MS 408 exists.** Nothing below is a decipherment. Every gloss is marked **HYPOTHESIS**. No plant is identified. No language is identified. EVA letters are not phonemes. Do not grind `keerodal`. Do not open balneo as a folio walk.

Sources on disk this cycle: `/workspace/voynich-src/IT2a-n.txt`, `ZL3b-n.txt` (same public versions as the series; not republished). Scorer: `scripts/section_matched_null.py`. Results: `results/gauntlet-4-section-matched.json`.

---

## 0. Why this test

Gauntlet 3 rejected the label-only-page confound and left one named falsifier open (gauntlet-3 §7.1): **a section-matched design**. L0 is zodiac-heavy; L1 is pharma-heavy. If the register collapses when L is compared to same-section P on the same pages, the held law is a *section mix* artifact, not a label lexicon that survives inside a single section.

README / rollup still say idle / no folio without a named gate. This cycle names the gate gauntlet 3 already wrote down. No folio opens.

---

## 1. Source transcription (citation + URL)

| Item | Value |
|---|---|
| File | `IT2a-n.txt` (IVTFF 2.0) |
| Transliteration | Takeshi Takahashi, LSI extract, code **IT** |
| Alphabet | Basic EVA (Eva-T) |
| Version | 2a of 2023-02-02, modified 2025-06-25 |
| URL | https://voynich.nu/data/IT2a-n.txt |
| Control | `ZL3b-n.txt` (Zandbergen-Landini, version 3b of 2025-05-13) |
| Format | https://www.voynich.nu/software/ivtt/IVTFF_format.pdf |
| Label background | https://voynich.nu/extra/labels.html |
| Manuscript | Yale Beinecke MS 408 |
| Prior | `notes/gauntlet-3-label-only-page-null.md` §7.1 |

**Tokenisation:** series default (passes 2-8 / gauntlets 2-3). `.` = word break; `<->` = space; other `<>` stripped; ≥1 letter; `?` kept. P = locus type contains `P`; L = contains `L`. ZL: commas joined, `[a:b]` first alt, `{..}` expanded.

Sanity this parse: IT **34,486 P / 7,140 types; 1,038 L / 763 types**. Page-matched (L1): **632 L on 36 pages**.

**What this is not:** a language ID, EVA-as-phonemes, a plant ID, a reading of any token, or a public post.

---

## 2. Hypothesis under attack and the attack

**Held law (HYPOTHESIS, compounded by gauntlets 2-3):** labels are a different vocabulary from running text (`qo-` suppressed, `ok-`/`ot-` enriched), and that split is not a line-position effect and not a label-only-page effect.

**Attack (section-mix confound):** L1 mixes pharma, balneo, and other sections. If, inside a single section, page-matched L looks like same-section P on the two prefix rates, the register is carried by mixing sections, not by a label lexicon.

### 2.1 Pre-registered decision rule (written before the scorer ran)

**Load-bearing floors** (else section is secondary / not verdict-bearing):

- `n_L ≥ 50`, `n_P_same_sect ≥ 200`, `n_pages ≥ 5` on page-matched pages.

**Per load-bearing section:**

- **NULL** (register survives): L `qo-` ≤ 3.0% **and** L `ok+ot` ≥ 22.0% **and** within-page permutation p_le(`qo-`) < 0.001 **and** p_ge(`ok+ot`) < 0.001.
- **HIT** (section confound kills the law here): L `qo-` ≥ 5.0% **or** L `ok+ot` ≤ 18.0% **or** either perm p > 0.01.
- **PARTIAL**: anything else.

**Overall:** HIT if any load-bearing section is HIT; NULL only if every load-bearing section is NULL; else PARTIAL. IT primary, ZL control; compound HIT if either is HIT.

Secondary sections are recorded, not used for the overall verdict.

Calibration: corpus totals match series; odd/even L1 control gaps small vs P-to-L gap.

---

## 3. Results (IT primary; ZL agrees on compound)

### 3.1 Load-bearing sections

| Sect | n_L | n_P | pages | L `qo-` | L `ok+ot` | P `qo-` | P `ok+ot` | p_le qo | p_ge ok+ot | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| **P** (pharma) | 256 | 2102 | 15 | **0.0%** | **29.7%** | 12.9% | 10.6% | **< 1e-5** | **< 1e-5** | **NULL** |
| **B** (balneo) | 129 | 3450 | 11 | **2.3%** | **40.3%** | 26.7% | 6.8% | **< 1e-5** | **< 1e-5** | **NULL** |

Both load-bearing sections meet every NULL clause. Compound (IT+ZL): **NULL**.

### 3.2 Secondary sections (recorded, not verdict)

| Sect | n_L | n_P | pages | L `qo-` | L `ok+ot` | Notes |
|---|---|---|---|---|---|---|
| A | 110 | 188 | 3 | 0.9% | 29.1% | floors miss on P and pages; direction still label-shaped |
| C | 57 | 123 | 3 | 0.0% | 17.5% | ok+ot soft; n small; not HIT under floors |
| H | 21 | 209 | 2 | 0.0% | **0.0%** | tiny L; no `ok`/`ot` heads - noise, not a law |
| T | 59 | 844 | 2 | **6.8%** | **1.7%** | HIT-*shaped* but only 2 pages; **not load-bearing** |

**HYPOTHESIS (not promoted):** section `T` (text-heavy / Cosmic?) on its two both-band pages looks unlike the label register. Promote only after a pre-registered redesign that meets floors or accepts a two-page rule explicitly. Not a kill of the corpus law.

Zodiac `Z` has L=367 and P=0 - cannot section-match; already handled as L0 in gauntlet 3.

### 3.3 Odd/even L1 control

Odd vs even L1 prefix gaps remain small next to the P-to-L gap (see JSON). Gate passes.

---

## 4. Verdict: NULL

| Clause | Result |
|---|---|
| Pharma `P` NULL clauses | all met |
| Balneo `B` NULL clauses | all met |
| Any load-bearing HIT | none |
| ZL control | agrees (compound NULL) |

**The section-mix confound is rejected as a killer of the law on the two sections large enough to test.** Pharma labels vs pharma prose, and balneo labels vs balneo prose, both keep `qo-` suppressed and `ok-`/`ot-` enriched at p < 1e-5 against an exact within-page null.

This is a negative result for the attack and a third structural survival for the held law. It is not a decipherment.

---

## 5. What SURVIVED / what is new

**Every row is a HYPOTHESIS.**

| Held constraint | This cycle | Mark |
|---|---|---|
| Labels ≠ running text (`qo-` down, `ok+ot` up) | Survived inside pharma and inside balneo, page-matched | **compounded** |
| Not line-position (g2) / not label-only-page (g3) | Not re-litigated | held |

**New observations, recorded, not promoted:**

1. Secondary section `T` (n_L=59, 2 pages) is HIT-shaped (`qo-` 6.8%, `ok+ot` 1.7%). Needs its own gate if chased.
2. Secondary `H` L has `ok+ot` = 0 at n=21. Noise.

**Still dead (not revived):** three-name titles; visual twins as lexical matches; species readings; `keerodal` grind; plant ID; language ID; EVA-as-phonemes; f75v as a `qo-` ban test.

---

## 6. What would still falsify

1. A redesign that makes section `T` load-bearing and still HIT.
2. A generator / mode-switch account (rollup already grants this).
3. A third transliteration whose section flags move load-bearing membership.
4. Label-locus-type narrowing that splits the law (scored next as gauntlet 5).

---

## 7. Next

**Named leftover after this cycle:** label locus-type split (gauntlet 5) - already the next pass this same cook day.

**Not next:** f41r, f111v, f2v, `keeodal`, `keerodal` grind, f75v as `qo-` ban test, promoting secondary `T` without floors.

---

## 8. Bottom line

No folio. No translation. No plant ID. No language ID.

**IT pharma L1: `qo-` 0%, `ok+ot` 29.7% vs same-section P 12.9% / 10.6%. IT balneo L1: `qo-` 2.3%, `ok+ot` 40.3% vs P 26.7% / 6.8%. Within-page permutation 100,000 draws: p < 1e-5 both ways on both sections. ZL agrees. The label register is not a section-mix effect on load-bearing sections. NULL for the attack; the held law is compounded again.**

Reproduce: `python3 scripts/section_matched_null.py /path/to/IT2a-n.txt /path/to/ZL3b-n.txt > results/gauntlet-4-section-matched.json`.
