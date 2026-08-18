# Voynich pass 7 - f41v working notes (not a translation)

**For:** Jon Bailey
**Date:** 14 Aug 2026 (ET)
**Status:** constrained seventh pass on the leftover unique herbal whole-plant label. **No verified full translation of Beinecke MS 408 exists.** Nothing below is a decipherment. Every gloss is marked **HYPOTHESIS**. No plant is identified. The f9v Viola / herba trinitatis literature ID, the f10v hellebore catalogue note, the ZL "faces capsicum" comment, the quire-8 ELV/ThP IDs, and the quire-6 ELV/ThP IDs for this drawing (daucus / fern / maidenhair / tansy / "plain carrot") are **not imported**.

This note finishes the experiment pre-registered in pass 6 S7: take f41v (`$I=H`, `$L=B`), the remaining unique herbal `@Lp` in IT (`keerodal`, P=0 in prior notes), and test whether the exact string is still unique, whether the two-sided `ok-`/`ot-` vs `qo-` score returns on a page that actually has running text, and whether `daiin`/`chol`/`ol`/`or` stay in the prose and off the caption. Pass 6 already put `dam` on f41v.3 as P. This page is where that same-page check is scored.

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
| Folio description f41v | https://www.voynich.nu/q06/index.html (quire 6; site update 15/06/2025) |
| Colour-letter table | https://www.voynich.nu/writing.html (update 13/06/2025), keyword COL |
| Manuscript | Yale, Beinecke Rare Book & Manuscript Library, MS 408 |
| Prior notes | `notes/pass-1.md`, `notes/pass-2-f9v.md`, `notes/pass-3-f10v.md`, `notes/pass-4-f99r.md`, `notes/pass-5-f99v.md`, `notes/pass-6-f65r.md` |

**Tokenisation (IVTFF 2.0), same as the pass-2 / pass-3 / pass-4 / pass-5 / pass-6 practice.** `.` is a word break. `<->` is a **word space** (do not strip and concatenate). All remaining `<>` markup is stripped (`<%>`, `<$>`, `<!...>`, leftover `<@H=n>`). Tokens must contain at least one A-Z letter. `?` is kept if present. Paragraph text = loci whose flags contain `P`. Labels = flags containing `L`.

ZL is the **control**, not the running text. ZL extras: uncertain commas are **joined** (not a space); alternatives `[a:b]` take the first reading; ligature braces `{ct}` / `{cthh}` / `{ck}` expand to their contents.

Stripping leftover `<@H=n>` markup (two inline hand tags on f115r, not on f41v) keeps this parse's corpus totals in line with pass 2 / 3 / 4 / 5 / 6: **34,486 P / 7,140 types; 1,038 L / 763 types**.

**What this is not:** a download of any copyrighted monograph, a Cheshire/Gibbs-style "complete solution," a language identification, a claim that EVA letters are phonemes, a plant identification, or a public post.

---

## 2. Folio text used

### 2.1 Why f41v

Pass 6 pre-registered this page because:

- It is the leftover unique herbal `@Lp` after f65r: IT `keerodal`, prior notes P=0, L=1.
- f65r had **no** running text. f41v has both bands (the `Lp` **and** 7 lines of P), so the two-sided prefix test returns.
- `dam` was already visible on f41v.3 as P. Same-page check: formula in the prose, not in the caption.
- ZL reads `keer[e:o]dal`. The vowel split is the control.
- Do **not** import viola, hellebore, capsicum, geranium, rue, dropwort, *Spiraea*, daucus, fern, maidenhair, tansy, or "plain carrot."

Page header from IT2a-n (identical flags in ZL):

```
<f41v>  <! $Q=F $P=B $F=a $B=1 $I=H $L=B $H=5 $C=2>
```

`$Q=F` quire 6, `$I=H` herbal, `$L=B` Currier B, `$H=5` LFD hand 5, `$C=2` Currier hand 2. Quire 6 (https://www.voynich.nu/q06/index.html): RZ language **B** (page) / **B+** (folio) / **B** (bifolio); LFD hand 5. writing.html hand table: f41 is Currier 2 / LFD 5.

### 2.2 Public folio description (quire 6 only)

**Sourced, not invented.** Quire 6 page, current as of the 15/06/2025 site update:

- Herbal page.
- Plant drawing with **bright brown roots**, **frilled fingered leaves**, and **seeds at the top**.
- Herbal drawing characterisation (Gheuens/Rapaport): **! a: veined leaves** - an a-feature on a B-language page. Drawing-style note, not a plant ID, not an EVA pairing.
- **8** text items: **7** lines of standard paragraph text; **1** plant label. Matches IT (7 `P` loci, 1 `@Lp`).
- "There are 7 lines of writing in a single paragraph, near the bottom of the page. There is a single and separate word **(label?)** just above the start of the text." The parenthetical is the site's own uncertainty. writing.html (Labels) agrees: "A few whole plant labels in the herbal sections, on f2r, **f41v (uncertain)** and f65r."
- Currier language: B. RZ: B / B+ / B. LFD hand 5.

**Catalogue IDs printed on the quire-6 f41v block, recorded and unused:** ELV daucus; ThP fern, maidenham fern???, tansy? ZL comments add "Maidenhair fern??? Tansy?" and "Plain carrot or variety (RZ)." Same status as the f9v viola / f10v hellebore / ZL capsicum / quire-8 geranium notes. **Not imported. Not used as a crib.**

### 2.3 Labels vs running text

First same-page two-sided score on a **herbal** folio in this series (f99r / f99v were pharmaceutical). f65r could not run this test.

| Band | IT loci | IT tokens |
|---|---|---|
| Running text (`P`) | **7** (one paragraph: .2-.8) | **67** |
| Labels (`L`) | 1 (`@Lp`) | **1** (`keerodal`) |
| Whole-plant `Lp` | **1** | 1 |
| `Lf` / `Lc` | 0 / 0 | - |

ZL, under the comma-join / first-alt rule: **62** P tokens, **1** L token (`keeredal`).

This is the only herbal page in IT that has both a real plant `L` and P-text. f49v also flags L+P, but those L tokens are the left-margin SEQ single characters (`f o r y e k...`), not a plant label. Not used.

### 2.4 The Lp (IT primary; ZL control)

| Locus | Flag | IT EVA | ZL EVA | Notes |
|---|---|---|---|---|
| f41v.1 | `@Lp` | **keerodal** | **keer[e:o]dal** | IT: certain `o`. ZL: uncertain vowel `[e:o]`. |

**Exact readings**

- IT (as in the file): `keerodal` -> token **`keerodal`**.
- ZL (as in the file): `keer[e:o]dal`.
- ZL under this series' tokenisation (`[a:b]` take first): **`keeredal`**.
- ZL second-alt (sensitivity, not the running parse): `keerodal` - agrees with IT.

The disagreement is **only** the fourth letter (`o` vs `e`). Both files agree there is one word. Both files agree there is no word-space inside it. Both files agree there is no `qo-`, no `ok-`, no `ot-` on this locus. writing.html already flags the locus as an **uncertain** whole-plant label; the quire page's "label?" is the same hedge.

`keeredal` is a **hapax invented by taking the first alternative**. It does not exist as a string anywhere else in IT or ZL. It is not promoted to a second name.

### 2.5 f41v running text (IT, cleaned)

One paragraph, seven lines, near the bottom. Line IDs are Takahashi loci. `<->` already expanded to spaces.

```
f41v.2   pcheody qofcheepy ofchdy cfhekchdy ypchedy chepchefy shdchdy qotal dar
f41v.3   dshedy tchey s aiin shekey okedy okaly daiin okedy ykeeody choy keoy dam
f41v.4   qokeody okey qokeody oleeol lkedy lkeeody qokeedy okeey qokol sheols
f41v.5   ycheos olchey daiin or chol ol aiin oteedy qoteol oteodar orain
f41v.6   todaiin ol cheos yteedy okal old oteol qokal or oteody
f41v.7   ykeey okey ykeeol ckhdy chdal ykeo aiin okeody oly
f41v.8   daiin olkeeo lkol chedy okeey
```

Paragraph-initial word: **pcheody** (gallows `p` - the known paragraph-start preference). Not treated as a plant name. Line-initial first words: pcheody, dshedy, qokeody, ycheos, todaiin, ykeey, daiin. `dam` sits line-final on f41v.3 - the same common `dam` as f65r `@Lp`, f99r.40 `@Lf`, and f99v.34 P. **Verified this pass.**

### 2.6 IT vs ZL (control)

Seven of eight loci disagree. Most are P space-joins or one-letter reads. Function-word **direction** is stable. The Lp vowel is the disagreement that matters.

| Locus | IT | ZL (raw) | ZL (this parse) |
|---|---|---|---|
| f41v.1 `@Lp` | `keerodal` | `keer[e:o]dal` | **`keeredal`** (first-alt) |
| f41v.3 | `s aiin` | `s,aiin` | `saiin` |
| f41v.4 | `qokeody` | `qoke[o:d]dy` | `qokeody` (first-alt matches IT) |
| f41v.5 | `chol ol aiin` | `chol[a:o]laiin` | `cholalaiin` (swallows `chol`+`ol`+`aiin`) |
| f41v.6 | `todaiin` ... `old` | `tadaiin` ... `[o:a]ld` | `tadaiin` ... `old` (a/o on the first word; `old` matches) |
| f41v.7 | `ykeo aiin` | `ykeo,aiin` | `ykeoaiin` |
| f41v.8 | `lkol chedy` | `lkol,chedy` | `lkolchedy` |

That is why ZL P is **62** tokens against IT **67** (four comma-joins plus the `chol[a:o]laiin` collapse remove five tokens). `dam` survives in both. `daiin` x3 survives in both. `chol` is IT-only on this page (ZL eats it). `ol` is 2 IT / 1 ZL.

---

## 3. Stats (verified on IT2a-n / ZL3b-n this pass)

Method: same as pass 6, with the `<->` = space rule and the `<@H=n>` strip stated in S1. Every number below is computed from the files this pass. Corpus P/L totals **match pass 2 / 3 / 4 / 5 / 6**: 34,486 P tokens / 7,140 types; 1,038 L tokens / 763 types.

### 3.1 f41v running text (IT)

| Measure | Value | Source |
|---|---|---|
| Word tokens | **67** | verified (json list length) |
| Word types | **57** | verified |
| Type/token ratio | 0.851 | computed |
| Hapax types on the page | 49 | computed |
| Mean / median word length | 5.16 / 5 EVA letters | computed |
| Paragraphs | 1 | IT `<%` / `<$>` |
| Lines (P loci) | 7 | IT + ZL |
| EVA word-initial `qo-` | 8 tokens | computed |

**Top tokens on f41v P (IT)**

| Rank | EVA | n | Notes |
|---|---|---|---|
| 1-2 | aiin, daiin | 3 each | daiin still 0 as a label here |
| 3-8 | okedy, qokeody, okey, okeey, or, ol | 2 each | formulaic herbal-B prose |
| 9+ | 49 hapaxes | 1 each | including `dam`, `chol`, `pcheody` |

**Function-word check (the pass-1 / 2 / 3 / 4 / 5 / 6 table), now on a herbal-B page that has P**

| EVA | f41v P IT | f41v P ZL | f41v L IT | f41v L ZL | IT P corpus | Notes |
|---|---|---|---|---|---|---|
| daiin | **3** | 3 | **0** | 0 | 834 | fires in P (.3, .5, .8). Not the Lp. Prediction held. |
| dain | 0 | 0 | 0 | 0 | 207 | absent |
| chol | **1** | 0 | 0 | 0 | 384 | IT only (.5). ZL swallows it into `cholalaiin`. Not the Lp. |
| chor | 0 | 0 | 0 | 0 | 217 | absent |
| ol | **2** | 1 | 0 | 0 | 521 | fires (.5, .6). ZL keeps one. Not the Lp. |
| or | **2** | 2 | 0 | 0 | 345 | fires (.5, .6). Not the Lp. |

Prediction from pass 1 / 6: they stay common in P; they should **not** be the Lp. **Both halves held.** This is the first herbal page in the series where the P-side of that prediction is actually scorable (f9v/f10v were herbal A; f65r had no P). `ol`/`or` fire here. That does **not** save or kill the herbal-A ol/or claim. f2v remains that control (`ol` 0 / `or` 0 on f2v in this parse; `daiin` 5, `chol` 5, `chor` 5).

**Word-final letters on f41v P:** y 34, l 13, n 8, r 4, s 4. Same y/l/n/r preference. Almost no word ends in a gallows.

**Word-initial letters on f41v P:** o 24, q 8, c 8, y 7, d 6.

**Word-initial bigrams on f41v P:** ok 9, qo 8, ol 7, ch 6, da 5, yk 4, ot 4. Prose on this page is `ok-`/`qo-` present, as predicted for running text.

### 3.2 f41v labels (IT)

| Measure | Value | Source |
|---|---|---|
| Word tokens | **1** | verified |
| Word types | **1** | verified |
| Type/token ratio | **1.000** | computed |
| Hapax types on the page | 1 | no exact string repeats (n=1) |
| Mean / median word length | 8 / 8 | `keerodal` |
| `Lc` / `Lf` / `Lp` | 0 / 0 / 1 | IT flags |

ZL (first-alt): 1 token / 1 type (`keeredal`).

**Word-initial bigrams on f41v L (IT):** ke 1. **qo = 0. ok = 0. ot = 0.**

### 3.3 ok-/ot- vs qo- (the label-prefix test, two-sided again)

Corpus rates this parse (match pass 2 / 3 / 4 / 5 / 6):

| Band | n | ok- | ot- | ok+ot | qo- |
|---|---|---|---|---|---|
| IT P | 34,486 | 6.0% | 5.4% | **11.4%** | **15.1%** |
| IT L (all) | 1,038 | 16.0% | 17.1% | **33.0%** | **0.9%** |
| IT Lf only | 216 | 12.5% | 16.7% | 29.2% | **0** |
| IT Lc only | 40 | 17.5% | 15.0% | 32.5% | **0** |
| IT Lp only | 4 | 0 | 1 (`otaim`) | **1/4** | **0** |

The 9 corpus `qo-` labels are still not herbal-plant / pharma: f66r `L0` (qor, qotesy, qokal, qolsa), f67r2 `@Ls` qotoear, f73v `&Lz` qokeoly, f75v `Ln`/`Lt` (qokal, qoted, qotedy). **`qo-` remains 0 on `Lf` / `Lc` / `Lp`.**

**This page**

| Prefix | f41v P IT (n=67) | f41v L IT (n=1) | f41v P ZL (n=62) | f41v L ZL (n=1) |
|---|---|---|---|---|
| `ok-` | 9 (13.4%) | 0 | 9 (14.5%) | 0 |
| `ot-` | 4 (6.0%) | 0 | 4 (6.5%) | 0 |
| ok+ot | **13 / 67 = 19.4%** | **0 / 1 = 0%** | **13 / 62 = 21.0%** | **0 / 1 = 0%** |
| `qo-` | **8 / 67 = 11.9%** | **0 / 1 = 0%** | **8 / 62 = 12.9%** | **0 / 1 = 0%** |

Prediction from pass 6: `keerodal` is not `qo-`; running text may have `qo-`.

- **L `qo-` survived.** 0 in IT, 0 in ZL. Same suppression as every `Lf`/`Lc`/`Lp` in the series.
- **P `qo-` survived.** 11.9% is *near* the corpus-P mean (15.1%) and includes ordinary `qokeody`/`qokeedy`/`qokol`/`qokal`/`qoteol` plus rarer `qofcheepy`, `qotal`. Direction: legal in prose.
- **P ok+ot is above corpus-P, below corpus-L.** 19.4% vs 11.4% / 33.0%. Cause, marked as such: this herbal-B paragraph is `okedy`/`okey`/`okeey`/`okal` plus four `oteedy`/`oteol`/`oteody`/`oteodar`. It is not a conversion of running text into labels. The **cleaner discriminator on this page is still `qo-`**.
- **L ok+ot is 0.** The unique `Lp` is **not** an `ok-`/`ot-` word. Small-n (n=1): do not over-read the percentage. The **direction that was predicted** was "not `qo-`," and that held. The stronger pass-1 claim that name-*shaped* labels lean `ok-`/`ot-` is **stressed** here: the last unique herbal `Lp` does not wear the classifier. That is a fact about this token, not a wound to the corpus 33% rate.

### 3.4 keerodal (the point of this pass)

**IT corpus (this parse)**

| EVA | P | L | all | Other life (IT) | Role this pass |
|---|---|---|---|---|---|
| **keerodal** | **0** | **1** | 1 | L: **this page only**. Exact string nowhere else. 0 in P. 0 in non-P/non-L. | **still unique.** Name-*shaped* leftover. Not a verified name. |
| keeredal | 0 | 0 | 0 | ZL-first-alt artefact on this page only | not a token in IT |
| keerdal | 0 | 0 | 0 | - | absent |
| keer* (any token starting `keer`) | 0 | 1 | 1 | only `keerodal` | head is unique |
| keero* | 0 | 1 | 1 | only `keerodal` | head+mid is unique |

**ZL control (first-alt / comma-joined)**

| EVA | P | L | Notes |
|---|---|---|---|
| keerodal | 0 | **0** | the f41v head is read `keeredal` |
| keeredal | 0 | 1 (f41v.1 only) | hapax first-alt; 0 in P |
| keer* | 0 | 1 | only `keeredal` |
| keero* | 0 | 0 | first-alt breaks `keero-` |

**Close variants, pre-registered, not fished**

- `keer*` / `keero*`: **unique** in IT (this `Lp` only). Unique in ZL as `keeredal`.
- `*odal` (substring): a **productive tail**, not a unique stem. IT has 125 tokens containing `odal`, 95 ending in `odal`. Exact token `odal` is common-ish in P (dozens of hits across herbal / astro / recipes) and is a zodiac `Lz` on f72v1.10. Other L tails: `ytodal` f67r2 `@Ls`, `okeeodal` f68r1 `@Ls`. **None of those is `keerodal`.** A common tail does not make the full string common.
- Nearest neighbour, recorded and **not promoted**: `keeodal` (P only: f67r1.2, f111r.33). Same `-odal` tail, no `r`, not a label, not this page. Do not fish f67r1 or f111r.

**Still unique?** **Yes**, as an exact string, in IT. P=0, L=1, f41v.1 `@Lp` only. ZL's first-alt `keeredal` is also P=0, L=1, this page only. The vowel is uncertain; the uniqueness of *whichever* reading you take is not.

That uniqueness is the **filter** result, not a translation. One token on one drawing, with an uncertain vowel and an uncertain "is this even a label?" hedge on the public quire page, is as far as a name-candidate can get without a second hit.

### 3.5 Repeating labels on f41v

Exact string repeats on the L set: **none.** 1 token, 1 type.

The interesting same-page fact is **cross-band**: `dam` is in the P-text (f41v.3) and is **not** the caption. That is the pass-6 prediction, scored on the page that has both.

### 3.6 Prior hapax sets (record, do not fish)

| Set | Hits on f41v L | Hits on f41v P |
|---|---|---|
| f9v hapax set (`fochor`, `oporody`, `qopchypcho`, `olcfholy`, `ypcheey`, `rokyd`, `kyty`, `chshoty`) | **0** | **0** |
| f10v hapax set (`chckhan`, `chcthor`, `olty`, `qokchyky`, `qotchytor`) | **0** | **0** |
| f10v extra P<5 (`otydy`, `qotoiin`, `choraiin`, `pcheey`) | **0** | **0** |
| `otaim` | **0** | **0** |
| `alam` | **0** | **0** |
| `dam` | **0** | **1** (f41v.3) - already predicted; formula, not a hapax |

Sixth consecutive miss for "a rare herbal-page token from f9v/f10v recurs as a later `Lf`/`Lc`/`Lp`." Still not fatal. Still a miss. `keerodal` itself does **not** appear on f9v, f10v, f65r, f99r, or f99v (already true in prior passes).

### 3.7 Colour / paint Latin letters

**Absent.**

Sourced: writing.html COL table (update 13/06/2025) has **no f41v row**. writing.html also notes that all COL cases found so far are on language-A / LFD-hand-1 pages; f41v is Currier B, LFD hand 5.

**Not present in IT2a-n or ZL3b-n as EVA tokens.** No standalone Latin `p` / `r` / `g` / `rot`. Nothing to keep out, and nothing to import.

Folio number "41" is on f41r (quire page), a later folio number, not EVA. Reeds' red/green/blue colour note in the older interlinear header is paint on the drawing, not EVA.

### 3.8 Corpus totals vs earlier passes

This parse: **34,486 P / 7,140 types**; daiin 834, ol 521, chol 384, or 345, chor 217, dain 207. **1,038 L / 763 types.** Matches pass 2 / 3 / 4 / 5 / 6. Pass 1's 33,707 / daiin 776 pair remains unverified.

IT `Lp` tokens this parse: **4 / 4 types** (`keerodal`, `otaim`, `dam`, `alam`). ok+ot = 1/4 (`otaim`); qo- = 0. Matches the pass-5 / pass-6 corpus-Lp row.

After this pass the **unique P=0 L=1 herbal `Lp` leftover in IT is one token: `keerodal`.** `otaim` is P=1. `dam` is formula. `alam` is P=7. ZL-only `ytoail` on f2r is not an IT finding (IT marks f2r P-only). ZL-join `otaimdam` is a space-model artefact.

---

## 4. What survived / died from pass 1-6 predictions

Pre-registered tests, scored honestly.

1. **`keerodal` is still unique (P=0, L=1).** **Survived.** Exact string 0 in P, 1 in L, this `@Lp` only. `keer*` / `keero*` are the same one token. ZL first-alt `keeredal` is also unique. The `-odal` tail is common; the full string is not.

2. **ok-/ot- is label-legal; qo- may appear in running text, not on labels.** **Survived on qo- and on P; stressed on L ok+ot.** f41v P: qo- 11.9%, ok+ot 19.4%. f41v L: qo- **0**, ok+ot **0** (the Lp is `keer-`, not `ok-`/`ot-`). Whole-corpus `Lf`/`Lc`/`Lp` qo- remains 0. Two-sided score **returned**, as promised. The unique herbal name-candidate does not wear the classifier. That is a stress on "ok/ot is the name-like layer," not a kill of the corpus 33% rate and not a `qo-` leak.

3. **daiin / chol / chor / ol / or stay function-like, not names.** **Survived.** daiin x3 in P, 0 in L. chol x1 in P (IT), 0 in L. ol x2 / or x2 in P, 0 in L. They are not the Lp. First herbal page in the series where the P-half is scorable and holds.

4. **`dam` is formula, allowed in the prose on this page.** **Survived.** f41v.3 P, line-final. Same token as f65r `@Lp` and f99r.40 `@Lf`. Same-page evidence that the formula word lives in the paragraph, not in the caption.

5. **Unique rare tokens are the only name candidates.** **Survived as a filter, and the IT herbal `Lp` inventory is now exhausted.** After scoring f65r and f41v, the unique P=0 L=1 leftover is **one token**: `keerodal`. `otaim` is name-*shaped* but P=1. Nothing else in the IT `Lp` set qualifies.

6. **Do not identify any plant as a species. Do not import viola, hellebore, capsicum, geranium, rue, dropwort, *Spiraea*.** **Held.** Quire-6 ELV/ThP IDs (daucus / fern / maidenhair / tansy) and the ZL "plain carrot" comment recorded in S2.2 and left unused. The a-veined-leaves drawing note stays in the catalogue column. No rare EVA token was mapped onto a medieval plant name.

7. **Colour letters stay out of the EVA gloss.** **Held** (vacuously: no COL row).

8. **f9v / f10v hapax recurrence.** **Miss, not fatal.** Sixth miss.

---

## 5. Hypothesis gloss table

**Every row is a HYPOTHESIS.** Confidence is structural (distribution + position), never semantic. "Gloss" means *role in English*, not a claimed Voynichese meaning. No row identifies the language. No row identifies a plant.

### 5.1 The Lp token

| EVA | Where | Role (HYPOTHESIS) | Constrained gloss (HYPOTHESIS) | Why this pass allows it | Why it may be wrong |
|---|---|---|---|---|---|
| **keerodal** | f41v.1 `@Lp` (IT) | unique whole-plant label | **candidate plant-name piece**, not a verified name. The only IT herbal `Lp` that is still P=0 | Hapax. Sitting as `@Lp` on a herbal page. `keer*` / `keero*` unique. `qo-` 0. Function words are in the P-text, not here. | One token. ZL prefers `keeredal`. writing.html and the quire page both hedge ("uncertain" / "label?"). Not `ok-`/`ot-`. `-odal` is a common tail. No second hit on a matching drawing. |
| **keeredal** | ZL first-alt of f41v.1 only | space/alt artefact | **no gloss.** Not a second reading | Hapax invented by taking `[e:o]`'s first letter. 0 in P. | If independent transliterations (GC/v101, RF) also write `e` here, the IT `o` is the artefact. Stolfi-era interlinear already split (H/G `keero!dal`, F `teero!dal`, U `keesh,dal`) - recorded as background, not used as a third corpus. |
| **keeodal** | f67r1.2 P, f111r.33 P | nearest neighbour, **not merged** | **no gloss.** Not this plant's name | Same `-odal` tail, no `r`, not a label, not this page. | If a better space-model turns `keerodal` into `kee`+`rodal` or into `keeodal`, uniqueness dies. Not this parse. |
| **-odal** (tail) | productive in P; a few non-plant L (`ytodal`, `okeeodal`, `odal`) | generic tail | **not** a name by itself | Common. Opposite of "the tail is unique." | If almost every `-odal` word is independently a plant name, the tail-is-generic claim dies. Observed: they sit in ordinary P and in star/circle labels. |

### 5.2 Prefix split and function words (re-tested, two-sided)

| EVA | Role (HYPOTHESIS) | Constrained gloss (HYPOTHESIS) | Why this pass still allows it | Why it may be wrong |
|---|---|---|---|---|
| **ok- / ot-** (prefix) | label-legal classifier / construction | "item/herb-of ___" | Corpus 33.0% vs 11.4%. Legal in this page's **P** (19.4%). | **0 on this Lp.** The last unique herbal name-candidate does not wear it. Dual use in prose (`okedy`/`okeey`/`oteol`) weakens "classifier only." |
| **qo-** | prose-legal, label-illegal | legal running-text vocabulary; **not** names | **8x** in f41v P, **0** in f41v L. Still 0 on all `Lf`/`Lc`/`Lp`. | If a later transliteration finds a clean `Lp` `qo-` here, the ban is empirical not absolute. IT/ZL do not. |
| **daiin / chol / ol / or** | closed-class / generic | not names | daiin 3, chol 1, ol 2, or 2 in P; **0** on the Lp. | Null / default emit / minim-count. ZL can hide `chol`/`ol` in a join. |
| **dam** | formula / too-common-in-P | **not** a plant name. "of / and / this" **or** a generic caption-word | P=93. On this page as P (f41v.3). Already an `Lf` on f99r and half of the f65r `Lp`. | If a better space-model makes most of the 93 P hits *not* `dam`, the commonness is an artefact. Not this parse. IT and ZL both keep f41v.3 as `dam`. |
| **pcheody** | paragraph-initial gallows word | section-open / ordinary P-start, **not** a plant name | Gallows-`p` start matches the known paragraph-initial gallows rule. Lives in the paragraph, not on the drawing as a label. | Hapax paragraph-starters are unfalsifiable as "titles." |

**Explicitly refused glosses (this pass):**

- EVA letters as Latin phonemes (`keerodal` != a pronounced word; `dal` != Latin *dal*; `keer` != any Germanic / Arabic / Nahuatl stem).
- `keerodal` / `keeredal` / `keeodal` as any plant name (daucus, fern, maidenhair, tansy, carrot, viola, hellebore, capsicum, geranium, rue, dropwort, *Spiraea*, or anything else).
- A full caption translation of the seven-line paragraph, or of the one-word label.
- Any named language (Latin, German, Nahuatl, Hebrew, Occitan, Welsh, proto-Romance, Arabic, etc.).
- Importing the quire-6 ELV/ThP IDs, the ZL "plain carrot" comment, the f9v viola ID, the f10v hellebore catalogue note, the ZL "capsicum" comment, or the quire-8 geranium/rue/dropwort IDs onto this drawing.
- Treating the Gheuens/Rapaport a-veined-leaves exception as "the same plant class" in EVA.
- A twin-token test on `keeodal` (f67r1 / f111r), on f41r, or on f2r `ytoail`. Not pre-registered; not run as a name hunt.
- Promoting ZL-only `ytoail` (f2r `@Lp`) into the IT leftover list.
- A public post.

**Strongest claim this pass will defend:**
The leftover unique herbal whole-plant label in IT is still unique. `keerodal` is P=0, L=1, f41v.1 `@Lp` only. `keer*` / `keero*` have no other life. ZL's first-alt `keeredal` is the same one locus with an uncertain vowel. On the same page, `qo-` is legal in the paragraph (11.9%) and banned on the `Lp` (0); `daiin`/`chol`/`ol`/`or` fire in the prose and are not the caption; `dam` sits in the prose, as predicted. The token is name-*shaped* and unproven. It is not `ok-`/`ot-`. The public catalogue already hedges the locus ("label?" / "uncertain"). None of this is a plant identification. The IT herbal `Lp` inventory is now exhausted: the unique-name leftover is **one token**.

---

## 6. What would falsify this pass

1. **"keerodal is unique" dies if** the exact string appears as P or as another L in IT/ZL under this tokenisation, **or** if a better space-model splits it into common pieces that already exist (`kee` + `rodal`, `keer` + `odal`, etc.) *and* those pieces are the intended words. Observed: one token, no split in IT. ZL's vowel alt does not create a second locus.

2. **"keeredal is only an alt-artefact" dies if** independent transliterations (GC/v101, RF) read `e` here **and** that `keeredal` then matches some other page. Currently `keeredal` is 0 everywhere else.

3. **qo- label ban dies if** a clean `Lf`/`Lc`/`Lp` `qo-` label appears in IT/ZL. Not on this page. Not on any pharma/herbal plant label in this parse.

4. **"function words are not the Lp" dies if** a folio whose plant is independently identified uses `daiin`/`chol`/`chor`/`ol`/`or` *only* as a unique caption. Observed on this page: they are in the paragraph, not the caption.

5. **"dam is formula, allowed in this prose" dies if** the f41v.3 hit is shown to be a different lemma under a better space-model **and** the 93 P hits collapse. IT and ZL both keep `dam` here.

6. **"no f9v/f10v name on f41v" dies if** an independent transliteration reads one of those hapaxes as this `Lp`. IT and ZL do not.

7. **Daucus / fern / maidenhair / tansy / carrot as catalogue notes (not fact) is violated if** a later note treats those IDs as established and imports them onto `keerodal`. They are not.

8. **Constrained semi-language stance dies** on the same terms as pass 1 S6.5: a pre-registered simple substitution into a known language that yields grammatical running text **and** matching names on the rare / `Lp` words. Not observed.

---

## 7. Next folio to try

**Primary next step: stop-and-summarize (pass 1-7 rollup).**

Why that, given what this pass actually found:

- The IT herbal `@Lp` inventory is **exhausted**. Two loci, four tokens. `dam` is formula. `alam` is uncommon stars-prose. `otaim` is name-*shaped* but P=1. `keerodal` is the last unique P=0 L=1 leftover - **one token**.
- A name-candidate list of one unproven hapax, with an uncertain vowel and an uncertain "is this a label?" hedge, is not a licence to fish the next herbal page for lookalikes. That is how the series would start inventing names.
- The structural claims that can still be defended (function-words are generic; `qo-` is label-illegal; `ok-`/`ot-` is label-legal in the corpus; unique rare tokens are the only name *candidates*; a multi-word `Lp` is not automatically three names) are now scored on f1r, f9v, f10v, f99r, f99v, f65r, and f41v. They need a rollup, not a new drawing.

**Leftover control, if one more empirical page is wanted before the rollup: f2v (herbal-A ol/or control).**

Why f2v is still valid and still not a name-page:

- This parse: P=61, L=0. `ol` **0**, `or` **0**, `daiin` 5, `chol` 5, `chor` 5. That is the herbal-A ol/or absence the later pharma/herbal-B pages cannot test.
- It cannot grow the name-candidate list (no `L`). It can only re-score S5.1 function words.
- Do **not** import viola, hellebore, capsicum, daucus, fern, tansy, or carrot onto f2v.

**Not next:** f41r (recto of this leaf - not pre-registered; do not chase `dam` onto the other side). f111v (recipes; do not chase `otaim` or `keeodal`). f2r ZL-only `ytoail` (IT has no L there). Another quire-19 pharma page. A twin-token hunt for `keeodal`.

---

## 8. Bottom line for this pass

f41v is readable as *structure*: one uncertain whole-plant label, one herbal-B paragraph, no paint letters, and a caption whose exact string does **not** appear in the 67 words underneath it. `keerodal` is still unique (P=0, L=1). ZL's first-alt is `keeredal` (same locus, uncertain vowel). `qo-` is legal in the paragraph (11.9%) and banned on the `Lp`. `daiin`/`chol`/`ol`/`or` fire in the prose and are not the caption. `dam` sits in the prose, as predicted. The token is not `ok-`/`ot-`. It is not readable as *language*, and it is not a crib for the plant.

The pass-1 split survives its first real herbal page that has **both** bands: **high-frequency ch/d-words are generic and are not the caption; `qo-` is prose-legal and label-illegal; unique rare tokens are the only name candidates; a unique `Lp` hapax is still only a candidate.** `ok-`/`ot-` remains label-legal in the corpus and is simply **not worn** by this leftover hapax. The IT herbal `Lp` list is now scored. The unique-name leftover is one token, unproven.

Until `keerodal` is found on a matching drawing under two transliterations - or until a pre-registered substitution reads this caption as grammar plus a name - this file is still a lab notebook, not a crib.

---

## Appendix A - raw IT loci for f41v (as in the file)

```
<f41v>     <! $Q=F $P=B $F=a $B=1 $I=H $L=B $H=5 $C=2>
<f41v.1,@Lp>      keerodal
<f41v.2,+P0>      <%>pcheody.qofcheepy.ofchdy.cfhekchdy<->ypchedy.chepchefy.shdchdy.qotal.dar
<f41v.3,+P0>      dshedy.tchey.s.aiin.shekey.okedy.okaly<->daiin.okedy.ykeeody.choy.keoy.dam
<f41v.4,+P0>      qokeody.okey.qokeody.oleeol.lkedy<->lkeeody.qokeedy.okeey.qokol.sheols
<f41v.5,+P0>      ycheos.olchey.daiin.or.chol.ol.aiin<->oteedy.qoteol.oteodar.orain
<f41v.6,+P0>      todaiin.ol.cheos.yteedy.okal.old<->oteol.qokal.or.oteody
<f41v.7,+P0>      ykeey.okey.ykeeol.ckhdy.chdal<->ykeo.aiin.okeody.oly
<f41v.8,+P0>      daiin.olkeeo.lkol.chedy.okeey<$>
```

Source: https://voynich.nu/data/IT2a-n.txt

## Appendix B - raw ZL loci for f41v (control)

```
<f41v>     <! $Q=F $P=B $F=a $B=1 $I=H $L=B $H=5 $C=2>
# page 80
# herbal
# Currier's language B, hand 2
# Plant ID: <unreadable>, Fern, Maidenhair fern??? Tansy?
# Plain carrot or variety (RZ)
#
<f41v.1,@Lp>      keer[e:o]dal
<f41v.2,+P0>      <%>pcheody.qofcheepy.ofchdy.cfhekchdy<->ypchedy.chepchefy.shdchdy.qotal.dar
<f41v.3,+P0>      dshedy.tchey.s,aiin.shekey.okedy.okaly<->daiin.okedy.ykeeody.choy.keoy.dam
<f41v.4,+P0>      qoke[o:d]dy.okey.qokeody.oleeol.lkedy<->lkeeody.qokeedy.okeey.qokol.sheols
<f41v.5,+P0>      ycheos.olchey.daiin.or.chol[a:o]laiin<->oteedy.qoteol.oteodar.orain
<f41v.6,+P0>      tadaiin.ol.cheos.yteedy.okal.[o:a]ld<->oteol.qokal.or.oteody
<f41v.7,+P0>      ykeey.okey.ykeeol.ckhdy.chdal<->ykeo,aiin.okeody.oly
<f41v.8,+P0>      daiin.olkeeo.lkol,chedy.okeey<$>
```

ZL's "Fern / Maidenhair / Tansy / plain carrot" comments are catalogue notes, **not** findings of this pass. First-alt of the Lp is `keeredal`. Second-alt matches IT `keerodal`.

Source: https://voynich.nu/data/ZL3b-n.txt
