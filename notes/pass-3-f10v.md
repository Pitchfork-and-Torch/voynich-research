# Voynich pass 3 - f10v + f89v2 working notes (not a translation)

**For:** Jon Bailey
**Date:** 14 Aug 2026 (ET)
**Status:** constrained third pass on one herbal folio and its claimed pharma lookalike. **No verified full translation of Beinecke MS 408 exists.** Nothing below is a decipherment. Every gloss is marked **HYPOTHESIS**. The plants drawn on f10v and f89v2 are **not identified** here. The f9v viola literature ID is **not imported**.

This note finishes the experiment pre-registered in pass 2 (S7): take the next herbal-A page (f10v) and the first herbal/pharma pair that voynich.nu actually calls a lookalike (f89v2 fragment #50), and test whether any rare f10v token recurs as a label on that fragment. A prior worker computed stats and died before writing. Sources were already on disk. They were not re-downloaded. Stats in `(local stats extract, not published)` were recomputed against the files and **agree**. Full extract + expanded stats: `(local stats extract, not published)`, `(local stats extract, not published)`.

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
| Folio description / lookalike | https://www.voynich.nu/q02/index.html (quire 2, f10v); https://www.voynich.nu/q15/index.html (quire 15, f89v2) |
| Manuscript | Yale, Beinecke Rare Book & Manuscript Library, MS 408 |
| Prior notes | `notes/pass-1.md`, `notes/pass-2-f9v.md` |

Tokenisation (this pass, IVTFF 2.0, same intent as pass 2 with the rules stated explicitly):

- `.` is a word break.
- `<->` is a word space (not a join).
- ZL uncertain-space commas are **joined** (`paiin,daiin` -> `paiindaiin`).
- `[a:b]` takes the first alternative.
- `{ct}` / `{cthh}` / `{ch'}` keep the inner string (`{ct}` -> `ct`).
- IVTFF markup (`<%>`, `<$>`, locus tags, `<!...>`) is stripped.
- Tokens must contain at least one A-Z letter. `?` is kept if present.
- Paragraph text = loci whose flags contain `P`. Labels = flags containing `L`.

ZL is the **control**, not the running text. Function-word counts that matter still agree in direction.

**What this is not:** a download of any copyrighted monograph, a Cheshire/Gibbs-style "complete solution," a language identification, a plant identification, or a claim that EVA letters are phonemes.

---

## 2. Folio text used

### 2.1 Why f10v + f89v2

Pass 2 pre-registered this pair because:

- f9v produced **no** rare-token hit on `Lf`/`Lc`/`Lp`. The name test needed a herbal page that actually has a claimed pharma twin.
- f10v is the next herbal-A page in sequence (hand 1, short, two paragraphs above the drawing).
- voynich.nu states a visual lookalike. That claim is cited in S5. It is **not** treated as a fact that the two drawings are the same plant, and it is **not** used to identify either drawing.

Page header from IT2a-n (identical in ZL):

```
<f10v>  <! $Q=B $P=D $F=b $B=2 $I=H $L=A $H=1 $C=1>
```

`$I=H` herbal, `$L=A` Currier A, `$H=1` hand 1. Two short paragraphs (`<%` at f10v.1 and f10v.4; `<$>` at f10v.3 and f10v.7). Text sits above the plant. No `$X=C` colour-annotation flag (f9v had one).

f89v2 header:

```
<f89v2>  <! $Q=O $P=I $F=y $B=2 $I=P $L=A $H=1>
```

`$I=P` pharmaceutical, `$L=A` Currier A, `$H=1` hand 1. Three paragraphs of running text between three rows of plant fragments and containers.

### 2.2 Labels on f10v

**None.** All 7 IT loci are flagged `@P0` / `+P0`. No `Lp`, `Lf`, `Lc`, or any other `L` flag. f10v is running text around a plant, not a caption page. The label-prefix test on *this* folio can only be run on running text. The label test in this pass is run on f89v2.

Whole-plant herbal `Lp` in the same IT file remains exactly the pass-1 pair: **f41v** `keerodal`; **f65r** `otaim.dam.alam`.

### 2.3 f10v in EVA (Takahashi / IT, cleaned)

Line IDs are Takahashi loci. Two paragraphs.

**P1**
```
f10v.1   paiin daiin sheo pcheey qoty daiin cthor otydy sain
f10v.2   dain daiin ckhy chcthor choiin qot chodaiin cthy daiin
f10v.3   dsho ytey kchol olty chol dy
```

**P2**
```
f10v.4   qotchytor shoiin daiin qotchey shcthey ytor dain
f10v.5   sho ykeey daiin qotchy qotor chol daiin qokchyky
f10v.6   shoiin chor shcthy qoty qotoiin qokol choraiin
f10v.7   qokol chyky chol cheky daiin dain chckhan
```

Paragraph-initial words: **paiin** (gallows `p`) and **qotchytor** (word-initial `q`). The first matches the known paragraph-start gallows habit (`fachys`, `fochor`, `pchor`). The second does **not** - P2 opens with a `qo-` word, not `f`/`p`. They are not treated as plant names.

### 2.4 IT vs ZL on f10v (control)

Token lists are in `f10v-f89v2-stats.json` and match the prior `f10v-stats.json`. Space-split / ligature differences only:

| Locus | IT (primary) | ZL (control) |
|---|---|---|
| f10v.1 | `paiin` + `daiin` | `paiindaiin` (ZL `paiin,daiin` joined) |
| f10v.3 | `olty` | `olty` (ZL `ol,ty` joined - **agree** after the comma rule) |
| f10v.4 | `shcthey` | `shcthhy` (ZL `sh{cthh}y`) |
| f10v.5 | `sho` + `ykeey` | `shoykeey` (ZL `sho,ykeey` joined) |
| f10v.5 | `qokchyky` | `qokchyky` (ZL `qokchy,ky` joined - **agree**) |
| f10v.6 | `choraiin` | `choraiin` (ZL `chor,aiin` joined - **agree**) |
| f10v.7 | `chyky` | `chyky` (ZL `chy,ky` joined - **agree**) |
| f10v.7 | `chol` + `cheky` | `cholcheky` (ZL `chol,cheky` joined) |

Function-word counts that matter: **daiin 8 / 7**, **dain 3 / 3**, **chol 3 / 2**, **chor 1 / 1**, **ol 0 / 0**, **or 0 / 0**. The ZL joins eat one `daiin` and one `chol`. Direction is unchanged.

### 2.5 f89v2 labels (IT primary; ZL control)

Every `L` locus. No `Lp` on this page (pharma fragments are `Lf`; jars are `Lc`).

| Locus | Flags | IT EVA | ZL EVA | Role |
|---|---|---|---|---|
| f89v2.1 | `@Lc` | choeesy | choeesy | container |
| f89v2.2 | `@Lf` | okam | okam | plant fragment (row 1, first) |
| f89v2.3 | `@Lf` | darcheos | darcheor | plant fragment |
| f89v2.4 | `@Lf` | chokaro | chokaro | plant fragment |
| f89v2.5 | `@Lf` | sheol | sheol | plant fragment |
| f89v2.6 | `@Lf` | chokam | chokam | plant fragment |
| f89v2.11 | `@Lc` | okory | otory | container |
| f89v2.12 | `@Lf` | otair chody | otair chody | plant fragment (two words) |
| f89v2.13 | `@Lf` | dydariin | dykaran | plant fragment |
| f89v2.14 | `@Lf` | opcheedoy | opcheedey | plant fragment |
| f89v2.23 | `@Lc` | opaloiiry | opaloiiry | container |
| f89v2.24 | `@Lf` | otaram | otaram | plant fragment |
| f89v2.25 | `@Lf` | chtody | chtchy | plant fragment |
| f89v2.26 | `!Lf` | ?ds??o | *(absent)* | IT uncertain; see below |
| f89v2.27 | `@Lf` | rady | sada? | plant fragment |
| f89v2.28 | `@Lf` | dareky | daseky | plant fragment |

IT label tokens: **17 / 17 types** (including the two-word locus and `?ds??o`). ZL label tokens: **16 / 16 types** (locus 26 omitted; ZL Petersen comments mark 23-28 as `<!58a>` ... `<!61>`).

**Locus 26:** Zandbergen, quire 15 note (update 15/06/2025): item #59 was long read as two words one above the other; in May 2025 the bottom word was identified as shine-through from the recto. Stolfi's older interlinear already flagged `*ds**o` as possible bleedthrough of `otal`. This pass **does not** treat `?ds??o` as a real label. ZL is followed on that point.

### 2.6 f89v2 running text (IT, cleaned; three paragraphs)

**P1** (loci 7-10)
```
kosar sheol s aiin koiin chtodaiin pdan choto qofoiin dy qopdol doiir ofaiin ol cfheol dam
daiin ykodair okor chear oteee eeckhy s aiin ckhey otaiin okar dain okol al chor dar
yched okeey qoeol daiin chor chor cheos qol eeeey dal chody cheor chey qoaiin chody
dair or cheol chom qol cheo lcheo lor cheo daiin chkam
```

**P2** (loci 15-18)
```
sor oairar sheety chod s kory ochar eair sheotain ytodaiin
octhos okaiir okeos dar s ?ain ykeody dar okal dal doral dar am
y?eo qokeeol chey sair dam ??yfor opodaiin dam sary qodam yteos aiin
qokor chor cthy daiin chos ?eey dar aiin choeees okar chcthy darams
```

**P3** (loci 19-22)
```
toar qokeeody doefshey dairy sheos psheoepoain dain qekor ykeor otol sheey daldaiin
dol dair chey okaiin shy daiir odor sheos aiin daikeody qokorar sheody qoko ltcheody otal
dar qockhy qokal okeoy cho??? daiin odaiin ykeoda okols sheey keeody daiin qokos okeom
ockhody daiin ykam s chty chy cthey dairair chool loy dair cheodaiin
```

IT P on this page: **158 tokens / 122 types**. ZL P: 150 tokens (comma-joins). Top IT P tokens: daiin 7, dar 6, s 5, aiin 5, chor 4, dam 3, chey 3, dair 3. `sheol` and `chody` each appear in **both** a label and the running text on the same page - they are too common in the P-corpus (`sheol` 106, `chody` 90) to be unique names.

---

## 3. Stats (verified on IT2a-n / ZL3b-n this pass)

Method: S1. Prior `f10v-stats.json` was recomputed; every number below that also appears there **matches**. New numbers (f89v2 P, prefix rates, whole-IT locus lists) are computed from the same files.

### 3.1 f10v running text (IT)

| Measure | Value | Source |
|---|---|---|
| Word tokens | **53** | verified (json list length) |
| Word types | **39** | verified |
| Type/token ratio | 0.736 | computed |
| Hapax types on the page | 33 (62% of tokens) | computed |
| Mean / median word length | 5.09 / 5 EVA letters | computed |
| Paragraphs | 2 | IT `<%` / `<$>` |
| Lines (loci) | 7 | IT + ZL |
| Labels (`Lp`/`Lf`/`Lc`/any `L`) | **0** | IT flags |
| EVA `q` / word-initial `qo-` | 11 tokens | computed |

**Top tokens on f10v (IT)**

| Rank | EVA | n | Notes |
|---|---|---|---|
| 1 | daiin | 8 | 8/53 = 15%. Same workhorse as f1r (7) and f9v (7) |
| 2-3 | dain, chol | 3 each | dain stronger here than on f9v (1) |
| 4-6 | qoty, shoiin, qokol | 2 each | qoty P=85, qokol P=102 - prose-common `qo-` |
| 7+ | 33 hapax types | 1 each | only the P-corpus-rare ones are name *candidates* |

**Function-word prediction check (the pass-1 / pass-2 table)**

| EVA | f10v IT | f10v ZL | IT paragraph corpus (P) | Prediction | Result |
|---|---|---|---|---|---|
| daiin | 8 | 7 | 834 | stay common | **survived** (stronger than f9v) |
| dain | 3 | 3 | 207 | stay common | **survived** (clearer than f9v's 1) |
| chol | 3 | 2 | 384 | stay common | **survived** |
| chor | 1 | 1 | 217 | stay common | present (weak) |
| ol | 0 | 0 | 521 | stay common | **missed** (second herbal-A miss) |
| or | 0 | 0 | 345 | stay common | **missed** (second herbal-A miss) |

`ol` / `or` missing on 53 tokens, after also missing on f9v's 84, is now a **pattern on short herbal-A pages**, not a one-page fluke. Still not a strong kill of the corpus-level closed class (both remain huge in P). Do not promote them to "herbal-A-absent" without a longer page. daiin/dain/chol did fire, and they are the ones that would have been tempting "plant name" readings.

**Word-final letters on f10v:** n 20, y 17, r 6, l 6. Same y/n/r/l preference. Almost no word ends in a gallows.

**Word-initial letters on f10v:** c 14, d 13, q 11, s 7, y 3, p 2, o 2, k 1.

**Word-initial bigrams on f10v:** da 11, qo 11, ch 11, sh 6. `qo-` is tied for the commonest opening. That is a **prose** signal.

**Line-initial first letter (7 lines):** p 1, d 2, q 2, s 2. Opening word of the page is **paiin** (P=8, not a hapax).

### 3.2 ok-/ot- vs qo- on f10v running text

| Prefix | f10v tokens | rate | Tokens | Corpus P rate (this parse) |
|---|---|---|---|---|
| `ok-` | 0 | 0% | - | } |
| `ot-` | 1 | 1.9% | otydy | } **ok+ot = 1 / 53 = 1.9%** vs corpus P **11.4%** |
| `qo-` | 11 | 20.8% | qotyx2, qokolx2, qot, qotchytor, qotchey, qotchy, qotor, qokchyky, qotoiin | corpus P **15.1%** |

Prediction from pass 1: running text may have `qo-`; labels should not. **Survived, loudly.** f10v is *more* `qo-` than the P-corpus and almost empty of `ok-`/`ot-`. That is the opposite of the label profile, which is what you want on a page with no `L` loci.

Most of those `qo-` tokens are corpus-common (`qokol` 102, `qoty` 85, `qotchy` 63, `qotor` 28, `qotchey` 19). Rarity does not move a `qo-` word into the name slot.

### 3.3 Rare / hapax candidates on f10v (`cands_p5`)

Rule, pre-registered: tokens on f10v that occur **fewer than 5 times** in the whole IT paragraph corpus. Recomputed set **matches** the prior json (9 types):

| EVA | f10v | P | L | all | Other IT loci |
|---|---|---|---|---|---|
| chckhan | 1 | 1 | 0 | 1 | - |
| chcthor | 1 | 1 | 0 | 1 | - |
| olty | 1 | 1 | 0 | 1 | - (ZL `ol,ty` joins to the same string) |
| qokchyky | 1 | 1 | 0 | 1 | - |
| qotchytor | 1 | 1 | 0 | 1 | - (paragraph-initial `qo-`) |
| otydy | 1 | 2 | 1 | 3 | f51r.8 P; **f68r1.15 `@Ls`** |
| qotoiin | 1 | 3 | 0 | 3 | f37v.11 P; f58v.15 P |
| choraiin | 1 | 4 | 0 | 5 | f4r.2 P; f34v.8 P; f102v1.10 P; **f72v2.1 `@Cc`** |
| pcheey | 1 | 4 | 0 | 4 | f8r.9 P; f87v.1 P; f105r.24 P |

**Pharma `Lf` / `Lc` / `Lp` hits for these 9: none.**

The only non-P hits are not plant-fragment labels:

- `otydy` at f68r1.15 `@Ls` - astronomical / star label, not `Lf`/`Lc`/`Lp`.
- `choraiin` at f72v2.1 `@Cc` - cosmological circle, not a plant label (`@Cc` is not an `L` flag).

`pcheey` at f87v.1 is running text on a herbal page in the same quire as f89v2. That is geographic coincidence, not a label hit.

**f9v hapax set, re-searched on the whole IT file** (requested): `fochor`, `oporody`, `qopchypcho`, `olcfholy`, `ypcheey`, `rokyd`, `kyty`, `chshoty`. All still **P=1, L=0, locus = f9v only**. None appear on f10v. None appear on f89v2. The f9v miss is unchanged.

Extra requested leftovers from earlier passes:

| EVA | Hits |
|---|---|
| keerodal | **f41v.1 `@Lp` only.** 0 in P. Unchanged. |
| otaim | **f65r.1 `@Lp`** (`otaim.dam.alam`) and **f111v.3 `+P0`**. Not on f10v / f89v2. |
| toldy / otoldy / ytoldy / tsholdy | **not on f10v or f89v2.** `otoldy` remains the repeating pharma type-word (f89r1.4 Lf, f89r2.9 Lc, f99r.14 Lf, f99v.2 Lf, plus f82v.45 Lt). Unused this pass. |

Common f10v types that *do* appear as labels elsewhere (`daiin`, `dain`, `chol`, `chor`, `dy`) are the same high-frequency items pass 1 already refused to read as plant names.

### 3.4 f89v2: ok-/ot- vs qo- on L vs P (the test f9v could not run)

| Cut | n | ok- | ot- | ok+ot rate | qo- | qo- rate |
|---|---|---|---|---|---|---|
| f89v2 IT **labels** | 17 | 2 (okam, okory) | 2 (otair, otaram) | **23.5%** | **0** | **0%** |
| f89v2 IT **P-text** | 158 | 12 | 4 | 10.1% | 15 | 9.5% |
| f89v2 ZL labels | 16 | 1 (okam) | 3 (otory, otair, otaram) | 25.0% | 0 | 0% |
| f89v2 ZL P-text | 150 | 13 | 4 | 11.3% | 14 | 9.3% |
| IT corpus P | 34486 | - | - | 11.4% | - | 15.1% |
| IT corpus L | 1038 | - | - | 33.0% | - | 0.87% |

Prediction: `ok-`/`ot-` elevated on labels; `qo-` suppressed on labels and legal in running text. **Survived on a real label page.** f89v2 P is corpus-P-like (ok+ot 10.1%, qo- 9.5%). f89v2 L has zero `qo-` and a raised ok/ot rate. The page-level ok/ot rate (23.5%) is below the all-label 33% because several f89v2 labels are hapax stems without the prefix (`choeesy`, `darcheos`, `chokaro`, `dydariin`, `opcheedoy`, `opaloiiry`, `rady`, `dareky`, plus common `sheol` / `chody`). The *suppression of `qo-`* is clean.

**Label vocabulary on f89v2 is flat:** 17 tokens, 17 types. Hapax-in-the-whole-file labels (IT): `choeesy`, `darcheos`, `chokaro`, `dydariin`, `opcheedoy`, `opaloiiry`, `rady`, `dareky` (and the discarded `?ds??o`). Those are the only tokens on *this* page that even *could* be unique names - and none of them is an f10v rare token.

Generic / type-word-ish labels on the same page (too frequent in P to be unique species): `okam` (P=23, also 2x `&Lz` zodiac), `sheol` (P=106), `chody` (P=90), `otair` (P=18). `chokam` (P=3, L=1) and `otaram` (P=3, L=1) sit near the rare-name filter but are not f10v tokens.

### 3.5 Colour / paint Latin letters

**Not present in IT2a-n or ZL3b-n as EVA tokens on either page.** f10v has no `$X=C` flag. voynich.nu's f10v note does not list Latin paint letters (unlike f9v's `por` / `p` / `r` / `g`). Nothing to keep out, because nothing is there.

### 3.6 Corpus totals

This parse of IT paragraph text: **34,486 tokens / 7,140 types**; daiin 834, ol 521, chol 384, or 345, chor 217, dain 207. Matches pass 2 and both json files.

Label tokens this parse: 1,038 / 763 types. Unchanged.

---

## 4. The twin test

### 4.1 The public lookalike claim - sourced, not invented

**Sourced.** Rene Zandbergen, voynich.nu, both sides of the pair (latest update on those pages 15/06/2025):

- Quire 2, f10v: "This plant shows some similarity with plant fragment #50 on f89v2." https://www.voynich.nu/q02/index.html
- Quire 15, f89v2: "Fragment 50 shows some similarity with the plant on f10v." https://www.voynich.nu/q15/index.html

That is a **visual** claim ("some similarity"). It is not a claim that the labels match, and it is not a species ID. Literature plant IDs on f10v (ELV: helleborus?; THP: helleborus orientalis; ZL comment: "Hellebore? orientalis") are catalogue notes, **not** findings of this pass. They are not used.

Zandbergen numbers the f89v2 plant fragments 50-61 (row 1 = five plants = 50-54; row 2 = three = 55-57; row 3 = four = 58-61). That numbering matches the 5+3+4 layout in Stolfi's interlinear and the ZL Petersen tags `<!58a>`...`<!61>` on the last row. Under that mapping, **fragment #50 is the first plant-fragment of row 1**, IT/ZL locus **f89v2.2 `@Lf` `okam`**. Stolfi: "plant [1,1] - dark roots, leaves faded." If the sequential numbering is wrong, the lookalike label is still *one of* the row-1 `Lf` words (`okam` / `darcheos` / `chokaro` / `sheol` / `chokam`). This pass does **not** invent a tighter twin than the public note.

### 4.2 Does any f10v rare token match an f89v2 label?

**No. Complete miss.**

- None of the 9 f10v P<5 types appears in the f89v2 IT label set.
- None appears in the f89v2 ZL label set (including the IT/ZL reading variants `darcheor`, `otory`, `dykaran`, `opcheedey`, `chtchy`, `sada?`, `daseky`).
- **No f10v type at all** - rare or common - appears as an f89v2 label. Not `daiin`, not `chol`, not `otydy`, not `okam`.
- The likely fragment-50 label, `okam`, is P=23 and also a zodiac label (`&Lz` twice). It is a generic `ok-` stem, not a unique name, and it is **absent from f10v**.

A miss is not fatal (pass 2 already said that). It is still a miss. The public lookalike does **not** come with a matching rare EVA token. This pass will not write a plant-name hypothesis in ink for f10v or for fragment 50.

### 4.3 What the miss does and does not kill

It does **not** kill "labels are a different vocabulary." f89v2 labels are flat, `qo-`-free, and partly `ok-`/`ot-`. That half of the split **survived**.

It **does** fail the specific hope that a claimed herbal/pharma twin would share a rare token. Visual similarity, in this one public pair, is not accompanied by a shared name-candidate. Anyone who wants "labels are names of the drawn plant" now owes either (a) a different twin whose rare tokens actually match, or (b) a reason the herbal running text and the pharma label are allowed to name the same plant with different words.

---

## 5. What survived / died from pass 1-2 predictions

Pre-registered tests, scored honestly.

1. **daiin / dain / chol / chor stay common on a herbal page, therefore are not the plant name.** **Survived** for daiin (8), dain (3), chol (3). chor is present (1). A token that is 15% of a herbal page and the #1 word on text-only f1r cannot be "the name of the plant on f10v."

2. **ol / or stay common.** **Died on this page, again** (0 and 0). Two short herbal-A pages in a row (f9v, f10v) lack them. Wounded, not buried: n=53 and n=84. Re-test on a longer herbal-A running-text page (f13r / f15r / f16r) before calling the class herbal-absent.

3. **ok-/ot- is label-legal; qo- may appear in running text, not on labels.** **Survived on both halves.** f10v running text is qo-heavy (20.8%) and ok/ot-poor (1.9%). f89v2 labels are qo-free (0/17) and ok/ot-raised (23.5%). f89v2 running text is ordinary P (qo- 9.5%, ok+ot 10.1%). This is the test f9v could not run.

4. **Unique rare tokens are the only plant-name candidates.** **Survived as a filter, failed as a positive.** Nine P<5 types; five corpus hapaxes. **None** recur as pharma `Lf`/`Lc`/`Lp`. No f10v token is upgraded to a plant-name hypothesis.

5. **Claimed lookalike shares a rare token.** **Died.** Lookalike is real as a *published visual note*. It is not a lexical hit.

6. **Do not import the f9v viola ID. Do not identify f10v as hellebore.** **Held.**

7. **Colour letters stay out of the EVA gloss.** **Held** (none on these pages).

---

## 6. Hypothesis gloss table

**Every row is a HYPOTHESIS.** Confidence is structural (distribution + position), never semantic. "Gloss" means *role in English*, not a claimed Voynichese meaning. No row identifies the language. No row identifies the plant.

### 6.1 High-frequency function-word candidates (re-tested on f10v)

| EVA | Role (HYPOTHESIS) | Constrained gloss (HYPOTHESIS) | Why this pass still allows it | Why it may be wrong |
|---|---|---|---|---|
| **daiin** | closed-class / function | "and" / weak demonstrative / clause-joiner | 8x on f10v (15%), 7x on f9v, 7x on f1r, 834 in P, 7 in L. Mid-line. Cannot be the name of the plant on this page. | Null / default emit / loose minim-count for `dain` (also 3x here). |
| **dain** | same class as daiin | same, or a shorter/inflected twin | 3x on f10v; 207 in P. Stronger than f9v's single token. | May be a space/minim error. |
| **chol** | generic herbal-section token, **not** a plant name | "the plant / the herb / this preparation" **or** a second function word | 3x IT / 2x ZL on a page with a claimed pharma twin. 7x on text-only f1r. 384 in P, 2 in L. | If it is "herb," it is odd that it is equally at home on f1r. Generator ch-word remains simpler. |
| **chor** | same paradigm as chol | variant of chol | 1x on f10v; 3x on f9v; 217 in P. One stray `Lf` on f99v.28 (`chor.olekor`) does not make it a species name. | Weak on this page. Free variation under a generator. |
| **qoty / qokol / qotchy / qotor** | prose-legal `qo-` family | **not** names; ordinary A-language vocabulary | Dominant openings on f10v; all common in P (85 / 102 / 63 / 28); **0** as labels in this file. | If a later space-model splits them into rare stems that then match labels, revisit. Currently the opposite. |
| **ol / or** | short function (from pass 1) | "and/or / of" | Still #2 / #7 in the P-corpus. Present on f89v2 P (`ol` 1, `or` 1). | **Absent on f10v and f9v.** Do not lean on them for short herbal-A pages. |
| **paiin / qotchytor** | paragraph-initial words | section-open habit (`paiin`); P2 happens to open with a `qo-` hapax | `paiin` is P=8, gallows-`p` start. `qotchytor` is a corpus hapax but wears the prose-legal prefix. | Hapax paragraph-starters are unfalsifiable as "titles." |

**Explicitly refused glosses (this pass):**

- EVA letters as Latin phonemes.
- `chol` / `daiin` / `chor` / `okam` as hellebore, hellebora orientalis, viola, herba trinitatis, or any other plant name.
- Any mapping of a rare f10v token onto a medieval plant name. No substitution was introduced.
- Any named language (Latin, German, Nahuatl, Hebrew, Occitan, Welsh, proto-Romance, etc.).
- Importing the f9v viola literature ID onto f10v or f89v2.
- Treating the voynich.nu "some similarity" note as a species identification or as a textual twin.

### 6.2 Rare tokens and f89v2 labels - candidates, still unproven

| EVA | Where | Role (HYPOTHESIS) | Constrained gloss (HYPOTHESIS) | Why | Falsifier already in view |
|---|---|---|---|---|---|
| **chckhan, chcthor, olty, qokchyky, qotchytor** | f10v only (P=1) | the only tokens that *could* be a page-specific name | **no gloss.** Candidate list, not a reading. | Hapax in the whole P-corpus; not ch/d function words. `qotchytor` / `qokchyky` wear `qo-` (prose-legal). | Any one of them turning up as a high-frequency prose word under a better space-model, or sitting on a visually unrelated page as `Lf`/`Lc`/`Lp`. |
| **otydy** | f10v.1 P; f51r.8 P; f68r1 `@Ls` | not a herbal name | no plant gloss | The only L-hit in the rare set is a star label. | If `@Ls` is later reclassified as a plant-fragment label on a matching drawing, upgrade it. Currently the opposite. |
| **okam** | f89v2.2 `@Lf` (likely fragment #50); P=23; 2x `&Lz` | generic `ok-` stem / type-word, **not** a unique species | "item / this one" in the label-legal prefix class | Too frequent in running text and already used on zodiac labels. Absent from f10v. | If `okam` labelled only visually identical plants and never appeared in unrelated prose, upgrade it. Observed: the opposite. |
| **choeesy, darcheos, chokaro, dydariin, opcheedoy, opaloiiry, rady, dareky** | f89v2 labels only (P=0) | the only f89v2 tokens that *could* be unique names | **no gloss.** Not matched to f10v. | Hapax labels. Several disagree in ZL. | An independent transliteration merging one of them into a common word, or a match to an f10v rare token this parse missed. |
| **sheol / chody** | f89v2 label **and** f89v2 P; huge in corpus | generic, not a species | no plant-name gloss | P=106 / 90. Same-page L+P overlap. | - |
| **keerodal / otaim** | f41v / f65r `@Lp` | whole-plant label (rare) | still the only herbal `Lp` name *candidates* | Unchanged. Not on these pages. | One / two tokens. |
| **otoldy ~ toldy** | not on f10v / f89v2 | type-word leftover | same family as pass 1-2 | Unused this pass. Lives on f99r / f89r1 / f89r2 / f99v. | See pass 2 S6.5. |

**Strongest claim this pass will defend:**  
On a herbal page with a *published* pharma lookalike, the workhorses are still **daiin / dain / chol**. They are function-like, not the plant's name. The name, if the text has one, is hiding in the rare layer - and that layer does **not** reappear on f89v2 `Lf`/`Lc` labels, including the likely fragment-50 word `okam`. The lookalike is visual only. The function-word / label-prefix split survived contact with a real label page (`qo-` = 0 on f89v2 L). f10v therefore does **not** give a plant-name token worth writing in ink.

---

## 7. What would falsify this pass

1. **Function-word claim for daiin / dain / chol dies if** a folio whose plant is independently identified uses one of them *only* as a unique caption on that plant and not as a high-frequency token on f1r / f9v / f10v. Observed: the opposite.

2. **"ol/or are herbal-page function words" is now wounded on two pages.** It dies if the next two longer herbal-A running-text pages also lack them at rates far below corpus expectation.

3. **Rare-token-as-name filter dies if** a better space-model merges the hapaxes into common words (ZL already joins `ol,ty` -> `olty`, which remains a hapax), or if `qotchytor` is just a paragraph-initial `qo-` formula.

4. **"no f10v name on f89v2" dies if** an independent transliteration (GC/v101, RF) reads one of the five hapaxes as a known `Lf`/`Lc` on fragment 50, or if fragment 50 is not `okam` and its actual label *is* an f10v rare token. IT and ZL do not show that.

5. **ok-/ot- classifier / qo- suppression dies if** a large agreed label set uses `qo-` at P-like rates, or if f89v2's zero `qo-` is an artefact of a bad space-model that should have split `qofoiin` etc. onto labels. They are in P loci, not L.

6. **Visual-lookalike-without-shared-name** is the result, not a hypothesis to kill. It would be *softened* if a stronger "same plant" pair (Zandbergen: fragment 54 "appears to be the same plant as on f48v"; fragment 61 "appears to be the same plant as on f48r") shares a rare token.

7. **Constrained semi-language stance dies** on the same terms as pass 1 S6.5: a pre-registered simple substitution into a known language that yields grammatical running text **and** matching names on the rare / `Lp` words. Not observed.

---

## 8. Next folio to try

**Primary next experiment: f99r (pharmaceutical, `$I=P`) - the type-word + leftover `okary`/`oky` page.**

Why f99r, not another twin:

- This pass **consumed** the f10v / f89v2 name-test twin. It was a miss.
- This pass **also consumed** the `qo-` label-suppression test (survived on f89v2). That half of the old f99r backup is done.
- The unused leftover is the **toldy ~ otoldy** type-word family from passes 1-2. `otoldy` is an `Lf` on **f99r.14**, plus f89r1 / f89r2 / f99v. f99r also repeats `okary` / `oky` (pass 1's only same-page label repeat). That is the experiment this pair did not run.
- f99r is **not** consumed as a folio. Mentioning it as next is therefore allowed.

**Protocol (pre-registered for pass 4):**

1. Transcribe f99r from IT **and** ZL. List every `Lf`/`Lc` and the P-text.
2. Ask whether `otoldy` / `toldy` / `ytoldy` / `tsholdy` (f99r.32 `@Lc`) behave as one lemma across IT and ZL, and whether the four `otoldy` drawings share any visual class. Do not identify the plants.
3. Reconfirm `ok-`/`ot-` vs `qo-` on this page's L vs P (expected: same as f89v2).
4. Treat `okary` / `oky` as type-words unless they fail the P-frequency filter.
5. Do **not** identify any plant as a species. Do **not** import viola or hellebore.

**Optional later name-test, not the next folio:** f48v, because voynich.nu says fragment 54 on f89v2 "appears to be the same plant as on f48v" - a stronger wording than f10v's "some similarity." Use that only if the next pass should be another twin rather than the type-word leftover. Other backups: f2v, f65r, f48r (fragment 61).

---

## 9. Bottom line for this pass

f10v is readable as *structure*: two short paragraphs, no labels, a closed class that refuses to become a plant name (`daiin` 8, `dain` 3, `chol` 3), and a `qo-`-heavy running-text profile. f89v2 is readable as *the other half of the split*: flat labels, zero `qo-`, raised `ok-`/`ot-`, ordinary `qo-` in the paragraphs. Neither page is readable as *language*. Neither plant is identified.

The pass-1 split survives a claimed lookalike: **high-frequency ch/d-words are generic; unique rare tokens are the only name candidates; those candidates do not recur as pharma labels in IT, including on the public f10v ~ fragment #50 pair.** The lookalike is sourced and visual. The lexical twin is a miss. `okam` is a common `ok-` stem, not a name.

Until a rare herbal token is found on a matching fragment under two transliterations, this file is still a lab notebook, not a crib.

---

## Appendix A - raw IT loci for f10v (as in the file)

```
<f10v>     <! $Q=B $P=D $F=b $B=2 $I=H $L=A $H=1 $C=1>
<f10v.1,@P0>      <%>paiin.daiin.sheo.pcheey.qoty.daiin.cthor.otydy.sain
<f10v.2,+P0>      dain.daiin.ckhy.chcthor.choiin.qot.chodaiin.cthy.daiin
<f10v.3,+P0>      dsho.ytey.kchol.olty.chol.dy<$>
<f10v.4,+P0>      <%>qotchytor.shoiin.daiin.qotchey.shcthey.ytor.dain
<f10v.5,+P0>      sho.ykeey.daiin.qotchy.qotor.chol.daiin.qokchyky
<f10v.6,+P0>      shoiin.chor.shcthy.qoty.qotoiin.qokol.choraiin
<f10v.7,+P0>      qokol.chyky.chol.cheky.daiin.dain.chckhan<$>
```

Source: https://voynich.nu/data/IT2a-n.txt

## Appendix B - raw ZL loci for f10v (control)

```
<f10v>     <! $Q=B $P=D $F=b $B=2 $I=H $L=A $H=1 $C=1>
# page 20
# herbal
# Currier's language A, hand 1
# Plant ID: Hellebore? orientalis
#
<f10v.1,@P0>      <%>paiin,daiin.sheo.pcheey.qoty.daiin.cthor.otydy.sain
<f10v.2,+P0>      dain.daiin.ckhy.chcthor.choiin.qot.chodaiin.cthy.daiin
<f10v.3,+P0>      dsho.ytey.kchol.ol,ty.chol.dy<$>
#
<f10v.4,+P0>      <%>qotchytor.shoiin.daiin.qotchey.sh{cthh}y.ytor.dain
<f10v.5,+P0>      sho,ykeey.daiin.qotchy.qotor.chol.daiin.qokchy,ky
<f10v.6,+P0>      shoiin.chor.shcthy.qoty.qotoiin.qokol.chor,aiin
<f10v.7,+P0>      qokol.chy,ky.chol,cheky.daiin.dain.chckhan<$>
```

ZL's "Plant ID" comment is a catalogue note, **not** a finding of this pass.

## Appendix C - raw IT loci for f89v2 (as in the file)

```
<f89v2>    <! $Q=O $P=I $F=y $B=2 $I=P $L=A $H=1>
<f89v2.1,@Lc>     choeesy
<f89v2.2,@Lf>     okam
<f89v2.3,@Lf>     darcheos
<f89v2.4,@Lf>     chokaro
<f89v2.5,@Lf>     sheol
<f89v2.6,@Lf>     chokam
<f89v2.7,@P0>     <%>kosar.sheol.s.aiin.koiin.chtodaiin.pdan.choto.qofoiin.dy.qopdol.doiir.ofaiin.ol.cfheol.dam
<f89v2.8,+P0>     daiin.ykodair.okor.chear<->oteee.eeckhy.s.aiin.ckhey.otaiin.okar.dain.okol.al.chor.dar
<f89v2.9,+P0>     yched.okeey.qoeol.daiin<->chor.chor.cheos.qol.eeeey.dal.chody.cheor.chey.qoaiin.chody
<f89v2.10,+P0>    dair.or.cheol.chom<->qol.cheo.lcheo.lor.cheo.daiin.chkam<$>
<f89v2.11,@Lc>    okory
<f89v2.12,@Lf>    otair.chody
<f89v2.13,@Lf>    dydariin
<f89v2.14,@Lf>    opcheedoy
<f89v2.15,@P0>    <%>sor.oairar.sheety<->chod.s.kory.ochar.eair.sheotain.ytodaiin
<f89v2.16,+P0>    octhos.okaiir.okeos<->dar.s.?ain.ykeody.dar.okal.dal.doral.dar.am
<f89v2.17,+P0>    y?eo.qokeeol.chey.sair<->dam.??yfor.opodaiin.dam.sary.qodam.yteos.aiin
<f89v2.18,+P0>    qokor.chor.cthy.daiin<->chos.?eey.dar.aiin.choeees.okar.chcthy.darams<$>
<f89v2.19,+P0>    <%>toar.qokeeody.doefshey<->dairy.sheos.psheoepoain.dain.qekor.ykeor.otol.sheey.daldaiin
<f89v2.20,+P0>    dol.dair.chey.okaiin.shy<->daiir.odor.sheos.aiin.daikeody.qokorar.sheody.qoko.ltcheody.otal
<f89v2.21,+P0>    dar.qockhy.qokal.okeoy<->cho???.daiin.odaiin.ykeoda.okols.sheey.keeody.daiin.qokos.okeom
<f89v2.22,+P0>    ockhody.daiin.ykam.s<->chty.chy.cthey.dairair.chool.loy.dair.cheodaiin<$>
<f89v2.23,@Lc>    opaloiiry
<f89v2.24,@Lf>    otaram
<f89v2.25,@Lf>    chtody
<f89v2.26,!Lf>    ?ds??o
<f89v2.27,@Lf>    rady
<f89v2.28,@Lf>    dareky
```

Source: https://voynich.nu/data/IT2a-n.txt

## Appendix D - raw ZL label loci for f89v2 (control)

```
<f89v2.1,@Lc>     choeesy
<f89v2.2,@Lf>     okam
<f89v2.3,@Lf>     darcheor
<f89v2.4,@Lf>     chokaro
<f89v2.5,@Lf>     sheol
<f89v2.6,@Lf>     chokam
<f89v2.11,@Lc>    otory
<f89v2.12,@Lf>    otair.chody
<f89v2.13,@Lf>    dykaran
<f89v2.14,@Lf>    opcheedey
<f89v2.23,@Lc>    <!58a>opaloiiry
<f89v2.24,@Lf>    <!58b>otaram
<f89v2.25,@Lf>    <!59a>chtchy
<f89v2.27,@Lf>    <!60>sada?
<f89v2.28,@Lf>    <!61>daseky
```

ZL omits IT locus 26 (shine-through). Full ZL P-lines are in `(local stats extract, not published)`.
