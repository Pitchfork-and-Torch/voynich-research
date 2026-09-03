# Voynich Cook - Steward-keep rollup, passes 1-7 (not a translation)

**For:** Jon Bailey
**Date:** 14 Aug 2026 (ET)
**Status:** constrained rollup of seven working notes. **No verified full translation of Beinecke MS 408 exists.** Nothing below is a decipherment. Every gloss is marked **HYPOTHESIS**. No plant is identified. No language is identified. EVA letters are not phonemes. This file is a lab notebook Steward can keep, not a crib and published as lab notes, not a decipherment claim.

This note does not start a new folio. The IT herbal `@Lp` inventory is exhausted. The unique-name leftover is one token, already scored. Next is idle.

---

## 1. Source transcription (citation + URL)

Primary text used across the series:

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
| Pass notes | `notes/pass-1.md` ... `notes/pass-7-f41v.md` |
| Steward briefs | `(internal steward brief, omitted)` ... `(internal steward brief, omitted)` |
| Stats / extracts | `(local stats extract, not published)`, `*-extract.txt` |

ZL is the **control**, not the running text.

**What this is not:** a download of any copyrighted monograph, a Cheshire/Gibbs-style "complete solution," a language identification, a claim that EVA letters are phonemes, a plant identification, or a public post.

---

## 2. Method Steward must keep

Tokenisation (IVTFF 2.0), **passes 2-7 verified parse** - this is the series default:

- `.` is a word break.
- **`<->` is a word space** (do not strip and concatenate).
- All remaining `<>` markup is stripped (`<%>`, `<$>`, `<!...>`, leftover `<@H=n>`).
- Tokens must contain at least one A-Z letter. `?` is kept if present.
- Paragraph text = loci whose flags contain `P`. Labels = flags containing `L`.
- ZL extras: uncertain commas are **joined** (not a space); alternatives `[a:b]` take the first reading; ligature braces expand to their contents.

**Pass 1 method difference (do not recycle its corpus table):** pass 1 treated `.` as a word break and **ignored / stripped `<->`**, which joins across that mark. It also did not strip leftover `<@H=n>` on f115r. That is why pass 1 reported **33,707 P tokens / 7,526 types** and daiin **776**, and L **1,032 / 763**. Those figures are **unverified** against the later parse. **Prefer the later verified parse for all corpus numbers.**

**Verified corpus (passes 2-7, same files, `<->` = space, `<@H=n>` stripped):**

| Band | Tokens | Types |
|---|---|---|
| IT paragraph text (`P`) | **34,486** | **7,140** |
| IT labels (`L`) | **1,038** | **763** |

Top P function-word counts this parse: daiin **834**, ol **521**, chol **384**, or **345**, chor **217**, dain **207**.

Prefix rates this parse:

| Band | n | ok+ot | qo- |
|---|---|---|---|
| IT P | 34,486 | **11.4%** (ok 6.0% + ot 5.4%) | **15.1%** |
| IT L (all) | 1,038 | **33.0%** (ok 16.0% + ot 17.1%) | **0.9%** |
| IT `Lf` / `Lc` / `Lp` | 216 / 40 / 4 | 29.2% / 32.5% / 1/4 | **0 / 0 / 0** |

The 9 corpus `qo-` labels are not herbal-plant / pharma: f66r `L0`, f67r2 `@Ls`, f73v `&Lz`, f75v `Ln`/`Lt`. **`qo-` remains 0 on `Lf` / `Lc` / `Lp`.**

IT herbal `@Lp` inventory this parse: **2 loci, 4 tokens / 4 types** - `keerodal` (f41v), `otaim` `dam` `alam` (f65r). ZL also marks f2r `ytoail` as `@Lp`; IT does not (f2r is P-only in IT). ZL-only `ytoail` is **not** an IT leftover.

---

## 3. Folios covered (one-line result each)

| Pass | Folio | What it is | One-line result |
|---|---|---|---|
| 1 | **f1r** | text-only, Currier A, hand 1; 4 paragraphs. Pass-1 parse: 210 tokens / 163 types. No plant. EVA `q` = 0. | Closed class visible (`daiin`/`chol` 7 each). High-frequency ch/d-words are generic. `ok-`/`ot-` is the name-*like* layer on labels elsewhere. Unique `Lp` hapaxes are the only plant-name *candidates*, unproven. |
| 2 | **f9v** | herbal A, hand 1; 12 P-loci, 2 paragraphs, **no labels**. IT 84 / 66. | Workhorses stay function-like (`daiin` 7, `chol` 3, `chor` 3). 17 P<5 types; **no** `Lf`/`Lc`/`Lp` hits. Viola / herba trinitatis is literature-only, unused. Only lexical leftover: `toldy` ~ pharma `otoldy`. |
| 3 | **f10v + f89v2** | herbal A (7 P-loci, no L; IT 53 / 39) + claimed pharma lookalike (f89v2: 158 P / 17 L). | Visual lookalike is sourced ("some similarity," fragment #50 ~ `okam`). **Lexical twin = miss.** No f10v type matches any f89v2 label. `qo-` = 0/17 on f89v2 L (first label-page test). |
| 4 | **f99r** | pharma A, quire 19; 18 P + 4 Lc + 30 Lf. IT P 162 / 118; L 35 / 33. | First same-page two-sided score: P `qo-` 10.5%, L `qo-` **0/35**; L ok+ot 34.3%. `otoldy` nest (`otoldy` / `yteold` / `tsholdy` / `yteoldy`) = **one type-word**, not four species. `okary`x2 page-local; `oky`x2 too-common-in-P. |
| 5 | **f99v** | verso of f99r; 19 P + 4 Lc + 21 Lf. IT P 147 / 114; L 28 / 28 (TTR 1.0). | Second two-sided score: L `qo-` **0/28**. P ok+ot high (27.2%) because of `okol`/`okeol`/`qokeol` formula - cleaner split is `qo-`. Two type-word families, not one merge: `-oldy` vs `otal~`. `otoky` adjacent, not merged. Latin paint `p`/`r` kept out of EVA. |
| 6 | **f65r** | herbal, quire 8, hand 3; **no P**. Only multi-word herbal `@Lp` in IT. | IT `otaim.dam.alam` (ZL may join first break -> `otaimdam alam`). **Three-name title is dead.** `dam` is formula (P=93, also f99r.40 `Lf`). `alam` P=7, stars/recipes only. `otaim` is rare `ot-` head (P=1 on f111v, no longer unique). |
| 7 | **f41v** | herbal B, quire 6, hand 5; 1 uncertain `@Lp` + 7-line P. IT P 67 / 57; L 1. | `keerodal` still unique (P=0, L=1). ZL first-alt `keeredal` (vowel uncertain). `qo-` legal in P (11.9%), banned on the Lp. `daiin`/`chol`/`ol`/`or` fire in prose, not the caption. `dam` sits in the prose. Lp is **not** `ok-`/`ot-`. IT herbal `Lp` inventory exhausted. |

Literature plant IDs encountered and **left unused** (catalogue notes, not findings): f9v Viola / herba trinitatis; f10v hellebore; f99v "capsicum"; f65r geranium / rue / dropwort / *Spiraea filipendula*; f41v daucus / fern / maidenhair / tansy / "plain carrot." Colour letters (`por`/`p`/`r`/`g` on f9v; Latin `p`/`r` on f99v) are a separate paint layer, not EVA.

---

## 4. What SURVIVED as working hypotheses

**Every row is a HYPOTHESIS.** Confidence is structural (distribution + position), never semantic. "Gloss" means *role in English*, not a claimed Voynichese meaning.

### 4.1 Function-like / generic tokens - not plant names

| EVA | Role (HYPOTHESIS) | Constrained gloss (HYPOTHESIS) | Why it still stands after 7 passes | Stress |
|---|---|---|---|---|
| **daiin** / **dain** | closed-class / function | "and" / weak demonstrative / clause-joiner | Top or near-top on f1r (7), f9v (7), f10v (8), f99r P (8), f41v P (3). Corpus P=834, L=7. Never the caption on a scored herbal `Lp`. | Null / default emit / loose minim-count (`dain` / `daiiin` / `daim`). |
| **chol** / **chor** | generic herbal-section token, **not** a plant name | "the plant / the herb / this preparation" **or** a second function word | 7x on text-only f1r; common on f9v / f10v / f2v. On label pages they sit in P, not as unique captions. One stray `Lf` (`chor.olekor` on f99v.28) after P=217 does not make a species. | Generator ch-word remains simpler. If it is "herb," it is odd on f1r. |
| **ol** / **or** | short function (corpus-level) | "and/or / of" | Still #2 / #7 in P (521 / 345). Fire on pharma pages (f99r `or`; f99v both) and on herbal-B f41v (both). | **Absent on short herbal-A pages f9v and f10v.** Wounded as a *herbal-A page* claim; not buried as a corpus closed class. |
| **sheol** / **okeol** / **okeey** / **okol** / **qokeol** / **qokol** | common pharma-A / herbal-B prose | formula / generic predicate; **not** names | Dominate f99r / f99v / f41v P. Dual use (occasional label) is the same problem as `oky`. | Dual use weakens "classifier only" for the `ok-` pieces. |

**HYPOTHESIS that still holds:** a token that is the #1 word on text-only f1r cannot be "the name of the plant drawn on f9v / f10v / f41v."

### 4.2 Prefix split

| Claim (HYPOTHESIS) | Constrained gloss (HYPOTHESIS) | Pages that actually tested it | Result |
|---|---|---|---|
| **`ok-` / `ot-` is label-legal** | "item/root/herb-of ___" or a determiner that is *label-legal* | Corpus L 33.0% vs P 11.4%. Page L: f89v2 23.5%; f99r 34.3%; f99v 35.7%; f65r 1/3 (`otaim`). | **Survived at corpus and on pharma L.** Stressed on f41v L (the unique `Lp` is `keer-`, not `ok-`/`ot-`) and on f99v P (ok+ot 27.2% from formula, still below that page's L). Dual use in prose weakens "classifier *only*." |
| **`qo-` is prose-legal, label-illegal** | legal running-text vocabulary; **not** names | **P legal:** f9v 8.3%; f10v 20.8%; f89v2 P 9.5%; f99r P 10.5%; f99v P 18.4%; f41v P 11.9%. **L banned:** f89v2 0/17; f99r 0/35; f99v 0/28; f65r 0/3; f41v 0/1. Whole `Lf`/`Lc`/`Lp` = 0. | **Survived on every page that had labels.** Cleaner discriminator than the ok+ot percentage whenever P is formula-heavy. f9v / f10v / f65r could not score both sides (no L, or no P). |

### 4.3 Type-word families (not species)

| Family (HYPOTHESIS) | Members scored | Role (HYPOTHESIS) | Why not a species |
|---|---|---|---|
| **`-oldy` / `otoldy` nest** | `otoldy` (most-repeated pharma L, x4: f89r1 Lf, f89r2 Lc, f99r.14 Lf, f99v.2 Lf; also 6x P; IT `@Lt` f82v); `oldy` (f99v.4 Lf only, P=26); `tsholdy` / `yteold` / `yteoldy` (f99r only); P-only `toldy` / `ytoldy` | a **type** of plant-part or container-class | Occupies fragment **and** container slots; lives in prose; prefix variation `o-` / `o-` / `y-` / `yte-` / `tsh-`. A unique species name should not also be the most-repeated pharma label **and** a six-times prose word. |
| **`otal~` nest** | `otal` (P=128, mostly zodiac L); `otaly` (P=11, 3x zodiac L + 2 pharma Lf); `otaldy` (f88r Lc, f101v Lf) | a **second** type-word, related by `ot-`, **not merged** with `-oldy` | Too common in P and already a star-label workhorse. Shared prefix, different tail. |
| **`otoky`** | f88r.5 `@Lf`, f99v.9 `@Lf`; P=0; plus f67r1 `@Ri` | adjacent, not merged; type-word **or** reused epithet | P=0 is name-filter-shaped; two different pharma pages is the enemy of "this one root." **No plant-name gloss.** |

A generator that emits `ot-`/`o-`/`y-` + `oldy` / `al(y)` would produce the same nests. The *role* (type-word, not species) can survive either a language account or a generation account.

### 4.4 Rare-token filter, and the `Lp` inventory

**HYPOTHESIS:** unique rare tokens are the only plant-name *candidates*. A candidate list is not a reading. None was upgraded to a plant-name hypothesis in ink.

IT herbal `@Lp` after scoring both loci:

| EVA | P | L | Verdict after pass 6-7 |
|---|---|---|---|
| **keerodal** | **0** | **1** (f41v.1 only) | **still unique.** Name-*shaped* leftover. Unproven. Vowel uncertain (ZL `keer[e:o]dal`). Public catalogue hedges ("uncertain" / "label?"). Not `ok-`/`ot-`. |
| **otaim** | **1** (f111v.3, recipes B, next to `qotain`) | **1** (f65r.1) | Rare `ot-` head. Name-*shaped*. **No longer unique.** |
| **dam** | **93** | **2** (f65r Lp + f99r.40 Lf; also f99v.34 P, f41v.3 P) | **Formula.** Cannot be "name 2 of 3." |
| **alam** | **7** (all `$I=S`) | **1** (f65r only) | Uncommon formula / epithet. Not a hapax. |

**HYPOTHESIS that still holds:** labels are a different vocabulary (flatter curve, `ok-`/`ot-` heavy, `qo-` suppressed), not a random subsample of running text.

**Working stance (HYPOTHESIS, not a language ID):** treat the text as a **constrained semi-language** - function-word-like tokens plus a separate label lexicon. Do not assign phonetic values. Do not identify the language.

---

## 5. What DIED

Scored honestly. A hypothesis that cannot die was never a working hypothesis.

| Claim that died | Where it died | What remains |
|---|---|---|
| **Three-name title** (`otaim` + `dam` + `alam` as three names) | Pass 6, predicted from pass 4-5 (`dam` already Lf + P) | Rare head + formula. `otaim` still name-*shaped*, P=1. |
| **Visual twin => shared rare token** | Pass 3: f10v ~ f89v2 fragment #50. Sourced visual note; **no** shared EVA, rare or common. `okam` is P=23 + zodiac, absent from f10v. | "Labels are a different vocabulary" survived. "Labels are names of the drawn plant" now owes a different twin or a reason the herbal prose and the pharma label may use different words. |
| **`daiin` / `chol` / `chor` as plant names** | Pass 1 (7x on text-only f1r); re-killed on f9v, f10v, f99r, f41v | Function-like / generic. |
| **`otoldy` as a species** | Pass 4-5: most-repeated pharma label, 6x P, prefix nest, fragment **and** container | Type-word family. |
| **`oky` / `okary` / `okam` / `otal` as unique species** | Too-common-in-P and/or already zodiac labels | Generic / type-word / classifier-only. |
| **`otaim` as a unique `Lp` hapax** | Pass 6: P=1 on f111v.3 | Rare `ot-` head, no longer the clean unique leftover. |
| **Simple substitution of a known European language** | Pass 1 H3, unresurrected | Verbose / null-rich cipher remains untested, not endorsed. |
| **`ol` / `or` stay common on short herbal-A pages** | Missed on f9v (n=84) and f10v (n=53) | Wounded as a herbal-A *page* prediction. Corpus class still huge. Pharma and herbal-B pages do fire. Not promoted to "herbal-A-absent" without a longer herbal-A page - and that is **not** a leftover this rollup requires. |
| **A rare f9v / f10v token recurs as pharma `Lf`/`Lc`/`Lp`** | Six consecutive misses (passes 2-7) | Filter survived; positive failed. Pass 1 already said a miss is not fatal. Still a miss. |
| **Hope of a second unique herbal `Lp` after f65r** | Pass 6-7: `otaim` demoted; only `keerodal` left | One-token leftover, scored. |
| **Hope that the unique `Lp` would wear `ok-`/`ot-`** | Pass 7: `keerodal` is `keer-` | Corpus 33% rate stands; this one token does not wear the classifier. |

Generation-with-a-label-rule (pass 1 H2 completed) would **not** kill the role table - it would re-read "function word" as "high-frequency emit" and "classifier" as "label-mode emit." What it would kill is any temptation to pronounce the English glosses.

---

## 6. Unique-name leftover

**One token: `keerodal`.**

| Fact | Value | Source |
|---|---|---|
| IT exact string | `keerodal` | f41v.1 `@Lp` only |
| IT P / L / all | **0 / 1 / 1** | pass 7, verified parse |
| `keer*` / `keero*` | this token only | pass 7 |
| ZL | `keer[e:o]dal` -> first-alt **`keeredal`** (also P=0, L=1, this page only); second-alt matches IT | pass 7 |
| Public hedge | writing.html: f41v "uncertain"; quire 6: "label?" | not a finding of this series |
| Prefix | not `ok-`, not `ot-`, not `qo-` | pass 7 |
| `-odal` tail | productive in P; not a second `keerodal` | pass 7 |
| Nearest neighbour | `keeodal` (P only, f67r1 / f111r) - recorded, **not fished**, not merged | pass 7 |

**HYPOTHESIS:** `keerodal` is a candidate plant-name *piece*, not a verified name. One token, uncertain vowel, uncertain "is this even a label?", no second hit on a matching drawing. That is as far as a name-candidate can get without inventing one.

**`otaim` is not this leftover.** It is a rare `ot-` head (L=1, P=1). Name-*shaped*. No longer unique.

Do **not** chase `keeodal`, f41r, f111v, or ZL-only f2r `ytoail`. That is how the series would start inventing names.

---

## 7. What would still falsify the surviving claims

1. **`qo-` label ban dies if** a clean `Lf`/`Lc`/`Lp` `qo-` label appears in IT/ZL. Not observed on any scored page. Uncertain spaces that glue a `q` onto a label would also need checking; ZL joins in this series did not create one.

2. **Function-word claim for `daiin` / `chol` / `chor` dies if** a folio whose plant is independently identified uses one of them *only* as a unique caption and not as a high-frequency token on f1r / f9v / f10v. Observed: the opposite.

3. **"`keerodal` is unique" dies if** the exact string appears as P or as another L under this tokenisation, **or** if a better space-model splits it into common pieces that are the intended words. Observed: one token, no split in IT.

4. **"`otoldy` is one type-word" dies if** independent transliterations (GC/v101, RF) read the nest as unrelated, **or** if the four `otoldy` drawings share no visual class *and* the six P hits sit in demonstrably non-plant prose. ZL already agrees on the f99r / f99v strings. ZL `otold[:y]` on f89r2.9 and `okoldy` on f82v.45 are stress points, not a kill.

5. **"`otal~` is a second type-word, not merged" dies if** a better paradigm shows `-oldy` and `-al(y)` as the same tail, **or** if those fragments are the same visual class as the `otoldy` set *and* the zodiac hits are reclassified as plant-parts. Currently they are mostly star labels.

6. **"`dam` is formula" dies if** a folio whose plant is independently identified uses `dam` *only* as a unique caption and the 93 P hits are a different lemma. Observed: common P + a second `Lf` on f99r + P on f99v and f41v.

7. **Rare-token-as-name filter dies if** a better space-model merges the hapax labels into common words. Space-model shrinks the hapax *list*; it has not vanished.

8. **Constrained semi-language stance dies if** a pre-registered simple substitution into a known language yields grammatical running text **and** matching names on the rare / `Lp` words. Not observed. Public claims of this kind have not survived that test.

9. **Catalogue IDs as notes (not fact) is violated if** a later note treats Viola / hellebore / capsicum / geranium / rue / dropwort / *Spiraea* / daucus / fern / maidenhair / tansy / carrot as established and imports them onto any EVA token. They are not.

10. **Paint-letter-out-of-EVA dies if** a later note treats `por`/`p`/`r`/`g` (f9v) or the f99v Latin `p`/`r` as EVA tokens or as cribs. They are not in IT/ZL.

---

## 8. Next

**Idle.**

The IT herbal `@Lp` inventory is scored. The unique-name leftover is one unproven token (`keerodal`), already on f41v, with an uncertain vowel and an uncertain "label?" hedge. That is not a licence to open another herbal page and fish for lookalikes.

f2v (herbal-A ol/or control) is **not** named as a required leftover. Pass 1 already used it as a negative control; pass 7 already recorded this parse's check (P=61, L=0, `ol` 0 / `or` 0, `daiin`/`chol`/`chor` fire). It cannot grow the name-candidate list. Re-opening it would be a control re-score, not a leftover the rollup requires. Steward's default after this rollup is stop-and-idle.

**Not next:** f41r, f111v, f88r, another quire-19 pharma page, a `keeodal` hunt, ZL-only f2r `ytoail`, or any twin-token fishing trip.

---

## 9. Bottom line Steward can keep

Seven pages. No translation. No plant ID. No language ID.

The split that survived contact with running text, a claimed lookalike, two real label pages, a multi-word `Lp`, and a unique `Lp` is:

**High-frequency ch/d-words are generic (HYPOTHESIS). `ok-`/`ot-` is label-legal in the corpus (HYPOTHESIS). `qo-` is prose-legal and label-illegal on every page that had labels (HYPOTHESIS). Unique rare tokens are the only name *candidates* (HYPOTHESIS). The repeating `-oldy` and `otal~` families are type-words, not species (HYPOTHESIS). A multi-word `Lp` is not automatically three names. The unique-name leftover is one token, `keerodal` (P=0, L=1), unproven.**

Until that token is found on a matching drawing under two transliterations - or until a pre-registered substitution reads a caption as grammar plus a name - these files are a lab notebook, not a crib.

---

## Appendix - refused claims (series-wide)

- A verified full translation of Beinecke MS 408.
- EVA letters as Latin (or any) phonemes.
- Any named language (Latin, German, Nahuatl, Hebrew, Occitan, Welsh, proto-Romance, Arabic, etc.).
- Any plant identification, including all catalogue IDs listed in S3.
- `daiin` / `chol` / `chor` / `oky` / `okary` / `okam` / `otoldy` / `otal` / `otaly` / `otoky` / `dam` / `alam` as species names.
- `keerodal` / `otaim` as verified plant names (candidates only; `otaim` no longer unique).
- Treating a published visual lookalike as a textual twin or a species ID.
- Reading paint letters as Voynichese.
- A public post.
