# Voynich gauntlet 9 - ZL-only fRos tagging vs g8 IT/ZL disagreement (not a translation)

**For:** Pitchfork-and-Torch
**Date:** 22 Sep 2026 (ET)
**Status:** corpus-wide structural / transliteration-membership test. No folio opened. No reading of rosette labels. **TAGGING_EXPLAINS_DISAGREE**. **No verified full translation of Beinecke MS 408 exists.** Nothing below is a decipherment. Every gloss is marked **HYPOTHESIS**. No plant is identified. No language is identified. EVA letters are not phonemes. Do not grind `keerodal`.

Sources on disk this cycle: `/workspace/voynich-src/IT2a-n.txt`, `ZL3b-n.txt`. Scorer: `scripts/fros_tagging_null.py`. Results: `results/gauntlet-9-fros-tagging.json`.

---

## 0. Why this test

Gauntlet 8 compounded to PARTIAL because IT was STILL_WOUNDED and ZL was LENGTH_EXPLAINS. Inventory showed ZL page **`fRos`** (aggregate rosette foldout) carries **126** wordlike sole `L0` tokens; IT has **no** `fRos` page and does not place those labels in the L0 sole arm. Gauntlet 8 §6 named an IT↔ZL `L0`/fRos tagging audit as the next leftover. This cycle runs it. It is a **parser / membership** gate, not a folio walk.

---

## 1. Source transcription

Same as series default. IT primary, ZL control.

**What this is not:** a language ID, EVA-as-phonemes, a plant ID, a reading of any rosette token, a claim that fRos labels are plant names, or a public post.

---

## 2. Pre-registered rule (written before the scorer ran)

| Knob | Value |
|---|---|
| Contrast | same as gauntlet 8: L0 sole `len>=3` vs NAME sole `len>=3` |
| Exclusion | drop page `fRos` from both arms (ZL-only page) |
| IT expectation | no `fRos` page → baseline == exclude |

**Compound verdict:**

- **TAGGING_EXPLAINS_DISAGREE:** IT stays STILL_WOUNDED; ZL baseline is LENGTH_EXPLAINS; after excluding `fRos`, ZL flips to STILL_WOUNDED.
- **DISAGREE_REMAINS:** ZL still not STILL_WOUNDED after exclusion.
- **VOID:** neither file has `fRos`.

---

## 3. Results

### 3.1 fRos inventory (ZL only)

| | n | `ok+ot` | mean_len | note |
|---|---|---|---|---|
| ZL `fRos` all tokens | 184 | - | - | L=148 / P=36; sect C |
| ZL `fRos` L0 sole `len>=3` | **126** | **30.2%** | 6.06 | NAME-like enrichment |
| IT `fRos` page | **absent** | - | - | not in IT page list |

### 3.2 Length-matched contrast

| File | Condition | n_L0 | L0 `ok+ot` | n_NAME | NAME `ok+ot` | Verdict |
|---|---|---|---|---|---|---|
| IT | baseline (= excl) | 48 | 12.5% | 211 | 31.8% | STILL_WOUNDED |
| ZL | baseline (incl fRos) | 174 | 24.7% | 227 | 32.6% | LENGTH_EXPLAINS |
| ZL | **exclude fRos** | **48** | **10.4%** | 227 | 32.6% | **STILL_WOUNDED** |

Compound: **TAGGING_EXPLAINS_DISAGREE**.

After exclusion, ZL's non-fRos L0 sole wordlike pool matches IT in size (n=48) and rate (~10-12%), with the same top pages (f66r / f67r2 / f67v1 / f57v).

---

## 4. Verdict: TAGGING_EXPLAINS_DISAGREE

**HYPOTHESIS:** the gauntlet-8 IT/ZL disagreement is explained by ZL's extra `fRos` membership. Those 126 wordlike sole `L0` tokens are `ok+ot`-rich (~30%, NAME-like) and absent from IT's L inventory. Once they are excluded under a pre-registered ZL-only-page rule, ZL agrees with IT: shared-page `L0` sole remains wounded vs NAME.

**HYPOTHESIS (scope):** this does **not** say rosette labels are plant names. It says ZL tags a large, enriched circular-diagram label pool as `L0`, which dilutes the OTHER-wound statistic. The honest NAME ban (g5) is unchanged. Do not merge `fRos` `L0` into NAME without its own gate.

**HYPOTHESIS (series hygiene):** when quoting OTHER/`L0` weakness going forward, either (a) use IT primary, or (b) report ZL with `fRos` excluded / stratified. Raw ZL L0 averages overclaim enrichment relative to IT.

---

## 5. What SURVIVED / what is new

| Claim | Mark |
|---|---|
| NAME register (g5) | held |
| g8 IT STILL_WOUNDED | held; now ZL-aligned after fRos exclusion |
| g8 compound PARTIAL | **explained** (tagging), not a deep law split |
| Soft any-L ban | still narrowed to NAME |

**Still dead:** species readings; `keerodal`; plant ID; language ID; EVA-as-phonemes; reading fRos tokens; opening the rosette as a name hunt.

---

## 6. What would still falsify

1. IT gaining an equivalent rosette L inventory under a future IT release that lands `ok+ot`-poor (would reopen the wound as corpus-wide even with rosettes).
2. Showing ZL `fRos` tokens are mistagged and belong under `Ls` / another family that the series already treats as ok+ot-rich (would reframe, not kill, this result).
3. NAME sole collapsing toward 12% under revised tokenisation.

---

## 7. Next

**Structural leftovers from this cook day are largely closed.** Honest idle:

- Stop folio walks. No new named gate required.
- Optional later: stratify circular-diagram labels (`Ls` / ZL `fRos`) as their own family vs NAME (new gate, not a folio).

**Not next:** reading fRos; `keerodal`; f75v as NAME-ban test; X.

---

## 8. Bottom line

No folio. No translation.

**ZL `fRos` L0 sole `len>=3`: n=126, `ok+ot` 30.2% (NAME-like); absent from IT. ZL without `fRos`: L0 sole wordlike n=48, `ok+ot` 10.4% → STILL_WOUNDED, matching IT 12.5%. Compound TAGGING_EXPLAINS_DISAGREE. HYPOTHESIS only.**

Reproduce: `python3 scripts/fros_tagging_null.py /path/to/IT2a-n.txt /path/to/ZL3b-n.txt > results/gauntlet-9-fros-tagging.json`.
