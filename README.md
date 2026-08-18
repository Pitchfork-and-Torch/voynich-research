# Voynich research

Lab notes on Yale Beinecke MS 408 (the Voynich manuscript).

**This is not a translation.** No verified full reading of the manuscript exists
here or anywhere else in this work. Every gloss in the notes is marked
HYPOTHESIS. EVA letters are not phonemes. No plant is identified. No language
is identified.

Public product of Pitchfork-and-Torch. License: MIT.

## Last status (2026-08-15 ET)

- Passes 1-7: folio walks on f1r, f9v, f10v, f99r, f99v, f65r, f41v.
- Pass 8: statistical pass on leftover herbal `@Lp` token `keerodal`.
  Still unique (paragraph count 0, label count 1). Not a plant name.
- Herbal-A gauntlet (f1r-f8v labels vs paragraph tokens): FAIL.
  IT labels in that range: 0. Do not grind `keerodal`.
- Three-name title hypothesis: dead.
- `ok`/`ot` is label-legal; `qo-` is banned on herbal / pharma labels
  (`Lf` / `Lc` / `Lp` = 0).
- Two type-word families, not one merge: `-oldy` vs `otal~`.
- High-frequency ch/d-words (`daiin`, `chol`, `chor`) are generic.

Next is idle. Do not open a new folio unless a new gate is named.

## Notes

| File | What it is |
|---|---|
| [notes/rollup-pass-1-7.md](notes/rollup-pass-1-7.md) | Constrained rollup of passes 1-7 |
| [notes/pass-1.md](notes/pass-1.md) | f1r |
| [notes/pass-2-f9v.md](notes/pass-2-f9v.md) | f9v |
| [notes/pass-3-f10v.md](notes/pass-3-f10v.md) | f10v + f89v2 lookalike miss |
| [notes/pass-4-f99r.md](notes/pass-4-f99r.md) | f99r |
| [notes/pass-5-f99v.md](notes/pass-5-f99v.md) | f99v |
| [notes/pass-6-f65r.md](notes/pass-6-f65r.md) | f65r |
| [notes/pass-7-f41v.md](notes/pass-7-f41v.md) | f41v |
| [notes/pass-8-keerodal.md](notes/pass-8-keerodal.md) | `keerodal` uniqueness |
| [notes/gauntlet-1-herbalA-labels.md](notes/gauntlet-1-herbalA-labels.md) | Herbal-A f1r-f8v FAIL |
| [notes/gauntlet-1-f75r.md](notes/gauntlet-1-f75r.md) | Later gauntlet note (balneo hold) |

## Method (series default, passes 2-8)

Primary running text: Takeshi Takahashi IT2a-n.txt (IVTFF 2.0, EVA-T),
https://voynich.nu/data/IT2a-n.txt

Control (not running text): Zandbergen-Landini ZL3b-n.txt,
https://voynich.nu/data/ZL3b-n.txt

Label-behaviour background: Rene Zandbergen,
https://voynich.nu/extra/labels.html

Tokenisation:

- `.` is a word break.
- `<->` is a word space (do not strip and concatenate).
- Remaining `<>` markup is stripped.
- Paragraph text = loci whose flags contain `P`. Labels = flags containing `L`.

Verified corpus (this parse): 34,486 paragraph tokens / 7,140 types;
1,038 label tokens / 763 types.

Pass 1 used a different parse (`<->` stripped). Prefer passes 2-8 for counts.

## What this repo does not contain

- A decipherment, crib, or language identification
- Plant identifications
- Copyrighted monographs
- The raw IT/ZL transcription files (cite voynich.nu; do not republish)
- Liber Primus / Cicada material (that is a different desk)

## License

MIT. See LICENSE. Copyright Pitchfork-and-Torch.
