# Voynich pass 1 - working notes (not a translation)

**For:** Jon Bailey
**Date:** 14 Aug 2026 (ET)
**Status:** constrained first pass. **No verified full translation of Beinecke MS 408 exists.** Nothing below is a decipherment. Every gloss is marked **HYPOTHESIS**.

This note is a working attempt on a short public EVA sample: folio **f1r** (running text, Currier A) plus a small **pharmaceutical-label** set (f88r, f99r) where the same stems actually repeat. It is not a Wikipedia recap and it does not claim the manuscript has been read.

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
| Browser using a closely related Takahashi set (VT) | https://www.voynichese.com/ |
| Label-behaviour background | Rene Zandbergen, "Some special properties of labels in the Voynich MS", https://voynich.nu/extra/labels.html (update 2025-08-23) |
| Manuscript | Yale, Beinecke Rare Book & Manuscript Library, MS 408 |

Takahashi's 1998-99 EVA is the first essentially complete single-handed transliteration. Word spaces in the VMS are often ambiguous; Takahashi himself noted that he sometimes joined or split tokens differently from FSG/Currier. Uncertain glyphs are marked `?` in the file. This pass treats `.` as a word break and ignores IVTFF markup (`<%>`, `<$>`, `<->`, locus tags).

A later Zandbergen-Landini file (`ZL3b-n.txt`) exists at the same directory. It was **not** used as the running text here, so counts can be re-run against ZL later as a control.

**What this is not:** a download of any copyrighted monograph, a Cheshire/Gibbs-style "complete solution," or a claim that EVA letters are phonemes.

---

## 2. Folio text used

### 2.1 Why f1r + two pharma pages

- **f1r** is the opening page: text-only (`$I=T`), Currier language A (`$L=A`), hand 1. Four short paragraphs. No plant drawing, so it is a clean running-text sample, not a label page.
- **f2r / f2v** (herbal A) were used only as a check that the same high-frequency tokens appear next to a plant.
- **f88r and f99r** (pharmaceutical, `$I=P`) supply the actual **repeating plant-fragment and container labels**. Whole-plant labels in the herbal section are rare (Takahashi marks `Lp` on f41v `keerodal` and f65r `otaim.dam.alam` only).

Page header from IT2a-n:

```
<f1r>  <! $Q=A $P=A $F=a $B=1 $I=T $L=A $H=1 $C=1 $X=V>
```

### 2.2 f1r in EVA (Takahashi / IT, cleaned)

Four paragraphs. Line IDs are Takahashi loci. `?` = uncertain reading.

**P1**
```
f1r.1   fachys ykal ar ataiin shol shory cthres y kor sholdy
f1r.2   sory ckhar or y kair chtaiin shar are cthar cthar dan
f1r.3   syaiir sheky or ykaiin shod cthoary cthes daraiin sa
f1r.4   ooiin oteey oteos roloty cth?ar daiin otaiin or okan
f1r.5   dair y chear cthaiin cphar cfhaiin
f1r.6   ydaraishy
```

**P2**
```
f1r.7    ? odar o y shol cphoy oydar sh s cfhoaiin shodary
f1r.8    yshey shody okchoy otchol chocthy oschy dain chor kos
f1r.9    daiin shos cfhol shody
f1r.10   dain os teody
```

**P3**
```
f1r.11   ? ydain cphesaiin ol s cphey ytain shoshy cphodales
f1r.12   oksho kshoy otairin oteol okan shodain sckhey daiin
f1r.13   shoy ckhey kodaiin cphy cphodaiils cthey she oldain d
f1r.14   dain oiin chol odaiin chodain chdy okain dan cthy kod
f1r.15   daiin shckhey ckeor chor shey kol chol chol kor chal
f1r.16   sho chol shodan kshy kchy dor chodaiin sho kchom
f1r.17   ycho tchey chokain sheo pshol dydyd cthy daicthy
f1r.18   yto shol she kodshey cphealy dasain dain ckhyds
f1r.19   dchar shcthaiin okaiir chey rchy potol cthols dlocta
f1r.20   shok chor chey dain ckhey
f1r.21   otol daiiin
```

**P4**
```
f1r.22   cpho shaiin shokcheey chol tshodeesy shey pydeey chy ro d?
f1r.23   ?doin chol dain cthal dar shear kaiin dar shey cthar
f1r.24   cho?o kaiin shoaiin okol daiin far cthol daiin ctholdar
f1r.25   ycheey okay oky daiin okchey kokaiin ??chol k??chy dal
f1r.26   d?eeo shody koshey cthy okchey keey keey dal chtor
f1r.27   ?eo chol chok choty chotey
f1r.28   dchaiin
```

Paragraph-final singleton / short lines: `ydaraishy` | `dain os teody` | `otol daiiin` | `dchaiin`.

### 2.3 Repeating pharmaceutical labels used for the plant-label gloss

From the same IT file (locus type `Lc` = container, `Lf` = plant fragment):

| Folio | Locus | Type | EVA |
|---|---|---|---|
| f88r.6 | Lf | otaly |
| f88r.12 | Lc | otaldy |
| f88r.15 | Lf | okol |
| f99r.2 | Lf | okary |
| f99r.4 | Lf | oky |
| f99r.11 | Lf | okary |
| f99r.14 | Lf | otoldy |
| f99r.24 | Lf | oky |
| f89r1.4 | Lf | otoldy |
| f89r2.9 | Lc | otoldy |
| f99v.2 | Lf | otoldy |
| f99v.6 | Lf | otaly |
| f101v.2 | Lf | otaldy |
| f101v.3 | Lf | otal |

Across the pharma bifolios in IT, the most-repeated full labels are **otoldy (4), otoky / otaly / otaldy / okol / otory / okary / oky / otal (2 each)**. That is the only "repeated plant-label" set this pass is willing to gloss.

Rare herbal whole-plant labels in the same file: **f41v** `keerodal`; **f65r** `otaim dam alam`.

---

## 3. Stats (computed on IT2a-n, this pass)

Method: strip IVTFF tags; split on `.` and whitespace; keep tokens that contain at least one A-Z letter. Uncertain `?` kept inside the token. Paragraph text = loci whose flags contain `P`. Labels = flags containing `L`.

### 3.1 f1r running text

| Measure | Value |
|---|---|
| Word tokens | 210 |
| Word types | 163 |
| Type/token ratio | 0.776 |
| Hapax types | 139 (66% of tokens) |
| Mean / median word length | 4.74 / 5 EVA letters |
| Paragraphs | 4 |
| Lines (loci) | 28 |
| EVA `q` anywhere on the page | **0** |

**Top tokens on f1r**

| Rank | EVA | n | Notes |
|---|---|---|---|
| 1-2 | daiin, chol | 7 each | also the two biggest herbal-A workhorses |
| 3 | dain | 6 | same family as daiin (one fewer minim) |
| 4 | y | 4 | also line-initial-heavy |
| 5-11 | shol, or, cthar, shody, chor, cthy, shey | 3 each | ch/sh + ol/or/ey paradigm |
| 12+ | kor, dan, okan, s, ckhey, she, sho, chey, dar, kaiin, okchey, dal, keey | 2 each | |

**Word-final letters on f1r:** y 63, n 50, r 32, l 26, s 13, o 12. Almost no word ends in a gallows (`k/t/p/f`).

**Word-initial letters on f1r:** c 59, s 39, d 32, o 31, k 19, y 13.

**Word-initial bigrams on f1r:** sh 33, ch 26, da 24, ct 16, ok 11, ko 9, cp 9, ot 7.

**Line-initial first letter (28 lines):** d 8, y 6, s 5, o 4, c 2, ? 2, f 1. Opening word of the page is the hapax **fachys** (gallows `f` is a known paragraph-start preference).

**daiin-family on f1r (selected):** daiin 7, dain 6, plus many one-offs built the same way (`ataiin, chtaiin, ykaiin, otaiin, cthaiin, kodaiin, odaiin, chodain, okain, ...`). This is morphology or a generation rule, not a list of unrelated stems.

### 3.2 Herbal check (f2r + f2v, same file)

| Page | Tokens | Types | Top tokens |
|---|---|---|---|
| f2r | 78 | 69 | chy 3, saiin 3, daiin 2, cthy 2, dan 2, shol 2, sheey 2 |
| f2v | 55 | 44 | **chol 5, daiin 4, chor 3** |

So the f1r high-frequency set is not page-specific: **chol / chor / daiin** are also the workhorses on the first herbal plant pages. They are therefore poor candidates for *the name of the plant drawn on that page*.

### 3.3 Corpus context (IT paragraph text vs labels)

Paragraph text in this file: **33,707 tokens / 7,526 types**.

Top paragraph tokens: daiin 776, ol 509, chedy 485, shedy 415, aiin 412, chol 368, or 332, chey 326, qokeey 304, qokeedy 301, ar 283, qokain 277, shey 266, qokedy 265, qokaiin 262, dar 261, dal 213, al 206, chor 203, okaiin 200.

Label tokens in this file: **1,032 / 763 types**. Top *content-sized* labels lean `ot-`/`ok-`: otal 10, okar 6, okal 6, otol 6, oky 6, otaly 6, okaly 5, okaiin 5.

| Test | Paragraph text | Labels |
|---|---|---|
| Words starting `ok` or `ot` | 11.3% | **33.1%** |
| Words starting `qo` | 15.3% | **0.9%** (9 tokens) |
| daiin as a label | 776 in P | 7 in L (rare; Zandbergen's narrower "zodiac/pharma label" cut is even stricter) |
| chedy / qokeey / qokeedy / qokain / qokedy / shey as labels | hundreds in P | ~0 |

This matches Zandbergen's published label result: labels are a **different vocabulary** with a flatter frequency curve, not a random subsample of running text.

Pharma-label repeats in IT (232 labels, f87-f102): most frequent type **otoldy x4**; already the 10th type is a hapax. That is too flat for "the same function words reused as captions."

### 3.4 Rank-frequency on f1r (small-n, so weak)

`rank x freq` on the top 11 is 7, 14, 18, 16, 15, 18, 21, 24, 27, 30, 33 - rising, not Zipf-flat. On 210 tokens that is expected and **does not** decide language vs hoax. The useful signal is the **closed morphological families**, not the Zipf slope.

---

## 4. Language hypotheses (natural vs generated vs cipher)

Three live families. This pass does **not** pick a winner. It ranks them by how badly f1r + labels punish each one.

### H1 - Natural language (unknown, or known but heavily disguised)

**For:** paragraph structure; a small closed class that *looks* like function words; labels that look like a noun/name inventory; Currier A vs B is a real register or dialect split; Zandbergen's point that a flat, `ok`/`ot`-heavy label lexicon is the sort of thing a meaningful caption system would produce.

**Against, on this sample:**
- Rigid glyph-position rules (no `q` at all on f1r; `q` almost only word-initial in the corpus; `y` prefers word-final; gallows prefer word-initial / paragraph-initial).
- Extremely low entropy *inside* the word: `ch/sh + e* + y/ol/or/ey` and `d/ok/ot + aiin/ain` generate most of the page.
- Line-as-a-unit effects (line-initial `d/y/s`, paragraph-initial gallows `f/p`) are stronger than in ordinary running prose.
- If this were lightly-enciphered Latin/Italian/German/Dutch, the function-word set should map onto *et / de / la / und / van* **and** those words should be allowed as labels. They are not.

**Verdict on f1r:** possible only if the language is either unknown **or** so morphologically constrained (or so verbose-enciphered) that it no longer behaves like a typical European herbal.

### H2 - Generated / self-citing / grille text (Timm-style autocopy, Rugg-style Cardan)

**For:** neighbouring words are often one edit apart (`chol chol`, `keey keey`, `daiin` / `dain` / `odaiin` / `chodain` on the same lines); line-start preferences look like a writing habit more than syntax; A vs B could be two generation settings.

**Against:** labels are *not* the same generator output as the paragraphs. Anyone proposing meaninglessness now owes a **second rule** that (a) suppresses `qo` and `daiin`/`chedy`/`chol` on labels and (b) flattens the label frequency curve. Zandbergen is right that Rugg/Timm as usually stated do not automatically give that.

**Verdict:** still viable for running text; incomplete until it explains labels.

### H3 - Cipher of a known language (simple substitution, or simple homophonic)

**Against, strongly:** EVA is already a 1-to-1 shape mapping. If the underlying plaintext were ordinary Latin/Italian, decades of frequency attacks would have produced a stable word list. They have not. Verbose cipher / steganography / null-heavy systems remain possible but are unfalsified and currently unconstrained.

**Verdict:** simple substitution of a known European language is a **failed** hypothesis. A verbose or null-rich cipher is not tested by this pass.

### Working stance for the gloss

Treat the text as **a constrained semi-language**: it has function-word-like tokens and a separate label lexicon. Do **not** assign phonetic values to EVA letters. Do **not** identify the language. Gloss only (a) high-frequency closed-class candidates and (b) repeated label stems, and only as structural roles.

---

## 5. Hypothesis gloss table

**Every row is a HYPOTHESIS.** Confidence is structural (distribution + position), never semantic. "Gloss" means *role in English*, not a claimed Voynichese meaning.

### 5.1 High-frequency function-word candidates (from f1r, checked on f2r/f2v and the IT corpus)

| EVA | Role (HYPOTHESIS) | Constrained gloss (HYPOTHESIS) | Why this pass allows it | Why it may be wrong |
|---|---|---|---|---|
| **daiin** | closed-class / function | "and" / weak demonstrative / clause-joiner | Highest corpus word (776). 7x on f1r, mid-line, pairs with `chol`/`shos`/`okchey`. Almost never a plant label. Same slot as `dain`. | Could be a null, a line-filler, or a generated "default word." Minim-count (`daiin` vs `dain` vs `aiin`) may be one word written loosely. |
| **dain** | same class as daiin | same as daiin, or a shorter/inflected twin | 6x on f1r; appears in paragraph-final `dain os teody`. | May be a space/minim error for daiin (Takahashi vs Grove debates this). |
| **chol** | generic herbal-section token, **not** a plant name | "the plant / the herb / this preparation" **or** a second function word | 7x on f1r (no plant drawn); 5x on f2v (plant drawn). Corpus 368. Repeats as `chol chol` (f1r.15). Almost unused as a label. | If it is "herb," it is odd on a text-only page. If it is "and/the," it collides with daiin. Could be a generated ch-word. |
| **chor** | same paradigm as chol | variant of chol (inflection, agreement, or free variation) | 3x on f1r; 3x on f2v. `chol/chor/chey/shey` is a real family. | Free variation under a generator is the simpler account. |
| **chey / shey** | same ch/sh family | weak adverb / "then" / generic predicate | 2 / 3 on f1r; huge in Language B (`chedy`/`shedy`). | A/B shift (`chol` vs `chedy`) may be a generation setting, not grammar. |
| **shol / shody** | content-ish, still generic | "leaf / decoction / item" **or** another formula word | 3 / 3 on f1r; `shol` is corpus-frequent (168). Not used as a repeating pharma label. | No bilingual cue. Could just be the sh- counterpart of chol. |
| **or / ol** | short function | "and/or / of" (preposition or conjunction) | `or` 3x on f1r, 332 in corpus; `ol` 1x on f1r (f1r.11), 509 in corpus - the #2 word in the book. Too short and too common for content. | Classic null / padding candidates. `ol` is almost absent from labels (1). |
| **y** (standalone) | line / clause particle | "and then" / initial particle / null | 4x on f1r; `y` is also the commonest *word-final* letter. Line-initial `y-` is a known VMS habit. | Very likely a writing habit, not a word. |
| **s** (standalone) | abbreviation or particle | (no gloss - keep as unknown short) | 2x on f1r; 175 in corpus. | Too underspecified. |
| **fachys** | paragraph-initial hapax | section-open / rubric-like word, **not** a plant name | Unique in paragraph text; gallows-`f` start matches the known paragraph-initial gallows rule. | One token. Unfalsifiable as a "title." |

**Explicitly refused glosses (this pass):**
- EVA letters as Latin phonemes (`daiin` != "doin/thain/quin").
- `chol` as a specific Linnaean / medieval plant name.
- Any mapping onto a named language (Latin, Nahuatl, Hebrew, Occitan, Welsh, proto-Romance, etc.). Those have been claimed in public and none is verified.

### 5.2 Repeated plant-label words (pharma `Lf`/`Lc`, plus the two herbal `Lp`)

| EVA | Where | Role (HYPOTHESIS) | Constrained gloss (HYPOTHESIS) | Why | Falsifier already in view |
|---|---|---|---|---|---|
| **ok- / ot-** (prefix) | 33% of all labels vs 11% of P-text; 32-52% in Zandbergen's zodiac/pharma cuts | classifier / construction prefix on names | "item/root/herb-of ___" or a determiner that is *label-legal* | Stable across zodiac **and** pharma labels; `qo-` is almost banned in the same slot. | If a large set of securely identified plants take labels *without* ok/ot and *with* qo-/daiin-/chol-, the classifier story dies. |
| **otoldy** | f89r1, f89r2, f99r, f99v (4x) | repeated label stem | a **type** of plant-part or container-class, not a unique species name | Most-repeated pharma label. Also 5x in running text - so it is lexical, not a drawing-only code. | If the four labelled drawings are visually unrelated *and* the word sits in running text in non-plant sections, "plant-part type" weakens. |
| **otaldy / otaly / otal** | f88r, f99v, f101v | same family as otoldy | inflection or loose spelling of one lemma **otal~** | The four strings share `ot-al-(dy/y)`. | If ZL/GC split them as different loci/readings, family collapses to transcription artefact. |
| **okary** | f99r.2 and f99r.11 (both `Lf`) | plant-fragment name or local epithet | "this fragment / this herb" on **one page**, reused | Only a two-token repeat, same folio. | Need the two fragments to be the same organ/species or the gloss is just "scribe reused a word." |
| **oky** | f99r.4, f99r.24; 78x in P-text | short label, probably **not** a unique species | classifier-only or generic "item" | Too frequent in running text (78) to be a rare plant. | If `oky` labels a unique, identifiable species and never appears in unrelated prose, upgrade it. Currently the opposite. |
| **okol** | f88r.15, also f101v; 65x in P | same problem as oky | generic, not a species name | Common in prose. | Same as oky. |
| **keerodal** | f41v `Lp` | whole-plant label (rare) | **candidate plant name** (HYPOTHESIS only) | Hapax; sitting on a herbal page as `Lp`. 0x in paragraph text. | One token. Worth tracking if the same plant recurs in the pharma section. |
| **otaim dam alam** | f65r `Lp` | three-word whole-plant label | name or short caption; `dam` is common in P (84), `alam` less so (7), `otaim` is almost unique (1 in P) | The only multi-word herbal plant label in IT. | `dam` being common makes a pure "three-name title" unlikely; maybe `otaim` is the name and `dam alam` is formula. |

**Strongest label claim this pass will defend:**  
`ok-`/`ot-` is a **label-legal prefix** (classifier or determiner). The repeating `otal~ / otoldy` family is a **type-word**, not a unique species. Unique `Lp` hapaxes (`keerodal`, maybe `otaim`) are the only tokens that even *could* be plant names, and they are unproven.

---

## 6. What would falsify this pass

A hypothesis that cannot die is not a working hypothesis. These are the kill-switches.

1. **Function-word claim for daiin / ol / or dies if** a large, agreed label set (zodiac + pharma, ZL and IT agreeing) uses them at rates close to paragraph text. Current data: they are suppressed on labels. If a better space-model (Grove-style half-spaces) moves hundreds of `daiin`s onto labels, the closed-class story is an artefact.

2. **"chol is not a plant name" dies if** a folio whose plant is independently identified (the usual cautious candidates: f9v ~ viola/pansy, f1v ~ solanaceous) has `chol` *only* as a unique caption on that plant and not as a high-frequency token on text-only f1r. Observed: the opposite (7x on f1r, 5x on f2v).

3. **ok-/ot- classifier dies if** securely identified labels (stars in one constellation, or matching herbal/pharma twins) systematically lack the prefix, or if `qo-` labels become common once uncertain spaces are resolved.

4. **"otal~ is one lemma" dies if** independent transliterations (ZL, GC/v101, RF) read those four strings as unrelated, or if the four drawings share no visual class (root vs leaf vs jar).

5. **Constrained semi-language stance dies if** a simple substitution into a known language is shown to yield grammatical running text **and** matching plant names on the `Lp`/`Lf` words, under a pre-registered mapping. Public claims of this kind to date have not survived that test.

6. **Generation-with-a-label-rule (H2 completed) would not kill the gloss table** - it would re-read "function word" as "high-frequency emit" and "classifier" as "label-mode emit." The *roles* could survive as engineering descriptions. What it would kill is any temptation to pronounce the English glosses.

---

## 7. Next folio to try

**Primary next experiment: f9v (herbal A), then its lookalikes in the pharma section.**

Why f9v, not another text-only page:

- It is a well-known herbal folio; several pre-1960 identifications converge on *Viola* / herba trinitatis (O'Neill, ELV). That ID is **not** treated as fact here, but it is the least-bad plant ID in the book and therefore the best place to *test* names.
- Takahashi text is short and already in IT2a-n (12 lines, `daiin` still common - a predicted result if daiin is function-like).
- Colour annotations under the paint (`por` / `p` / `r`, and a `g`) are a separate Latin-letter layer and must be kept out of the EVA gloss.

**Protocol for pass 2 (pre-registered):**

1. Transcribe f9v from IT **and** ZL; list tokens that are hapax on f9v or rarer than 5 in the whole P-corpus. Those are the only plant-name *candidates*.
2. Search pharma `Lf` labels for those rare tokens (and for `keerodal`, `otaim`). A hit on a visually similar fragment is a positive for "labels are names." A miss is not fatal (the herbal page may not repeat in quire 15/19).
3. Count `daiin/dain/chol/chor/ol/or` on f9v. Prediction of *this* pass: they stay common. If they vanish, S5.1 is wrong.
4. Count `ok-/ot-` vs `qo-` on f9v running text vs any labels on that page. Prediction: running text may have some `qo-` (f2r already does); labels should not.
5. Do **not** introduce a language ID in pass 2. If a rare f9v token matches a medieval viola name under a *pre-stated* substitution, write it as a test, not a result.

**Secondary backup if f9v is too short:** f2v (already chol-heavy; good negative control) and f65r (the only multi-word `Lp`).

---

## 8. Bottom line for this pass

f1r is readable as *structure*: four paragraphs, a closed class (`daiin/dain`, `chol/chor/chey/shey`, `ol/or`, standalone `y`), a paragraph-initial hapax (`fachys`), and no `q`. It is not readable as *language*. The only translation-like move that survives contact with the labels is: **high-frequency ch/d-words are generic; ok-/ot-stems are the name-like layer; unique `Lp` hapaxes are the only plant-name candidates, and they are unproven.**

If pass 2 on f9v finds a rare EVA token that (a) is not a ch/d function word, (b) reappears on a matching pharma fragment, and (c) is stable across IT and ZL, *that* token becomes the first plant-name hypothesis worth writing in ink. Until then, this file is a lab notebook, not a crib.

---

## Appendix A - raw IT loci for f1r (as in the file)

```
<f1r>      <! $Q=A $P=A $F=a $B=1 $I=T $L=A $H=1 $C=1 $X=V>
<f1r.1,@P0>       <%>fachys.ykal.ar.ataiin.shol.shory.cthres.y.kor.sholdy
<f1r.2,+P0>       sory.ckhar.or.y.kair.chtaiin.shar.are.cthar.cthar.dan
<f1r.3,+P0>       syaiir.sheky.or.ykaiin.shod.cthoary.cthes.daraiin.sa
<f1r.4,+P0>       ooiin.oteey.oteos.roloty.cth?ar.daiin.otaiin.or.okan
<f1r.5,+P0>       dair.y.chear.cthaiin.cphar.cfhaiin
<f1r.6,=Pt>       ydaraishy<$>
<f1r.7,*P0>       <%>?.odar.o.y.shol.cphoy.oydar.sh.s.cfhoaiin.shodary
<f1r.8,+P0>       yshey.shody.okchoy.otchol.chocthy.oschy.dain.chor.kos
<f1r.9,+P0>       daiin.shos.cfhol.shody
<f1r.10,=Pt>      dain.os.teody<$>
<f1r.11,*P0>      <%>?.ydain.cphesaiin.ol.s.cphey.ytain.shoshy.cphodales
<f1r.12,+P0>      oksho.kshoy.otairin.oteol.okan.shodain.sckhey.daiin
<f1r.13,+P0>      shoy.ckhey.kodaiin.cphy.cphodaiils.cthey.she.oldain.d
<f1r.14,+P0>      dain.oiin.chol.odaiin.chodain.chdy.okain.dan.cthy.kod
<f1r.15,+P0>      daiin.shckhey.ckeor.chor.shey.kol.chol.chol.kor.chal
<f1r.16,+P0>      sho.chol.shodan.kshy.kchy.dor.chodaiin.sho.kchom
<f1r.17,+P0>      ycho.tchey.chokain.sheo.pshol.dydyd.cthy.daicthy
<f1r.18,+P0>      yto.shol.she.kodshey.cphealy.dasain.dain.ckhyds
<f1r.19,+P0>      dchar.shcthaiin.okaiir.chey.rchy.potol.cthols.dlocta
<f1r.20,+P0>      shok.chor.chey.dain.ckhey
<f1r.21,=Pt>      otol.daiiin<$>
<f1r.22,*P0>      <%>cpho.shaiin.shokcheey.chol.tshodeesy.shey.pydeey.chy.ro.d?
<f1r.23,+P0>      ?doin.chol.dain.cthal.dar.shear.kaiin.dar.shey.cthar
<f1r.24,+P0>      cho?o.kaiin.shoaiin.okol.daiin.far.cthol.daiin.ctholdar
<f1r.25,+P0>      ycheey.okay.oky.daiin.okchey.kokaiin.??chol.k??chy.dal
<f1r.26,+P0>      d?eeo.shody.koshey.cthy.okchey.keey.keey.dal.chtor
<f1r.27,+P0>      ?eo.chol.chok.choty.chotey
<f1r.28,=Pt>      dchaiin<$>
```

Source: https://voynich.nu/data/IT2a-n.txt
