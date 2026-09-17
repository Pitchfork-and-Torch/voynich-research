# Voynich gauntlet 2 - label prefix register vs line-position null (not a translation)

**For:** Pitchfork-and-Torch
**Date:** 17 Sep 2026 (ET)
**Status:** corpus-wide structural test. No folio opened. **NULL** for the attack; the held label-register law survives a page-matched positional null. **No verified full translation of Beinecke MS 408 exists.** Nothing below is a decipherment. Every gloss is marked **HYPOTHESIS**. No plant is identified. No language is identified. EVA letters are not phonemes. Do not grind `keerodal`. Do not open balneo.

Sources were re-downloaded this cycle from voynich.nu (same versions as the series). Raw files are not committed. The scorer is committed at `scripts/line_position_null.py`; it reproduces every number below from the two public files.

---

## 0. Why this test and not f75v

The README says next is idle and no folio opens without a named gate. Two gauntlet notes dated 15 Aug disagree: `gauntlet-1-f75r.md` names f75v as cycle 2; `gauntlet-1-herbalA-labels.md` FAILs and says STOP, do not open balneo. The README is later and puts balneo on hold. This cycle follows the README.

f75v is also not a clean falsifier. Its three `qo-` labels (`qokal` / `qoted` / `qotedy`, `Ln` / `Lt`) are already in the corpus inventory (rollup S2). Opening the page would confirm a known count, not risk a law.

The highest-leverage untested claim in the notebook is the one every pass leans on: **labels are a different vocabulary** (`qo-` suppressed, `ok-`/`ot-` enriched). That claim has only ever been scored against *all* running text. It has never been scored against the obvious positional confound.

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
| Format spec | IVTFF format description, https://www.voynich.nu/software/ivtt/IVTFF_format.pdf (locator and locus-type tables; `<%>` = paragraph start, `<$>` = paragraph end) |
| Label-behaviour background | Rene Zandbergen, "Some special properties of labels in the Voynich MS", https://voynich.nu/extra/labels.html |
| Manuscript | Yale, Beinecke Rare Book & Manuscript Library, MS 408 |
| Prior notes | `notes/rollup-pass-1-7.md` S4.2 (prefix split), S7 items 1 and 7 |

**Tokenisation (IVTFF 2.0), series default.** `.` is a word break. `<->` is a word space. All remaining `<>` markup is stripped. Tokens must contain at least one letter. `?` is kept. Paragraph text = loci whose type contains `P`. Labels = loci whose type contains `L`. ZL extras: commas joined, `[a:b]` first reading, `{..}` expanded.

Sanity this parse: IT **34,486 P / 7,140 types; 1,038 L / 763 types**. Matches passes 2-8 exactly. ZL: 32,594 P / 8,214; 1,140 L / 867.

**Position classes (new this cycle).** One IVTFF `P` locus is one written line. First token of a `P` locus = **line-initial**. Last token = **line-final**. Everything else = **medial**. A one-token line = **sole** (n=28, reported, not used). A line whose locus carries `<%>` is **paragraph-initial**. Within `L` loci the same split is applied (label-initial vs later tokens of multi-word labels).

**What this is not:** a language identification, a claim that EVA letters are phonemes, a plant identification, a reading of any token, or a public post.

---

## 2. Hypothesis under attack and the attack

**Held law (HYPOTHESIS, rollup S4.2):** labels are a different vocabulary from running text. Evidence to date: corpus L `qo-` 0.9% vs P 15.1%; L `ok+ot` 33.0% vs P 11.4%; the same split on every scored label page.

**Attack (positional account):** a label is a one-word text unit. Every label token is therefore a *first word of a line*. Voynich running text has known strong line effects (Currier: line-final `-m`; line-initial glyph skew; paragraph-initial gallows). If the first word of an ordinary text line already suppresses `qo-` and enriches `ok-`/`ot-`, then the "label register" is a *position* effect, not a *vocabulary* effect, and the law collapses into a positional law that says nothing about a separate label lexicon.

The attack is falsifiable in one run because both populations exist in the same files.

### 2.1 Pre-registered decision rule (written before the scorer ran)

Two statistics, both on IT, ZL as control:

- **S1** = `qo-` rate of L vs line-initial P.
- **S2** = `ok+ot` rate of L vs line-initial P.

Nulls:

- **N1 corpus:** line-initial P rate, Wilson 95% CI.
- **N2 page-matched permutation:** restrict L to pages that also carry P text. For each such page the pool is (that page's L tokens + that page's line-initial P tokens); draw |L| tokens without replacement; sum prefix hits across pages. Exact hypergeometric sampling, 100,000 draws, seed 408. Repeat with pool = all P on the page and pool = non-initial P on the page.
- **N3 length-matched:** expected L rate if each L token were a random P token of the same length.

Verdict:

- **HIT** (positional account absorbs the law): corpus line-initial P `qo-` <= 3.0% **and** N2 vs line-initial P gives p > 0.01 for both S1 and S2.
- **NULL** (positional confound rejected): corpus line-initial P `qo-` >= 10.0% **and** N2 vs line-initial P gives p < 0.001 for both S1 and S2.
- **PARTIAL**: anything else. Record. Law marked wounded if line-initial P moves more than half the P-to-L gap on either statistic.

Calibration gates (run is void if any fails):

- C1 parse totals reproduce 34,486 / 7,140 and 1,038 / 763.
- C2 known line-final `-m` enrichment reproduces (line-final vs non-final).
- C3 known line-initial first-glyph skew reproduces (initial vs non-initial).
- C4 negative control: split P by odd/even locus number; `qo-` and `ok+ot` gaps must be small next to the P-to-L gap.

---

## 3. Results (IT primary; ZL control in brackets)

### 3.1 Corpus, by band and position

| Band / position | n | `qo-` | 95% CI | `ok+ot` | 95% CI | mean len |
|---|---|---|---|---|---|---|
| **P all** | 34,486 | **15.1%** | 14.7-15.4 | **11.4%** | 11.1-11.7 | 5.07 |
| P **line-initial** (incl. sole) | 4,118 | **12.6%** [12.5] | 11.6-13.6 | **5.7%** [5.8] | 5.0-6.4 | 5.51 |
| P medial | 26,278 | 16.5% | 16.1-17.0 | 12.4% | 12.0-12.8 | 5.05 |
| P line-final | 4,090 | 8.1% | 7.3-8.9 | 10.3% | 9.5-11.3 | 4.71 |
| P not-initial | 30,368 | 15.4% | 15.0-15.8 | 12.2% | 11.8-12.5 | 5.01 |
| P line-initial, **paragraph-initial** | 772 | **3.0%** [3.2] | 2.0-4.4 | **3.6%** [2.4] | 2.5-5.2 | 6.28 |
| P line-initial, not paragraph-initial | 3,346 | 14.8% | 13.6-16.0 | 6.1% | 5.4-7.0 | 5.33 |
| **L all** | 1,038 | **0.9%** [0.9] | 0.5-1.6 | **33.0%** [34.7] | 30.3-36.0 | 5.16 |
| L label-initial (incl. sole) | 875 | 1.0% | 0.5-1.9 | 37.8% | 34.7-41.1 | 5.40 |
| L later tokens of multi-word labels | 163 | 0.0% | 0.0-2.3 | 7.4% | 4.3-12.4 | 3.90 |

Reading:

- Line-initial P `qo-` is **12.6%**. That is one-sixth lower than medial P, and **fourteen times** the L rate. N1 fails the HIT bound (<= 3.0%) and clears the NULL bound (>= 10.0%).
- Line-initial P `ok+ot` is **5.7%**. Line-initial position **depletes** `ok-`/`ot-` relative to medial text (12.4%). Labels go the other way (33.0%). The positional account predicts the wrong sign on S2.
- The only positional class that suppresses `qo-` like a label is the **paragraph-initial first word** (3.0%, n=772). It also suppresses `ok+ot` (3.6%). That class is the known gallows-initial paragraph effect (`p`/`t` heads), not a label lookalike. Labels are not paragraph-initial words either.
- Length is not the confound. L mean length 5.16 vs P 5.07; line-initial P 5.51.

### 3.2 Page-matched (36 pages carry both L and P; 632 L tokens)

406 L tokens sit on 16 pages with no `P` text at all (zodiac and astro pages whose text is `C`/`R`). They cannot be page-matched and are excluded from N2 only.

| Population on the 36 pages | n | `qo-` | `ok+ot` |
|---|---|---|---|
| L (used in N2) | 632 | **1.3%** [1.2] | **27.1%** [28.9] |
| P all, same pages | 6,916 | 19.9% [20.5] | 8.6% [9.0] |
| P line-initial, same pages | 799 | **19.5%** [18.8] | **3.6%** [4.5] |
| P not-initial, same pages | 6,117 | 20.0% | 9.2% |

Expected L rate if each L token were a random draw from its own page (weighted by page):

| Prefix | L observed | random P same page | random **line-initial** P same page | random non-initial P same page |
|---|---|---|---|---|
| `qo-` | 1.3% | 14.0% | **12.7%** [10.0] | 14.2% |
| `ok-` | 12.7% | 6.9% | **2.5%** [9.3] | 7.5% |
| `ot-` | 14.4% | 3.7% | **1.4%** [4.4] | 3.9% |

On the pages that actually carry labels, the running text is `qo-`-heavier than the corpus (Currier B), and its first words are `ok-`/`ot-`-poorer than the corpus. Page matching widens the gap; it does not close it.

### 3.3 Permutation (N2), 100,000 within-page relabellings

The pool includes the page's own L tokens, so the null mean sits between the L rate and the P rate. That is the conservative direction: it makes rejection harder.

| Statistic | pool | L obs | null mean | null range (k) | p |
|---|---|---|---|---|---|
| **S1 `qo-`** | line-initial P | 8 / 632 = 1.3% | 7.9% | 29-74 | **p_le < 1e-5** [< 1e-5] |
| S1 `qo-` | all P | 1.3% | 12.4% | 43-114 | p_le < 1e-5 |
| S1 `qo-` | non-initial P | 1.3% | 12.3% | 47-115 | p_le < 1e-5 |
| **S2 `ok+ot`** | line-initial P | 171 / 632 = 27.1% | 16.0% | 76-125 | **p_ge < 1e-5** [< 1e-5] |
| S2 `ok+ot` | all P | 27.1% | 12.7% | 53-115 | p_ge < 1e-5 |
| S2 `ok+ot` | non-initial P | 27.1% | 13.6% | 58-117 | p_ge < 1e-5 |
| `ok-` alone | line-initial P | 12.7% | 7.7% | 31-67 | p_ge < 1e-5 |
| `ot-` alone | line-initial P | 14.4% | 8.3% | 34-70 | p_ge < 1e-5 |

In 100,000 draws the observed L `qo-` count (8) was never reached from below (minimum 29). The observed `ok+ot` count (171) was never reached from above (maximum 125).

### 3.4 Length-matched (N3, corpus-wide)

| Prefix | L observed | expected from length-matched all P | expected from length-matched line-initial P |
|---|---|---|---|
| `qo-` | 0.9% | 15.3% | 11.2% |
| `ok-` | 16.0% | 5.6% | 3.1% |
| `ot-` | 17.1% | 5.0% | 2.3% |

### 3.5 By Currier language (IT)

| Band | n | `qo-` | `ok+ot` |
|---|---|---|---|
| P A, line-initial | 1,557 | 13.4% | 7.9% |
| P A, not-initial | 9,572 | 9.2% | 9.5% |
| P B, line-initial | 2,466 | 12.4% | 4.1% |
| P B, not-initial | 20,356 | 18.5% | 13.5% |
| L on A pages | 276 | **0.0%** | 27.5% |
| L on B pages | 189 | 3.7% (7 tokens) | 28.0% |
| L on pages with no `$L` header | 573 | 0.3% | 37.4% |

In A, line-initial position *raises* `qo-`. In B it lowers it by a third. Neither language brings a first word anywhere near a label. The seven B-page `qo-` labels are the known f66r / f73v / f75v set (rollup S2).

---

## 4. Calibration

| Gate | Result | Mark |
|---|---|---|
| C1 totals | 34,486 / 7,140; 1,038 / 763 | **pass** |
| C2 line-final `-m` | final tokens end in `m` 16.4% vs non-final 0.9% [ZL 15.4% vs 0.9%] | **pass** (known Currier effect reproduces) |
| C3 line-initial glyph skew | first glyph of line-initial P: `d` 15.5%, `s` 14.8%, `y` 14.6%, `o` 13.5%, `q` 12.9%, `t` 9.6%, `p` 9.2%. Non-initial: `o` 21.7%, `c` 20.7%, `q` 15.8%, `s` 11.9%, `d` 8.8%, `y` 3.6%, `p` 0.5% | **pass** (`y`/`d`/`s`/gallows up, `o`/`c` down at line start; known effect) |
| C4 negative control | odd vs even loci: `qo-` 14.6% vs 15.5%; `ok+ot` 11.1% vs 11.7%. Gaps 0.9 and 0.6 points against a P-to-L gap of 14.2 and 21.7 points | **pass** |

L first glyph for the record: `o` **51.7%**, `d` 9.9%, `y` 8.3%, `s` 7.5%, `c` 7.1%, `a` 5.9%, `q` 1.1%. Line-initial P has `o` at 13.5%. The label `o-` head is not a line-start head.

ZL control agrees on every direction and every verdict-relevant number (bracketed above).

---

## 5. Verdict: NULL

| Clause | Threshold | Observed | Result |
|---|---|---|---|
| N1 corpus line-initial P `qo-` | >= 10.0% for NULL | 12.6% (CI 11.6-13.6) | **NULL clause met** |
| N2 S1 `qo-`, L vs line-initial P | p < 0.001 | p_le < 1e-5 | **NULL clause met** |
| N2 S2 `ok+ot`, L vs line-initial P | p < 0.001 | p_ge < 1e-5 | **NULL clause met** |
| HIT bound | line-initial P `qo-` <= 3.0% | 12.6% | not met |
| Wounded bound | line-initial P moves > half the P-to-L gap | `qo-` moved 2.5 of 14.2 points (18%); `ok+ot` moved -5.7 points, wrong direction | not met |

**The positional account is rejected.** The first word of a Voynich text line is not label-shaped. It keeps `qo-` at running-text levels and is *poorer* in `ok-`/`ot-` than the middle of the line. Labels are the opposite on both counts, on the same pages, at p < 1e-5 against an exact within-page null, in both transliterations.

This is a negative result for the attack and a positive survival for the held law. It is not a decipherment and not a claim about what labels mean.

---

## 6. What SURVIVED / what did not fire / what is new

**Every row is a HYPOTHESIS.**

| Held constraint | This cycle | Mark |
|---|---|---|
| Labels are a different vocabulary from running text (`qo-` suppressed, `ok-`/`ot-` enriched) | Survived a page-matched, position-matched, length-matched null. First test against the line-position confound. | **compounded** (first structural null it has beaten; previous scores were raw P-vs-L) |
| `qo-` banned on labels (legal in P) | Not re-scored as a ban. The 9 corpus `qo-` labels are unchanged. Line-initial P `qo-` 12.6% shows the suppression is not positional. | held, not wounded |
| `ok-`/`ot-` label-legal | Enrichment is not a line-start effect (line-start depletes it). | held, not wounded |

**New observations, recorded, not promoted:**

1. **Paragraph-initial first words** (n=772) suppress `qo-` to 3.0% and `ok+ot` to 3.6%. That is the known gallows-head paragraph effect. It is the only text position that matches labels on `qo-`, and it fails on `ok+ot`. A later cycle that wants a positional twin for labels has exactly one candidate class and it already fails half the test.
2. **Inside multi-word labels**, `ok+ot` sits on the first token (37.8%, n=875) and drops on later tokens (7.4%, n=163). Later tokens are dominated by `L0` (n=196, mean length 3.6, `ok+ot` 8.7%), so type and position are confounded here. Not separated this cycle. Not a claim.
3. Line-initial `ok+ot` depletion (5.7% vs 12.4% medial) is itself a line effect the series had not recorded. Same sign in A and B. Descriptive only.

**Still dead (not revived):** three-name titles; visual twins as lexical matches; species readings of `daiin` / `chol` / `chor` / `otoldy` / `oky` / `okary` / `okam` / `otal`; `keerodal` grind; plant ID; language ID; EVA-as-phonemes.

---

## 7. What would still falsify the compounded claim

1. A **different positional class** that matches labels on *both* `qo-` <= 3% and `ok+ot` >= 25%. Tested and failed this cycle: line-initial, line-final, medial, paragraph-initial. Untested: word position relative to drawings inside a line (`P1` indent boundaries), first word after an intra-line gap. Neither is exposed by IVTFF flags alone.
2. A **generator account** that emits `o`-headed tokens in "label mode" and `qo`-headed tokens in "line mode." That would keep the register and delete the word "vocabulary." Rollup S5 already grants this. Nothing here separates a lexicon from a mode switch.
3. A **third transliteration** (GC / v101, RF) whose label flags move more than a few dozen tokens between `L` and `P`. IT and ZL agree here to within a point on every rate.
4. A demonstration that the 16 label-only pages (406 L tokens, no `P`) behave differently from the 36 page-matched pages on `ok+ot`. Not tested. Their `qo-` count is 1 of 406.

---

## 8. Next

**Idle.** No folio is named. The one structural confound the notebook had never scored is scored and rejected. f75v remains on hold; its `qo-` count is already known and cannot risk a law.

If a later gate wants a positional attack, the only surviving candidate class is paragraph-initial first words, and it already fails on `ok+ot`.

**Not next:** f41r, f111v, f2v, `keeodal`, another herbal, a `keerodal` re-grind, f75v as a `qo-` ban test.

---

## 9. Bottom line

No folio. No translation. No plant ID. No language ID.

**IT line-initial P: `qo-` 12.6%, `ok+ot` 5.7%. IT L: `qo-` 0.9%, `ok+ot` 33.0%. Page-matched permutation, 100,000 draws: p < 1e-5 both ways. ZL agrees. The label register is not a line-position effect. NULL for the attack; the held law is compounded.**

Reproduce: `python3 scripts/line_position_null.py IT2a-n.txt ZL3b-n.txt > results.json`.
