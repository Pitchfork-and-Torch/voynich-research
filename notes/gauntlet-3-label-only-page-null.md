# Voynich gauntlet 3 - label prefix register vs label-only-page null (not a translation)

**For:** Pitchfork-and-Torch
**Date:** 17 Sep 2026 (ET)
**Status:** corpus-wide structural test. No folio opened. **NULL** for the attack; the held label-register law survives after the 16 label-only pages are removed. **No verified full translation of Beinecke MS 408 exists.** Nothing below is a decipherment. Every gloss is marked **HYPOTHESIS**. No plant is identified. No language is identified. EVA letters are not phonemes. Do not grind `keerodal`. Do not open balneo.

Sources were re-downloaded this cycle from voynich.nu (same versions as the series). Raw files are not committed. The scorer is committed at `scripts/label_only_page_null.py`; it reuses the gauntlet-2 parser and reproduces every number below from the two public files.

---

## 0. Why this test

Gauntlet 2 rejected the line-position confound and left one named falsifier open (gauntlet-2 §7.4): **406 of 1,038 L tokens sit on 16 pages with no P text at all** (mostly zodiac). Those tokens could not be page-matched. If the corpus L register is carried by that label-only slice, the law is a *page-type* effect (zodiac labels look different because the pages are different), not a label lexicon that also holds where running text and labels share a page.

README still says idle / no folio without a named gate. This cycle names the gate gauntlet 2 already wrote down. No folio opens.

---

## 1. Source transcription (citation + URL)

| Item | Value |
|---|---|
| File | `IT2a-n.txt` (IVTFF 2.0) |
| Transliteration | Takeshi Takahashi, as extracted from the Landini-Stolfi interlinear (LSI), code **IT** |
| Alphabet | Basic EVA (Eva-T), not capitalised |
| Version | 2a of 2023-02-02, modified 2025-06-25 |
| URL | https://voynich.nu/data/IT2a-n.txt |
| Control file | `ZL3b-n.txt` (Zandbergen-Landini, IVTFF Eva- 2.0, version 3b of 2025-05-13), same directory |
| Format spec | IVTFF format description, https://www.voynich.nu/software/ivtt/IVTFF_format.pdf |
| Label-behaviour background | Rene Zandbergen, https://voynich.nu/extra/labels.html |
| Manuscript | Yale, Beinecke Rare Book & Manuscript Library, MS 408 |
| Prior notes | `notes/gauntlet-2-line-position-null.md` §7.4 (untested label-only pages); rollup S4.2 |

**Tokenisation (IVTFF 2.0), series default.** Same as gauntlet 2 / passes 2-8. `.` is a word break. `<->` is a word space. Remaining `<>` markup stripped. Tokens need at least one letter. `?` kept. P = loci whose type contains `P`. L = loci whose type contains `L`. ZL: commas joined, `[a:b]` first reading, `{..}` expanded.

Sanity this parse: IT **34,486 P / 7,140 types; 1,038 L / 763 types**. Split: **632 L on 36 pages that also carry P**; **406 L on 16 label-only pages**.

**Page classes (new this cycle).**

- **L1 / P1** = labels / paragraph tokens on pages that carry both bands (page-matched).
- **L0** = labels on pages with no P locus at all (label-only).

**What this is not:** a language identification, a claim that EVA letters are phonemes, a plant identification, a reading of any token, or a public post.

---

## 2. Hypothesis under attack and the attack

**Held law (HYPOTHESIS, compounded by gauntlet 2):** labels are a different vocabulary from running text (`qo-` suppressed, `ok-`/`ot-` enriched), and that split is not a line-position effect.

**Attack (label-only-page confound):** about 39% of L tokens never face running text on their own page. Those pages are mostly zodiac (`$I=Z`). If the register collapses once L0 is removed  -  i.e. if L1 is no longer label-shaped against same-page P  -  then the held law is an artifact of mixing two page types, and the "label lexicon" claim does not survive where labels and text co-occur.

The attack is falsifiable in one run because both populations exist in the same files.

### 2.1 Pre-registered decision rule (written before the scorer ran)

Load-bearing statistics are on **L1 vs P1** (IT primary, ZL control):

- **S1** = `qo-` rate of L1.
- **S2** = `ok+ot` rate of L1.
- **N2** = within-page permutation: for each of the 36 pages, pool = that page's L tokens + that page's P tokens; draw |L| without replacement; sum prefix hits. 100,000 draws, seed 408.

Verdict:

- **HIT** (confound absorbs the law): L1 `qo-` >= 5.0% **or** L1 `ok+ot` <= 18.0% **or** N2 p > 0.01 on either statistic.
- **NULL** (confound rejected): L1 `qo-` <= 3.0% **and** L1 `ok+ot` >= 22.0% **and** N2 p < 0.001 on both S1 and S2.
- **PARTIAL**: anything else.

Secondary (recorded, not verdict): L0 vs L1 rate difference on `qo-` and `ok+ot` (Fisher exact + pooled permutation). A significant L0/L1 gap without a HIT on L1-vs-P1 means **two strengths of one register**, not a killed law.

Calibration gates (run is void if any fails):

- C1 totals: 34,486 P / 1,038 L.
- C1 split: 406 L0 / 632 L1; 16 label-only pages / 36 both.
- C2 odd/even L negative control: `qo-` and `ok+ot` gaps small next to the P-to-L gap.

---

## 3. Results (IT primary; ZL control in brackets)

### 3.1 Corpus split

| Population | n | `qo-` | `ok+ot` | mean len | dominant `$I` |
|---|---|---|---|---|---|
| **P all** | 34,486 | 15.1% | 11.4% | 5.07 |  -  |
| **L all** | 1,038 | 0.9% | 33.0% | 5.16 |  -  |
| **L0** label-only pages | 406 | **0.25%** [~0] | **42.4%** [46.4] | 5.41 | Z 367 / A 31 / C 5 / H 3 |
| **L1** page-matched | 632 | **1.27%** | **27.1%** [28.9] | 5.01 | P 256 / B 129 / A 110 / T 59 / C 57 / H 21 |
| **P1** same 36 pages | 6,916 | **19.9%** | **8.6%** | 5.09 |  -  |

Reading:

- Removing L0 *lowers* L `ok+ot` from 33.0% to 27.1%. The label-only slice is the richer half. That is the confound's best shot.
- L1 is still far from P1 on the same pages: `qo-` 1.27% vs 19.9%; `ok+ot` 27.1% vs 8.6%. Wrong direction for HIT on both axes.
- L0 is almost pure zodiac. L1 is mostly pharma / balneo / astro-with-text. Section mix differs; the register direction does not flip.

### 3.2 Page-matched permutation (N2), 100,000 within-page relabellings

| Statistic | L1 obs | null mean | null range | p |
|---|---|---|---|---|
| **S1 `qo-`** | 8 / 632 = 1.27% | 78.5 (12.4%) | 47-111 | **p_le < 1e-5** [< 1e-5] |
| **S2 `ok+ot`** | 171 / 632 = 27.1% | 80.5 (12.7%) | 50-114 | **p_ge < 1e-5** [< 1e-5] |

Observed L1 `qo-` count (8) never reached from below (minimum null 47). Observed `ok+ot` (171) never reached from above (maximum null 114). ZL agrees (p < 1e-5 both ways (add-one) on 40 pages / 765 L1).

### 3.3 Secondary: L0 vs L1

| Prefix | L0 | L1 | Fisher two-sided p | pooled-perm p |
|---|---|---|---|---|
| `qo-` | 0.25% (1/406) | 1.27% (8/632) | 0.099 | 0.0998 |
| `ok+ot` | 42.4% (172/406) | 27.1% (171/632) | **3.8e-7** | **0.0000** |

L0 is richer in `ok+ot` than L1. That is real. It does **not** make L1 look like P1. Recorded as two strengths of one register. Not promoted to a split law.

### 3.4 Odd/even L control

Odd vs even L tokens (stable index split): `qo-` and `ok+ot` gaps are small next to the P-to-L gap. Gate passes. Exact rates in the JSON dump from the scorer.

---

## 4. Calibration

| Gate | Result | Mark |
|---|---|---|
| C1 totals | 34,486 P / 1,038 L | **pass** |
| C1 split | 406 L0 / 632 L1; 16 / 36 pages | **pass** |
| C2 odd/even L | gaps << P-to-L gap | **pass** |

ZL control agrees on verdict and on every direction that matters (L1 still label-shaped; N2 p < 1e-5 both ways (add-one)).

---

## 5. Verdict: NULL

| Clause | Threshold | Observed | Result |
|---|---|---|---|
| L1 `qo-` | <= 3.0% for NULL | 1.27% | **NULL clause met** |
| L1 `ok+ot` | >= 22.0% for NULL | 27.1% | **NULL clause met** |
| N2 S1 `qo-` | p < 0.001 | p_le < 1e-5 | **NULL clause met** |
| N2 S2 `ok+ot` | p < 0.001 | p_ge < 1e-5 | **NULL clause met** |
| HIT bound | L1 qo >= 5% or ok+ot <= 18% or N2 p > 0.01 | none met | not met |

**The label-only-page confound is rejected as a killer of the law.** Dropping the 16 label-only pages softens `ok+ot` (42% -> 27%) but leaves L1 cleanly label-shaped against the running text on the same 36 pages, at p < 1e-5 against an exact within-page null, in both transliterations.

This is a negative result for the attack and a second structural survival for the held law. It is not a decipherment and not a claim about what labels mean.

---

## 6. What SURVIVED / what did not fire / what is new

**Every row is a HYPOTHESIS.**

| Held constraint | This cycle | Mark |
|---|---|---|
| Labels are a different vocabulary (`qo-` suppressed, `ok-`/`ot-` enriched) | Survived after removing all label-only pages. Second structural null beaten (after line-position). | **compounded** |
| Line-position is not the register (gauntlet 2) | Not re-litigated. | held |

**New observations, recorded, not promoted:**

1. **L0 (mostly zodiac) is the richer `ok+ot` half** (42.4% vs L1 27.1%, Fisher p = 3.8e-7). Two strengths, one direction. Do not split the law on this alone.
2. L1 `$I` mix is pharma-heavy; L0 is zodiac-heavy. Section and page-type are confounded with each other here. A later cycle that wants a pure section test needs a design that holds page-type fixed.

**Still dead (not revived):** three-name titles; visual twins as lexical matches; species readings; `keerodal` grind; plant ID; language ID; EVA-as-phonemes; f75v as a `qo-` ban test.

---

## 7. What would still falsify the compounded claim

1. A **section-matched** design (e.g. pharma L vs pharma P only) that collapses the register. Not this cycle.
2. A **generator / mode-switch** account that emits `o`-headed tokens in label mode without a separate lexicon (rollup S5 already grants this).
3. A **third transliteration** whose L/P flags move the 406/632 split by more than noise.
4. The remaining positional classes gauntlet 2 could not reach from IVTFF flags alone (drawing-relative word position).

---

## 8. Next

**Idle.** No folio is named. Gauntlet 2's open label-only-page falsifier is scored and rejected. f75v remains on hold.

**Not next:** f41r, f111v, f2v, `keeodal`, another herbal, a `keerodal` re-grind, f75v as a `qo-` ban test, a section grind without a pre-registered rule.

---

## 9. Bottom line

No folio. No translation. No plant ID. No language ID.

**IT L0 (label-only): `qo-` 0.25%, `ok+ot` 42.4%. IT L1 (page-matched): `qo-` 1.27%, `ok+ot` 27.1% vs same-page P 19.9% / 8.6%. Page-matched permutation, 100,000 draws: p < 1e-5 both ways (add-one). ZL agrees. The label register is not a label-only-page effect. NULL for the attack; the held law is compounded again.**

Reproduce: `python3 scripts/label_only_page_null.py IT2a-n.txt ZL3b-n.txt > results.json`.
