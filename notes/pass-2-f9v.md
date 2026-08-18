# Voynich pass 2 - f9v working notes (not a translation)

**For:** Jon Bailey
**Date:** 14 Aug 2026 (ET)
**Status:** constrained second pass on one herbal folio. **No verified full translation of Beinecke MS 408 exists.** Nothing below is a decipherment. Every gloss is marked **HYPOTHESIS**. The plant drawn on f9v is **not identified** here.

This note finishes the experiment pre-registered in pass 1 (S7): take a short herbal-A page that the literature treats as a *Viola* / herba trinitatis candidate, and test whether the function-word / label-prefix / rare-name split still holds. The literature ID is a **test case**, not a result. It is never used as a fact.

Sources were already on disk from the first worker. They were not re-downloaded. Stats in `(local stats extract, not published)` were recomputed against the files and **agree**.

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
| Folio description / colour notes | https://www.voynich.nu/q02/index.html (quire 2, f9v) |
| Colour-annotation table | https://voynich.nu/writing.html (rows tagged COL on f9v) |
| Manuscript | Yale, Beinecke Rare Book & Manuscript Library, MS 408 |
| Prior note | `notes/pass-1.md` |

Same parsing rule as pass 1: `.` is a word break; IVTFF markup (`<%>`, `<$>`, `<->`, locus tags, `<!...>`) is stripped; tokens must contain at least one A-Z letter; `?` is kept if present. Paragraph text = loci whose flags contain `P`. Labels = flags containing `L`.

ZL is the **control**, not the running text. ZL uses extra Eva- notation (`,` uncertain space, `[a:b]` alternatives, `{...}` ligature comments). After the first worker's cleanup those produce three space-split disagreements with IT, listed in S2.3. Function-word counts still agree.

**What this is not:** a download of any copyrighted monograph, a Cheshire/Gibbs-style "complete solution," a language identification, or a claim that the plant is *Viola*.

---

## 2. Folio text used

### 2.1 Why f9v

Pass 1 pre-registered this page because:

- It is herbal A, hand 1, short (12 loci), and the high-frequency closed class was predicted to stay common if those tokens are function-like rather than plant names.
- Several pre-1960 identifications converge on *Viola* / herba trinitatis (O'Neill; ELV: viola/pansy; ZL comment: "Viola allright but all upside down"). That ID is **literature only**. This pass uses it as the least-bad named test case, then refuses to promote it.
- Colour annotations in the flowers (`por` / `p` / `r`, and a `g`) are a separate Latin-letter layer and must stay out of the EVA gloss.

Page header from IT2a-n (identical in ZL):

```
<f9v>  <! $Q=B $P=B $F=a $B=1 $I=H $L=A $H=1 $C=1 $X=C>
```

`$I=H` herbal, `$L=A` Currier A, `$H=1` hand 1. Two paragraphs of running text (`<%` at f9v.1 and f9v.5; `<$>` at f9v.4 and f9v.12). The text avoids the drawing.

### 2.2 Labels on this page

**None.** All 12 IT loci are flagged `@P0` / `+P0`. No `Lp`, `Lf`, `Lc`, or any other `L` flag. f9v is running text around a plant, not a caption page. The label-prefix test on *this* folio can only be run on running text.

Whole-plant herbal `Lp` in the same IT file remains exactly the pass-1 pair: **f41v** `keerodal`; **f65r** `otaim.dam.alam`.

### 2.3 f9v in EVA (Takahashi / IT, cleaned)

Line IDs are Takahashi loci. Two paragraphs.

**P1**
```
f9v.1   fochor oporody opy shor daiin qopchypcho qofol shol cfhol daiin
f9v.2   dchor qoaiin chkaiin cthor chol chor cphol dy oty qokaiin dy
f9v.3   ykey chor ykaiin daiin cthy otaiin oky oeees daiin
f9v.4   ytey tchy kaiin cthor otol oty toldy
```

**P2**
```
f9v.5   pchor ypcheey qotor ypchy olcfholy te ar chty daiiin
f9v.6   odol choy ksheody chody dain otchy cthod yky
f9v.7   qochol chol ctchy daiin otal dor daim
f9v.8   soiin daiin qokcho rokyd daly
f9v.9   daiin chy tor chyty dary ytoldy
f9v.10  oty kchol chol chy kyty
f9v.11  ychor chshoty oky kaiin
f9v.12  chkaiin ckhy chor
```

Paragraph-initial words: **fochor** (gallows `f`) and **pchor** (gallows `p`). That matches the known paragraph-start gallows habit from f1r (`fachys`). They are not treated as plant names.

### 2.4 IT vs ZL (control)

Token lists are in `f9v-stats.json`. Small space-split differences only:

| Locus | IT (primary) | ZL (control) |
|---|---|---|
| f9v.4 | `ytey` + `tchy` | `yteytchy` (ZL `ytey,tch,y` joined) |
| f9v.5 | `te` | `to` (ZL `t[o:e]`, first alternative) |
| f9v.6 | `dain` + `yky` | `dain` + `yko` (ZL `da[in:iin]`, `yko`) |
| f9v.7 | `qochol` | `qo` + `chol` (so ZL `chol` = 4, IT `chol` = 3) |
| f9v.11 | `oky` + `kaiin` | `okykaiin` (ZL `oky,kaiin` joined) |

Function-word counts that matter for the hypothesis are stable: **daiin 7 / 7**, **dain 1 / 1**, **chor 3 / 3**. `chol` is 3 (IT) vs 4 (ZL) only because of the `qochol` split. `ol` and `or` are 0 in both.

---

## 3. Stats (verified on IT2a-n / ZL3b-n this pass)

Method: same as pass 1. f9v-stats.json was recomputed; every number below that also appears in the json **matches**. Where this pass adds a number that was not in the json, it is computed from the same files and marked as such.

### 3.1 f9v running text (IT)

| Measure | Value | Source |
|---|---|---|
| Word tokens | **84** | verified (json list length) |
| Word types | **66** | verified (json counts) |
| Type/token ratio | 0.786 | computed |
| Hapax types on the page | 56 (67% of tokens) | computed |
| Mean / median word length | 4.68 / 5 EVA letters | computed |
| Paragraphs | 2 | IT `<%` / `<$>` |
| Lines (loci) | 12 | IT + ZL |
| Labels (`Lp`/`Lf`/`Lc`/any `L`) | **0** | IT flags |
| EVA `q` / word-initial `qo-` | 7 tokens | computed |

**Top tokens on f9v (IT)**

| Rank | EVA | n | Notes |
|---|---|---|---|
| 1 | daiin | 7 | same workhorse as f1r (7) and f2v (4) |
| 2-4 | chol, chor, oty | 3 each | chol/chor also top on f2v; oty is ok/ot-family, common in P (101) |
| 5-10 | chkaiin, cthor, dy, oky, kaiin, chy | 2 each | |
| 11+ | 56 hapax types | 1 each | only the P-corpus-rare ones are name *candidates* |

**Function-word prediction check (the pass-1 table)**

| EVA | f9v IT | f9v ZL | IT paragraph corpus (P) | Prediction | Result |
|---|---|---|---|---|---|
| daiin | 7 | 7 | 834 | stay common | **survived** |
| dain | 1 | 1 | 207 | stay common | present (weak) |
| chol | 3 | 4 | 384 | stay common | **survived** |
| chor | 3 | 3 | 217 | stay common | **survived** |
| ol | 0 | 0 | 521 | stay common | **missed** |
| or | 0 | 0 | 345 | stay common | **missed** |

`ol` / `or` missing on 84 tokens is not a strong kill - a short page can omit even a #2 corpus word - but the prediction as written did not fire. daiin/chol/chor did, and they are the ones that would have been tempting "plant name" readings.

**Word-final letters on f9v:** y 33, n 18, r 14, l 12. Same y/n/r/l preference as f1r. Almost no word ends in a gallows.

**Word-initial letters on f9v:** c 23, d 16, o 14, y 8, q 7, k 5.

**Word-initial bigrams on f9v:** ch 15, da 12, qo 7, ot 7, ct 5, ok 2.

**Line-initial first letter (12 lines):** y 3, d 2, o 2, f 1, p 1, q 1, s 1, c 1. Opening word of the page is the corpus hapax **fochor**.

### 3.2 ok-/ot- vs qo- on f9v running text (computed)

| Prefix | f9v tokens | rate | Tokens | Corpus P rate (this parse) |
|---|---|---|---|---|
| `ok-` | 2 | 2.4% | oky, oky | } |
| `ot-` | 7 | 8.3% | otyx3, otaiin, otol, otchy, otal | } **ok+ot = 9 / 84 = 10.7%** vs corpus P **11.4%** |
| `qo-` | 7 | 8.3% | qopchypcho, qofol, qoaiin, qokaiin, qotor, qochol, qokcho | corpus P **15.1%** |

Prediction from pass 1: running text may have `qo-` (f2r already did); labels should not. **Survived, within the limits of a page that has no labels.** `qo-` is present in the paragraphs. `ok-`/`ot-` sit at the ordinary running-text rate, not the 33% label rate - which is what you want on a page with no `L` loci.

f1r had **zero** `q`. f9v has seven `qo-` words. Herbal A is allowed to use `qo-` in prose. That does not license `qo-` as a label prefix.

### 3.3 Rare / hapax candidates (`cands_p5`)

Rule, pre-registered: tokens on f9v that occur **fewer than 5 times** in the whole IT paragraph corpus. Recomputed set **matches** the json (17 types):

| EVA | f9v | P | L | all | Other IT loci |
|---|---|---|---|---|---|
| chshoty | 1 | 1 | 0 | 1 | - |
| fochor | 1 | 1 | 0 | 1 | - |
| kyty | 1 | 1 | 0 | 1 | - |
| olcfholy | 1 | 1 | 0 | 1 | - |
| oporody | 1 | 1 | 0 | 1 | - |
| qopchypcho | 1 | 1 | 0 | 1 | - |
| rokyd | 1 | 1 | 0 | 1 | - |
| te | 1 | 1 | 0 | 1 | - (ZL reads `to`) |
| ypcheey | 1 | 1 | 0 | 1 | - |
| ctchy | 1 | 2 | 0 | 2 | f42v.10 P |
| odol | 1 | 2 | 0 | 2 | f93r.28 P |
| qochol | 1 | 2 | 0 | 2 | f25v.5 P |
| qofol | 1 | 2 | 0 | 2 | f85r1.20 P |
| toldy | 1 | 2 | 0 | 2 | f43r.11 P |
| ypchy | 1 | 3 | 0 | 4 | f17r.4 P; f52r.1 P; **f68v2.17 `@Ro`** |
| chyty | 1 | 4 | 0 | 4 | f16v.5, f34r.3, f35v.3 (all P) |
| cthod | 1 | 4 | 0 | 4 | f8v.1, f9r.3, f29v.6 (all P) |

**Pharma `Lf` / `Lc` / `Lp` hits for these 17: none.**

Extra requested searches:

| EVA | Hits |
|---|---|
| keerodal | **f41v.1 `@Lp` only.** 0 in P. Unchanged from pass 1. |
| otaim | **f65r.1 `@Lp`** (`otaim.dam.alam`) and **f111v.3 `+P0`** (one running-text hit). Not on f9v. |

One rare candidate appears as a **non-pharma** label: `ypchy` at f68v2.17 `@Ro` (astronomical page, `$I=A`, paired with `ykeeepol`). That is not `Lf`/`Lc`/`Lp` and is not treated as a plant-name hit.

The only lexical *bridge* from this page into the label layer is the **toldy / otoldy** family: `toldy` is in f9v running text and once more at f43r.11 P; `otoldy` is the most-repeated pharma label in IT (f89r1.4 Lf, f89r2.9 Lc, f99r.14 Lf, f99v.2 Lf; also f82v.45 Lt). That is a type-word family from pass 1, not a species name, and `toldy` itself is never a label.

Common f9v types that *do* appear as labels elsewhere (`daiin`, `chol`, `chor`, `oky`, `otal`, `otol`, `oty`, `chy`, ...) are the same high-frequency items pass 1 already refused to read as plant names. Their rare label uses do not make them names on f9v.

### 3.4 Colour / paint Latin letters (kept out of the EVA gloss)

**Not present in IT2a-n or ZL3b-n as EVA tokens.** There is no `por`, standalone `p`, standalone `r`, or standalone `g` on f9v in either file.

Literature only (Zandbergen, quire 2 page and writing-system COL table; readings marked tentative):

- top-left flower, under the blue paint: **`por`** in the top petal, **`p`** in the lower-left petal, **`r`** (?) in the lower-right petal; an unclear scribble by the top petal
- a clear single **`g`** just right of the top-right flower

These are treated as a **separate Latin-letter paint-instruction layer** (compare `rot` on f4r, `g` on f1v). They are not Voynichese, not EVA, and not evidence that the running text is Latin. `por` as "purple" is a published guess, not used here.

### 3.5 Corpus totals vs pass 1

This parse of IT paragraph text: **34,486 tokens / 7,140 types**; daiin 834, ol 521, chol 384, or 345, chor 217, dain 207. Those P_it function-word counts **match the json**.

Pass 1 reported 33,707 P tokens and daiin 776. That lower pair does **not** match this recompute. Unverified which pass-1 filter produced it (stricter uncertainty drop, different `<->` handling, or a subset). **This pass uses the verified 34,486 / 834 figures** and does not recycle the pass-1 corpus table.

Label tokens this parse: 1,038 / 763 types (pass 1: 1,032 / 763). Close; the +6 is not investigated further.

---

## 4. What survived / died from pass 1 predictions

Pre-registered tests, scored honestly.

1. **daiin / dain / chol / chor stay common on a herbal page, therefore are not the plant name.** **Survived** for daiin (7), chol (3), chor (3). dain is present (1). This is the same pattern as f1r (no plant) and f2v (plant). A token that is the #1 word on a text-only page cannot be "the name of the viola."

2. **ol / or stay common.** **Died on this page** (0 and 0). Weak falsifier: n=84, and both remain huge in the corpus. Do not promote ol/or to "herbal-page-absent." Re-test on the next running-text herbal page.

3. **ok-/ot- is label-legal; qo- may appear in running text, not on labels.** **Survived in the half that can be tested.** f9v has no labels, so label-suppression of `qo-` is unchecked here. Running text has both families: ok+ot 10.7% (corpus-P-like), qo- 8.3% (present, as predicted). Several `qo-` tokens are themselves rare (`qopchypcho` hapax, `qofol`/`qochol` P=2) - rarity does not move them into the name slot if they wear the prose-legal prefix.

4. **Unique rare tokens are the only plant-name candidates.** **Survived as a filter, failed as a positive.** The 17 P<5 types are the only things this pass is willing to *consider*. Nine of them are corpus hapaxes. **None** recur as pharma `Lf`/`Lc`/`Lp`. Pass 1 already said a miss is not fatal (the herbal page may not repeat in quire 15/19). It is still a miss. No f9v token is upgraded to a plant-name hypothesis in ink.

5. **Viola / herba trinitatis as a test, not a fact.** **Held.** ZL's own comment records the O'Neill / "Viola upside down" ID. This pass does not adopt it. No rare EVA token was mapped onto a medieval viola name. No substitution was introduced (pass 1 forbade a language ID in pass 2).

6. **Colour letters stay out of the EVA gloss.** **Held.** They are not in the files.

---

## 5. Hypothesis gloss table

**Every row is a HYPOTHESIS.** Confidence is structural (distribution + position), never semantic. "Gloss" means *role in English*, not a claimed Voynichese meaning. No row identifies the language. No row identifies the plant.

### 5.1 High-frequency function-word candidates (re-tested on f9v)

| EVA | Role (HYPOTHESIS) | Constrained gloss (HYPOTHESIS) | Why this pass still allows it | Why it may be wrong |
|---|---|---|---|---|
| **daiin** | closed-class / function | "and" / weak demonstrative / clause-joiner | 7x on f9v, 7x on f1r, 4x on f2v, 834 in P, 7 in L. Mid-line. Cannot be the name of the plant on this page. | Null / default emit / loose minim-count for `dain`/`daiiin`/`daim` (all three also sit on f9v). |
| **dain** | same class as daiin | same, or a shorter/inflected twin | 1x on f9v (f9v.6); 207 in P. ZL alternative `da[in:iin]` shows the minim is unstable. | May be a space/minim error. Too few on this page to re-prove the class. |
| **chol** | generic herbal-section token, **not** a plant name | "the plant / the herb / this preparation" **or** a second function word | 3x IT / 4x ZL on a page whose plant the literature wants to name. 7x on text-only f1r. 384 in P, 2 in L. | If it is "herb," it is odd that it is equally at home on f1r. Generator ch-word remains simpler. |
| **chor** | same paradigm as chol | variant of chol | 3x on f9v, 3x on f1r, 5x on f2v (f2v's top token). One stray `Lf` on f99v.28 (`chor.olekor`) does not make it a species name. | Free variation under a generator. |
| **oty / oky / otal / otol** | ok-/ot- family in **prose** | classifier-or-stem pieces that are legal in running text; **not** unique names | oty 3x on f9v (P=101); oky 2x (P=92); otal/otol 1x each and common in P. These are the same short items that dominate labels when the page *is* a label page. | On a label page they look name-like; on f9v they look like ordinary A-language vocabulary. Dual use weakens "classifier only." |
| **ol / or** | short function (from pass 1) | "and/or / of" | Still #2 / #7 in the P-corpus. | **Absent on f9v.** Do not lean on them for this page. |
| **fochor / pchor** | paragraph-initial gallows words | section-open / paragraph-start habit, **not** a plant name | `f-`/`p-` start matches the f1r `fachys` rule. `fochor` is a corpus hapax; `pchor` is P=12. | Hapax paragraph-starters are unfalsifiable as "titles." |

**Explicitly refused glosses (this pass):**

- EVA letters as Latin phonemes.
- `chol` / `daiin` / `chor` as *Viola*, herba trinitatis, pansy, or any other plant name.
- Any mapping of a rare f9v token onto a medieval viola name (viola, viola tricoloris, jacea, flos trinitatis, Freyschamkraut, herba trinitatis, pansy). No pre-stated substitution was applied; none is claimed.
- Any named language (Latin, German, Nahuatl, Hebrew, Occitan, Welsh, proto-Romance, etc.).
- Reading `por` / `p` / `r` / `g` as Voynichese.

### 5.2 Rare tokens - the only name *candidates*, still unproven

| EVA | Where | Role (HYPOTHESIS) | Constrained gloss (HYPOTHESIS) | Why | Falsifier already in view |
|---|---|---|---|---|---|
| **chshoty, fochor, kyty, olcfholy, oporody, qopchypcho, rokyd, te, ypcheey** | f9v only (P=1) | the only tokens that *could* be a page-specific name | **no gloss.** Candidate list, not a reading. | Hapax in the whole P-corpus; not ch/d function words (except `te`, which is also a ZL-unstable two-letter). | Any one of them turning up as a high-frequency prose word under a better space-model, or sitting on a visually unrelated page as a label, kills "this page's name." |
| **toldy** | f9v.4 P; f43r.11 P | type-word stem, not a species | same family as pass-1 **otoldy** ("a type of plant-part or container-class") | Only rare f9v token with a repeating pharma-label relative (`otoldy` x4 Lf/Lc). Also `ytoldy` on f9v.9 (P=5, just off the candidate list). | If f99r/f89 `otoldy` drawings share no class with each other or with f9v/f43r context, the family is a glyph coincidence. |
| **ypchy** | f9v.5 P; two other P; f68v2 `@Ro` | not a herbal name | no plant gloss | The `@Ro` hit is astronomical, not `Lf`/`Lc`/`Lp`. | If `@Ro` is later reclassified as a plant-fragment label on a matching drawing, upgrade it. Currently the opposite. |
| **keerodal** | f41v `@Lp` only | whole-plant label (rare) | **candidate plant name** (still) | Unchanged from pass 1. Not on f9v. | One token. |
| **otaim** | f65r `@Lp`; 1x P on f111v | whole-plant label piece | name-ish; `dam alam` may be formula | Unchanged. Not on f9v. | `dam` is common in P. |

**Strongest claim this pass will defend:**  
On a herbal page the literature wants to call a viola, the workhorses are still **daiin / chol / chor**. They are function-like, not the plant's name. The name, if the text has one, is hiding in the rare layer - and that layer does **not** reappear on pharma `Lf`/`Lc`/`Lp` labels in IT. f9v therefore does **not** yet give a plant-name token worth writing in ink. The only positive lexical leftover is the **toldy ~ otoldy** type-word family.

---

## 6. What would falsify this pass

1. **Function-word claim for daiin / chol / chor dies if** a folio whose plant is independently identified uses one of them *only* as a unique caption on that plant and not as a high-frequency token on f1r / f9v / f2v. Observed: the opposite.

2. **"ol/or are herbal-page function words" is already wounded on f9v.** It dies if the next two herbal-A running-text pages also lack them at rates far below corpus expectation.

3. **Rare-token-as-name filter dies if** a better space-model (Grove half-spaces, ZL commas resolved the other way) merges the hapaxes into common words, or if several of the P=1 types are just paragraph-initial gallows formulae (`fochor`).

4. **"no f9v name in the pharma section" dies if** an independent transliteration (GC/v101, RF) reads one of the nine hapaxes as a known `Lf`/`Lc` on a visually similar fragment. IT and ZL do not.

5. **toldy ~ otoldy type-word dies if** the four `otoldy` drawings are unrelated *and* `toldy` in f9v/f43r sits in non-plant prose with no part/container sense. Bio-section `otoldy` at f82v.45 Lt is already a stress test.

6. **Viola-as-test (not fact) is violated if** a later note treats the O'Neill / ELV ID as established. It is not.

7. **Constrained semi-language stance dies** on the same terms as pass 1 S6.5: a pre-registered simple substitution into a known language that yields grammatical running text **and** matching names on the rare / `Lp` words. Not observed.

---

## 7. Next folio to try

**Primary next experiment: f10v (herbal A) plus the claimed lookalike fragment on f89v2.**

Why that pair, not another text-only page:

- f9v produced **no** rare-token hit on `Lf`/`Lc`/`Lp`. The name test needs a herbal page that actually has a claimed pharma twin, so a rare token can fire.
- f10v is the next herbal-A page in sequence; the f89v2 lookalike is the first herbal/pharma twin that can actually run that test.
- Do **not** import the f9v viola literature ID onto either page.

**Type-word backup: f99r (pharmaceutical, `$I=P`).** The one lexical bridge from f9v is `toldy` -> repeating pharma label **`otoldy`** (f99r.14 `Lf`). f99r also carries `okary`/`oky` and lets the `qo-` label-suppression test run (f9v could not; no labels). Use f99r if the twin test is a miss or the next pass should be type-word rather than name-page.

**Protocol (pre-registered for pass 3):**

1. Transcribe f10v from IT **and** ZL; list hapax / P-freq < 5 tokens. Those are the only name candidates.
2. Check the claimed f89v2 lookalike for those rare tokens (and for the f9v hapax set). A hit is a positive for "labels are names." A miss is not fatal.
3. Count `daiin/dain/chol/chor/ol/or` on f10v. Prediction: they stay common.
4. If doing the f99r backup instead: score `ok-`/`ot-` on `L` vs `P`; ask whether `otoldy`/`toldy`/`ytoldy`/`tsholdy` behave as one lemma.
5. Do **not** identify any plant as a species. Do **not** import the f9v viola ID.

**Other backups:** f2v (chol/daiin/chor-heavy negative control) and f65r (the only multi-word `Lp`).

---

## 8. Bottom line for this pass

f9v is readable as *structure*: two paragraphs, no labels, a closed class that refuses to become a plant name (`daiin` 7, `chol` 3, `chor` 3), ordinary running-text rates of `ok-`/`ot-`, and real `qo-` in the prose. It is not readable as *language*, and it is not a viola crib.

The pass-1 split survives contact with a famous herbal page: **high-frequency ch/d-words are generic; unique rare tokens are the only name candidates; those candidates do not recur as pharma labels in IT.** The viola literature ID was used as a test and is left unused as a result. Colour letters `por`/`p`/`r`/`g` stay in a separate Latin paint layer.

Until a rare f9v token is found on a matching fragment under two transliterations, this file is still a lab notebook, not a crib.

---

## Appendix A - raw IT loci for f9v (as in the file)

```
<f9v>      <! $Q=B $P=B $F=a $B=1 $I=H $L=A $H=1 $C=1 $X=C>
<f9v.1,@P0>       <%>fochor.oporody.opy.shor.daiin.qopchypcho.qofol.shol.cfhol.daiin
<f9v.2,+P0>       dchor.qoaiin.chkaiin.cthor.chol.chor.cphol.dy<->oty.qokaiin.dy
<f9v.3,+P0>       ykey.chor.ykaiin.daiin.cthy.otaiin.oky<->oeees.daiin
<f9v.4,+P0>       ytey.tchy.kaiin.cthor.otol.oty.toldy<$>
<f9v.5,+P0>       <%>pchor.ypcheey.qotor.ypchy.olcfholy.te<->ar<->chty.daiiin
<f9v.6,+P0>       odol.choy.ksheody.chody<->dain<->otchy<->cthod.yky
<f9v.7,+P0>       qochol.chol.ctchy.daiin<->otal<->dor<->daim
<f9v.8,+P0>       soiin.daiin.qokcho.rokyd<->daly
<f9v.9,+P0>       daiin.chy.tor.chyty.dary<->ytoldy
<f9v.10,+P0>      oty.kchol.chol.chy.kyty
<f9v.11,+P0>      ychor.chshoty.oky.kaiin
<f9v.12,+P0>      chkaiin.ckhy.chor<$>
```

Source: https://voynich.nu/data/IT2a-n.txt

## Appendix B - raw ZL loci for f9v (control)

```
<f9v>      <! $Q=B $P=B $F=a $B=1 $I=H $L=A $H=1 $C=1 $X=C>
# page 18
# herbal
# Currier's language A, hand 1
# Plant ID: Herba Trinitatis, Freyschamkraut(sp?) (O'Neill)
# Viola Tricoloris, Jacca sive Flos Trinitatis
# RZ: Viola allright but all upside down
#
<f9v.1,@P0>       <%>fochor.oporody.opy.shor.daiin.qopchypcho.qofol.shol.cfhol.daiin
<f9v.2,+P0>       dchor.qoaiin.chkaiin.cthor.chol.chor.cphol.dy<->oty.qokaiin.dy
<f9v.3,+P0>       ykey.chor.ykaiin.daiin.cthy.otaiin.oky<->oeees.daiin
<f9v.4,+P0>       ytey,tch,y.kaiin.cthor.otol.oty.toldy<$>
#
<f9v.5,+P0>       <%>pchor.ypcheey.qotor.ypchy.olcfholy.t[o:e]<->ar<->chty.daiiin
<f9v.6,+P0>       odol.choy.ksheody.chody<->da[in:iin]<->otchy.cthod<->yko
<f9v.7,+P0>       qo.chol.chol.{ct}chy.daiin<->otal<->dor<->daim
<f9v.8,+P0>       soiin.daiin.qokcho.rokyd<->daly
<f9v.9,+P0>       daiin.chy.tor.chyty.dary<->ytoldy
<f9v.10,+P0>      oty.kchol.chol.chy.kyty
<f9v.11,+P0>      ychor.chshoty.oky,kaiin
<f9v.12,+P0>      chkaiin.ckhy.chor<$>
```

ZL's "Plant ID" comments are catalogue notes, **not** findings of this pass.
