# Voynich pass 6 - f65r working notes (not a translation)

**For:** Jon Bailey
**Date:** 14 Aug 2026 (ET)
**Status:** constrained sixth pass on the leftover herbal name-page. **No verified full translation of Beinecke MS 408 exists.** Nothing below is a decipherment. Every gloss is marked **HYPOTHESIS**. No plant is identified. The f9v Viola / herba trinitatis literature ID, the f10v hellebore catalogue note, the ZL "faces capsicum" comment, and the quire-8 ELV/ThP IDs for this drawing (geranium / rue / dropwort / *Spiraea filipendula*) are **not imported**.

This note finishes the experiment pre-registered in pass 5 S7: take f65r (`$I=H`), the only multi-word herbal whole-plant label in IT (`otaim.dam.alam`, `@Lp`), and test whether the three tokens are three names, or a rare head plus formula. Pass 4 already put `dam` on f99r.40 as `@Lf`. Pass 5 already put `dam` in f99v.34 P. A pure "three-name title" was already unlikely. This page is where that prediction is scored.

Sources were already on disk. They were not re-downloaded. Stats in `(local stats extract, not published)` were computed against the files this pass. Raw loci: `(local stats extract, not published)`.

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
| Folio description f65r | https://www.voynich.nu/q08/index.html (quire 8; site update 15/06/2025) |
| Colour-letter table | https://www.voynich.nu/writing.html (update 13/06/2025), keyword COL |
| Manuscript | Yale, Beinecke Rare Book & Manuscript Library, MS 408 |
| Prior notes | `notes/pass-1.md`, `notes/pass-2-f9v.md`, `notes/pass-3-f10v.md`, `notes/pass-4-f99r.md`, `notes/pass-5-f99v.md` |

**Tokenisation (IVTFF 2.0), same as the pass-2 / pass-3 / pass-4 / pass-5 practice.** `.` is a word break. `<->` is a **word space** (do not strip and concatenate). All remaining `<>` markup is stripped (`<%>`, `<$>`, `<!...>`, leftover `<@H=n>`). Tokens must contain at least one A-Z letter. `?` is kept if present. Paragraph text = loci whose flags contain `P`. Labels = flags containing `L`.

ZL is the **control**, not the running text. ZL extras: uncertain commas are **joined** (not a space); alternatives `[a:b]` take the first reading; ligature braces `{ct}` / `{cthh}` / `{ck}` expand to their contents.

Stripping leftover `<@H=n>` markup (two inline hand tags on f115r, not on f65r) keeps this parse's corpus totals in line with pass 2 / 3 / 4 / 5: **34,486 P / 7,140 types; 1,038 L / 763 types**.

**What this is not:** a download of any copyrighted monograph, a Cheshire/Gibbs-style "complete solution," a language identification, a claim that EVA letters are phonemes, a plant identification, or a public post.

---

## 2. Folio text used

### 2.1 Why f65r

Pass 5 pre-registered this page because:

- It is the leftover name-page from pass 1: the only multi-word herbal `@Lp` in IT.
- `dam` is now an `Lf` on f99r.40 **and** a P-word on f99v.34. That already wounds "three unique names in a row." This page is where `otaim` / `dam` / `alam` have to be counted properly.
- The `otoldy` / `otal~` type-word families do **not** need a third pharma witness.
- Do **not** import viola, hellebore, capsicum, or the quire-8 catalogue IDs.

Page header from IT2a-n (identical flags in ZL):

```
<f65r>  <! $Q=H $P=E $F=y $B=2 $I=H $H=3>
```

`$Q=H` quire 8, `$I=H` herbal, `$H=3` LFD hand 3. **No `$L=` Currier-language flag** on this page (IT or ZL). Quire 8 (https://www.voynich.nu/q08/index.html): RZ language **-** (page) / **C** (folio) / **A** (bifolio); LFD hand 3. Currier language: unmarked.

### 2.2 Public folio description (quire 8 only)

**Sourced, not invented.** Quire 8 page, current as of the 15/06/2025 site update:

- Herbal page. Folio number 65 in the upper right corner.
- A plant drawing completely filling the page. Roots have bulbs; leaves have fingers with frills, **very much like f57r**. Many small starry flowers, **without any paint**.
- **1** text item: **1 plant label**. "There are only two (or three?) words of writing near the plant (label)." Matches IT (one `@Lp` locus, three period-separated words) and ZL (one `@Lp` locus, uncertain comma then a period - two or three words depending on the space model).
- Herbal drawing characterisation (Gheuens/Rapaport): (none).
- writing.html (Labels): "A few whole plant labels in the herbal sections, on f2r, f41v (uncertain) and f65r."

The f57r lookalike is a **drawing** note. This pass does **not** run a twin-token test on f57r (not pre-registered; do not fish). Checked only so the refusal is evidenced: `otaim` / `dam` / `alam` / `keerodal` are **0** on f57r (87 P tokens, 0 L).

**Catalogue IDs printed on the quire-8 f65r block, recorded and unused:** ELV geranium; ThP rue, dropwort, *Spiraea filipendula*. Same status as the f9v viola / f10v hellebore / ZL capsicum notes. **Not imported. Not used as a crib.**

### 2.3 Labels vs running text

This page has **no running text**. It is a one-locus label page.

| Band | IT loci | IT tokens |
|---|---|---|
| Running text (`P`) | **0** | **0** |
| Labels (`L`) | 1 (`@Lp`) | **3** (`otaim`, `dam`, `alam`) |
| Whole-plant `Lp` | **1** | 3 |
| `Lf` / `Lc` | 0 / 0 | - |

ZL, under the comma-join rule: **2** tokens (`otaimdam`, `alam`). If the ZL comma is treated as a space instead, ZL matches IT (`otaim`, `dam`, `alam`). The quire page's "two (or three?)" is exactly this disagreement.

### 2.4 The Lp (IT primary; ZL control)

| Locus | Flag | IT EVA | ZL EVA | Notes |
|---|---|---|---|---|
| f65r.1 | `@Lp` | **otaim.dam.alam** | **otaim,dam.alam** | IT: three certain word-spaces. ZL: uncertain space (`comma`) between `otaim` and `dam`, certain space before `alam`. |

**Exact readings**

- IT (as in the file): `otaim.dam.alam` -> tokens **`otaim` `dam` `alam`**.
- ZL (as in the file): `otaim,dam.alam`.
- ZL under this series' tokenisation (commas joined): **`otaimdam` `alam`**.
- ZL if the comma is a space (sensitivity, not the running parse): `otaim` `dam` `alam` - agrees with IT.

The space disagreement is **only** the first break. Both files agree that `alam` is a separate word. Both files agree there is no `qo-` on this locus. ZL's own comment: "Plant with only two or three words next to it, treated as a label."

`otaimdam` is a **hapax invented by the join**. It does not exist as a string anywhere else in IT or ZL. It is not promoted to a name.

### 2.5 f65r running text

**None.** No `P` locus in IT or ZL. Prefix scores and function-word counts on P are **not scorable** on this page. That is a property of the folio, not a missing extract.

The verso (f65v) has two short centred paragraphs (6 P loci). It is **not** this pass. Record only: the verso does **not** repeat `otaim`, `dam`, or `alam` as exact tokens. `dalam` sits on f65v.2 - a different string, not fished.

### 2.6 IT vs ZL (control)

One locus, one disagreement, and it is the one that matters.

| Locus | IT | ZL (raw) | ZL (comma joined) |
|---|---|---|---|
| f65r.1 `@Lp` | `otaim` `dam` `alam` | `otaim,dam.alam` | `otaimdam` `alam` |

Function-word **direction** is stable (all zero on the page). The `ot-` head is stable (`otaim` / `otaimdam`). `alam` is stable. `dam` as a standalone label-word is IT-only on this page; ZL swallows it into the join.

Whole-corpus `Lp` inventory also splits:

| File | `@Lp` loci | Tokens |
|---|---|---|
| IT | **2**: f41v.1 `keerodal`; f65r.1 `otaim dam alam` | **4** tokens / 4 types |
| ZL | **3**: f2r.14 `ytoail`; f41v.1 `keer[e:o]dal` -> first-alt **`keeredal`**; f65r.1 `otaimdam alam` | 4 tokens / 4 types |

writing.html lists f2r as a whole-plant label; IT does **not** mark any `L` on f2r (the page is P-only in IT). ZL's `ytoail` is a ZL-only `Lp`. Not used as a finding of this pass. f41v remains the other IT `Lp`.

---

## 3. Stats (verified on IT2a-n / ZL3b-n this pass)

Method: same as pass 5, with the `<->` = space rule and the `<@H=n>` strip stated in S1. Every number below is computed from the files this pass. Corpus P/L totals **match pass 2 / 3 / 4 / 5**: 34,486 P tokens / 7,140 types; 1,038 L tokens / 763 types.

### 3.1 f65r running text (IT)

| Measure | Value | Source |
|---|---|---|
| Word tokens | **0** | no `P` locus |
| Word types | 0 | - |
| Paragraphs | 0 | - |
| EVA word-initial `qo-` | n/a | no P |

**Function-word check (the pass-1 / 2 / 3 / 4 / 5 table), now on a P-less label page**

| EVA | f65r P IT | f65r P ZL | f65r L IT | f65r L ZL | IT P corpus | Notes |
|---|---|---|---|---|---|---|
| daiin | 0 | 0 | **0** | 0 | 834 | not the Lp. Prediction held. |
| dain | 0 | 0 | 0 | 0 | 207 | absent |
| chol | 0 | 0 | 0 | 0 | 384 | not the Lp |
| chor | 0 | 0 | 0 | 0 | 217 | not the Lp |
| ol | 0 | 0 | 0 | 0 | 521 | not the Lp. Page is not a herbal-A prose test. |
| or | 0 | 0 | 0 | 0 | 345 | not the Lp |

Prediction from pass 1 / 5: if there is P-text they stay common; they should **not** be the Lp. **Second half held.** First half is vacuously untested (no P). f2v remains the herbal-A ol/or control.

### 3.2 f65r labels (IT)

| Measure | Value | Source |
|---|---|---|
| Word tokens | **3** | verified |
| Word types | **3** | verified |
| Type/token ratio | **1.000** | computed |
| Hapax types on the page | 3 | no exact string repeats (n=3) |
| Mean / median word length | 4.33 / 4 | computed (`otaim` 5, `dam` 3, `alam` 4) |
| `Lc` / `Lf` / `Lp` | 0 / 0 / 1 | IT flags |

ZL (comma joined): 2 tokens / 2 types (`otaimdam`, `alam`).

**Word-initial bigrams on f65r L (IT):** ot 1, da 1, al 1. **qo = 0.**

### 3.3 ok-/ot- vs qo- (the label-prefix test, P-less page)

Corpus rates this parse (match pass 2 / 3 / 4 / 5):

| Band | n | ok- | ot- | ok+ot | qo- |
|---|---|---|---|---|---|
| IT P | 34,486 | 6.0% | 5.4% | **11.4%** | **15.1%** |
| IT L (all) | 1,038 | 16.0% | 17.1% | **33.0%** | **0.9%** |
| IT Lf only | 216 | 12.5% | 16.7% | 29.2% | **0** |
| IT Lc only | 40 | 17.5% | 15.0% | 32.5% | **0** |
| IT Lp only | 4 | 0 | 1 (`otaim`) | **1/4** | **0** |

The 9 corpus `qo-` labels are still not herbal-plant / pharma: f66r `L0` (qor, qotesy, qokal, qolsa), f67r2 `@Ls` qotoear, f73v `&Lz` qokeoly, f75v `Ln`/`Lt` (qokal, qoted, qotedy). **`qo-` remains 0 on `Lf` / `Lc` / `Lp`.**

**This page**

| Prefix | f65r P IT (n=0) | f65r L IT (n=3) | f65r P ZL (n=0) | f65r L ZL (n=2) |
|---|---|---|---|---|
| `ok-` | n/a | 0 | n/a | 0 |
| `ot-` | n/a | 1 (`otaim`) | n/a | 1 (`otaimdam`) |
| ok+ot | n/a | **1 / 3 = 33.3%** | n/a | **1 / 2 = 50%** |
| `qo-` | n/a | **0 / 3 = 0%** | n/a | **0 / 2 = 0%** |

Prediction from pass 5: `otaim` is an `ot-` whole-plant label; `qo-` should not appear on the `Lp`.

- **L `qo-` survived.** 0 in IT, 0 in ZL. Same suppression as every `Lf`/`Lc`/`Lp` in the series.
- **L ok+ot sits on the label rate in IT** (33.3% on n=3). ZL 50% is the same one `ot-` token over a smaller denominator. Small-n: do not over-read the percentage. The **direction** (legal `ot-` head, illegal `qo-`) is what was predicted.
- **P side cannot be scored.** No running text. That is not a wound and not a save.

### 3.4 otaim / dam / alam (the point of this pass)

**IT corpus (this parse)**

| EVA | P | L | all | Other life (IT) | Role this pass |
|---|---|---|---|---|---|
| **otaim** | **1** | **1** | 2 | P: f111v.3 `+P0` (quire 20, `$I=S` recipes/stars, language B, hand 3). L: **this page only**. Exact string nowhere else. | rare head. Name-*shaped*. Not unique (one P hit). |
| **dam** | **93** | **2** | 98 | L: f65r.1 `@Lp` + **f99r.40 `@Lf`**. Plus 3 non-P/non-L: f70r1.8 `@Ri`, f70r1.10 `@Ri`, f86v4.4 `@Cc`. P hits all over herbal, pharma, bio, stars (including **f99v.34** and **f41v.3**). | **too-common-in-P / formula.** Cannot be "name 2 of 3." |
| **alam** | **7** | **1** | 8 | L: **this page only**. P: f58r.8, f58v.26, f104r.20, f107r.14, f108r.12, f111r.28, f111v.21 - all `$I=S` (quire-8 star-text + quire 20). **0** in herbal P. | uncommon prose word; **not** a hapax; only label hit is this Lp. Formula-or-epithet, not a second unique name. |
| otaimdam | 0 | 0 | 0 | ZL-join artefact on this page only | not a token in IT |

**ZL control (comma-joined)**

| EVA | P | L | Notes |
|---|---|---|---|
| otaim | 1 (f111v.3) | **0** | the f65r head is swallowed into `otaimdam` |
| dam | 71 | 1 (f99r.40 `@Lf` only) | f65r `dam` disappears into the join; still an `Lf` on f99r and common in P |
| alam | 5 | 1 (f65r.1) | still the stable third word |
| otaimdam | 0 | 1 (f65r.1 only) | hapax join; 0 in P |

`dam` P is 93 IT / 71 ZL because ZL joins some `dam` into neighbours (the same space-model effect as earlier passes). **Direction is stable:** `dam` is a common prose word and an `Lf` on f99r whether or not f65r keeps it as a separate token.

**The f111v.3 `otaim` (the only P hit)**

IT (ZL agrees on the last word):

```
f111v.3   dain chedy shedal otedy oteeo chedy qokeey dain chcthar otar qotain otaim
```

Line-final, in a recipes/stars B paragraph, sitting next to `qotain` in a page that is saturated with `otain` / `qotain` / `otaiin`. **HYPOTHESIS:** the P hit is a rare tail-variant of the common `otaiin`/`otain` family (`m` for `n`/`in`), not "the f65r plant-name reused as a recipe title." It is still the same string. That is enough to keep `otaim` off the "unique Lp hapax" slot that `keerodal` still occupies (P=0).

Do **not** fish f111v. Not a plant page. Not pre-registered.

**`otalam` (adjacent, not merged, not fished as a name)**

IT: P=1 (f76r.42), L=2 (f70v2.25 `&Lz`, f99r.13 `@Lf`). Shared `-alam` tail, different head (`ot-` + `al` vs `otaim`). Already on the pass-4 f99r label list. **Not** folded into `alam` and **not** treated as the f65r plant name.

**`dam` as a substring on other labels (record, do not promote):** `oldam` f89r1.3 `@Lf`, `saldam` f89r1.25 `@Lf`, `doldam` f99v.31 `@Lf`, plus zodiac `okldam` / `damamm`. These are different tokens. They show that `-dam` is label-legal as a tail, which is the opposite of "`dam` is a unique name."

### 3.5 Repeating labels on f65r

Exact string repeats on the L set: **none.** 3 tokens, 3 types (IT). The interesting repeat is **cross-page**: `dam` as `@Lp` here and `@Lf` on f99r.40.

That cross-page repeat is a **negative** for "`dam` is this plant's name." A workhorse that is 93x in P and also captions a quire-19 root-fragment cannot be the unique name of the f65r whole plant.

### 3.6 Prior hapax sets (record, do not fish)

| Set | Hits on f65r L | Hits on f65r P |
|---|---|---|
| f9v hapax set (`fochor`, `oporody`, `qopchypcho`, `olcfholy`, `ypcheey`, `rokyd`, `kyty`, `chshoty`) | **0** | **0** (no P) |
| f10v hapax set (`chckhan`, `chcthor`, `olty`, `qokchyky`, `qotchytor`) | **0** | **0** |
| f10v extra P<5 (`otydy`, `qotoiin`, `choraiin`, `pcheey`) | **0** | **0** |
| `keerodal` | **0** | **0** |

Fifth consecutive miss for "a rare herbal-page token from f9v/f10v recurs as a later `Lf`/`Lc`/`Lp`." Still not fatal. Still a miss. `otaim` itself does **not** appear on f9v or f10v (already true in pass 4 / 5).

### 3.7 Colour / paint Latin letters

**Absent.**

Sourced: writing.html COL table (update 13/06/2025) has **no f65r row**. The quire-8 f65r block says the starry flowers are **without any paint**. writing.html also notes that all COL cases found so far are on language-A / LFD-hand-1 pages; f65r is LFD hand 3, Currier language unmarked.

**Not present in IT2a-n or ZL3b-n as EVA tokens.** No standalone Latin `p` / `r` / `g` / `rot`. Nothing to keep out, and nothing to import.

Folio number "65" in the upper right is a later folio number, not EVA.

### 3.8 Corpus totals vs earlier passes

This parse: **34,486 P / 7,140 types**; daiin 834, ol 521, chol 384, or 345, chor 217, dain 207. **1,038 L / 763 types.** Matches pass 2 / 3 / 4 / 5. Pass 1's 33,707 / daiin 776 pair remains unverified.

IT `Lp` tokens this parse: **4 / 4 types** (`keerodal`, `otaim`, `dam`, `alam`). ok+ot = 1/4 (`otaim`); qo- = 0. Matches the pass-5 corpus-Lp row.

---

## 4. What survived / died from pass 1-5 predictions

Pre-registered tests, scored honestly.

1. **`dam` is formula (already Lf + P); `otaim` stays the rare head; `alam` needs a count.** **Survived, and this is the first time the three tokens are scored on their own page.** `dam` P=93, L=2 (this Lp + f99r.40 Lf), plus P on f99v.34. `otaim` P=1 / L=1. `alam` P=7 / L=1 (this page only). Three-name title is **dead**. Rare-head + formula is the remaining reading.

2. **ok-/ot- is label-legal; qo- may appear in running text, not on labels.** **Survived on L; P untested.** f65r L: qo- **0**, ok+ot 1/3 (IT) / 1/2 (ZL). The head is `ot-`. Whole-corpus `Lf`/`Lc`/`Lp` qo- remains 0. No P on the page, so the two-sided score cannot be repeated here.

3. **daiin / chol / chor stay function-like, not names.** **Survived (they are not the Lp).** 0/0 on this page. The prediction was that they should not be the caption. They are not.

4. **Unique rare tokens are the only name candidates.** **Survived as a filter, and it demotes two of the three words.** Only `otaim` still looks name-*shaped*, and even that has a recipes-section P hit. `keerodal` (f41v, P=0) is now the cleaner leftover unique `Lp`.

5. **Do not identify any plant as a species. Do not import viola, hellebore, or capsicum.** **Held.** Quire-8 ELV/ThP IDs (geranium / rue / dropwort / *Spiraea filipendula*) recorded in S2.2 and left unused. f57r lookalike stays in the catalogue column. No rare EVA token was mapped onto a medieval plant name.

6. **Colour letters stay out of the EVA gloss.** **Held** (vacuously: no COL row, no paint on the flowers).

7. **f9v / f10v hapax recurrence.** **Miss, not fatal.** Fifth miss.

---

## 5. Hypothesis gloss table

**Every row is a HYPOTHESIS.** Confidence is structural (distribution + position), never semantic. "Gloss" means *role in English*, not a claimed Voynichese meaning. No row identifies the language. No row identifies a plant.

### 5.1 The three Lp tokens

| EVA | Where | Role (HYPOTHESIS) | Constrained gloss (HYPOTHESIS) | Why this pass allows it | Why it may be wrong |
|---|---|---|---|---|---|
| **otaim** | f65r.1 `@Lp` (IT); 1x P on f111v.3 | rare head of a whole-plant label | **candidate plant-name piece**, not a verified name. "item/herb ___" if `ot-` is the classifier | `ot-` is label-legal. Exact string is almost unique (2). Only herbal `Lp` head of this shape. | The f111v.3 P hit sits in an `otain`/`qotain` nest - may be a minim/tail variant of a common family, not a name at all. ZL can join it to `dam` (`otaimdam`). One token on the drawing. |
| **dam** | f65r.1 `@Lp` (IT only); f99r.40 `@Lf`; 93x P; also f99v.34 P, f41v.3 P | formula / too-common-in-P | **not** a plant name. "of / and / this" **or** a generic caption-word | P=93. Already an `Lf` on a different quire, different section, different drawing class. ZL is willing to glue it to the head. | If a better space-model makes most of the 93 P hits *not* `dam`, the commonness is an artefact. Not this parse. IT and ZL both keep f99r.40 as `dam`. |
| **alam** | f65r.1 `@Lp` (IT and ZL); 7x P, all `$I=S` | uncommon formula / epithet | **not** a unique species name. A second formula word, or a weak epithet | P=7 is too many for a unique name and too few for a workhorse. Never a label except here. Never in herbal P. | If the seven stars-section hits are independently the same lemma *and* those pages name this plant, upgrade it. Currently they are recipes/stars prose on other quires. |
| **otaimdam** | ZL join of f65r.1 only | space-model artefact | **no gloss.** Not a third reading | Hapax invented by joining an uncertain comma. 0 in P. | If independent transliterations (GC/v101, RF) also write one word here, the IT three-word parse is the artefact. Quire page already says "two or three?" |
| **ot-** (prefix on the head) | this `Lp`; corpus L 17.1% | label-legal classifier | "item/herb-of ___" | Predicted, observed. `qo-` still 0 on the Lp. | Dual use of `ot-` in prose (`otaiin` family) weakens "classifier only." |

### 5.2 Prefix split and function words (re-tested where possible)

| EVA | Role (HYPOTHESIS) | Constrained gloss (HYPOTHESIS) | Why this pass still allows it | Why it may be wrong |
|---|---|---|---|---|
| **ok- / ot-** (prefix) | label-legal classifier / construction | "item/root/herb-of ___" | 1/3 of f65r L (the head). Corpus 33.0% vs 11.4%. Whole `Lp` set 1/4. | n=3. The other two words are not `ok-`/`ot-`. |
| **qo-** | prose-legal, label-illegal | legal running-text vocabulary; **not** names | **0** on f65r L. Still 0 on all `Lf`/`Lc`/`Lp`. | P side of this page cannot test the "legal in prose" half. |
| **daiin / chol / chor / ol / or** | closed-class / generic | not names | 0 on this Lp, as predicted. | Vacuous on P (no P). f2v is still the herbal-A control. |

**Explicitly refused glosses (this pass):**

- EVA letters as Latin phonemes (`otaim` != a pronounced word; `dam` != Latin *dam* / German *Damm*; `alam` != Arabic *alam* / Latin *alam*).
- `otaim` / `dam` / `alam` as any plant name (geranium, rue, dropwort, *Spiraea*, viola, hellebore, capsicum, or anything else).
- A "three-name title" or a full caption translation ("X of Y Z", "X and Y Z", etc.) written as if verified.
- Any named language (Latin, German, Nahuatl, Hebrew, Occitan, Welsh, proto-Romance, Arabic, etc.).
- Importing the quire-8 ELV/ThP IDs, the f9v viola ID, the f10v hellebore catalogue note, or the ZL "capsicum" comment onto this drawing.
- Treating the f57r lookalike as "the same plant" in EVA. The lookalike is a published **drawing**. No token is shared.
- A twin-token test on f65v `dalam`, on f111v, or on `otalam`. Not pre-registered; not run as a name hunt.
- A full translation of a page that has three words.

**Strongest claim this pass will defend:**
The only multi-word herbal whole-plant label in IT is **not** three names. `dam` is formula (93x P, already an `Lf` on f99r, also in f99v P). `alam` is an uncommon stars-section prose word (P=7) that is a label only here. `otaim` is the rare `ot-` head (L=1, P=1) and is the only token on the page that still *could* be a name-piece - and even that has a recipes-line P hit next to `qotain`, so it is no longer as clean as `keerodal`. `qo-` is still banned on the `Lp`. IT and ZL disagree on whether the first break is a word space. None of this is a plant identification.

---

## 6. What would falsify this pass

1. **"dam is formula, not a name" dies if** a folio whose plant is independently identified uses `dam` *only* as a unique caption and the 93 P hits are shown to be a different lemma under a better space-model. Observed: the opposite (common P + a second `Lf` on f99r).

2. **"otaim is the rare head" dies if** independent transliterations (GC/v101, RF) read the first word as a common `otaiin`/`otain`, **or** if the f111v.3 hit is the same drawing-class / same plant (it is a stars page; it is not). ZL's join to `otaimdam` is a stress, not a kill.

3. **"alam is not a unique name" dies if** the seven `$I=S` P hits sit only in captions of this same plant *and* never in unrelated prose. Observed: they are recipes/stars running text on other folios.

4. **"three-name title is dead" is reversed if** a pre-registered substitution yields three matching medieval plant-name elements on this locus **and** the `dam`/`alam` extra-page hits are independently the same three plants. Not observed. Not attempted.

5. **qo- label ban dies if** a clean `Lf`/`Lc`/`Lp` `qo-` label appears in IT/ZL. Not on this page. Not on any pharma/herbal plant label in this parse.

6. **"no f9v/f10v name on f65r" dies if** an independent transliteration reads one of those hapaxes as this `Lp`. IT and ZL do not.

7. **Function-word claim for daiin / chol / chor dies if** a folio whose plant is independently identified uses one of them *only* as a unique caption. Observed on this page: they are not the caption.

8. **Geranium / rue / dropwort / Spiraea as catalogue notes (not fact) is violated if** a later note treats those IDs as established and imports them onto `otaim`. They are not.

9. **Constrained semi-language stance dies** on the same terms as pass 1 S6.5: a pre-registered simple substitution into a known language that yields grammatical running text **and** matching names on the rare / `Lp` words. Not observed. This page has no running text to satisfy the first half.

---

## 7. Next folio to try

**Primary next experiment: f41v (herbal B, the remaining unique `Lp`: `keerodal`).**

Why that page, given what this pass actually found:

- f65r is now scored. The three-name title is dead. `otaim` is name-*shaped* but no longer unique (P=1). The **cleaner leftover unique `Lp` is `keerodal`**: IT P=0, L=1, f41v.1 `@Lp` only.
- f41v has **both** bands: the `Lp` **and** 7 lines of running text (67 P tokens in this parse). That restores the two-sided `ok-`/`ot-` vs `qo-` score this page could not run, and it puts `daiin`/`chol`/`ol`/`or` back on a herbal page that actually has prose. `dam` already sits in f41v.3 P - a same-page check that the formula word is in the prose, not in the caption.
- ZL reads `keer[e:o]dal` (first-alt `keeredal`). The IT/ZL vowel split is the control, the same job `otaim`/`otaimdam` did here.
- Do **not** import viola, hellebore, capsicum, geranium, rue, dropwort, or *Spiraea* onto f41v.

**Protocol (pre-registered for pass 7):**

1. Transcribe f41v from IT **and** ZL; keep the `@Lp` (`keerodal` / `keeredal`) separate from the P-text.
2. Score `keerodal` against the whole IT P and L sets (prediction: still P=0, L=1). Note the ZL `[e:o]` split.
3. Score `ok-`/`ot-` vs `qo-` on L vs P. Prediction: `keerodal` is not `qo-`; running text may have `qo-`.
4. Count `daiin`/`dain`/`chol`/`chor`/`ol`/`or` in the P-text. Prediction: they stay common in P and are not the Lp. `dam` should be allowed in the prose (already visible on f41v.3).
5. Check the f9v hapax set and the f10v hapax set. A hit is a late positive. A miss is still not fatal.
6. Do **not** identify any plant as a species. Do **not** import viola, hellebore, capsicum, geranium, rue, dropwort, or *Spiraea*.

**Not next:** f2v (ol/or + function-word control). Still a valid later herbal-A control (`ol` 0 / `or` 0 on f2v in this parse - that is why it remains useful). The live leftover is the last unused unique `Lp`. Another quire-19 pharma page is not needed. f111v is a recipes page; do not chase the `otaim` P hit there.

---

## 8. Bottom line for this pass

f65r is readable as *structure*: one whole-plant label, no paragraph text, no paint letters, and a three-word (or two-word) caption whose pieces do **not** share a fate. `otaim` is a rare `ot-` head. `dam` is a book-wide formula word that already captions a different fragment on f99r. `alam` is an uncommon stars-section word, a label only here. IT and ZL disagree on the first space. It is not readable as *language*, and it is not a crib for the plant.

The pass-1 split survives its first real herbal `Lp` page in this series: **high-frequency ch/d-words are generic and are not the caption; `ok-`/`ot-` is label-legal; `qo-` is label-illegal; unique rare tokens are the only name candidates; a multi-word `Lp` is not automatically three names.** `dam` being common was the prediction; it held. `otaim` is the only token this pass will still *consider* as a name-piece, and it is unproven. `keerodal` on f41v is now the cleaner unique-`Lp` leftover.

Until `otaim` is found on a matching drawing under two transliterations - or until a pre-registered substitution reads this caption as grammar plus a name - this file is still a lab notebook, not a crib.

---

## Appendix A - raw IT loci for f65r (as in the file)

```
<f65r>     <! $Q=H $P=E $F=y $B=2 $I=H $H=3>
<f65r.1,@Lp>      otaim.dam.alam
```

Source: https://voynich.nu/data/IT2a-n.txt

## Appendix B - raw ZL loci for f65r (control)

```
<f65r>     <! $Q=H $P=E $F=y $B=2 $I=H $H=3>
# page 115
# herbal
# Plant with only two or three words next to it,
# treated as a label.
#
<f65r.1,@Lp>      otaim,dam.alam
```

ZL's "two or three words" comment is a catalogue note that matches the comma, **not** a finding of this pass. `alam` matches IT. The first break does not.

Source: https://voynich.nu/data/ZL3b-n.txt
