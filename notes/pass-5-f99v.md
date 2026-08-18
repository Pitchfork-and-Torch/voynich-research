# Voynich pass 5 - f99v working notes (not a translation)

**For:** Jon Bailey
**Date:** 14 Aug 2026 (ET)
**Status:** constrained fifth pass on the verso of the pass-4 pharmaceutical folio. **No verified full translation of Beinecke MS 408 exists.** Nothing below is a decipherment. Every gloss is marked **HYPOTHESIS**. No jar-plant is identified. The f9v Viola / herba trinitatis literature ID, the f10v hellebore catalogue note, and the ZL "faces capsicum" comment are **not imported**.

This note finishes the experiment pre-registered in pass 4 S7: take f99v (`$I=P`), the verso of the f99r type-word nest, and test (a) whether `otoldy` / `oldy` / `otaly` / `otal` / `otoky` still look like one lemma or split into two type-word families, and (b) whether `qo-` stays banned on labels on the other side of the same leaf. A family that continues as a class-word is a positive for "type-word, not species." A `qo-` label on this page would wound the prefix split.

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
| Folio description f99v | https://www.voynich.nu/q19/index.html (quire 19; site update 14/06/2025) |
| Colour-letter table | https://www.voynich.nu/writing.html (update 13/06/2025), keyword COL |
| Manuscript | Yale, Beinecke Rare Book & Manuscript Library, MS 408 |
| Prior notes | `notes/pass-1.md`, `notes/pass-2-f9v.md`, `notes/pass-3-f10v.md`, `notes/pass-4-f99r.md` |

**Tokenisation (IVTFF 2.0), same as the pass-2 / pass-3 / pass-4 practice.** `.` is a word break. `<->` is a **word space** (do not strip and concatenate). All remaining `<>` markup is stripped (`<%>`, `<$>`, `<!...>`, leftover `<@H=n>`). Tokens must contain at least one A-Z letter. `?` is kept if present. Paragraph text = loci whose flags contain `P`. Labels = flags containing `L`.

ZL is the **control**, not the running text. ZL extras: uncertain commas are **joined** (not a space); alternatives `[a:b]` take the first reading; ligature braces `{ct}` / `{cthh}` / `{ck}` expand to their contents. ZL rare-character codes `{c@NNN;x}` (one pair on f99v.37) are treated as a weirdo placeholder so they do not leak into the IT corpus.

Stripping leftover `<@H=n>` markup (two inline hand tags on f115r, not on f99v) keeps this parse's corpus totals in line with pass 2 / 3 / 4: **34,486 P / 7,140 types; 1,038 L / 763 types**.

**What this is not:** a download of any copyrighted monograph, a Cheshire/Gibbs-style "complete solution," a language identification, a claim that EVA letters are phonemes, a plant identification, or a public post.

---

## 2. Folio text used

### 2.1 Why f99v

Pass 4 pre-registered this page because:

- The type-word family **continues on the verso**. IT already showed `otoldy` `@Lf` (f99v.2), `oldy` `@Lf` (f99v.4), `otaly` `@Lf` (f99v.6), `otal` `@Lf` (f99v.27), plus `otaramy` `@Lc` and `otoky` `@Lf`. That was the cleanest next test of "one lemma across a bifolio."
- Same quire, same hand/language flags, same prefix test, no new plant-ID temptation from f9v/f10v.
- Do **not** import viola, hellebore, or any f99r fragment lookalike onto f99v.

Page header from IT2a-n (identical flags in ZL):

```
<f99v>  <! $Q=S $P=B $F=a $B=1 $I=P $L=A $H=1>
```

`$Q=S` quire 19, `$I=P` pharmaceutical, `$L=A` Currier A, `$H=1` hand 1. ZL's own comment says "hand 4?" and "B&R p88; faces capsicum" - catalogue notes, **not** findings of this pass. Quire 19 (https://www.voynich.nu/q19/index.html): RZ language Ae+ (page) / Ae (folio / bifolio); LFD hand 1.

### 2.2 Public folio description (quire 19 only)

**Sourced, not invented.** Quire 19 page, current as of the 14/06/2025 site update:

- Pharmaceutical page. Hole in the upper half.
- Four simple containers and four rows of herb fragments consisting primarily of roots (**20** fragments).
- **44** text items: **19** lines of standard paragraph text; **4** container labels; **21** labels of plant fragments. Matches IT (19 `P` loci, 4 `@Lc`, 21 `Lf`).
- Running text is four paragraphs. The fourth immediately follows the third and is the longest. Its lines are interrupted by the largest plant fragment at the bottom of the page.
- **Fragment 95** shows some similarity with the plant on **f44r**.
- **Fragment 110** shows some similarity with the plant on **f34v**.
- In the fourth root of the third row, a single character has been written under the brown paint. This looks like a Latin **'p' or 'r'**. The quire page and writing.html both call this the only known colour annotation in the pharmaceutical section.

Petersen numbers sit in ZL comments, not on the quire page. Inference, marked as such: ZL `<!95a>` / `<!95b>` are `okaramy` (IT `otaramy`, `@Lc`) and `otoldy` (`@Lf`); ZL `<!110>` / `<!110b>` are `otal` (`@Lf`) and `chor.olekor` (`@Lf`). The published lookalikes are **drawings**, not EVA pairings. This pass does **not** run a twin-token test on f44r or f34v (not pre-registered; do not fish).

No tentative species ID is printed on the quire-19 f99v block. The ZL "capsicum" comment is **not** used. None is added here.

### 2.3 Labels vs running text

Second same-page two-sided score in the series (f99r was the first).

| Band | IT loci | IT tokens |
|---|---|---|
| Running text (`P`) | 19 (four paragraphs: .10-13, .21-24, .32-35, .37-43) | **147** |
| Labels (`L`) | 25 (4 `@Lc` + 21 `Lf`) | **28** (three two-word labels: .3 `otor.chy`, .5 `dar.ary`, .28 `chor.olekor`) |
| Whole-plant `Lp` | **0** | - |

Container labels (`@Lc`): `otaramy` (.1), `okoldody` (.14), `darolaly` (.25), `dralas` (.36).

### 2.4 f99v labels (IT primary; ZL control)

| Locus | Flag | IT EVA | ZL EVA | Petersen (ZL comment) | Notes |
|---|---|---|---|---|---|
| f99v.1 | `@Lc` | **otaramy** | okaramy | 95a | container, row 1. Hapax. IT/ZL prefix disagree (`ot-`/`ok-`). Inferred fragment-**#95** pair with .2 |
| f99v.2 | `@Lf` | **otoldy** | otoldy | 95b | the type-word under test; inferred #95 plant-fragment label |
| f99v.3 | `@Lf` | otor chy | otor chy | 96 | two words (`<->`). `otor` P=37 |
| f99v.4 | `@Lf` | **oldy** | oldy | 97 | only `L` hit in whole IT; also in P on this page (.24) |
| f99v.5 | `@Lf` | dar ary | dar ary | 98 | two words (`<->`). `dar` P=281 |
| f99v.6 | `@Lf` | **otaly** | otaly | 99 | otal~ family |
| f99v.7 | `@Lf` | olsy | olsy | 100 | P=1 |
| f99v.8 | `@Lf` | arol | arol | 101 | P=10 |
| f99v.9 | `@Lf` | **otoky** | otoky | 102 | P=0; also `@Lf` on f88r.5 |
| f99v.14 | `@Lc` | okoldody | okoldody | 103a | container, row 2. Hapax |
| f99v.15 | `@Lf` | oeeesary | oeeesary | 103b | hapax |
| f99v.16 | `@Lf` | daiiine | daiiinc | 104 | hapax; IT/ZL last letter disagrees |
| f99v.17 | `@Lf` | sory | sary | 105 | IT P=2; also `+La` on f67v2 |
| f99v.18 | `@Lf` | saiino | saiino | 106 | hapax |
| f99v.19 | `@Lf` | otolsar | otolsar | 107 | hapax |
| f99v.20 | `@Lf` | osary | osary | 108 | hapax in this IT parse |
| f99v.25 | `@Lc` | darolaly | darolaly | 109a | container, row 3. Hapax |
| f99v.26 | `@Lf` | okechy | okechy | 109b | P=5 |
| f99v.27 | `@Lf` | **otal** | otal | 110 | otal~; P=128. Inferred fragment-**#110** pair with .28 |
| f99v.28 | `@Lf` | chor olekor | chor olekor | 110b | two words. `chor` P=217 - the stray workhorse label flagged in pass 3 |
| f99v.29 | `@Lf` | okeodor | okeodor | 111 | hapax. Nearest EVA locus to the painted fourth root (inference only) |
| f99v.30 | `@Lf` | olky | olky | 112 | P=20; also `~Ln` on f80r |
| f99v.31 | `@Lf` | doldam | doldam | 113 | hapax |
| f99v.36 | `@Lc` | dralas | oralas | 114a | container, row 4. Hapax. IT/ZL first letter disagrees |
| f99v.44 | `@Lf` | koleearol | koleearol | 114b | hapax |

Family tokens that **agree** in IT and ZL on this page: `otoldy`, `oldy`, `otaly`, `otoky`, `otal`. The container `otaramy` / `okaramy` is the only family-adjacent string that splits.

### 2.5 f99v running text (IT, cleaned)

Four paragraphs. Line IDs are Takahashi loci. `<->` already expanded to spaces.

**P1** (below row 1; hole in the upper half)
```
f99v.10   sol cheols ockhey qockhy qkoldy s ok oleees oteey dain
f99v.11   okoiin choty qokchol qokeol okoldy qkholdy toly daiin
f99v.12   qokeo qokeol chockhy otol daiin oty otockey da chosaiin
f99v.13   okoraiin okol shocthy qokor oloiram
```

**P2** (below row 2)
```
f99v.21   doror okeeody opar okor eosaiin otoraiin shey ols aiiin qoetal
f99v.22   doiin otey okeeol saiin okeol qokeol ctheol qokeol dy qokaiin
f99v.23   qokeey chol okeoldy qokol qokeolo lchol okeol sheodol qokeechom
f99v.24   shokeeey chol shey okol qokey okeodal oldy
```

**P3** (below row 3)
```
f99v.32   qoteeoy chokol qokeeo dy qokeeol olpchey doiir okeedy okolol
f99v.33   dol okeeol okeor okol okaiin ckheol okolaiin okolaiin cheol dy
f99v.34   yoiin ol ol olaiin qockhey qokol olshy qokeeor or aiin dol dam
f99v.35   ol okeeey oqoeeol cheol chody okoiin
```

**P4** (follows P3; longest; interrupted by the large bottom fragment)
```
f99v.37   oteol socthey qokol olkeol daiin okoly
f99v.38   olcheey qokeol okeol okeol shokol ykey
f99v.39   dor shol okchey ckhey qokololal okeol
f99v.40   or aiin okeody okol odaiin qoky olaldy
f99v.41   qockhol aiin shody qokol aiidal aii daiim
f99v.42   olsheol olkeol okol or oraloly ykeol okal okoldaly
f99v.43   ychol olkeeoldy
```

Paragraph-initial words: **sol**, **doror**, **qoteeoy**, **oteol**. P1 does **not** wear a paragraph-start gallows (the hole may be why). P3 opens with a `qo-` word. None is treated as a plant name. `oldy` sits in P2 (f99v.24) **and** as an `Lf` (.4). `dam` sits in P3 (f99v.34) - the same common `dam` as f99r.40 `Lf` and f65r `otaim.dam.alam`.

### 2.6 IT vs ZL (control)

19 loci disagree. Most are P space-joins (ZL commas concatenated) or one-letter reads. Function-word **direction** is stable. Core family labels are stable.

Label disagreements that change a string:

| Locus | IT | ZL |
|---|---|---|
| f99v.1 Lc | `otaramy` | `okaramy` |
| f99v.16 Lf | `daiiine` | `daiiinc` |
| f99v.17 Lf | `sory` | `sary` |
| f99v.36 Lc | `dralas` | `oralas` |

P-side joins / reads that move counts: ZL `olsaiiin`, `keeolsaiin`, `cholshey`, `okeodaloldy`, `cheoldy`, `yoiinol`, `doldam`, `olokeeey`, `WeolsoWhey` (rare-char `{c@132;}eol,so{c@133;h}ey` vs IT `oteol socthey`), `aiidaiim`, `ychololkeeoldy`, plus `qockhhy` / `choraiin` / `qokeeoy` / `daiir` / `okal` / `oiin` / `okaldaly` / `dar`. That is why ZL P is 138 tokens against IT 147.

The container `otaramy` -> `okaramy` is the only reason IT L has seven `ot-` tokens rather than six. Either figure sits in the ~33% label band (both give ok+ot **10/28 = 35.7%**).

---

## 3. Stats (verified on IT2a-n / ZL3b-n this pass)

Method: same as pass 4, with the `<->` = space rule and the `<@H=n>` strip stated in S1. Every number below is computed from the files this pass. Corpus P/L totals **match pass 2 / 3 / 4**: 34,486 P tokens / 7,140 types; 1,038 L tokens / 763 types.

### 3.1 f99v running text (IT)

| Measure | Value | Source |
|---|---|---|
| Word tokens | **147** | verified (json list length) |
| Word types | **114** | verified |
| Type/token ratio | 0.776 | computed |
| Hapax types on the page | 97 | computed |
| Mean / median word length | 5.27 / 5 EVA letters | computed |
| Paragraphs | 4 | IT `<%` / `<$>` |
| Lines (P loci) | 19 | IT + ZL |
| EVA word-initial `qo-` | 27 tokens | computed |

**Top tokens on f99v P (IT)**

| Rank | EVA | n | Notes |
|---|---|---|---|
| 1-3 | qokeol, okol, okeol | 5 each | formulaic pharma-A prose |
| 4 | qokol | 4 | |
| 5-9 | daiin, dy, ol, or, aiin | 3 each | daiin still 0 as a label here |
| 10+ | okoiin, shey, okeeol, chol, dol, okolaiin | 2 each | |

**Function-word check (the pass-1 / 2 / 3 / 4 table), now on the verso**

| EVA | f99v P IT | f99v P ZL | f99v L IT | IT P corpus | Notes |
|---|---|---|---|---|---|
| daiin | 3 | 3 | **0** | 834 | survived as prose workhorse; still not a label here |
| dain | 1 | 1 | 0 | 207 | present (P1) |
| chol | 2 | 1 | 0 | 384 | present, not a caption |
| chor | 0 | 0 | **1** | 217 | the stray `Lf` on .28; does **not** make it a species |
| ol | 3 | 2 | 0 | 521 | **fires** on this pharma page (including line-initial .35) |
| or | 3 | 3 | 0 | 345 | fires in P3/P4 |

`ol` / `or` were wounded on f9v and f10v (herbal A). f99v is pharmaceutical A, like f99r. Both fire here (`ol` did **not** fire on f99r). Do **not** retire or save the herbal-page ol/or claim from this folio. f2v remains the control for that claim.

**Word-final letters on f99v P:** l 55, y 44, n 23, r 11. Same y/l/r/n preference, but **l beats y** on this verso (f99r P was y 58 / l 44). Almost no word ends in a gallows.

**Word-initial letters on f99v P:** o 64, q 29, d 16, c 13, s 12.

**Word-initial bigrams on f99v P:** ok 33, qo 27, ol 16, ch 10, sh 8, ot 7, da 7. Prose on this page is **`ok-`/`qo-` heavy**, even more than f99r (f99r P: ok 21, qo 17, ot 3).

**Line-initial first words (19 P lines):** sol, okoiin, qokeo, okoraiin, doror, doiin, qokeey, shokeeey, qoteeoy, dol, yoiin, ol, oteol, olcheey, dor, or, qockhol, olsheol, ychol.

### 3.2 f99v labels (IT)

| Measure | Value | Source |
|---|---|---|
| Word tokens | **28** | verified (json list length) |
| Word types | **28** | verified |
| Type/token ratio | **1.000** | computed |
| Hapax types on the page | 28 | **no exact string repeats** |
| Mean / median word length | 5.46 / 5.5 | computed |
| `Lc` / `Lf` / `Lp` | 4 / 21 / 0 | IT flags |

Flatter than f99r (that page at least had `okary`x2 and `oky`x2). Already the first type is a page-hapax.

**Word-initial bigrams on f99v L:** ot 7, ol 4, da 3, ok 3, ch 2. **qo = 0.**

### 3.3 ok-/ot- vs qo- (the label-prefix test, verso)

Corpus rates this parse (match pass 2 / 3 / 4):

| Band | n | ok- | ot- | ok+ot | qo- |
|---|---|---|---|---|---|
| IT P | 34,486 | 6.0% | 5.4% | **11.4%** | **15.1%** |
| IT L (all) | 1,038 | 16.0% | 17.1% | **33.0%** | **0.9%** |
| IT Lf only | 216 | 12.5% | 16.7% | 29.2% | **0** |
| IT Lc only | 40 | 17.5% | 15.0% | 32.5% | **0** |
| IT Lp only | 4 | 0 | 1 | 1/4 | **0** |

The 9 corpus `qo-` labels are still not pharma: f66r `L0` (qor, qotesy, qokal, qolsa), f67r2 `@Ls` qotoear, f73v `&Lz` qokeoly, f75v `Ln`/`Lt` (qokal, qoted, qotedy). **`qo-` remains 0 on `Lf` / `Lc` / `Lp`.**

**This page**

| Prefix | f99v P IT (n=147) | f99v L IT (n=28) | f99v P ZL (n=138) | f99v L ZL (n=28) |
|---|---|---|---|---|
| `ok-` | 33 (22.4%) | 3 (`okoldody`, `okechy`, `okeodor`) | 31 (22.5%) | 4 (adds `okaramy`) |
| `ot-` | 7 (4.8%) | 7 (`otaramy`, `otoldy`, `otor`, `otaly`, `otoky`, `otolsar`, `otal`) | 6 (4.3%) | 6 (drops `otaramy`) |
| ok+ot | **40 / 147 = 27.2%** | **10 / 28 = 35.7%** | **37 / 138 = 26.8%** | **10 / 28 = 35.7%** |
| `qo-` | **27 / 147 = 18.4%** | **0 / 28 = 0%** | **27 / 138 = 19.6%** | **0 / 28 = 0%** |

Prediction from pass 1 / 3 / 4: running text may have `qo-`; labels should not; ok+ot should sit near 33% on L and near 11% on P.

- **L side survived.** ok+ot 35.7% (both IT and ZL), **qo- = 0**. Same suppression as the whole `Lf`/`Lc` set, as f89v2 L (0/17), and as f99r L (0/35).
- **P `qo-` survived.** 18.4% is *above* the corpus-P mean (15.1%) and includes ordinary `qokol`/`qokeol`/`qokeey` plus rarer `qoteeoy`, `qokeechom`, `qokololal`, `qoetal`.
- **P ok+ot is the new stress.** 27.2% is well above corpus-P 11.4% and above f99r P 14.8%. It is still *below* this page's L rate (35.7%), but it is closer to the label band than any previous P score in the series. Cause, marked as such: this verso's prose is `okol`x5 / `okeol`x5 / `qokeol`x5 / `qokol`x4 - a pharma-A formula, not a sudden conversion of running text into labels. The **cleaner discriminator on this page is `qo-`**, not the ok+ot percentage alone.
- Several `qo-` P tokens are themselves uncommon (`qoteeoy`, `qokeechom`, `qokololal`). Rarity does not move a `qo-` word into the name slot.
- Standalone `ok` (f99v.10, from `s<->ok`) is counted as `ok-`. Dropping it would be 39/147 = 26.5%. Direction unchanged.

### 3.4 The otoldy / otal~ families (the point of this pass)

**On f99v (IT = ZL for these five strings)**

| EVA | Locus | Flag | P | L | all | Role this pass |
|---|---|---|---|---|---|---|
| otoldy | f99v.2 | `@Lf` | 6 | 5 | 11 | the repeating pharma type-word; continues from f99r.14 |
| oldy | f99v.4 | `@Lf` | 26 | **1** (this page only) | 28 | unprefixed sibling; also in P on this page (.24) and on f99r.43 |
| otaly | f99v.6 | `@Lf` | 11 | 6 | 19 | otal~ type-word; 3 of the other L hits are zodiac |
| otoky | f99v.9 | `@Lf` | 0 | 2 | 3 | also f88r.5 `@Lf`; plus f67r1.9 `@Ri` (not a plant label) |
| otal | f99v.27 | `@Lf` | 128 | 10 | 143 | too-common-in-P; 7 of the other L hits are zodiac |
| oldy | f99v.24 | `+P0` | (same 26) | - | - | same tail, in **prose** on this page |

**Whole IT label set for the requested stems**

| EVA | IT L loci | IT P (n) |
|---|---|---|
| **otoldy** | f82v.45 `@Lt`; **f89r1.4 `@Lf`**; **f89r2.9 `@Lc`**; **f99r.14 `@Lf`**; **f99v.2 `@Lf`** | 6 |
| **toldy** | **none** | 2 (f9v.4, f43r.11) |
| **ytoldy** | **none** | 5 (f2r, f9v, f52rx2, f89r2) |
| **tsholdy** | **f99r.32 `@Lc` only** | 0 |
| **yteold / yteoldy** | **f99r.26 / f99r.45 only** | 0 |
| **oldy** | **f99v.4 `@Lf` only** | 26 |
| **otaly** | 3 zodiac `Lz` + f84r `@Lt` + f88r.6 `@Lf` + **f99v.6 `@Lf`** | 11 |
| **otal** | 7 zodiac `Lz` + f75v `@Lt` + **f99v.27 `@Lf`** + f101v.3 `@Lf` | 128 |
| **otaldy** | f88r.12 `@Lc`, f101v.2 `@Lf` | 4 |
| **otoky** | f88r.5 `@Lf`, **f99v.9 `@Lf`** | 0 |

Pharma `$I=P` label tokens this parse: **256 / 235 types**. Most frequent type still **otoldy x4** (f89r1, f89r2, f99r, f99v). Matches pass 1 / pass 4. `otoky` and `otaly` are now x2 in that pharma-L list (with `otaldy`, `otal`, `okary`, `oky`). Already the lower ranks are hapaxes. Flat.

**Do they look like one lemma, or two?**

**HYPOTHESIS: two related type-word families, not one, and not five species names.**

1. **`otoldy` / `oldy` / (recto) `tsholdy` / `yteold` / `yteoldy` / (P-only) `toldy` / `ytoldy`.** Shared tail `-oldy` / `-eold`. Prefix variation `o-` (`oldy`, `toldy`), `o-` (`otoldy`), `y-` (`ytoldy`), `yte-`, `tsh-`. This verso **adds the unprefixed label form** `oldy` - the piece pass 4 only had in prose. Label form still prefers `ot-` (`otoldy` is the repeating pharma caption; `oldy` is the unique L hapax of a common P word).
2. **`otal` / `otaly` / `otaldy`.** Shared tail `-al` / `-aly` / `-aldy`. Related prefix `ot-`, different stem. `otal` is too common in P (128) and already a zodiac workhorse. `otaly` lives as a zodiac label (x3) plus two pharma `Lf`. That is the opposite of a unique jar-plant name.
3. **`otoky` sits next to both and is not merged.** P=0, only two plant-fragment labels (f88r, f99v), plus one `@Ri` on f67r1. Rarer than either family. Two different pharma pages still argues type-word (or a reused epithet), not "the name of this one root." It is the strongest *name-candidate-shaped* family-adjacent token on the verso, and it is still **not** written as a plant name.

`tsholdy` remains adjacent, not merged (still f99r only). `otaramy` (IT) / `okaramy` (ZL) is a hapax container label with the same `ot-`/`ok-` legal prefix; it is **not** folded into either family.

What this is **not**: a proof that the strings are inflections of one (or two) dictionary lemmas in a known language. A generator that emits `ot-`/`o-`/`y-` + `oldy` / `al(y)` would produce the same nest. The *role* (type-word, not species) can survive either account.

### 3.5 Repeating labels on f99v

Exact string repeats on the L set: **none.** 28 tokens, 28 types.

The family members each appear **once** as labels here; the repeat is the *paradigm* (and the bifolio: `otoldy` on f99r.14 and f99v.2), not a same-page string.

Other labels that look tempting and are refused as names because they are common in P: `chor` (P=217), `dar` (P=281), `chy` (P=140), `otal` (P=128), `otor` (P=37), `oldy` (P=26), `olky` (P=20), `ary` (P=18), `otaly` (P=11), `arol` (P=10), `okechy` (P=5).

Hapax / P<5 labels that remain name *candidates* (no gloss): `otaramy`, `okoldody`, `oeeesary`, `daiiine`, `saiino`, `otolsar`, `osary`, `darolaly`, `olekor`, `okeodor`, `doldam`, `dralas`, `koleearol`, plus near-hapax `olsy`, `sory`, `otoky`. A candidate list is not a reading. `otoky` is the only one of those that already recurs as an `Lf` on another pharma page.

### 3.6 Prior hapax sets (record, do not fish)

| Set | Hits on f99v L | Hits on f99v P |
|---|---|---|
| f9v hapax set (`fochor`, `oporody`, `qopchypcho`, `olcfholy`, `ypcheey`, `rokyd`, `kyty`, `chshoty`) | **0** | **0** |
| f10v hapax set (`chckhan`, `chcthor`, `olty`, `qokchyky`, `qotchytor`) | **0** | **0** |
| f10v extra P<5 (`otydy`, `qotoiin`, `choraiin`, `pcheey`) | **0** | **0** in IT. ZL P f99v.12 joins `chor,aiin` -> `choraiin` - a space-model artefact, not a label hit, not fished |
| `keerodal` | **0** | **0** |
| `otaim` | **0** | **0** |

Fourth consecutive miss for "a rare herbal-page token recurs as a pharma `Lf`/`Lc`/`Lp`." Still not fatal (pass 1 already allowed that). Still a miss. The only herbal->pharma lexical leftover remains the **toldy ~ otoldy** family, which this page was chosen to score.

`dam` in P3 (f99v.34) is **not** a hit for `otaim`. It is the common prose word, already an `Lf` on f99r.40.

### 3.7 Colour / paint Latin letters

**Present on the drawings, absent from the EVA files.**

Sourced: writing.html COL table (update 13/06/2025) and the quire-19 f99v block:

> A letter in the fourth root of the third row, perhaps a 'p' or an 'r'. The only colour annotation found in the pharmaceutical section so far.

The quire page adds that characters in or near the flowers appear like colour annotations, and points at the same writing.html table. That table lists **one** f99v COL row.

**Not present in IT2a-n or ZL3b-n as EVA tokens.** No standalone Latin `p` or `r` locus. The EVA words `otor`, `chor`, `arol`, `sory` etc. are Voynichese labels, not the paint letter.

The paint letter stays in this separate column. It is **not** EVA. It is **not** folded into the gloss table. It is **not** read as `por` / `p` / `r` colour-code evidence for any jar-plant. Reeds' red/tan/green/blue note (ZL comment) is paint on the drawings, not EVA.

Nearest EVA locus, inference only, not a pairing: third-row fragments run `.26 okechy`, `.27 otal`, `.28 chor.olekor`, `.29 okeodor` ... so the fourth root is in the neighbourhood of `okeodor`. The letter is under the brown paint on the **drawing**, not a fifth label.

### 3.8 Corpus totals vs earlier passes

This parse: **34,486 P / 7,140 types**; daiin 834, ol 521, chol 384, or 345, chor 217, dain 207. **1,038 L / 763 types.** Matches pass 2 / 3 / 4. Pass 1's 33,707 / daiin 776 pair remains unverified.

---

## 4. What survived / died from pass 1-4 predictions

Pre-registered tests, scored honestly.

1. **ok-/ot- is label-legal; qo- may appear in running text, not on labels.** **Survived on L and on qo-; stressed on P ok+ot.** f99v P: qo- 18.4%, ok+ot **27.2%** (high). f99v L: qo- **0**, ok+ot **35.7%**. Whole-corpus `Lf`/`Lc`/`Lp` qo- remains 0. Second same-page two-sided score. The verso does **not** produce a `qo-` label.

2. **`otoldy` / `toldy` / `ytoldy` / `tsholdy` behave as one lemma; `otal~` related but distinct.** **Survived as two type-word families, not as a proven inflection, and not as one merged lemma.** Verso adds `oldy` as the unprefixed **label** form of the otoldy stem, and parks `otaly` / `otal` next to it without collapsing the tails. `otoky` stays adjacent, not merged. `toldy`/`ytoldy` remain P-only. `tsholdy` remains f99r-only.

3. **Repeating labels.** **Scored, empty.** No exact L-repeat on this page (TTR 1.0). The bifolio repeat is `otoldy` (f99r.14 + f99v.2), which is the type-word prediction, not a new species.

4. **Unique rare tokens are the only name candidates.** **Survived as a filter.** The hapax labels listed in S3.5 are the only things this pass will *consider*. None is upgraded to a plant-name hypothesis in ink. No f9v or f10v hapax appears as a label.

5. **daiin / chol / chor stay function-like, not names.** **Survived, with the predicted chor stray.** daiin x3 in P, **0** in L. chol x2 in P, 0 in L. chor **0** in P, **1** in L (`.28 chor.olekor`). A workhorse that is 217x in P cannot become "the name of fragment 110b" by sitting once next to `olekor`.

6. **Do not identify any plant as a species. Do not import viola, hellebore, or capsicum.** **Held.** Fragment 95 ~ f44r and fragment 110 ~ f34v stay in the catalogue column. No rare EVA token was mapped onto a medieval plant name.

7. **Colour letters stay out of the EVA gloss.** **Held, and this time there is one to keep out.** Latin `p`/`r` under brown paint, fourth root of row 3. Not in IT/ZL.

---

## 5. Hypothesis gloss table

**Every row is a HYPOTHESIS.** Confidence is structural (distribution + position), never semantic. "Gloss" means *role in English*, not a claimed Voynichese meaning. No row identifies the language. No row identifies a plant.

### 5.1 Prefix split and function words (re-tested on the verso)

| EVA | Role (HYPOTHESIS) | Constrained gloss (HYPOTHESIS) | Why this pass still allows it | Why it may be wrong |
|---|---|---|---|---|
| **ok- / ot-** (prefix) | label-legal classifier / construction | "item/root/herb-of ___" or a determiner that is *label-legal* | 35.7% of f99v L vs 27.2% of f99v P; corpus 33.0% vs 11.4%. | This verso's **P** ok+ot is the highest in the series. Dual use in prose (`okol`/`okeol`/`qokeol` x5 each) weakens "classifier only." |
| **qo-** | prose-legal, label-illegal | legal running-text vocabulary; **not** names | 27x in f99v P, **0** in f99v L. Still 0 on all `Lf`/`Lc`/`Lp`. The clean discriminator on a page whose P is ok-heavy. | If a later transliteration finds a clean `Lf` `qo-` on this page, the ban is empirical not absolute. IT/ZL do not. |
| **daiin** | closed-class / function | "and" / weak demonstrative / clause-joiner | 3x in f99v P, 0x in f99v L, 834 in P, 7 in L corpus-wide. | Null / default emit / minim-count. |
| **chol / chor** | generic, **not** a plant name | "the plant / the herb / this preparation" **or** a second function word | chol 2 in P, 0 in L. chor 0 in P, 1 in L as half of `chor.olekor`. Same tokens that topped f1r / f9v / f10v. | The stray `Lf` is the obvious objection. P=217 kills "this fragment's name." |
| **okol / okeol / qokeol / qokol** | common pharma-A prose | formula / generic predicate; **not** names on this page | 5 / 5 / 5 / 4 in P. This is why P ok+ot is high. | Dual use (prose + occasional label: `okol` is also a pharma L type x3) is the same problem as `oky`. |
| **ol / or** | short function (from pass 1) | "and/or / of" | `ol` x3, `or` x3 in P. Both fire. | This page is not herbal A. Do not use it to save or kill the herbal ol/or claim. |
| **sol / doror / qoteeoy / oteol** | paragraph-initial words | P1 has no gallows-start; P3 wears `qo-`; none treated as titles | Hole may explain the missing gallows. | Hapax paragraph-starters are unfalsifiable as "titles." |

**Explicitly refused glosses (this pass):**

- EVA letters as Latin phonemes.
- `chol` / `daiin` / `chor` / `otal` / `otaly` / `otoldy` / `oldy` / `otoky` as any plant name (viola, hellebore, capsicum, or anything else).
- Any mapping of a rare f99v label onto a medieval plant name. No pre-stated substitution was applied; none is claimed.
- Any named language (Latin, German, Nahuatl, Hebrew, Occitan, Welsh, proto-Romance, etc.).
- Importing the f9v viola ID, the f10v hellebore catalogue note, or the ZL "capsicum" comment onto any jar or fragment.
- Treating fragment #95 as "the f44r plant" or fragment #110 as "the f34v plant" in EVA. The lookalikes are published **drawings**. The inferred EVA pairings (`otoldy`, `otal`) are not printed on the quire page.
- Reading the paint `p`/`r` as EVA, or as a colour-name crib for the fourth root.
- A full translation of the four paragraphs.

### 5.2 Labels - type-words vs name candidates

| EVA | Where | Role (HYPOTHESIS) | Constrained gloss (HYPOTHESIS) | Why | Falsifier already in view |
|---|---|---|---|---|---|
| **otoldy** | f99v.2 `@Lf`; also f89r1 `@Lf`, f89r2 `@Lc`, f99r `@Lf`; 6x P; IT `@Lt` on f82v | type-word | a **type** of plant-part or container-class, not a unique species | Most-repeated pharma label. Lives in prose. Continues from the recto onto the matching verso slot. | If the four `otoldy` drawings share no visual class *and* the P hits sit in non-plant prose. Bio `Lt` (IT) / `fRos` (ZL) is already a stress test. |
| **oldy** | f99v.4 `@Lf`; 26x P; also f99r.43 P | same lemma as otoldy (unprefixed) | same type-word, no prefix | Only L hit, but P=26. Sits on the same page as `otoldy` and in the verso prose. | If independent transliterations split `oldy` from `otoldy`, or if the `.4` fragment shares no class with the `otoldy` fragments. ZL agrees on the string. |
| **tsholdy / yteoldy / yteold / toldy / ytoldy** | not on f99v (recto / P-only leftovers) | same otoldy stem | unchanged from pass 4 | Verso did not add or break them. | Same as pass 4. |
| **otaly** | f99v.6 `@Lf`; 3x zodiac L; f84r `@Lt`; f88r `@Lf`; P=11 | otal~ type-word, **related, not merged** | a second type-word, not a unique species | Zodiac + pharma + prose. Shared `ot-`, different tail from `-oldy`. | If the f99v.6 fragment is independently the same organ/species as the three zodiac `otaly` stars. Currently the opposite. |
| **otal** | f99v.27 `@Lf`; 7x zodiac L; f75v `@Lt`; f101v `@Lf`; P=128 | too-common-in-P / generic | **not** a unique species | P=128. Mostly a star label. | If `otal` labelled a unique identifiable species and never appeared in unrelated prose. Observed: the opposite. |
| **otoky** | f99v.9 `@Lf`; f88r.5 `@Lf`; f67r1 `@Ri`; P=0 | type-word **or** reused epithet; strongest family-adjacent name *shape* | **no plant-name gloss.** Two pharma fragments, zero prose. | P=0 is the name-filter's friend. Two different pharma pages is its enemy. | A third `Lf` on a visually unrelated fragment, or a better space-model that merges it into `oky` / `otol`. |
| **otaramy / okoldody / darolaly / dralas** | the four `@Lc` | hapax container labels | **no gloss.** Candidate list, not a reading. | Hapax. `otaramy`/`okaramy` is the IT/ZL split. | Any one of them turning up as a high-frequency prose word. |
| **chor / dar / chy / otor / olky / ary / arol / okechy** | one `Lf` each (some as half of a two-word label) | too-common-in-P | no name gloss | P=217 / 281 / 140 / 37 / 20 / 18 / 10 / 5. | A better space-model that makes them rare. Not this parse. |
| **oeeesary, daiiine, saiino, otolsar, osary, olekor, okeodor, doldam, koleearol** (and near-hapax `olsy`, `sory`) | f99v L only or nearly | the only tokens that *could* be fragment-specific names | **no gloss.** Candidate list, not a reading. | Hapax or P<5, and not the workhorses. | Any one of them turning up as a high-frequency prose word, or sitting on a visually unrelated page as a label, kills "this fragment's name." |
| **keerodal** | f41v `@Lp` only | whole-plant label (rare) | **candidate plant name** (still) | Unchanged. Not on f99v. | One token. |
| **otaim** | f65r `@Lp`; 1x P on f111v | whole-plant label piece | name-ish; `dam alam` may be formula | Unchanged. `dam` is now on f99r.40 as `Lf` **and** in f99v.34 P, which makes a pure "three-name title" on f65r even less likely. | `dam` is common in P. |

**Strongest claim this pass will defend:**
On the verso of the first real label page in this series, `qo-` is again legal in the four prose paragraphs (18.4%) and banned on the labels (0/28). ok+ot sits at the label rate on L (36%). P ok+ot is unusually high (27%) because the verso is `okol`/`okeol`/`qokeol` formula - the cleaner split on this page is `qo-`. The `otoldy` nest continues (`otoldy` Lf, `oldy` now as an Lf, `oldy` again in the prose) and sits **next to** an `otal~` nest (`otaly`, `otal`) without merging. `otoky` is adjacent, P-less, and already reused on f88r - type-word-shaped, not a unique species. No exact label string repeats. No f9v or f10v hapax appears. The Latin paint `p`/`r` is kept out of the EVA gloss. f99v therefore still does **not** give a plant-name token worth writing in ink.

---

## 6. What would falsify this pass

1. **qo- label ban dies if** a clean `Lf`/`Lc`/`Lp` `qo-` label appears in IT/ZL on this page or any other pharma page. Not observed. Uncertain spaces that glue a `q` onto a label would also need checking; ZL joins on this page do not create one.

2. **"otoldy-family is one type-word" dies if** independent transliterations (GC/v101, RF) read `otoldy` / `oldy` as unrelated, **or** if the f99r nest and the f99v.2 / f99v.4 drawings share no visual class, **or** if `otoldy` in the six P hits sits in demonstrably non-plant prose. ZL already agrees on the f99v strings.

3. **"otal~ is a second type-word, not merged" dies if** a better paradigm shows `-oldy` and `-al(y)` as the same tail under one space-model, **or** if the `otal` / `otaly` fragments are the same visual class as the `otoldy` / `oldy` fragments *and* the zodiac `otal`/`otaly` hits are reclassified as plant-parts. Currently they are mostly star labels.

4. **"otoky is not a unique species" dies if** the f88r.5 and f99v.9 fragments are independently identified as the same organ/species **and** the f67r1 `@Ri` is shown to name the same thing. Currently they are two pharma fragments plus a non-plant `Ri`.

5. **Rare-token-as-name filter dies if** a better space-model merges the hapax labels into common words. ZL already reads `sory` as `sary` and `dralas` as `oralas` (still rare) and `otaramy` as `okaramy` (still a hapax). The hapax *list* shrinks by space-model; it does not vanish.

6. **"no f9v/f10v name on f99v" dies if** an independent transliteration reads one of those hapaxes as a known `Lf`/`Lc` on this page. IT and ZL do not. ZL's P-side `choraiin` join is not a label.

7. **Function-word claim for daiin / chol / chor dies if** a folio whose plant is independently identified uses one of them *only* as a unique caption. Observed on this page: daiin/chol in prose only; chor once as half of a two-word label next to a hapax, after 217 P hits.

8. **Viola / hellebore / capsicum as catalogue notes (not fact) is violated if** a later note treats those IDs as established and imports them onto f99v. They are not.

9. **Paint-letter-out-of-EVA dies if** a later note treats the Latin `p`/`r` as an EVA token or as a crib for the fourth-root label. It is not in IT/ZL.

10. **Constrained semi-language stance dies** on the same terms as pass 1 S6.5: a pre-registered simple substitution into a known language that yields grammatical running text **and** matching names on the rare / `Lp` words. Not observed.

---

## 7. Next folio to try

**Primary next experiment: f65r (herbal, the only multi-word `Lp`: `otaim.dam.alam`).**

Why that page, given what this pass actually found:

- The type-word family now has a **recto nest** (f99r: `otoldy` / `yteold` / `tsholdy` / `yteoldy`) **and** a **verso continuation** (f99v: `otoldy` / `oldy` / `otaly` / `otal` / `otoky`), plus the earlier f89r1 / f89r2 hits. It does **not** need a third pharma witness.
- The leftover name-page from pass 1 is still f65r. `dam` is now an `Lf` on f99r.40 **and** a P-word on f99v.34, which makes "three unique names in a row" even less likely and "rare head + formula" more likely. That is the experiment this bifolio did not run.
- f2v (ol/or + function-word control) remains weak as a *next* pick: ol/or already fired on this pharma verso, and the herbal-A absence still wants a longer herbal-A page, but the live leftover is the `Lp` name-page.
- Do **not** import viola, hellebore, capsicum, or any f99v fragment lookalike onto f65r.

**Protocol (pre-registered for pass 6):**

1. Transcribe f65r from IT **and** ZL; keep the `@Lp` (`otaim.dam.alam`) separate from any P-text on the page.
2. Score `otaim` / `dam` / `alam` against the whole IT P and L sets. Prediction: `dam` is formula (already Lf + P); `otaim` stays the rare head; `alam` needs a count.
3. Score `ok-`/`ot-` vs `qo-` on that page if it has both bands. Prediction: `otaim` is an `ot-` whole-plant label; `qo-` should not appear on the `Lp`.
4. Check the f9v hapax set and the f10v hapax set. A hit is a late positive. A miss is still not fatal.
5. Do **not** identify any plant as a species. Do **not** import viola, hellebore, or capsicum.

**Not next:** another quire-19 pharma page (f100r / f101v / f88r). f88r would be a tidy *later* check (`otoky` + `otaly` + `otaldy` on one leaf) only if a later pass needs a third family witness. It does not, today.

---

## 8. Bottom line for this pass

f99v is readable as *structure*: four containers, four paragraphs, 28 label tokens with **zero** same-page repeats, a closed class that still refuses to become a plant name (`daiin` 3 in P, 0 in L; `chor` once as half a label after 217 P hits), legal `qo-` in the prose (18.4%) and **zero** `qo-` on the labels, and an `otoldy` nest that continues from the recto (`otoldy` / `oldy`) sitting next to a distinct `otal~` nest (`otaly` / `otal`). It is not readable as *language*, and it is not a crib for any jar-plant. The Latin paint letter (`p` or `r` under brown paint, fourth root of row 3) is recorded and kept out of the EVA gloss.

The pass-1 split survives its second real label page: **high-frequency ch/d-words are generic; `ok-`/`ot-` is label-legal; `qo-` is prose-legal and label-illegal; unique rare tokens are the only name candidates; the repeating `otoldy` family is a type-word, not a species; `otal~` is a second type-word, not a merge and not a species.** P ok+ot is high on this verso because the prose is `okol`/`okeol` formula - that stresses the percentage, not the `qo-` ban. No f9v or f10v hapax appears. The viola, hellebore, and capsicum literature IDs were left unused.

Until a rare f99v hapax label is found on a matching drawing under two transliterations, this file is still a lab notebook, not a crib.

---

## Appendix A - raw IT loci for f99v (as in the file)

```
<f99v>     <! $Q=S $P=B $F=a $B=1 $I=P $L=A $H=1>
<f99v.1,@Lc>      otaramy
<f99v.2,@Lf>      otoldy
<f99v.3,@Lf>      otor<->chy
<f99v.4,@Lf>      oldy
<f99v.5,@Lf>      dar<->ary
<f99v.6,@Lf>      otaly
<f99v.7,@Lf>      olsy
<f99v.8,@Lf>      arol
<f99v.9,@Lf>      otoky
<f99v.10,@P0>     <%>sol.cheols.ockhey.qockhy.qkoldy.s<->ok.oleees.oteey.dain
<f99v.11,+P0>     okoiin.choty.qokchol.qokeol.okoldy<->qkholdy.toly.daiin
<f99v.12,+P0>     qokeo.qokeol.chockhy.otol.daiin.oty<->otockey.da.chosaiin
<f99v.13,+P0>     okoraiin.okol.shocthy.qokor.oloiram<$>
<f99v.14,@Lc>     okoldody
<f99v.15,@Lf>     oeeesary
<f99v.16,@Lf>     daiiine
<f99v.17,@Lf>     sory
<f99v.18,@Lf>     saiino
<f99v.19,@Lf>     otolsar
<f99v.20,@Lf>     osary
<f99v.21,@P0>     <%>doror.okeeody.opar.okor.eosaiin.otoraiin.shey.ols.aiiin.qoetal
<f99v.22,+P0>     doiin.otey.okeeol.saiin.okeol.qokeol.ctheol.qokeol.dy.qokaiin
<f99v.23,+P0>     qokeey.chol.okeoldy.qokol.qokeolo.lchol.okeol.sheodol.qokeechom
<f99v.24,+P0>     shokeeey.chol.shey.okol.qokey.okeodal.oldy<$>
<f99v.25,@Lc>     darolaly
<f99v.26,@Lf>     okechy
<f99v.27,@Lf>     otal
<f99v.28,@Lf>     chor.olekor
<f99v.29,@Lf>     okeodor
<f99v.30,@Lf>     olky
<f99v.31,@Lf>     doldam
<f99v.32,@P0>     <%>qoteeoy.chokol.qokeeo.dy.qokeeol.olpchey.doiir.okeedy<->okolol
<f99v.33,+P0>     dol.okeeol.okeor.okol.okaiin.ckheol.okolaiin.okolaiin.cheol.dy
<f99v.34,+P0>     yoiin.ol.ol.olaiin.qockhey.qokol.olshy.qokeeor.or.aiin.dol.dam
<f99v.35,+P0>     ol.okeeey.oqoeeol.cheol.chody.okoiin<$>
<f99v.36,@Lc>     dralas
<f99v.37,@P0>     <%>oteol.socthey.qokol.olkeol.daiin<->okoly
<f99v.38,+P0>     olcheey.qokeol.okeol.okeol.shokol<->ykey
<f99v.39,+P0>     dor.shol.okchey.ckhey.qokololal<->okeol
<f99v.40,+P0>     or.aiin.okeody.okol.odaiin.qoky<->olaldy
<f99v.41,+P0>     qockhol.aiin.shody.qokol.aiidal<->aii.daiim
<f99v.42,+P0>     olsheol.olkeol.okol.or.oraloly<->ykeol.okal.okoldaly
<f99v.43,+P0>     ychol.olkeeoldy<$>
<f99v.44,@Lf>     koleearol
```

Source: https://voynich.nu/data/IT2a-n.txt

## Appendix B - raw ZL loci for f99v (control)

```
<f99v>     <! $Q=S $P=B $F=a $B=1 $I=P $L=A $H=1>
# page 202
# phamaceutical
# B@R p88; faces "capsicum"
# Currier's language A, hand 4?
<f99v.1,@Lc>      <!95a>okaramy
<f99v.2,@Lf>      <!95b>otoldy
<f99v.3,@Lf>      <!96>otor<->chy
<f99v.4,@Lf>      <!97>oldy
<f99v.5,@Lf>      <!98>dar<->ary
<f99v.6,@Lf>      <!99>otaly
<f99v.7,@Lf>      <!100>olsy
<f99v.8,@Lf>      <!101>arol
<f99v.9,@Lf>      <!102>otoky
<f99v.10,@P0>     <%>sol.cheols.ockhey.qo{ckhh}y.qkoldy.s<->ok.oleees.oteey.dain
<f99v.11,+P0>     okoiin.choty.qokchol.qokeol.okoldy<->q{kh}oldy.toly.daiin
<f99v.12,+P0>     qokeo.qokeol.chockhy.otol.daiin.oty<->oto{ck}ey.da.chor,aiin
<f99v.13,+P0>     okoraiin.okol.shocthy<->qokor.oloiram<$>
<f99v.14,@Lc>     <!103a>okoldody
<f99v.15,@Lf>     <!103b>oeeesary
<f99v.16,@Lf>     <!104>daiiinc
<f99v.17,@Lf>     <!105>sary
<f99v.18,@Lf>     <!106>saiino
<f99v.19,@Lf>     <!107>otolsar
<f99v.20,@Lf>     <!108>osary
<f99v.21,@P0>     <%>doror.okeeody.opar.okor.eosaiin.otoraiin.shey.ols,aiiin.qoetal
<f99v.22,+P0>     doiin.otey.o.keeol,s,aiin.okeol.qokeol.ctheol.qokeol.dy.qokaiin
<f99v.23,+P0>     qokeey.chol.okeoldy.qokol.qokeolo.lchol.okeol.sheodol.qokeechom
<f99v.24,+P0>     shokeeey.cholshey.okol.qokey.okeodal,oldy<$>
<f99v.25,@Lc>     <!109a>darolaly
<f99v.26,@Lf>     <!109b>okechy
<f99v.27,@Lf>     <!110>otal
<f99v.28,@Lf>     <!110b>chor.olekor
<f99v.29,@Lf>     <!111>okeodor
<f99v.30,@Lf>     <!112>olky
<f99v.31,@Lf>     <!113>doldam
<f99v.32,@P0>     <%>qokeeoy.chokol.qokeeo.dy.qokeeol.olpchey.daiir.okeedy<->okolol
<f99v.33,+P0>     dol.okeeol.okeor.okal.okaiin.ckheol.okolaiin.okolaiin.cheoldy
<f99v.34,+P0>     yoiin,ol.ol.olaiin.qockhey.qokol.olshy.qokeeor.or.aiin.doldam
<f99v.35,+P0>     ol,okeeey.oqoeeol.cheol.chody.okoiin<$>
<f99v.36,@Lc>     <!114a>oralas
<f99v.37,@P0>     <%>{c@132;}eol,so{c@133;h}ey.qokol.olkeol.daiin<->okoly
<f99v.38,+P0>     ol.cheey.qokeol.okeol.okeol.shokol<->ykey
<f99v.39,+P0>     dar.shol.okchey.ckhey.qokololal<->okeol
<f99v.40,+P0>     or.aiin.okeody.okol.odaiin.qoky<->olaldy
<f99v.41,+P0>     qockhol.oiin.shody.qokol.aiidal<->aiidaiim
<f99v.42,+P0>     ol,sheol.olkeol.okol.or.oraloly<->ykeol.okal.okaldaly
<f99v.43,+P0>     ychol,olkeeoldy<$>
<f99v.44,@Lf>     <!114b>koleearol
```

ZL's "hand 4?" and "faces capsicum" comments are catalogue notes, **not** findings of this pass. Family strings `otoldy` / `oldy` / `otaly` / `otoky` / `otal` match IT.

Source: https://voynich.nu/data/ZL3b-n.txt
