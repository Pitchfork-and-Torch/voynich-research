# Voynich gauntlet 1 - f75r working notes (not a translation)

**For:** Jon Bailey
**Date:** 15 Aug 2026 (ET)
**Status:** first unused balneo folio in f75-f84. Herbal name hunt is closed. **No verified full translation of Beinecke MS 408 exists.** Nothing below is a decipherment. Every gloss is marked **HYPOTHESIS**. No plant is identified. No language is identified. EVA letters are not phonemes. Do not grind `keerodal`. Do not chase `keeodal`, f41r, f111v, or f2v.

This note opens the balneo / biological quire (quire 13) on the first unused page. Two pre-registered hypotheses are scored below. Held constraints are tested, not assumed. A constraint that survives is marked **manuscript-wide for balneo** (provisional: one page). A break would have stopped the cycle.

Sources were already on disk. They were not re-downloaded. Stats in `(local stats extract, not published)` were computed against the files this cycle. Raw loci: `(local stats extract, not published)`.

---

## 1. Source transcription (citation + URL)

Primary text used here:

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
| Folio description f75r | https://www.voynich.nu/q13/index.html (quire 13; site update 08/06/2025) |
| Section illustrations | https://www.voynich.nu/illustr.html (update 16/06/2025) |
| Colour-letter table | https://www.voynich.nu/writing.html (update 13/06/2025), keyword COL |
| Manuscript | Yale, Beinecke Rare Book & Manuscript Library, MS 408 |
| Prior notes | `notes/rollup-pass-1-7.md` (passes 1-7). Herbal `@Lp` inventory is exhausted. |

**Tokenisation (IVTFF 2.0), same as the pass-2-7 verified parse.** `.` is a word break. `<->` is a **word space** (do not strip and concatenate). All remaining `<>` markup is stripped (`<%>`, `<$>`, `<!...>`, leftover `<@H=n>`). Tokens must contain at least one A-Z letter. `?` is kept if present. Paragraph text = loci whose flags contain `P`. Labels = flags containing `L`.

ZL is the **control**, not the running text. ZL extras: uncertain commas are **joined** (not a space); alternatives `[a:b]` take the first reading; ligature braces `{ct}` / `{cthh}` / `{ith}` expand to their contents.

This parse's corpus totals match the series default: **34,486 P / 7,140 types; 1,038 L / 763 types**.

**What this is not:** a download of any copyrighted monograph, a Cheshire/Gibbs-style "complete solution," a language identification, a claim that EVA letters are phonemes, a plant identification, a nymph-as-person reading, or a public post.

---

## 2. Folio text used

### 2.1 Why f75r

Gauntlet cycle 1 is the first unused balneo folio in f75-f84. Herbal name-hunting is closed. This page is the start of quire 13 (`$Q=M`, `$I=B`). It is the clean first test of whether the held prefix and type-word laws still hold when the pictures change from plants/jars to baths and pipes.

Page header from IT2a-n (identical flags in ZL):

```
<f75r>     <! $Q=M $P=A $F=a $B=1 $I=B $L=B $H=2 $C=2>
```

`$Q=M` quire 13, `$I=B` biological / balneo, `$L=B` Currier B, `$H=2` hand 2. Quire 13 (https://www.voynich.nu/q13/index.html): RZ language Bb+ (page / folio / bifolio); LFD hand 2. ZL comment: "biological / Currier's language B, hand 2 / 2 lakes and 14 nymphs."

### 2.2 Public folio description (quire 13 only)

**Sourced, not invented.** Quire 13 page, current as of the 08/06/2025 site update; illustration details from illustr.html (16/06/2025). Clinical / folio-technical only.

- So-called biological (or balneological) page. Folio number **75** in the upper right corner (later addition; not EVA).
- Two pools with green water, populated by small feminine figures (catalogue term: nymphs). ZL counts two lakes and 14 figures.
- Fourth figure from the top holds a stick-like object (illustr.html, "Objects held by people").
- **53** text items: **46** lines of standard paragraph text; **7** lines of short text in floating paragraphs. Matches IT (46 `P0` + 7 `Pb`).
- Main text is in three paragraphs. A separate piece of writing in 7 short lines sits inside a loop near the top of the page (IT `@Pb` / `+Pb`; ZL: "Text inside loop near top of page transcribed as block").
- Currier B; RZ Bb+; LFD hand 2.
- **No labels** on this page. Quire 13 does not list nymph labels, tub/tube labels, or stand-alone character labels for f75r. Those start on f75v.
- Tentative identifications block on the quire page is empty for f75r. None is added here.
- Section-wide catalogue background (illustr.html), not a finding of this cycle: the biological quire has been compared with copies of the 13th-century *Balneis Puteolanis* (medicinal-bath manuscripts; Vatican Ross.379 cited). Binding of the quire may not be original (f78v-f81r water-flow join). Not imported as a reading of any EVA token.

**Colour / paint Latin letters:** writing.html COL table has **no** entry for f75r. All listed colour annotations are herbal-A / hand 1, plus one pharmaceutical `p`/`r` on f99v. Nothing on this page is kept out of EVA because nothing extra-EVA is recorded here. The folio number 75 is a later hand, not a colour letter.

Do **not** identify the figures as historical persons, and do not read the baths as a scene involving minors. This is a historical manuscript of adult bath / nymph drawings. Stay on the loci.

### 2.3 Labels vs running text

First balneo page is **P-only**. Not a two-sided score.

| Band | IT loci | IT tokens | IT types |
|---|---|---|---|
| Paragraph `P0` (three main paragraphs) | 46 | 412 | - |
| Floating `Pb` (loop, 7 short lines) | 7 | 10 | - |
| **All P** | **53** | **422** | **195** |
| **All L** (`Lf` / `Lc` / `Lp` / `Ln` / `Lt` / other) | **0** | **0** | **0** |

ZL control: **390 P / 209 types; L = 0**. ZL is lower because uncertain commas are joined. 36 loci disagree on at least one break or letter; IT is the running text.

The 7 `Pb` lines are **not** labels. IT flags them `P`. The quire page calls them floating paragraphs. Tokens: `sal okeedy` / `daly ychey` / `sols daro` / `ychty` / `saino` / `saldy` / `dainy`. `sal` (P=48), `okeedy` (P=103), `daly` (P=27), `ychey` (P=16) are too-common-in-P. `daro` / `ychty` / `dainy` are corpus hapaxes **inside a floating paragraph**, not captions next to a figure. **HYPOTHESIS:** do not promote `Pb` to `L`.

---

## 3. Hypothesis 1 - `qo-` is still 0 on labels on f75r

**Pre-registered kill:** if any `Lf` / `Lc` / `Lp` / other `L` on this page starts with `qo-`, the constraint BREAKS.

**Result: SURVIVES (vacuous).** L = 0, so `qo-` on L = **0**. No label exists to break the ban.

This is **not** a two-sided score. The interesting half of the split is still visible in P:

| Band | n | ok | ot | ok+ot | qo- |
|---|---|---|---|---|---|
| IT f75r P | 422 | 16 | 20 | **36 (8.5%)** | **108 (25.6%)** |
| IT f75r L | 0 | 0 | 0 | - | **0** |
| IT f75r P0 | 412 | 15 | 20 | 35 | 108 |
| IT f75r Pb | 10 | 1 (`okeedy`) | 0 | 1 | 0 |
| ZL f75r P | 390 | - | - | 37 | 107 |
| Corpus IT P | 34,486 | 2,060 | 1,864 | 11.4% | 15.1% |
| Corpus IT L | 1,038 | 166 | 177 | 33.0% | 0.9% (9 tokens) |

`qo-` is **legal and heavy** in this Currier-B prose (25.6% vs corpus P 15.1%). `ok+ot` is **light** (8.5% vs corpus P 11.4%, vs corpus L 33.0%). That is the inverse of a label page, and it is what the held split predicts for running text.

The 9 corpus `qo-` labels remain the known non-herbal / non-pharma set: f66r `L0` (`qor` / `qotesy` / `qokal` / `qolsa`), f67r2 `@Ls` (`qotoear`), f73v `&Lz` (`qokeoly`), **f75v `Ln`/`Lt`** (`qokal` / `qoted` / `qotedy`). `Lf` / `Lc` / `Lp` are still 0. **Do not score f75v in this file.** It is the next unused folio and the first balneo page that actually has `L`. The strict "any L" reading of the ban is already known to be stressed there; that is a job for cycle 2, not a break on f75r.

**HYPOTHESIS (survived, manuscript-wide for balneo, provisional: one page):** `qo-` is prose-legal on f75r and label-illegal because there are no labels. The ban did not break.

---

## 4. Function-like tokens - `daiin` / `dain` / `chol` / `chor` / `ol` / `or`

Held: these are function-like, not names. Tested on a page with no captions.

| EVA | IT f75r P | IT f75r L | Corpus P | Corpus L |
|---|---|---|---|---|
| **daiin** | **0** | 0 | 834 | 7 |
| **dain** | **7** | 0 | 207 | 1 |
| **chol** | **0** | 0 | 384 | 2 |
| **chor** | **0** | 0 | 217 | 1 |
| **ol** | **13** | 0 | 521 | 1 |
| **or** | **5** | 0 | 345 | 4 |

`dain` loci (7 tokens / 5 lines): `.2`, `.26` (x2), `.29` (x2), `.30`, `.46`. Bare `daiin` is absent; `.30` has `qodaiin` (a `qo-` compound, not the bare token). `chol` / `chor` are absent. That is expected Currier-B behaviour, not a wound: the B workhorses take the slot.

B-language workhorses on this page (all P, all too-common-in-P, **HYPOTHESIS:** formula / generic predicate, not names):

| EVA | f75r P | Corpus P | Corpus L |
|---|---|---|---|
| qokain | 22 | 279 | 0 |
| shedy | 16 | 417 | 1 |
| qokeedy | 14 | 305 | 0 |
| qokedy | 14 | 272 | 0 |
| shey | 13 | 273 | 0 |
| chedy | 12 | 490 | 0 |
| qoky | 7 | 147 | 0 |
| qokar | 7 | 151 | 0 |
| qokal | 4 | 187 | 2 |

**HYPOTHESIS (survived, manuscript-wide for balneo, provisional: one page):** `daiin` / `dain` / `chol` / `chor` / `ol` / `or` are not names on f75r. `dain` / `ol` / `or` fire in prose. `chol` / `chor` sit out (B page). None can be a caption, because there is no L.

---

## 5. Hypothesis 2 - type-word families `-oldy` and `otal~`

Held: `-oldy` and `otal~` are type-word families, not species. Presence on this page supports manuscript-wide-for-balneo. Absence is **not** a kill (first balneo page). A new repeating family that behaves like a type-word would be a LOCK.

### 5.1 `-oldy` - PRESENT in P, absent in L (L empty)

IT tokens on f75r that end in `oldy` or sit in the scored nest:

| EVA | Locus | Band | Corpus P | Corpus L |
|---|---|---|---|---|
| **koldy** | f75r.39 `+P0` | P | 6 | 0 |
| **oldy** | f75r.43 `+P0` (x2) | P | 26 | 1 (f99v.4 `@Lf` only) |
| **okoldy** | f75r.44 `+P0` | P | 6 | 2 (f68r1 `@Ls`, f82r.37 `@Ln`) |

`otoldy` / `toldy` / `ytoldy` / `tsholdy` / `yteold` / `yteoldy` = **0** on this page.

ZL control agrees on `koldy` `.39` and `okoldy` `.44`. Two space-model stresses, IT primary:

- f75r.35: IT `qokar.ol.dy` vs ZL first-alt `qoka[in:r].oldy` -> ZL adds a third `oldy`. Not imported.
- f75r.43: IT `otar.oldy` (two tokens) vs ZL `otar,oldy` joined -> `otaroldy`. IT keeps the second `oldy`.

**HYPOTHESIS:** the `-oldy` nest is in balneo **prose**, not as a caption. `oldy` x2 on one line is the same type-word already scored as a pharma `Lf` (f99v.4) and as P=26. `okoldy` / `koldy` are prefix variants (`ok-` / `k-` + `oldy`), the same kind of nest already refused as species. Do not read any of them as a bath, a pipe, or a figure.

Presence in P on the first balneo page **supports manuscript-wide-for-balneo** (provisional: one page).

### 5.2 `otal~` - ABSENT in P and L

Exact scored members `otal` / `otaly` / `otaldy` = **0 / 0** on f75r.

Do **not** drag in `otar` (page x7, corpus P=124, L=3), `otam` (page x1, P=44), or `otain` (page x1, P=95). Those are too-common-in-P and were already refused as species readings of `otal`. Shared `ot-` is not a merge.

Absence of `otal~` is **not a kill**. The family remains a type-word on the pages that actually have it. First balneo page is allowed to miss it.

### 5.3 `dam` - ABSENT

`dam` = 0 on f75r. Corpus still P=93, L=2 (f65r `@Lp`, f99r.40 `@Lf`). Formula claim is not tested here and does not die by absence. **HYPOTHESIS (survived, manuscript-wide for balneo, provisional: one page, absent-not-kill).**

### 5.4 Adjacent `-aldy` - recorded, not merged, not a LOCK

| EVA | Locus | Corpus P | Corpus L |
|---|---|---|---|
| okaldy | f75r.27 P | 7 | 2 (zodiac `Lz`) |
| daldy | f75r.31 P | 16 | 1 (**f75v.32 `@Ln`** - next page, not scored) |
| saldy | f75r.52 Pb | 2 | 0 |

One hit each. Not a repeating on-page family. Not merged with `-oldy` (same rule that kept `otal~` unmerged). Not a LOCK.

### 5.5 No new type-word LOCK

Repeating tokens with page n>=2 and corpus P<20: `pchey` (2 / 12), `lo` (2 / 15), `sheety` (2 / 8), `yshedy` (2 / 10). None is `ok-`/`ot-` class, none is a label, none behaves like `otoldy` (most-repeated pharma L **and** prose). The page's actual repeats are the B workhorses in S4 (`qokain` 22, `shedy` 16, ...) - too-common-in-P.

25 page/corpus hapaxes exist in P (`ady`, `chedykar`, `chekam`, `dackhy`, `dainy`, `daro`, ...). Unglossed. Not promoted. A hapax in running text on a page with no labels is not a name candidate.

**H2 result:** `-oldy` **present** in P; `otal~` **absent** in P and L; no new family locked. Presence of `-oldy` supports manuscript-wide-for-balneo. Absence of `otal~` is not a kill.

---

## 6. Labels (none) - repeating-label table

There are **no** `L` tokens on f75r. The repeating-label triage (type-word vs too-common-in-P vs unglossed hapax) has nothing to triage.

If the floating `Pb` block is ever re-flagged as labels by a later transliteration, the triage **HYPOTHESIS** would be: `sal` / `okeedy` / `daly` / `ychey` = too-common-in-P; `saino` / `saldy` / `sols` = uncommon, not hapax; `daro` / `ychty` / `dainy` = unglossed hapax. That is a note for a parser change, not a finding of this cycle. IT and ZL both keep them as `P`.

---

## 7. IT vs ZL (control only)

36 of 53 loci disagree. Most are comma-joins (ZL concatenates). Letter-level stresses worth keeping:

| Locus | IT (primary) | ZL (control) | Why it matters |
|---|---|---|---|
| .4 | `or.shey` | `ok.shey` | `or` vs `ok` |
| .8 | `qotardy` | `qokardy` | `t`/`k` |
| .11 | `qokain` | `qokair` | minim |
| .16 | `otshedy` | `okshedy` | `t`/`k` |
| .21 | `oqekain` | `oqokain` | `e`/`o` |
| .25 | `saiin` | `sain` | minim |
| .26 | `ady` | `ajy` (joined `darajy`) | weirdo |
| .27 | `otedy` | `otody` | vowel |
| .30 | `qodaiin` | `qodain` (from `qo,dain`) | minim; not bare `daiin` |
| .32 | `qokar` | `qotar` | `k`/`t` |
| .35 | `qokar.ol.dy` | `qokain.oldy` | **extra ZL `oldy` - not imported** |
| .43 | `otar.oldy` | `otaroldy` | IT keeps the second `oldy` |
| .49 | `daro` | `dara` | Pb hapax vowel |

No ZL disagreement creates a `qo-` label. No ZL disagreement creates an `L` locus. The control does not break H1.

---

## 8. What SURVIVED / what did not fire / what is still dead

**Every row is a HYPOTHESIS.**

| Held constraint | This page | Mark |
|---|---|---|
| `qo-` banned on labels (legal in P) | 0 L, so 0 `qo-` on L. P `qo-` 25.6%. Did not break. Vacuous two-sided. | **manuscript-wide for balneo** (provisional: one page) |
| `daiin` / `chol` / `chor` function-like, not names | `daiin` 0, `dain` 7 P, `chol`/`chor` 0, `ol` 13, `or` 5. No captions. | **manuscript-wide for balneo** (provisional: one page) |
| `-oldy` is a type-word family, not a species | Present in P: `oldy` x2, `okoldy`, `koldy`. | **manuscript-wide for balneo** (provisional: one page). Presence supports. |
| `otal~` is a type-word family, not a species | Absent. Not a kill. | Held law not wounded. Not a positive balneo witness. |
| `dam` is formula | Absent. Not a kill. | **manuscript-wide for balneo** (provisional: one page, absent-not-kill) |
| `ok-`/`ot-` label-legal | No L to score. P ok+ot 8.5% (prose-like). | Not wounded. Not a two-sided confirm. |

**Still dead (not revived):** three-name titles; visual twins as lexical matches; species readings of `otoldy` / `oky` / `okary` / `okam` / `otal`; `keerodal` grind; plant ID; language ID; EVA-as-phonemes; paint letters as EVA (none here).

**No new type-word family locked.** Steward does **not** need a break/lock copy. The brief is written for the cycle record only.

---

## 9. Next folio

**f75v** - first unused page in f75-f84 after f75r. Law did not break, so the cycle does not STOP.

f75v is the first balneo page with actual labels (quire 13: 20 nymph labels, 7 tub/tube labels, 6 stand-alone characters; 70 loci). Corpus already lists three `qo-` tokens on f75v `Ln`/`Lt` (`qokal`, `qoted`, `qotedy`). That is the pre-registered stress for cycle 2: the strict "any L" reading of the `qo-` ban vs the series' harder `Lf`/`Lc`/`Lp` = 0 reading. Also sitting on f75v, not scored here: `oldy` in P, `otal` as `@Lt`, `daldy` as `@Ln`.

**Not next:** f41r, f111v, f2v, `keeodal`, another herbal, a `keerodal` re-grind.

---

## 10. Bottom line

One balneo page. No translation. No plant ID. No language ID. No labels.

**IT f75r: P 422 / 195 types; L 0. `qo-` on L = 0 (vacuous survive). `-oldy` present in P; `otal~` absent. Held laws did not break. Next is f75v.**

Paths:

- Notes: `notes/gauntlet-1-f75r.md`
- Steward brief: `(internal steward brief, omitted)`
- Extract: `(local stats extract, not published)`
- Stats: `(local stats extract, not published)`
