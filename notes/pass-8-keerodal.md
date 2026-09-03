# Voynich pass 8 - keerodal statistical pass (not a folio walk, not a translation)

**For:** Jon Bailey
**Date:** 14 Aug 2026 (ET)
**Status:** folio-independent statistical pass on the leftover unique herbal `@Lp` token **`keerodal` only**. **No verified full translation of Beinecke MS 408 exists.** Nothing below is a decipherment. Every gloss is marked **HYPOTHESIS**. No plant is identified. No language is identified. EVA letters are not phonemes. This is not a new folio walk. Next is idle.

This note does **not** open f41r, f111v, f2v, or ZL-only f2r. It does **not** chase `keeodal`. Close variants appear only as corpus counts, to prove uniqueness.

Sources were already on disk. They were not re-downloaded. Counts in `(local stats extract, not published)` were computed against the files this pass.

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
| Manuscript | Yale, Beinecke Rare Book & Manuscript Library, MS 408 |
| Prior notes | `notes/pass-7-f41v.md`, `notes/rollup-pass-1-7.md` |

**Tokenisation (IVTFF 2.0), same as passes 2-7.** `.` is a word break. `<->` is a **word space** (do not strip and concatenate). All remaining `<>` markup is stripped (`<%>`, `<$>`, `<!...>`, leftover `<@H=n>`). Tokens must contain at least one A-Z letter. `?` is kept if present. Paragraph text = loci whose flags contain `P`. Labels = flags containing `L`.

ZL is the **control**, not the running text. ZL extras: uncertain commas are **joined** (not a space); alternatives `[a:b]` take the first reading; ligature braces `{ct}` / `{cthh}` / `{ck}` expand to their contents.

This parse's corpus totals match passes 2-7: **34,486 P / 7,140 types; 1,038 L / 763 types**. Sanity-checked this pass (`sanity.*_ok` all true).

**What this is not:** a download of any copyrighted monograph, a Cheshire/Gibbs-style "complete solution," a language identification, a claim that EVA letters are phonemes, a plant identification, a new folio walk, or a public post.

---

## 2. Method

Compute from the **whole IT corpus** (ZL as control). Do not walk another page.

1. Confirm the locus, flags, and exact string in IT and ZL.
2. Exact-token P/L counts. Prefix `keer-` / `keero-`. Suffix `-odal` (how common is the tail, without claiming a second `keerodal`).
3. Glyph / word-shape vs the other IT `Lp` tokens (`keerodal`, `otaim`, `dam`, `alam`). f65r is **not** re-opened as a folio pass.
4. Where a P=0 L=1 token sits on the label frequency curve.
5. What would falsify "unique name-shaped leftover."
6. Stop. Do not name another folio.

---

## 3. Locus (confirm only)

Page header (IT = ZL flags):

```
<f41v>  <! $Q=F $P=B $F=a $B=1 $I=H $L=B $H=5 $C=2>
```

| File | Locus | Flag | Exact string in file | Token this parse |
|---|---|---|---|---|
| IT (primary) | f41v.1 | `@Lp` | `keerodal` | **`keerodal`** |
| ZL (control) | f41v.1 | `@Lp` | `keer[e:o]dal` | first-alt **`keeredal`**; second-alt `keerodal` |

IT exact-string hits in the whole file: **1** (`f41v.1 @Lp`). Zero in P. Zero in non-P/non-L.

ZL: `keerodal` as a first-alt token = **0**. `keeredal` = **1** (`f41v.1 @Lp` only). The disagreement is the fourth letter (`o` vs `e`). Both files agree there is one word, no internal space, no `qo-`, no `ok-`, no `ot-`.

writing.html and the quire-6 page already hedge this locus ("uncertain" / "label?"). That hedge is catalogue, not a finding of this pass.

---

## 4. Uniqueness (IT primary; ZL control)

### 4.1 Exact token

| EVA | IT P | IT L | IT all | ZL P | ZL L | Notes |
|---|---|---|---|---|---|---|
| **keerodal** | **0** | **1** | 1 | 0 | 0 | IT: this `@Lp` only. ZL first-alt does not emit this string. |
| keeredal | 0 | 0 | 0 | 0 | 1 | ZL first-alt artefact on this locus only. Not a token in IT. |

**Still unique?** **Yes**, as an exact string, in IT. P=0, L=1, f41v.1 `@Lp` only. ZL's first-alt `keeredal` is also P=0, L=1, this page only. Whichever vowel you take, that reading is a hapax.

### 4.2 Prefix `keer-` / `keero-`

| Prefix | IT tokens | IT types | IT P | IT L | Types |
|---|---|---|---|---|---|
| `keer-` | **1** | **1** | 0 | 1 | `keerodal` only |
| `keero-` | **1** | **1** | 0 | 1 | `keerodal` only |
| `keer-` (ZL) | 1 | 1 | 0 | 1 | `keeredal` only |
| `keero-` (ZL) | 0 | 0 | 0 | 0 | first-alt breaks `keero-` |

The head is unique. There is no second `keer-` word in IT or in ZL under this parse.

`kee-` (wider, uniqueness proof only, **not a ticket**): 201 tokens / 46 types in IT, almost all P (`keedy` 53, `keey` 44, ...). The **only** `kee-` type that is a label is `keerodal` itself. Nearest neighbour `keeodal` is P=2, L=0 (f67r1.2, f111r.33) - recorded as a count, **not opened**, not merged.

`ke-` on labels: **2** tokens (`keerodal` `@Lp`; `ker` `@Lc` on f102v1, with `ron??`). `ke-` is *rarer* on L (0.19%) than on P (1.02%). `keerodal` is not a typical label prefix.

### 4.3 Suffix `-odal` (common tail, not a second keerodal)

| Measure | IT | ZL |
|---|---|---|
| tokens ending `-odal` | **95** / **43** types | 102 / 47 types |
| of those, P / L | **75 / 4** | 76 / 4 |
| tokens containing `odal` | **125** / **67** types | - |
| tokens ending `-dal` (wider) | 525 / 128 types | - |

IT `-odal` L tokens (counts only; those pages are **not** opened):

| EVA | P | L | Flag | Role this pass |
|---|---|---|---|---|
| **keerodal** | 0 | 1 | `@Lp` f41v.1 | the token |
| odal | 12 | 1 | `&Lz` f72v1.10 | exact tail as a zodiac label; also common in P |
| ytodal | 0 | 1 | `&Ls` f67r2.55 | star/circle label |
| okeeodal | 0 | 1 | `@Ls` f68r1.32 | star/circle label |

A common tail does **not** make the full string common. None of those other `-odal` labels is `keerodal`. Extra contains-`odal` L types (`chodalg`, `okodaly`, `otchodals`, `odalydary`) are likewise not this token and not herbal `Lp`.

Exact piece `odal` is common-ish (IT P=12, L=1). Exact piece `dal` is a workhorse (IT P=222, L=5). That matters for the split-model falsifier in S7, not as a second name.

---

## 5. Glyph / word-shape vs the other IT `Lp` tokens

IT herbal `@Lp` inventory this parse: **2 loci, 4 tokens / 4 types**. Compared structurally. f65r is not re-opened.

| EVA | len | gallows | ch/sh | prefix | tail | P | L | unique P=0 L=1 |
|---|---|---|---|---|---|---|---|---|
| **keerodal** | **8** | `k` (1) | no / no | **`keer-`** (not ok/ot, not qo) | `-odal` | **0** | **1** | **yes** |
| otaim | 5 | `t` (1) | no / no | `ot-` | `-aim` / `-m` | 1 | 1 | no |
| dam | 3 | none | no / no | `da-` | `-m` | 93 | 2 | no |
| alam | 4 | none | no / no | `al-` | `-m` | 7 | 1 | no |

`keerodal` is the longest IT `Lp`, the only `ke-` / `keer-` `Lp`, the only `-odal` `Lp`, and the only P=0 L=1 leftover. It does **not** wear the corpus label classifier (`ok-`/`ot-` = 33.0% of all L; 1/4 of `Lp`, and that one is `otaim`). `qo-` = 0 on all `Lf`/`Lc`/`Lp`, including this token.

ZL `Lp` control inventory (not IT leftovers; **not tickets**): first-alt `keeredal` (this locus), `otaimdam`+`alam` (f65r join), and ZL-only `ytoail` on f2r. IT does not mark f2r as L. `ytoail` is not promoted.

---

## 6. Label-class context (frequency curve)

Labels are a **hapax-heavy** band. A P=0 L=1 type is not rare *as a label type*. It is rare *as an herbal `Lp`*.

| Measure | Value |
|---|---|
| IT L tokens / types | 1,038 / **763** |
| L types with L=1 | **649** (85.1%) |
| L types with P=0 | 412 |
| L types with **P=0 and L=1** | **399** (52.3% of L types; 38.4% of L tokens) |
| of those, length >= 6 | 304 |
| L=2 / L=3-5 / L=6-10 / L>10 types | 60 / 39 / 12 / 3 |
| P=0 L=2 / P=0 L>=3 / P>0 any L | 8 / 5 / 351 |
| `Lf` P=0 L=1 types | 92 / 198 |
| `Lc` P=0 L=1 types | 33 / 40 |
| **`Lp` P=0 L=1 types** | **1 / 4** (`keerodal` only) |
| mean / median P=0 L=1 type length | 6.66 / **7** |
| `keerodal` length vs that median | 8 = median + 1 |
| `keerodal` rank on the L-count curve | **115** (tied at the hapax floor after 114 types with L>=2) |

Top of the L curve is the opposite of this token: single letters and formula (`o` 13, `y` 12, `s` 11, `otal` 10, `ar` 9, `am` 8, `daiin` 7, ...). `keerodal` sits at the **floor**, with the majority of label types.

**What that means (HYPOTHESIS, structural only):** being P=0 L=1 does **not** by itself pick a name out of the label lexicon - more than half of L types are already there. What is scarce is the intersection: herbal whole-plant `@Lp` n P=0 n L=1 n unique `keer-` head. That intersection is one token.

ZL control curve: 1,140 L / 868 types; P=0 L=1 = 483 types. Same shape (hapax-heavy). ZL first-alt `keeredal` is one of those 483, this locus only.

---

## 7. What would falsify "unique name-shaped leftover"

1. **Exact string appears elsewhere** in IT or ZL under this tokenisation, as P or as another L. Observed: it does not.

2. **A better space model splits it into common pieces that are the intended words.**
   - `kee` + `rodal`: both pieces are **0** in IT and ZL. That split invents two new hapaxes; it does not land on existing common words.
   - `keer` + `odal`: `keer` is 0; `odal` is common (IT P=12, L=1). This is the **dangerous** split - the tail already exists as a word.
   - `keero` + `dal`: `keero` is 0; `dal` is a workhorse (IT P=222). Also dangerous if the intended cut is after `keero`.
   - Drop-`r` -> `keeodal`: exists (P=2, L=0). Not a label. Not this string. Not chased.
   Observed this parse: IT writes one undivided word. ZL writes one undivided word with an uncertain vowel. No file puts a `.` or `<->` inside it.

3. **ZL first-alt becomes a different common word.** Observed: `keeredal` is also P=0, L=1, this page only. Taking `[e:o]`'s first letter does not land on a known type.

4. **The catalogue hedge is right, and it is not a label.** writing.html: f41v "uncertain." Quire 6: "label?" If the isolated word above the paragraph is a stray line-start, a catchword, or a discarded draft, "unique herbal `Lp` hapax" is a flag error, not a name. This pass cannot settle that. It can only record that IT and ZL both flag `@Lp`, and that the public catalogue already doubts it.

5. **Constrained semi-language stance dies** on the same terms as pass 1 / the rollup: a pre-registered simple substitution into a known language that yields grammatical running text **and** a matching name on this token. Not observed.

---

## 8. Hypothesis (no gloss beyond the ticket)

**HYPOTHESIS:** `keerodal` is a unique herbal `@Lp` hapax, name-*shaped*, unproven.

Allowed, and no further:

- Unique as an exact string (IT P=0 L=1; `keer-` / `keero-` this token only).
- Sits as `@Lp` on a herbal page, with a public "label?" hedge.
- Not `ok-`/`ot-`, not `qo-`. One gallows `k`. No `ch`/`sh`. Length 8, near the P=0 L=1 median.
- The `-odal` tail is productive; the full string is not.
- Among the four IT `Lp` tokens it is the only leftover that still passes the rare-token filter.

**Not allowed, and not claimed:**

- A plant identification (daucus, fern, maidenhair, tansy, carrot, viola, hellebore, capsicum, geranium, rue, dropwort, *Spiraea*, or anything else).
- A language identification.
- EVA letters as phonemes (`keerodal` != a pronounced word; `dal` != Latin *dal*; `keer` != any Germanic / Arabic / Nahuatl stem).
- A translation of the caption or of the paragraph under it.
- Promoting `keeredal`, `keeodal`, `ytodal`, `okeeodal`, `odal`, `ker`, or ZL-only `ytoail` to a second name or a next ticket.
- A public post.

**Strongest claim this pass will defend:**
The leftover unique herbal whole-plant label in IT is still unique under a whole-corpus recount. `keerodal` is P=0, L=1, f41v.1 `@Lp` only. `keer*` / `keero*` have no other life. ZL's first-alt `keeredal` is the same one locus with an uncertain vowel, also a hapax. The `-odal` tail is common (95 tokens / 43 types); the full string is not. P=0 L=1 is ordinary for *labels* (399/763 types) and scarce for *herbal `Lp`* (1/4). The token is name-*shaped* and unproven. The catalogue already hedges the locus. None of this is a plant identification.

---

## 9. Next

**Idle / stop.**

Do not name another folio. The IT herbal `@Lp` inventory was already exhausted in pass 7. This pass re-counted the leftover token from the whole corpus and did not grow the list. A one-token unproven hapax, with an uncertain vowel and an uncertain "is this a label?" hedge, is not a licence to fish.

**Not next (banned this ticket, still banned):** `keeodal`, f41r, f111v, f2v, ZL-only f2r `ytoail`.

---

## 10. Bottom line

Whole-corpus recount, not a new page. `keerodal` is still the only unique herbal `Lp` hapax in IT (P=0, L=1). The head is unique; the tail is not. It does not wear `ok-`/`ot-`/`qo-`. It sits at the hapax floor of a hapax-heavy label curve, and it is the only IT `Lp` that sits there. Name-shaped, unproven. No plant. No language. No next folio.

Until the exact string is found on a matching drawing under two transliterations - or until a pre-registered substitution reads this caption as grammar plus a name - this file is still a lab notebook, not a crib.

---

## Appendix - refused claims (this pass)

- A verified full translation of Beinecke MS 408.
- EVA letters as Latin (or any) phonemes.
- Any named language.
- Any plant identification, including all catalogue IDs already left unused in passes 1-7.
- `keerodal` / `keeredal` / `keeodal` as a verified plant name.
- Opening f41r, f111v, f2v, or f2r, or writing a pass on `keeodal`.
- A public post.
