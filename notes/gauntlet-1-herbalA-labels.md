# Voynich gauntlet 1 - Herbal-A labels f1r-f8v (not a translation)

**For:** Jon Bailey
**Date:** 15 Aug 2026 (ET)
**Status:** SUPERSEDED GAUNTLET CYCLE 1. Herbal-A only (Currier A + Davis Scribe 1). Plant labels vs paragraph tokens on f1r-f8v. **FAIL.** **No verified full translation of Beinecke MS 408 exists.** Nothing below is a decipherment. Every gloss is marked **HYPOTHESIS**. No plant is identified. No language is identified. EVA letters are not phonemes. Do not grind `keerodal`. Do not open balneo. Do not chase `keeodal`, f41r, f111v, or ZL-only f2r `ytoail`.

Stats and extract were already on disk. They were not re-downloaded. This note recounts the key figures against `https://voynich.nu/data/ (IT2a-n.txt / ZL3b-n.txt)` (running text) and `https://voynich.nu/data/ (IT2a-n.txt / ZL3b-n.txt)` (control). Raw loci: `(local stats extract, not published)`. Computed stats: `(local stats extract, not published)`.

---

## 1. Source transcription (citation + URL)

| Item | Value |
|---|---|
| File | `IT2a-n.txt` (IVTFF 2.0) |
| Transliteration | Takeshi Takahashi, as extracted from the Landini-Stolfi interlinear (LSI), code **IT** |
| Alphabet | Basic EVA (Eva-T), not capitalised |
| Version | 2a of 2023-02-02, modified 2025-06-25 |
| URL | https://voynich.nu/data/IT2a-n.txt |
| Catalogue page | https://www.voynich.nu/transcr.html |
| Control file | `ZL3b-n.txt` (Zandbergen-Landini, IVTFF Eva- 2.0, version 3b of 2025-05-13), same directory |
| Label-behaviour background | Rene Zandbergen, "Some special properties of labels in the Voynich MS", https://voynich.nu/extra/labels.html (update 2025-08-23) |
| Manuscript | Yale, Beinecke Rare Book & Manuscript Library, MS 408 |
| Prior notes | `notes/rollup-pass-1-7.md` (passes 1-7). Herbal `@Lp` inventory is exhausted. Herbal name hunt is closed. |

**Tokenisation (IVTFF 2.0), same as the pass-2-7 verified parse.** `.` is a word break. `<->` is a **word space** (do not strip and concatenate). All remaining `<>` markup is stripped (`<%>`, `<$>`, `<!...>`, leftover `<@H=n>`). Tokens must contain at least one A-Z letter. `?` is kept if present. Paragraph text = loci whose flags contain `P`. Labels = flags containing `L`. `=Pt` (paragraph-end titles) are scored as **P, not L**. Three-name titles already DIED; they are not revived as labels.

ZL is the **control**, not the running text. ZL extras: uncertain commas are **joined** (not a space); alternatives `[a:b]` take the first reading; ligature braces `{ct}` expand to their contents.

This parse's corpus totals match the series default: **34,486 P / 7,140 types; 1,038 L / 763 types**.

**What this is not:** a download of any copyrighted monograph, a Cheshire/Gibbs-style "complete solution," a language identification, a claim that EVA letters are phonemes, a plant identification, or a public post.

---

## 2. Range and inclusion

Cycle gate: include a page in f1r-f8v iff IT `$L=A` (Currier A) and `$H=1` (Davis Scribe 1). **All 16 pages qualify. None excluded.**

| Page | IT `$I` | `$L` | `$H` | `$C` | `$Q` | Included |
|---|---|---|---|---|---|---|
| f1r | T (text-only) | A | 1 | 1 | A | yes |
| f1v | H | A | 1 | 1 | A | yes |
| f2r | H | A | 1 | 1 | A | yes |
| f2v | H | A | 1 | 1 | A | yes |
| f3r | H | A | 1 | 1 | A | yes |
| f3v | H | A | 1 | 1 | A | yes |
| f4r | H | A | 1 | 1 | A | yes |
| f4v | H | A | 1 | 1 | A | yes |
| f5r | H | A | 1 | 1 | A | yes |
| f5v | H | A | 1 | 1 | A | yes |
| f6r | H | A | 1 | 1 | A | yes |
| f6v | H | A | 1 | 1 | A | yes |
| f7r | H | A | 1 | 1 | A | yes |
| f7v | H | A | 1 | 1 | A | yes |
| f8r | H | A | 1 | 1 | A | yes |
| f8v | H | A | 1 | 1 | A | yes |

ZL headers match on `$L=A` / `$H=1` for every page in the range.

**f1r is text-only (`$I=T`). No plant, no labels. That is expected.** The other 15 pages are herbal (`$I=H`). IT still marks **zero** `L` loci on those 15. The empty label inventory is not "f1r only." It is the whole slice.

IT locus flags in range (225 loci): `+P0` 197, `@P0` 16, `=Pt` 7, `*P0` 5. **No `Lp` / `Lf` / `Lc` / `L0` / other `L`.**

ZL adds two loci IT does not have, both on f2r: `@Lp` `ytoail` and `@L0` `ios.an.on`. ZL comment on that page: "1 label near plant leaf." Those four tokens are the **control leftover**, not IT running text. Rollup already said do not chase ZL-only f2r `ytoail`. This cycle does not chase them.

Public Beinecke pixel images were attempted earlier this cycle and not fetched (timeout / 404 / viewer-only). Scoring is from IT/ZL flags only. No new L locus was invented from a description.

ZL page comments list literature plant IDs (belladonna, centaurea, dittany, ...). **Left unused.** Catalogue IDs are not findings.

---

## 3. Pre-stated PASS / FAIL rule

**HYPOTHESIS under test:** labels have a smaller type inventory and different slot occupancy than running text; `qo-` stays 0 on labels.

**PASS** = a significant register split (hurts one-generator hoax and uniform substitution).

**FAIL** = labels are the same process, **or** there is no usable L inventory to demonstrate a split.

PASS iff all of:

1. IT L tokens >= 10
2. L TTR < P TTR
3. L `qo-` count = 0
4. L top types are not the P workhorses `daiin` / `chol` / `chedy` / `qokeey`
5. L prefix-slot occupancy differs from P (L is not a random subsample of P)

FAIL if IT L n < 10, or L looks like a random subsample of P, or any positive PASS clause fails.

Vacuous zeros (empty L) do **not** lock the `qo-` ban.

---

## 4. P vs L numbers (verified against IT)

Independent recount of IT2a-n on f1r-f8v, same token rules as the json. Figures match `(local stats extract, not published)`. Nothing below is invented.

| Band | Loci | Tokens | Types | TTR | Hapax types | Mean len |
|---|---|---|---|---|---|---|
| **IT P** (flags contain `P`, including 7 `=Pt`) | 225 | **1506** | **752** | **0.499** | 577 (76.7%) | 4.80 |
| **IT L** | **0** | **0** | **0** | undefined | 0 | - |
| IT `=Pt` only (subset of P; not L) | 7 | 12 | 12 | 1.000 | 12 | 5.33 |
| ZL P (control) | 225 | 1431 | 781 | 0.546 | 613 | 5.06 |
| ZL L (control only) | 2 | 4 | 4 | 1.000 | 4 | 3.25 |

IT P minus `=Pt`: 218 loci, 1494 tokens. The 12 title tokens stay in P.

IT P top types: `daiin` 56, `chol` 50, `chor` 47, `shol` 31, `cthy` 24, `s` 23, `sho` 21, `dain` 18, `chy` 16, `dar` / `cthol` / `shor` / `dy` 14 each.

IT P workhorses named in the PASS rule: `daiin` 56, `chol` 50, `chedy` **0**, `qokeey` 2. Early herbal-A is A-language: `chedy` is a B workhorse and is absent here. That is expected, not a wound.

IT P prefix slots (n=1506): `ch` 338 (22.4%), `sh` 179 (11.9%), `da` 139 (9.2%), `ct` 90 (6.0%), **`qo-` 89 (5.91%)**, `ok` 56 (3.72%), `ot` 56 (3.72%), ok+ot 112 (7.44%). Prose-legal `qo-`; ok+ot below the corpus-L 33% rate. That is running-text occupancy.

IT L prefix slots: all n=0, all rates undefined.

### 4.1 Per folio (IT)

| Page | `$I` | Loci | P tok / typ | L tok | P `qo-` | `daiin` | `chol` | `chor` |
|---|---|---|---|---|---|---|---|---|
| f1r | T | 28 | 210 / 163 | **0** | 0 | 7 | 7 | 3 |
| f1v | H | 10 | 90 / 65 | **0** | 1 | 1 | 5 | 0 |
| f2r | H | 13 | 99 / 80 | **0** | 4 | 3 | 3 | 2 |
| f2v | H | 8 | 61 / 47 | **0** | 3 | 5 | 5 | 5 |
| f3r | H | 20 | 115 / 86 | **0** | 22 | 2 | 7 | 7 |
| f3v | H | 14 | 83 / 73 | **0** | 5 | 1 | 2 | 3 |
| f4r | H | 13 | 64 / 47 | **0** | 7 | 5 | 2 | 2 |
| f4v | H | 14 | 83 / 71 | **0** | 8 | 4 | 1 | 2 |
| f5r | H | 7 | 56 / 46 | **0** | 9 | 2 | 0 | 0 |
| f5v | H | 6 | 45 / 36 | **0** | 3 | 5 | 3 | 2 |
| f6r | H | 14 | 85 / 66 | **0** | 3 | 3 | 1 | 4 |
| f6v | H | 21 | 115 / 88 | **0** | 7 | 2 | 2 | 6 |
| f7r | H | 10 | 62 / 56 | **0** | 6 | 2 | 2 | 1 |
| f7v | H | 9 | 73 / 58 | **0** | 7 | 5 | 0 | 1 |
| f8r | H | 21 | 146 / 114 | **0** | 3 | 5 | 2 | 5 |
| f8v | H | 17 | 119 / 88 | **0** | 1 | 4 | 8 | 4 |
| **sum** | | **225** | **1506 / 752** | **0** | **89** | **56** | **50** | **47** |

Every herbal page in the range is P-only in IT. f1r (`$I=T`) is the expected text-only page. The other 15 have plants and still have no IT labels.

### 4.2 `=Pt` titles - P, not L

Seven loci, 12 tokens, 12 types (all hapaxes in this band):

- f1r.6 `ydaraishy`
- f1r.10 `dain os teody`
- f1r.21 `otol daiiin`
- f1r.28 `dchaiin`
- f8r.8 `ocho daiin`
- f8r.13 `okokchodm`
- f8r.21 `schol sair`

`daiin` and `dain` appear here as they do in running text. **HYPOTHESIS:** these are paragraph-end titles / flushed words, not plant labels. Three-name titles DIED on f65r. Not revived.

### 4.3 ZL-only L (control; not imported)

| Locus | Flags | Tokens |
|---|---|---|
| f2r.14 | `@Lp` | `ytoail` |
| f2r.15 | `@L0` | `ios` `an` `on` |

ZL L n=4, types=4, TTR=1.0, `qo-`=0, none of `daiin`/`chol`/`chedy`/`qokeey`. ZL L TTR **1.0 is not <** ZL P TTR 0.546. n=4 < 10. Even as a control this is not a PASS. Rollup: do not chase ZL-only f2r `ytoail`. Not typical running-text EVA (`ios.an.on`). Not an IT leftover.

---

## 5. Verdict: FAIL

Clause-by-clause against the pre-stated rule (IT primary):

| Clause | Result |
|---|---|
| IT L tokens >= 10 | **FAIL** - L n=**0** |
| L TTR < P TTR | **untestable** - L TTR undefined |
| L `qo-` = 0 | **vacuous 0**, not a lock |
| L top types != P workhorses | **untestable** - no L types |
| L not a P subsample | **untestable** - empty set is not a subsample and not a split |

**FAIL.** There is no usable label inventory on f1r-f8v in IT. A register split cannot be demonstrated. Vacuous `qo-`=0 does not lock the ban. The cycle does not get to "labels are the same process" either: there are no IT labels to be the same process.

ZL control does not rescue the slice (n=4 < 10; TTR higher than P, not lower).

This FAIL is **insufficient L**, not a held-law break.

---

## 6. Held laws this slice (none compounded)

A law is **compounded** only if the slice PASSes and the law survives on both sides. Verdict is FAIL, so **compounded = []**.

| Held law | This slice | Status |
|---|---|---|
| `daiin` / `chol` / `chor` function-like | P: 56 / 50 / 47 (top three). L: untested (empty). | **HOLDS_ON_P**, **UNTESTED_L**. Not compounded. |
| `qo-` banned on labels | IT L `qo-`=0 on n=0. ZL L `qo-`=0 on n=4. | **UNTESTED_IT_L_EMPTY**. Vacuous, not a lock. Does not BREAK. |
| `-oldy` and `otal~` type-words | P `-oldy` n=7 (`sholdy`, `ytoldy`, `cpholdy`, `choldy`, `dold`, `chkoldy`, `koltoldy`). P `otal` n=1 (f3r.6). L empty. | **SCARCE_NOT_A_KILL** (pre-stated: absence in early herbal-A is not a kill). |
| `dam` formula | P n=5 (f1v.4, f3r.2, f3r.6, f6v.5, f8r.4). L n=0. | **P_PRESENT_L_UNTESTED**. Formula claim not tested on L. Does not die. |

P-side function-like claim is the same pattern already scored on f1r in pass 1 and on later herbal-A pages: the workhorses dominate running text. That is not new and is not a lock of the L-side claim.

`ol` 9 / `or` 12 in this 1506-token slice (present, low). Not promoted. The herbal-A page-level wound from f9v / f10v is not re-litigated here.

---

## 7. What already DIED (not revived)

| Claim | Status |
|---|---|
| Three-name titles | DIED pass 6. `=Pt` on f1r / f8r scored as P. |
| Visual twins as lexical matches | DIED pass 3. |
| Species readings of `daiin` / `chol` / `chor` / `otoldy` / `oky` / `okary` / `okam` / `otal` | DIED. They fire in P on this slice. |
| ZL-only f2r `ytoail` as an IT name leftover | Already refused in the rollup. Not chased. |
| Herbal name hunt / `keerodal` grind | Closed. Not opened. |

---

## 8. Next

**STOP.**

Pre-stated: if FAIL, STOP. Do not open f9r-f16v. Do not open balneo. Do not grind `keerodal`.

For the record only (not a next step): f9r-f16v are still `$L=A` / `$H=1` where those pages exist (f12r / f12v are absent from IT). Every one of those pages is also IT L=0. Continuing the unused Herbal-A slice would not create a label inventory. The FAIL already forbids it.

**Steward copy: NO.** Rule: YES only if the split LOCKS (=PASS) or a held constraint BREAKS. Neither happened.

---

## 9. Bottom line

Sixteen pages, all Currier A / Scribe 1. IT P **1506 / 752**. IT L **0 / 0**. `qo-` on L = **0** (empty set). **FAIL.** No law compounded. Held laws remain held; the L-side is untested because Takahashi writes no labels on f1r-f8v. f1r text-only is expected; the fifteen herbal pages are also P-only in IT. ZL's four f2r tokens do not pass the rule and are not imported.

This is a lab notebook, not a crib. No translation. No plant ID. No language ID.
