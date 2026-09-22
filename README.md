# Voynich research

Lab notes on Yale Beinecke MS 408 (the Voynich manuscript).

**This is not a translation.** No verified full reading of the manuscript exists
here or anywhere else in this work. Every gloss in the notes is marked
HYPOTHESIS. EVA letters are not phonemes. No plant is identified. No language
is identified.

Public product of Pitchfork-and-Torch. License: MIT.

## Last status (2026-09-22 ET)

- Gauntlets 4-5: section-matched null **NULL** (pharma + balneo); locus-type
  **STRICT_NULL** for NAME (`Lf`/`Lc`/`Lp`). Soft any-label `qo-` ban narrowed.
- Gauntlets 6-9: section T **TINY_HIT** (secondary, word-like floor on f66r);
  OTHER/L0 position **CONFOUND_PARTIAL**; length-matched OTHER vs NAME
  **PARTIAL**; ZL-only `fRos` tagging **TAGGING_EXPLAINS_DISAGREE**. Shared-page
  L0 sole stays weak vs NAME once `fRos` is stratified. Hypothesis only.
- Gauntlets 2-3: line-position and label-only-page nulls still hold (NULL).
- Passes 1-8 + herbal-A: unchanged. Do not grind `keerodal`.
- `ok`/`ot` is label-legal on NAME; `qo-` banned on `Lf`/`Lc`/`Lp` (= 0).
- Two type-word families, not one merge: `-oldy` vs `otal~`.

Next is idle. Do not open a new folio unless a new gate is named. Not a translation.

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
| [notes/gauntlet-2-line-position-null.md](notes/gauntlet-2-line-position-null.md) | Label register vs line-position null: NULL |
| [notes/gauntlet-3-label-only-page-null.md](notes/gauntlet-3-label-only-page-null.md) | Label register vs label-only-page null: NULL |
| [notes/gauntlet-4-section-matched.md](notes/gauntlet-4-section-matched.md) | Section-matched null (pharma/balneo): NULL |
| [notes/gauntlet-5-label-locus-type.md](notes/gauntlet-5-label-locus-type.md) | Locus-type families; NAME STRICT_NULL |
| [notes/gauntlet-6-section-t-tiny.md](notes/gauntlet-6-section-t-tiny.md) | Section T tiny-n length floor: TINY_HIT |
| [notes/gauntlet-7-other-l0-position.md](notes/gauntlet-7-other-l0-position.md) | OTHER/L0 sole vs initial: CONFOUND_PARTIAL |
| [notes/gauntlet-8-other-vs-name-length.md](notes/gauntlet-8-other-vs-name-length.md) | Length-matched L0 vs NAME: PARTIAL |
| [notes/gauntlet-9-fros-tagging.md](notes/gauntlet-9-fros-tagging.md) | ZL fRos tagging explains g8 disagree |


## Scripts

| File | What it is |
|---|---|
| [scripts/line_position_null.py](scripts/line_position_null.py) | Gauntlet 2 scorer. Takes the two public IVTFF files as arguments, prints JSON. Needs `numpy`. |
| [scripts/label_only_page_null.py](scripts/label_only_page_null.py) | Gauntlet 3 scorer. Label-only vs page-matched split; prints JSON. Needs `numpy`. |
| [scripts/section_matched_null.py](scripts/section_matched_null.py) | Gauntlet 4 scorer. Section-matched L vs P. Needs `numpy`. |
| [scripts/label_locus_type_null.py](scripts/label_locus_type_null.py) | Gauntlet 5 scorer. Locus-type families. Needs `numpy`. |
| [scripts/section_t_tiny_null.py](scripts/section_t_tiny_null.py) | Gauntlet 6 scorer. Section T length floor. |
| [scripts/other_l0_position_null.py](scripts/other_l0_position_null.py) | Gauntlet 7 scorer. OTHER/L0 position split. |
| [scripts/other_vs_name_length_null.py](scripts/other_vs_name_length_null.py) | Gauntlet 8 scorer. Length-matched L0 vs NAME. |
| [scripts/fros_tagging_null.py](scripts/fros_tagging_null.py) | Gauntlet 9 scorer. ZL fRos exclusion. |


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

## Results

JSON receipts for gauntlets 4-9 (reproduce from `scripts/` + public IVTFF files on disk; files not republished here):

| File | Gate |
|---|---|
| [results/gauntlet-4-section-matched.json](results/gauntlet-4-section-matched.json) | g4 |
| [results/gauntlet-5-label-locus-type.json](results/gauntlet-5-label-locus-type.json) | g5 |
| [results/gauntlet-6-section-t-tiny.json](results/gauntlet-6-section-t-tiny.json) | g6 |
| [results/gauntlet-7-other-l0-position.json](results/gauntlet-7-other-l0-position.json) | g7 |
| [results/gauntlet-8-other-vs-name-length.json](results/gauntlet-8-other-vs-name-length.json) | g8 |
| [results/gauntlet-9-fros-tagging.json](results/gauntlet-9-fros-tagging.json) | g9 |
