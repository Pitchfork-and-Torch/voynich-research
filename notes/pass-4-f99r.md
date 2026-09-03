# Voynich pass 4 - f99r working notes (not a translation)

**For:** Jon Bailey
**Date:** 14 Aug 2026 (ET)
**Status:** constrained fourth pass on one pharmaceutical folio. **No verified full translation of Beinecke MS 408 exists.** Nothing below is a decipherment. Every gloss is marked **HYPOTHESIS**. No jar-plant is identified. The f9v Viola / herba trinitatis literature ID and the f10v hellebore catalogue note are **not imported**.

This note finishes the experiment pre-registered in pass 3 S7: take f99r (`$I=P`), the type-word backup after the f10v / f89v2 twin miss, and test (a) whether `otoldy` / `toldy` / `ytoldy` / `tsholdy` behave as one lemma in a nest of other `Lf`/`Lc`, and (b) whether `qo-` stays banned on labels on a page that actually has many of them. A family that repeats as a class-word is a positive for "type-word, not species." A `qo-` label on this page would wound the prefix split.

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
| Folio description f99r | https://www.voynich.nu/q19/index.html (quire 19; site update 14/06/2025) |
| Manuscript | Yale, Beinecke Rare Book & Manuscript Library, MS 408 |
| Prior notes | `notes/pass-1.md`, `notes/pass-2-f9v.md`, `notes/pass-3-f10v.md` |

**Tokenisation (IVTFF 2.0), same as the pass-2 / pass-3 practice, not the pass-1 wording.** `.` is a word break. `<->` is a **word space** (do not strip and concatenate - pass 2 already split f9v.2 as `dy oty`; this pass does not regress that). All remaining `<>` markup is stripped (`<%>`, `<$>`, `<!...>`, leftover `<@H=n>`). Tokens must contain at least one A-Z letter. `?` is kept if present. Paragraph text = loci whose flags contain `P`. Labels = flags containing `L`.

ZL is the **control**, not the running text. ZL extras: uncertain commas are **joined** (not a space); alternatives `[a:b]` take the first reading; ligature braces `{ct}` / `{cthh}` / `{ck}` expand to their contents.

Stripping leftover `<@H=n>` markup (two inline hand tags on f115r, not on f99r) brings this parse's corpus totals into line with pass 2 / pass 3: **34,486 P / 7,140 types; 1,038 L / 763 types**. Without that strip the parser invented two spurious tokens (`H` and a glued `2>fshdar`-type remnant). Those two were never EVA.

**What this is not:** a download of any copyrighted monograph, a Cheshire/Gibbs-style "complete solution," a language identification, a claim that EVA letters are phonemes, a plant identification, or a public post.

---

## 2. Folio text used

### 2.1 Why f99r

Pass 3 pre-registered this page because:

- The f10v / f89v2 twin test was a **miss**. The only lexical bridge still standing from herbal running text into the label layer is the **toldy ~ otoldy** family. `otoldy` is an `Lf` on f99r.14.
- f9v and f10v had **no** labels, so the `qo-` suppression half of the prefix claim could not be scored at page scale. f99r has many `Lf`/`Lc`.
- Do **not** import the f9v viola literature ID or the f10v hellebore catalogue note.

Page header from IT2a-n (identical flags in ZL):

```
<f99r>  <! $Q=S $P=A $F=a $B=1 $I=P $L=A $H=1>
```

`$Q=S` quire 19, `$I=P` pharmaceutical, `$L=A` Currier A, `$H=1` hand 1. ZL's own comment says "hand 4?" - catalogue note, not a finding of this pass. Quire 19 (https://www.voynich.nu/q19/index.html): RZ language Ae (page / folio / bifolio); LFD hand 1.

### 2.2 Public folio description (quire 19 only)

**Sourced, not invented.** Quire 19 page, current as of the 14/06/2025 site update:

- Pharmaceutical page. Hole in the upper half. Folio number 99 in the upper right corner.
- Four simple containers and five rows of herb fragments consisting primarily of roots (**27** fragments).
- **52** text items: **18** lines of standard paragraph text; **4** container labels; **30** labels of plant fragments. Matches IT (18 `P` loci, 4 `@Lc`, 30 `Lf` including one `+Lf`).
- Running text is four paragraphs. Each paragraph seems to belong to one of the containers and is written below the rows of plant fragments.
- **Fragment 80** shows some similarity with the plant on **f51r**.
- **Fragment 94** shows some similarity with the plant on **f96v** (also stated on the quire-17 page for f96v).

Petersen numbers sit in ZL comments, not on the quire page. Inference, marked as such: ZL `<!80a>` / `<!80b>` are `oparal` (`@Lc`) and `oaro` (`@Lf`); ZL `<!94a>` / `<!94b>` are `yteoldy` (`@Lc`) and `tolsasy` (`@Lf`). The published lookalikes are **drawings**, not EVA pairings. This pass does **not** run a twin-token test on f51r or f96v (not pre-registered; do not fish).

No tentative species ID is printed on the quire-19 f99r block. None is added here.

### 2.3 Labels vs running text

This is the first page in the series that can score **both** sides on the same folio.

| Band | IT loci | IT tokens |
|---|---|---|
| Running text (`P`) | 18 (four paragraphs: .15-18, .28-31, .41-44, .47-52) | **162** |
| Labels (`L`) | 34 (4 `@Lc` + 30 `Lf`, one of them `+Lf`) | **35** (f99r.37 is two words: `rchey.ot`) |
| Whole-plant `Lp` | **0** | - |

Container labels (`@Lc`): `okoramog` (.1), `oparal` (.19), `tsholdy` (.32), `yteoldy` (.45).

### 2.4 f99r labels (IT primary; ZL control)

| Locus | Flag | IT EVA | ZL EVA | Petersen (ZL comment) | Notes |
|---|---|---|---|---|---|
| f99r.1 | `@Lc` | okoramog | okaradag | 68a | container, row 1. Hapax |
| f99r.2 | `@Lf` | **okary** | okary (`okar,y` joined) | 68b | repeats at .11 |
| f99r.3 | `@Lf` | darar | darar | 69 | P=2 |
| f99r.4 | `@Lf` | **oky** | oky | 70 | repeats at .24; P=92 |
| f99r.5 | `@Lf` | salo | salo | 71 | P=1 |
| f99r.6 | `@Lf` | oro | aro | 72 | same Petersen # as .7 |
| f99r.7 | `+Lf` | ain | ain | 72 | two-line label with .6; P=88 |
| f99r.8 | `@Lf` | okor | okor | 73 | also in P on this page (.51) |
| f99r.9 | `@Lf` | salol | ralol | 74 | P=1 |
| f99r.10 | `@Lf` | skeeal | skeeal | 75 | hapax |
| f99r.11 | `@Lf` | **okary** | okary | 76 | second hit |
| f99r.12 | `@Lf` | okolo | okolo | 77 | also `=Ln` on f80r |
| f99r.13 | `@Lf` | otalam | otalam | 78 | also `&Lz` on f70v2 |
| f99r.14 | `@Lf` | **otoldy** | otoldy | 79 | the type-word under test |
| f99r.19 | `@Lc` | oparal | oparal | 80a | container, row 2. Inferred fragment-**#80** pair with .20 |
| f99r.20 | `@Lf` | oaro | oaro | 80b | inferred #80 plant-fragment label |
| f99r.21 | `@Lf` | aloly | aloly | 81 | also `&Lz` on f72r3 |
| f99r.22 | `@Lf` | ooror | aora? (`aora[?:r]`) | 82 | IT/ZL disagree |
| f99r.23 | `@Lf` | choky | choky | 83 | P=33 |
| f99r.24 | `@Lf` | **oky** | oky | 84 | second hit |
| f99r.25 | `@Lf` | okeoly | okeoly | 85a | also in P on this page (.18) |
| f99r.26 | `@Lf` | **yteold** | yteold | 85b | family; hapax |
| f99r.27 | `@Lf` | cheotchy | cheotchy | 86a | hapax |
| f99r.32 | `@Lc` | **tsholdy** | tsholdy | 87a | container, row 3. Family; hapax |
| f99r.33 | `@Lf` | okos | okos | 87b | P=3; also `@Ls` on f68r3 |
| f99r.34 | `@Lf` | oekey | oekey | 87c | P=1 |
| f99r.35 | `@Lf` | dor | dar | 88 | IT P=71; too common |
| f99r.36 | `@Lf` | chockhhy | chockhia (`chockhi[a:y]`) | 89 | hapax |
| f99r.37 | `@Lf` | rchey.ot | rcheyet (`r,cheyet` joined) | 90 | IT two tokens; the split `ot` is the extra L `ot-` |
| f99r.38 | `@Lf` | saiiny | saiiny | 91 | hapax |
| f99r.39 | `@Lf` | rory | sory | 92 | P=1 |
| f99r.40 | `@Lf` | dam | dam | 93 | P=93; same common `dam` as f65r `otaim.dam.alam` |
| f99r.45 | `@Lc` | **yteoldy** | yteoldy | 94a | container, row 4. Family; hapax. Inferred fragment-**#94** pair with .46 |
| f99r.46 | `@Lf` | tolsasy | tolsasy | 94b | inferred #94 plant-fragment label. Hapax |

Family tokens **agree** in IT and ZL on this page: `otoldy`, `yteold`, `tsholdy`, `yteoldy`. `okary` and `oky` agree (ZL joins `okar,y`).

### 2.5 f99r running text (IT, cleaned)

Four paragraphs. Line IDs are Takahashi loci.

**P1** (below row 1)
```
f99r.15   pcheody oteody daiin cpheey tshol dal cfheol olaiin rar
f99r.16   raroshy shor sshor sheol kol sheol qoeol shol kol ckhol ckhory
f99r.17   dcheor chs al yckhy okeol ckhor oraiin chor qokeeor chory
f99r.18   qokeor chol ykol cheey chody ckhol daiin okeoly daiin ckhy
```

**P2** (below row 2)
```
f99r.28   kodaiin opchey qoky dor otchor opsho okeol sheol oteoefol
f99r.29   dsheol ckhey ckheol okeol ctheol qokey ckhol okeol okeey dald
f99r.30   tol cheody qokol okoly okoldy qokoly qokal okchol qokold
f99r.31   chees okeey qotol sheol daiin qotol okeol
```

**P3** (below row 3)
```
f99r.41   tsheeor cpheol ckey pchol ckhey ypchol chor choly qotocthey qkory
f99r.42   sol sheol keshey qokeeey chs chey dolchey ctheey daiin cheom
f99r.43   daiin cheeokeey checkhey dor oldy sheey keody okeeey s aiin ols
f99r.44   qokey chkeey chey ckhey ckhey ykeey oiin air chody oeksa
```

**P4** (below row 4; short first line)
```
f99r.47   tol keey ctheey
f99r.48   ykeol okeol o ckheo chol cheodal okeo r olcheem orar
f99r.49   okeeey keey keeor okeey daiin okeols aiin olaiir oolsal
f99r.50   qokeeo okeey qokeey okesy qokeeo sar sheseky or al
f99r.51   yshain ykhey octhey dy daiin okor okeey shcty sh
f99r.52   ychor ols or am air om
```

Paragraph-initial words: **pcheody** (gallows `p`), **kodaiin**, **tsheeor**, **tol**. P1 matches the known paragraph-start gallows habit. The other three do not. None is treated as a plant name. `oldy` sits in P3 (f99r.43), not as a label.

### 2.6 IT vs ZL (control)

21 loci disagree. Most are P space-joins (ZL commas concatenated) or one-letter reads. Function-word **direction** is stable. Family labels are stable.

Label disagreements that change a string:

| Locus | IT | ZL |
|---|---|---|
| f99r.1 Lc | `okoramog` | `okaradag` |
| f99r.6 Lf | `oro` | `aro` |
| f99r.9 Lf | `salol` | `ralol` |
| f99r.22 Lf | `ooror` | `aora?` |
| f99r.35 Lf | `dor` | `dar` |
| f99r.36 Lf | `chockhhy` | `chockhia` |
| f99r.37 Lf | `rchey` + `ot` | `rcheyet` |
| f99r.39 Lf | `rory` | `sory` |

P-side joins that move counts: ZL `kolsheol`, `sholkol`, `sheoldaiin`, `tolcheody`, `tolkeey`, `ypcholchor`, `dydaiin`, `okeoralcheeg`, `oragairom`. That is why ZL P is 148 tokens against IT 162, and why ZL `daiin` on this page is 6 not 8, `sheol` 3 not 5, `or` 1 not 2.

The split `ot` on f99r.37 is the only reason IT L has three `ot-` tokens rather than two. Without it, IT L ok+ot is 11/34 = 32.4%, matching ZL. Either figure sits in the ~33% label band.

---

## 3. Stats (verified on IT2a-n / ZL3b-n this pass)

Method: same as pass 3, with the `<->` = space rule stated in S1. Every number below is computed from the files this pass. Corpus P/L totals **match pass 2 / pass 3**: 34,486 P tokens / 7,140 types; 1,038 L tokens / 763 types.

### 3.1 f99r running text (IT)

| Measure | Value | Source |
|---|---|---|
| Word tokens | **162** | verified (json list length) |
| Word types | **118** | verified |
| Type/token ratio | 0.728 | computed |
| Hapax types on the page | 93 | computed |
| Mean / median word length | 4.87 / 5 EVA letters | computed |
| Paragraphs | 4 | IT `<%` / `<$>` |
| Lines (P loci) | 18 | IT + ZL |
| EVA `q` / word-initial `qo-` | 17 tokens | computed |

**Top tokens on f99r P (IT)**

| Rank | EVA | n | Notes |
|---|---|---|---|
| 1 | daiin | 8 | workhorse again; 0 as a label on this page |
| 2 | okeol | 6 | common `ok-` prose (also 1x `Lf` as `okeoly`) |
| 3-4 | sheol, okeey | 5 each | sheol is also an `Lf` on f89v2; **0** as L on f99r |
| 5 | ckhey | 4 | |
| 6 | ckhol | 3 | |
| 7+ | chol, chor, or, dor, qokey, qotol, ... | 2 each | |

**Function-word check (the pass-1 / 2 / 3 table), now on a pharma page**

| EVA | f99r P IT | f99r P ZL | f99r L IT | IT P corpus | Notes |
|---|---|---|---|---|---|
| daiin | 8 | 6 | **0** | 834 | survived as prose workhorse; still not a label here |
| dain | 0 | 0 | 0 | 207 | absent (weak; page is `okeol`/`sheol`-heavy) |
| chol | 2 | 2 | 0 | 384 | present, not a caption |
| chor | 2 | 1 | 0 | 217 | present, not a caption |
| ol | 0 | 0 | 0 | 521 | missed again - but this is **not** a herbal-A page, so it does not count as the third herbal miss |
| or | 2 | 1 | 0 | 345 | present in P4 |

`ol` / `or` were wounded on f9v and f10v (herbal A). f99r is pharmaceutical A. `or` fires; `ol` does not. Do **not** retire or save the herbal-page ol/or claim from this folio. f2v remains the control for that claim.

**Word-final letters on f99r P:** y 58, l 44, r 24, n 15. Same y/l/r/n preference. Almost no word ends in a gallows.

**Word-initial letters on f99r P:** o 42, c 39, q 18, d 16, s 15.

**Word-initial bigrams on f99r P:** ok 21, ch 20, qo 17, ck 13, sh 11, da 10. `ot` = 3 only (`oteody`, `otchor`, `oteoefol`). Prose on this page is `ok-`/`qo-` heavy, not `ot-` heavy.

**Line-initial first words (18 P lines):** pcheody, raroshy, dcheor, qokeor, kodaiin, dsheol, tol, chees, tsheeor, sol, daiin, qokey, tol, ykeol, okeeey, qokeeo, yshain, ychor.

### 3.2 f99r labels (IT)

| Measure | Value | Source |
|---|---|---|
| Word tokens | **35** | verified (json list length) |
| Word types | **33** | verified |
| Type/token ratio | 0.943 | computed |
| Hapax types on the page | 31 | only `okary` and `oky` repeat |
| Mean / median word length | 5.06 / 5 | computed |
| `Lc` / `Lf` / `Lp` | 4 / 30 / 0 | IT flags |

That is the flat label curve Zandbergen described. Already the third type is a page-hapax.

**Word-initial bigrams on f99r L:** ok 9, sa 3, ot 3, ch 3, da 2, yt 2. **qo = 0.**

### 3.3 ok-/ot- vs qo- (the label-prefix test, now on one page)

Corpus rates this parse (match pass 2 / pass 3):

| Band | n | ok- | ot- | ok+ot | qo- |
|---|---|---|---|---|---|
| IT P | 34,486 | 6.0% | 5.4% | **11.4%** | **15.1%** |
| IT L (all) | 1,038 | 16.0% | 17.1% | **33.0%** | **0.9%** |
| IT Lf only | 216 | 12.5% | 16.7% | 29.2% | **0** |
| IT Lc only | 40 | 17.5% | 15.0% | 32.5% | **0** |
| IT Lp only | 4 | 0 | 1 | 1/4 | **0** |

The 9 corpus `qo-` labels are still not pharma: f66r `L0` (qor, qotesy, qokal, qolsa), f67r2 `@Ls` qotoear, f73v `&Lz` qokeoly, f75v `Ln`/`Lt` (qokal, qoted, qotedy). **`qo-` remains 0 on `Lf` / `Lc` / `Lp`.**

**This page**

| Prefix | f99r P IT (n=162) | f99r L IT (n=35) | f99r P ZL (n=148) | f99r L ZL (n=34) |
|---|---|---|---|---|
| `ok-` | 21 (13.0%) | 9 | 21 (14.2%) | 9 |
| `ot-` | 3 (1.9%) | 3 (`otalam`, `otoldy`, split `ot`) | 3 (2.0%) | 2 (`otalam`, `otoldy`) |
| ok+ot | **24 / 162 = 14.8%** | **12 / 35 = 34.3%** | **24 / 148 = 16.2%** | **11 / 34 = 32.4%** |
| `qo-` | **17 / 162 = 10.5%** | **0 / 35 = 0%** | **17 / 148 = 11.5%** | **0 / 34 = 0%** |

Prediction from pass 1 / 3: running text may have `qo-`; labels should not; ok+ot should sit near 33% on L and near 11% on P. **Survived, and this is the first same-page two-sided score in the series.**

- P is slightly *above* corpus-P ok+ot (14.8% vs 11.4%) because this page's prose is `okeol`/`okeey` heavy. It is *below* the 33% label rate. `qo-` is legal (10.5%), a bit under the corpus-P mean (15.1%), and includes ordinary `qokol`/`qokal`/`qokeey` plus rarer `qotocthey`, `qokeeey`, `qokeeor`.
- L sits on the label side: ok+ot 34.3% (32.4% in ZL), **qo- = 0**. Same suppression as the whole `Lf`/`Lc` set and as f89v2 L (0/17).
- Several `qo-` P tokens are themselves uncommon (`qotocthey`, `qokeeey`, `qokeeor`). Rarity does not move a `qo-` word into the name slot.

### 3.4 The otoldy family (the point of this pass)

**On f99r (IT = ZL for these four strings)**

| EVA | Locus | Flag | P | L | all | Role this pass |
|---|---|---|---|---|---|---|
| otoldy | f99r.14 | `@Lf` | 6 | 5 | 11 | the repeating pharma type-word |
| yteold | f99r.26 | `@Lf` | 0 | 1 | 1 | hapax; shorter sibling of `yteoldy` |
| tsholdy | f99r.32 | `@Lc` | 0 | 1 | 1 | hapax container label (pass-2 leftover) |
| yteoldy | f99r.45 | `@Lc` | 0 | 1 | 1 | hapax container label |
| oldy | f99r.43 | `+P0` | (common) | 1 elsewhere (f99v.4 `@Lf`) | - | same tail, in **prose** on this page |

**Whole IT label set for the requested stems, plus the close `otal~` relatives from pass 1**

| EVA | IT L loci | IT P loci (selected) |
|---|---|---|
| **otoldy** | f82v.45 `@Lt`; **f89r1.4 `@Lf`**; **f89r2.9 `@Lc`**; **f99r.14 `@Lf`**; **f99v.2 `@Lf`** | f22r.11, f28r.7, f44v.1, f48v.9, f53v.13, f79r.28 (6) |
| **toldy** | **none** | f9v.4, f43r.11 (2) |
| **ytoldy** | **none** | f2r.6, f9v.9, f52r.2, f52r.3, f89r2.22 (5) |
| **tsholdy** | **f99r.32 `@Lc` only** | none |
| **yteold** | **f99r.26 `@Lf` only** | none |
| **yteoldy** | **f99r.45 `@Lc` only** | none |
| otaly | f70v2.15 `&Lz`, f72v3.31 `&Lz`, f73r.6 `@Lz`, f84r.47 `@Lt`, f88r.6 `@Lf`, **f99v.6 `@Lf`** | several P |
| otaldy | f88r.12 `@Lc`, f101v.2 `@Lf` | several P |
| otal | 8 zodiac `&Lz`/`@Lz` + f75v.50 `@Lt` + **f99v.27 `@Lf`** + f101v.3 `@Lf` | very common in P |
| oldy | **f99v.4 `@Lf` only** | many P, including f99r.43 |

Pharma `$I=P` label tokens this parse: **256 / 235 types**. Most frequent type **otoldy x4** (f89r1, f89r2, f99r, f99v). Matches pass 1's "most-repeated pharma label" and sits next to Zandbergen's published pharma-label list (his study counted `otoldy` x3 on a 234-label cut; this IT `$I=P` L parse is 4). Already the 5th type in that list is a hapax. Flat.

**ZL control on the family, not just on f99r**

- f99r's four family strings: **agree**.
- f89r1.4 and f99v.2 `otoldy`: **agree**.
- f89r2.9: ZL writes `otold[:y]` (uncertain final `y`). First-alternative `[:y]` is an empty left side, so a mechanical `[a:b]`-first parse does **not** emit `otoldy`. Raw reading is "`otold` or `otoldy`." Family membership survives either way.
- f82v.45: IT `@Lt otoldy`; ZL `@Lt okoldy`. ZL's `otoldy` label hit on the large foldout is `fRos.45 @L0 otoldy` instead. **Unverified as the same drawing.** The bio-section stress test is IT-only unless a later pass lines the two files up.

**Do they look like one lemma?**

**HYPOTHESIS: yes, as a type-word family, not as four species names.** Shared tail `-oldy` / `-eold` / `-eoldy`; prefix variation `o-` (`toldy`), `o-` (`otoldy`), `y-` (`ytoldy`), `yte-` (`yteold` / `yteoldy`), `tsh-` (`tsholdy`). On this one page the nest occupies **both** `Lf` (fragment) and `Lc` (container) slots. `toldy` / `ytoldy` never appear as labels - they are the P-side of the same stem (already on f9v). A unique species name should not also be the most-repeated pharma label **and** a six-times prose word **and** a container caption under two other prefixes.

What this is **not**: a proof that the strings are inflections of one dictionary lemma in a known language. A generator that emits `ot-`/`yt-`/`tsh-` + `oldy` would produce the same nest. The *role* (type-word, not species) can survive either account.

### 3.5 Repeating labels on f99r

Exact string repeats on the L set:

| EVA | n on f99r L | Other life | HYPOTHESIS role |
|---|---|---|---|
| **okary** | 2 (`Lf` .2, .11) | P=7 (herbal + stars); 2x zodiac `&Lz`/`@Lz` (f72v3, f73r) | page-local reuse. Too much extra-page life for a unique species. Type-word **or** local epithet. |
| **oky** | 2 (`Lf` .4, .24) | P=92; 4 other L, all zodiac | **too-common-in-P.** Classifier-only / generic "item." Same verdict as pass 1. |

No other exact label type repeats on this page. The family members each appear **once** as labels here; the repeat is the *paradigm*, not the string.

Other labels that look tempting and are refused as names because they are common in P: `ain` (P=88), `dor` (P=71), `dam` (P=93; the same `dam` as f65r `otaim.dam.alam`), `choky` (P=33), `okor` (P=31; also in P on this page).

Hapax / P<5 labels that remain name *candidates* (no gloss): `okoramog`, `skeeal`, `oparal`, `oaro`, `ooror`, `yteold`, `cheotchy`, `tsholdy`, `chockhhy`, `saiiny`, `yteoldy`, `tolsasy`, plus near-hapax `salo`, `salol`, `rory`, `oekey`. A candidate list is not a reading.

### 3.6 Prior hapax sets (record, do not fish)

| Set | Hits on f99r L | Hits on f99r P |
|---|---|---|
| f9v hapax set (`fochor`, `oporody`, `qopchypcho`, `olcfholy`, `ypcheey`, `rokyd`, `kyty`, `chshoty`) | **0** | **0** |
| f10v P<5 (`chckhan`, `chcthor`, `olty`, `qokchyky`, `qotchytor`, `otydy`, `qotoiin`, `choraiin`, `pcheey`) | **0** | **0** |
| `keerodal` | **0** | **0** |
| `otaim` | **0** | **0** |

Third consecutive miss for "a rare herbal-page token recurs as a pharma `Lf`/`Lc`/`Lp`." Still not fatal (pass 1 already allowed that). Still a miss. The only herbal->pharma lexical leftover remains the **toldy ~ otoldy** family, which this page was chosen to score.

`dam` as an `Lf` (f99r.40) is **not** a hit for `otaim`. It is the common prose word.

### 3.7 Colour / paint Latin letters

**Not present in IT2a-n or ZL3b-n as EVA tokens.** No `por`, standalone `p`, standalone `g`. The standalone `r` on f99r.48 is EVA in running text (IT `okeo.r.olcheem`; ZL joins to `okeoralcheeg`), not a paint annotation.

The quire-19 page for f99r does **not** mention Latin colour annotations. Reeds' red/tan/green note on the old Stolfi interlinear is paint on the drawings, not EVA. Nothing to import.

### 3.8 Corpus totals vs earlier passes

This parse: **34,486 P / 7,140 types**; daiin 834, ol 521, chol 384, or 345, chor 217, dain 207. **1,038 L / 763 types.** Matches pass 2 / pass 3. Pass 1's 33,707 / daiin 776 pair remains unverified.

---

## 4. What survived / died from pass 1-3 predictions

Pre-registered tests, scored honestly.

1. **ok-/ot- is label-legal; qo- may appear in running text, not on labels.** **Survived, first same-page two-sided score.** f99r P: qo- 10.5%, ok+ot 14.8%. f99r L: qo- **0**, ok+ot **34.3%** (32.4% ZL). Whole-corpus `Lf`/`Lc`/`Lp` qo- remains 0.

2. **`otoldy` / `toldy` / `ytoldy` / `tsholdy` behave as one lemma.** **Survived as a type-word family, not as a proven inflection.** Four related strings sit on this page (`otoldy` Lf, `yteold` Lf, `tsholdy` Lc, `yteoldy` Lc) plus `oldy` in the prose. `toldy`/`ytoldy` remain P-only. The nest occupies fragment **and** container slots. That is the opposite of four unique species names.

3. **Repeating labels: `okary` / `oky` / `otoldy`.** **Scored.** `okary` and `oky` are the only exact L-repeats. `oky` is too common in P. `okary` is page-local but also lives in herbal P and as a zodiac label. `otoldy` does not repeat *as a string* on this page; the family does.

4. **Unique rare tokens are the only name candidates.** **Survived as a filter.** The hapax labels listed in S3.5 are the only things this pass will *consider*. None is upgraded to a plant-name hypothesis in ink. No f9v or f10v hapax appears.

5. **daiin / chol / chor stay function-like, not names.** **Survived on a label page.** daiin x8 in P, **0** in L. chol x2 / chor x2 in P, 0 in L.

6. **Do not identify any plant as a species. Do not import viola or hellebore.** **Held.** Fragment 80 ~ f51r and fragment 94 ~ f96v stay in the catalogue column. No rare EVA token was mapped onto a medieval plant name.

7. **Colour letters stay out of the EVA gloss.** **Held** (vacuously for paint letters; the EVA `r` on f99r.48 is running text).

---

## 5. Hypothesis gloss table

**Every row is a HYPOTHESIS.** Confidence is structural (distribution + position), never semantic. "Gloss" means *role in English*, not a claimed Voynichese meaning. No row identifies the language. No row identifies a plant.

### 5.1 Prefix split and function words (re-tested on a label page)

| EVA | Role (HYPOTHESIS) | Constrained gloss (HYPOTHESIS) | Why this pass still allows it | Why it may be wrong |
|---|---|---|---|---|
| **ok- / ot-** (prefix) | label-legal classifier / construction | "item/root/herb-of ___" or a determiner that is *label-legal* | 34.3% of f99r L vs 14.8% of f99r P; corpus 33.0% vs 11.4%. | Dual use in prose (`okeol` x6 on this page) weakens "classifier only." |
| **qo-** | prose-legal, label-illegal | legal running-text vocabulary; **not** names | 17x in f99r P, **0** in f99r L. Still 0 on all `Lf`/`Lc`/`Lp`. | If a later transliteration finds a clean `Lf` `qo-` on this page, the ban is empirical not absolute. IT/ZL do not. |
| **daiin** | closed-class / function | "and" / weak demonstrative / clause-joiner | 8x in f99r P, 0x in f99r L, 834 in P, 7 in L corpus-wide. | Null / default emit / minim-count. |
| **chol / chor** | generic, **not** a plant name | "the plant / the herb / this preparation" **or** a second function word | 2 / 2 in P, 0 in L. Same tokens that topped f1r / f9v / f10v. | Generator ch-word remains simpler. |
| **sheol / okeol / okeey** | common pharma-A prose | formula / generic predicate; **not** names on this page | sheol 5, okeol 6, okeey 5 in P. sheol is an `Lf` on f89v2; that does not make it a species here. | Dual use (prose + occasional label) is the same problem as `oky`. |
| **ol / or** | short function (from pass 1) | "and/or / of" | `or` x2 in P4. `ol` still 0. | This page is not herbal A. Do not use it to save or kill the herbal ol/or claim. |
| **pcheody / kodaiin / tsheeor / tol** | paragraph-initial words | P1 = gallows-start habit; others not treated as titles | `pcheody` wears `p-`. | Hapax paragraph-starters are unfalsifiable as "titles." |

**Explicitly refused glosses (this pass):**

- EVA letters as Latin phonemes.
- `chol` / `daiin` / `chor` / `oky` / `okary` / `otoldy` as any plant name (viola, hellebore, or anything else).
- Any mapping of a rare f99r label onto a medieval plant name. No pre-stated substitution was applied; none is claimed.
- Any named language (Latin, German, Nahuatl, Hebrew, Occitan, Welsh, proto-Romance, etc.).
- Importing the f9v viola ID or the f10v hellebore catalogue note onto any jar or fragment.
- Treating fragment #80 as "the f51r plant" or fragment #94 as "the f96v plant" in EVA. The lookalikes are published **drawings**. The inferred EVA pairings (`oaro`, `tolsasy`) are not printed on the quire page.
- A full translation of the four paragraphs.

### 5.2 Labels - type-words vs name candidates

| EVA | Where | Role (HYPOTHESIS) | Constrained gloss (HYPOTHESIS) | Why | Falsifier already in view |
|---|---|---|---|---|---|
| **otoldy** | f99r.14 `@Lf`; also f89r1 `@Lf`, f89r2 `@Lc`, f99v `@Lf`; 6x P; IT `@Lt` on f82v | type-word | a **type** of plant-part or container-class, not a unique species | Most-repeated pharma label. Lives in prose. Sits in a prefix nest on this page. | If the four `otoldy` drawings share no visual class *and* the P hits sit in non-plant prose with no part/container sense. Bio `Lt` (IT) / `fRos` (ZL) is already a stress test. |
| **tsholdy / yteoldy / yteold** | f99r.32 `@Lc`; f99r.45 `@Lc`; f99r.26 `@Lf` | same lemma as otoldy (prefix variants) | same type-word, different prefix (`tsh-`, `yte-`) | Hapax labels, but they share the `-oldy`/`-eold` tail and sit on the same page as `otoldy`. Two of them are **container** labels. | If independent transliterations split them as unrelated, or if the three drawings share no class with the `otoldy` fragments. ZL agrees on the strings. |
| **toldy / ytoldy** | P only (f9v, f43r, f2r, f52r, f89r2) | P-side of the same stem | not a label, not a species | Never `L` in IT. The unprefixed / `y-` forms stay in running text. | A clean `Lf` `toldy` on a matching fragment would pull them into the label layer. Not observed. |
| **okary** | f99r.2 and .11 `@Lf` | page-local repeat | "this fragment / this herb" **or** a second type-word | Only exact L-repeat besides `oky`. P=7 + two zodiac labels: not unique. | Need the two fragments to be the same organ/species *and* the zodiac hits to be reclassified. Currently the opposite. |
| **oky** | f99r.4 and .24 `@Lf` | generic / classifier-only | **not** a unique species | P=92. Four other L, all zodiac. | If `oky` labelled a unique identifiable species and never appeared in unrelated prose. Observed: the opposite. |
| **ain / dor / dam / choky / okor** | one `Lf` each | too-common-in-P | no name gloss | P=88 / 71 / 93 / 33 / 31. `dam` is the f65r formula word. | A better space-model that makes them rare. Not this parse. |
| **okoramog, skeeal, oparal, oaro, ooror, cheotchy, chockhhy, saiiny, tolsasy** (and near-hapax `salo`, `salol`, `rory`, `oekey`) | f99r L only or nearly | the only tokens that *could* be fragment-specific names | **no gloss.** Candidate list, not a reading. | Hapax or P<5, and not the workhorses. | Any one of them turning up as a high-frequency prose word, or sitting on a visually unrelated page as a label, kills "this fragment's name." |
| **keerodal** | f41v `@Lp` only | whole-plant label (rare) | **candidate plant name** (still) | Unchanged. Not on f99r. | One token. |
| **otaim** | f65r `@Lp`; 1x P on f111v | whole-plant label piece | name-ish; `dam alam` may be formula | Unchanged. `dam` *is* on f99r.40 as `Lf`, which makes a pure "three-name title" on f65r even less likely. | `dam` is common in P. |

**Strongest claim this pass will defend:**
On a pharmaceutical page that actually has many `Lf`/`Lc` labels, `qo-` is legal in the four prose paragraphs (10.5%) and banned on the labels (0/35). ok+ot sits at the label rate on L (34%) and at a prose-like rate on P (15%). The `otoldy` nest (`otoldy` / `yteold` / `tsholdy` / `yteoldy`, plus `oldy` in the prose) behaves as **one type-word lemma with prefix variation**, not as four species names. Repeating `okary` is page-local reuse of a moderately common `ok-` word; `oky` is too common in P to be a unique name. No f9v or f10v hapax appears. f99r therefore still does **not** give a plant-name token worth writing in ink.

---

## 6. What would falsify this pass

1. **qo- label ban dies if** a clean `Lf`/`Lc`/`Lp` `qo-` label appears in IT/ZL on this page or any other pharma page. Not observed. Uncertain spaces that glue a `q` onto a label would also need checking; ZL joins on this page do not create one.

2. **"otoldy-family is one type-word" dies if** independent transliterations (GC/v101, RF) read `otoldy` / `tsholdy` / `yteoldy` / `yteold` as unrelated, **or** if the four drawings (three fragments + two containers, depending how `yteold` is paired) share no visual class, **or** if `otoldy` in the six P hits sits in demonstrably non-plant prose. ZL already agrees on the f99r strings. ZL's `otold[:y]` on f89r2.9 and `okoldy` on f82v.45 are the current stress points, not a kill.

3. **"okary is not a unique species" dies if** the two f99r fragments are independently identified as the same organ/species **and** the two zodiac `okary` labels are shown to name the same thing. Currently they are a herbal-P word plus two star labels.

4. **Rare-token-as-name filter dies if** a better space-model merges the hapax labels into common words. ZL already joins `okar,y` -> `okary` (a common-ish word) and `r,cheyet` -> `rcheyet` (still a hapax). The hapax *list* shrinks by space-model; it does not vanish.

5. **"no f9v/f10v name on f99r" dies if** an independent transliteration reads one of those hapaxes as a known `Lf`/`Lc` on this page. IT and ZL do not.

6. **Function-word claim for daiin / chol / chor dies if** a folio whose plant is independently identified uses one of them *only* as a unique caption. Observed on this page: the opposite (prose only).

7. **Viola / hellebore as catalogue notes (not fact) is violated if** a later note treats those IDs as established and imports them onto f99r. They are not. Same rule as pass 2 / pass 3.

8. **Constrained semi-language stance dies** on the same terms as pass 1 S6.5: a pre-registered simple substitution into a known language that yields grammatical running text **and** matching names on the rare / `Lp` words. Not observed.

---

## 7. Next folio to try

**Primary next experiment: f99v (pharmaceutical, `$I=P`, verso of this leaf).**

Why that page, given what this pass actually found:

- The type-word family **continues on the verso**. IT already shows `otoldy` `@Lf` (f99v.2), `oldy` `@Lf` (f99v.4), `otaly` `@Lf` (f99v.6), `otal` `@Lf` (f99v.27), plus `otaramy` `@Lc` and `otoky` `@Lf`. That is the cleanest next test of "one lemma across a bifolio."
- Same quire, same hand/language flags, same prefix test, no new plant-ID temptation from f9v/f10v.
- Do **not** import viola, hellebore, or any f99r fragment lookalike onto f99v.

**Protocol (pre-registered for pass 5):**

1. Transcribe f99v from IT **and** ZL; keep P and L separate.
2. Score `ok-`/`ot-` vs `qo-` on L vs P. Prediction: same split as f99r.
3. List every otoldy-family token and ask whether the verso adds forms or breaks the lemma (especially `oldy` / `otal` / `otaly` / `otoky` sitting next to `otoldy`).
4. Check the f9v hapax set and the f10v P<5 set. A hit is a late positive. A miss is still not fatal.
5. Do **not** identify any plant as a species. Do **not** import viola or hellebore.

**Other backups:** f65r (the only multi-word `Lp`, `otaim.dam.alam` - now even more "formula + rare head" given `dam` as an `Lf` on f99r.40) and f2v (ol/or + function-word control; the herbal-A claim is still waiting on a third herbal page, and f2v already had them in pass 1). Prefer f99v while the type-word family is the live experiment.

---

## 8. Bottom line for this pass

f99r is readable as *structure*: four containers, four paragraphs, 35 label tokens, a closed class that still refuses to become a plant name (`daiin` 8 in P, 0 in L), legal `qo-` in the prose (10.5%) and **zero** `qo-` on the labels, and an `otoldy` nest that looks like one type-word with prefix variation (`otoldy` / `yteold` / `tsholdy` / `yteoldy`). It is not readable as *language*, and it is not a crib for any jar-plant.

The pass-1 split survives its first real label page in this series: **high-frequency ch/d-words are generic; `ok-`/`ot-` is label-legal; `qo-` is prose-legal and label-illegal; unique rare tokens are the only name candidates; the repeating `otal~` / `otoldy` family is a type-word, not a species.** No f9v or f10v hapax appears. The viola and hellebore literature IDs were left unused. Colour letters were not an issue.

Until a rare f99r hapax label is found on a matching drawing under two transliterations, this file is still a lab notebook, not a crib.

---

## Appendix A - raw IT loci for f99r (as in the file)

```
<f99r>     <! $Q=S $P=A $F=a $B=1 $I=P $L=A $H=1>
<f99r.1,@Lc>      okoramog
<f99r.2,@Lf>      okary
<f99r.3,@Lf>      darar
<f99r.4,@Lf>      oky
<f99r.5,@Lf>      salo
<f99r.6,@Lf>      oro
<f99r.7,+Lf>      ain
<f99r.8,@Lf>      okor
<f99r.9,@Lf>      salol
<f99r.10,@Lf>     skeeal
<f99r.11,@Lf>     okary
<f99r.12,@Lf>     okolo
<f99r.13,@Lf>     otalam
<f99r.14,@Lf>     otoldy
<f99r.15,@P0>     <%>pcheody.oteody.daiin.cpheey.tshol.dal.cfheol.olaiin.rar
<f99r.16,+P0>     raroshy.shor.sshor.sheol.kol.sheol.qoeol.shol.kol.ckhol.ckhory
<f99r.17,+P0>     dcheor.chs.al.yckhy.okeol.ckhor.oraiin.chor.qokeeor.chory
<f99r.18,+P0>     qokeor.chol.ykol.cheey.chody.ckhol.daiin.okeoly.daiin.ckhy<$>
<f99r.19,@Lc>     oparal
<f99r.20,@Lf>     oaro
<f99r.21,@Lf>     aloly
<f99r.22,@Lf>     ooror
<f99r.23,@Lf>     choky
<f99r.24,@Lf>     oky
<f99r.25,@Lf>     okeoly
<f99r.26,@Lf>     yteold
<f99r.27,@Lf>     cheotchy
<f99r.28,@P0>     <%>kodaiin.opchey.qoky.dor.otchor.opsho.okeol.sheol.oteoefol
<f99r.29,+P0>     dsheol.ckhey.ckheol.okeol.ctheol.qokey.ckhol.okeol.okeey.dald
<f99r.30,+P0>     tol.cheody.qokol.okoly.okoldy.qokoly.qokal.okchol.qokold
<f99r.31,+P0>     chees.okeey.qotol.sheol.daiin.qotol.okeol<$>
<f99r.32,@Lc>     tsholdy
<f99r.33,@Lf>     okos
<f99r.34,@Lf>     oekey
<f99r.35,@Lf>     dor
<f99r.36,@Lf>     chockhhy
<f99r.37,@Lf>     rchey.ot
<f99r.38,@Lf>     saiiny
<f99r.39,@Lf>     rory
<f99r.40,@Lf>     dam
<f99r.41,@P0>     <%>tsheeor.cpheol.ckey.pchol.ckhey.ypchol.chor.choly.qotocthey.qkory
<f99r.42,+P0>     sol.sheol.keshey.qokeeey.chs.chey.dolchey.ctheey.daiin.cheom
<f99r.43,+P0>     daiin.cheeokeey.checkhey.dor.oldy.sheey.keody.okeeey.s.aiin.ols
<f99r.44,+P0>     qokey.chkeey.chey.ckhey.ckhey.ykeey.oiin.air.chody.oeksa<$>
<f99r.45,@Lc>     yteoldy
<f99r.46,@Lf>     tolsasy
<f99r.47,@P0>     <%>tol.keey.ctheey
<f99r.48,+P0>     ykeol.okeol.o.ckheo.chol.cheodal.okeo.r.olcheem.orar
<f99r.49,+P0>     okeeey.keey.keeor.okeey.daiin.okeols.aiin.olaiir.oolsal
<f99r.50,+P0>     qokeeo.okeey.qokeey.okesy.qokeeo.sar.sheseky.or.al
<f99r.51,+P0>     yshain.ykhey.octhey.dy.daiin.okor.okeey.shcty.sh
<f99r.52,+P0>     ychor.ols.or.am.air.om<$>
```

Source: https://voynich.nu/data/IT2a-n.txt

## Appendix B - raw ZL loci for f99r (control)

```
<f99r>     <! $Q=S $P=A $F=a $B=1 $I=P $L=A $H=1>
# page 201
# pharmaceutical
# Kraus plate XXXI labeled jars
# Currier's language A, hand 4?
<f99r.1,@Lc>      <!68a>okaradag
<f99r.2,@Lf>      <!68b>okar,y
<f99r.3,@Lf>      <!69>darar
<f99r.4,@Lf>      <!70>oky
<f99r.5,@Lf>      <!71>salo
<f99r.6,@Lf>      <!72>aro
<f99r.7,+Lf>      <!72>ain
<f99r.8,@Lf>      <!73>okor
<f99r.9,@Lf>      <!74>ralol
<f99r.10,@Lf>     <!75>skeeal
<f99r.11,@Lf>     <!76>okary
<f99r.12,@Lf>     <!77>okolo
<f99r.13,@Lf>     <!78>otalam
<f99r.14,@Lf>     <!79>otoldy
<f99r.15,@P0>     <%>pcheody.oteody.<!gap>daiin.cpheey.tshol.dal.cfheol.olaiin.sar
<f99r.16,+P0>     saroshy.shor.s,shor.sheol.kolsheol.qoeol.sholkol.ckhol.ckhory
<f99r.17,+P0>     dcheor.chr.al.yckhy.okeol.ckhor.oraiin.chor.qokeeor.chory
<f99r.18,+P0>     qokeor.chol.ykol.cheey.chody.ckhol.daiin.okeoly.daiin.ckhy<$>
<f99r.19,@Lc>     <!80a>oparal
<f99r.20,@Lf>     <!80b>oaro
<f99r.21,@Lf>     <!81>aloly
<f99r.22,@Lf>     <!82>aora[?:r]
<f99r.23,@Lf>     <!83>choky
<f99r.24,@Lf>     <!84>oky
<f99r.25,@Lf>     <!85a>okeoly
<f99r.26,@Lf>     <!85b>yteold
<f99r.27,@Lf>     <!86a>cheotchy
<f99r.28,@P0>     <%>kodaiin.opchey.qoky.dar.otchor.opsho.okeol.sheol.oteoefol
<f99r.29,+P0>     dsheol.ckhey.ckheol.okeol.ctheol.qokey.ckhol.okeol.okeey.dald
<f99r.30,+P0>     tol,cheody.qokol.okoly.okoldy.qokoly.qokal.okchol.qokold
<f99r.31,+P0>     chees.okeey.qotol.sheol,daiin.qotol.okeol<$>
<f99r.32,@Lc>     <!87a>tsholdy
<f99r.33,@Lf>     <!87b>okos
<f99r.34,@Lf>     <!87c>oekey
<f99r.35,@Lf>     <!88>dar
<f99r.36,@Lf>     <!89>chockhi[a:y]
<f99r.37,@Lf>     <!90>r,cheyet
<f99r.38,@Lf>     <!91>saiiny
<f99r.39,@Lf>     <!92>sory
<f99r.40,@Lf>     <!93>dam
<f99r.41,@P0>     <%>tsheeor.cpheol.{ck}ey.pchol.ckhey.ypchol,chor.choly.qotocthey.qkory
<f99r.42,+P0>     sol.sheol.keshey.qokeeey.chs.chey.dalchey.ctheey.daiin.cheom
<f99r.43,+P0>     daiin.cheeokeey.checkhey.dor.oldy.sheey.keody.okeeey.s.aiin.ols
<f99r.44,+P0>     qokey.chkeey.chey.ckhey.ckhey.ykeey.oiin.air.chody.oeksa<$>
<f99r.45,@Lc>     <!94a>yteoldy
<f99r.46,@Lf>     <!94b>tolsasy
<f99r.47,@P0>     <%>tol,keey.ctheey
<f99r.48,+P0>     ykeol.okeol.ockhey.chol.cheodal.okeo,r,alcheeg.orar
<f99r.49,+P0>     okeeey.keey.keear.okeey.daiin.okeol,s.aiin.olaiir.oolsal
<f99r.50,+P0>     qokeeo.okeey.qokeey.okesy.qokeeo.sar.sheseky.or.al
<f99r.51,+P0>     yshaiin.{ykh}ey.octhey.dy,daiin.okor.okeey.sh{cty}sh
<f99r.52,+P0>     ychor.ols.or,agairom<$>
```

ZL's "hand 4?" comment is a catalogue note, **not** a finding of this pass. Family strings `otoldy` / `yteold` / `tsholdy` / `yteoldy` match IT.

Source: https://voynich.nu/data/ZL3b-n.txt
