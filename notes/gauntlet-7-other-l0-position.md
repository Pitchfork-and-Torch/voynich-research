# Voynich gauntlet 7 - OTHER/L0 sole vs multi-word position split (not a translation)

**For:** Pitchfork-and-Torch
**Date:** 22 Sep 2026 (ET)
**Status:** corpus-wide structural test. No folio opened. **IT: CONFOUND_SUPPORTED**; **ZL: CONFOUND_PARTIAL**; **compound CONFOUND_PARTIAL**. Length diagnostic: IT LENGTH_PARTIAL / ZL LENGTH_CONFOUND. **No verified full translation of Beinecke MS 408 exists.** Nothing below is a decipherment. Every gloss is marked **HYPOTHESIS**. No plant is identified. No language is identified. EVA letters are not phonemes. Do not grind `keerodal`.

Sources on disk this cycle: `/workspace/voynich-src/IT2a-n.txt`, `ZL3b-n.txt`. Scorer: `scripts/other_l0_position_null.py`. Results: `results/gauntlet-7-other-l0-position.json`.

---

## 0. Why this test

Gauntlet 2 §5 recorded that inside multi-word labels `ok+ot` sits on the first token, and later tokens are `L0`-heavy - **type and position confounded, not separated**. Gauntlet 5 wounded `ok+ot` enrichment for OTHER/`L0` (~10%) and left that split as a leftover. This cycle separates sole / initial / later inside `L0` and OTHER, and short vs word-like inside sole.

---

## 1. Source transcription

Same as series default. IT primary, ZL control.

**What this is not:** a language ID, EVA-as-phonemes, a plant ID, a reading of any token, or a public post.

---

## 2. Pre-registered rule (written before the scorer ran)

| Class | Definition |
|---|---|
| sole | `pos=sole` (one-token locus) |
| initial | `pos=initial` (first token of multi-word locus) |
| later | `pos=medial` or `final` |
| short | sole with `len<=2` |
| wordlike | sole with `len>=3` |

Floors: sole n≥50, initial n≥20.

**Position verdict (L0 primary; OTHER reported):**

- **CONFOUND_SUPPORTED:** initial `ok+ot` ≥ 18% **and** sole `ok+ot` ≤ 12%
- **UNIFORM_WEAK:** initial ≤ 12% **and** sole ≤ 12%
- **CONFOUND_PARTIAL:** else (floors met)
- Compound: agree → that label; IT/ZL disagree → PARTIAL

**Length diagnostic inside L0 sole:**

- **LENGTH_CONFOUND:** wordlike `ok+ot` ≥ 18% **and** short ≤ 5%
- **SOLE_STILL_WEAK:** wordlike ≤ 12%
- **LENGTH_PARTIAL:** else

Does **not** touch the NAME law.

---

## 3. Results

### 3.1 L0 position (IT primary)

| Class | n | `qo-` | `ok+ot` | mean_len |
|---|---|---|---|---|
| L0 sole | 120 | 3.3% | **5.0%** | 3.14 |
| L0 initial | 30 | 0.0% | **20.0%** | 4.63 |
| L0 later | 46 | 0.0% | 10.9% | 4.07 |
| NAME sole (contrast) | 211 | 0.0% | **31.8%** | 6.01 |
| NAME initial (contrast) | 23 | 0.0% | **39.1%** | 4.26 |

IT position verdict: **CONFOUND_SUPPORTED** (initial 20% ≥ 18%; sole 5% ≤ 12%). OTHER family agrees.

### 3.2 L0 sole length split (IT)

| Class | n | `ok+ot` | mean_len |
|---|---|---|---|
| short `len<=2` | 72 | **0.0%** | 1.04 |
| wordlike `len>=3` | 48 | **12.5%** | 6.29 |

IT length verdict: **LENGTH_PARTIAL** (wordlike 12.5% is above the ≤12% SOLE_STILL_WEAK cut and below the ≥18% LENGTH_CONFOUND cut). Short glyphs are pure zeros; they drag the sole average down but do not fully explain the gap to NAME.

### 3.3 ZL control

| Class | n | `ok+ot` |
|---|---|---|
| L0 sole | 246 | **17.5%** |
| L0 initial | 42 | **31.0%** |
| L0 sole short | 72 | 0.0% |
| L0 sole wordlike | 174 | **24.7%** |

ZL position: **CONFOUND_PARTIAL** (sole 17.5% is *not* ≤ 12%, so the "sole is weak" clause fails even though initial is richer). ZL length: **LENGTH_CONFOUND** (wordlike 24.7% ≥ 18%; short 0%).

**Why ZL sole is larger:** ZL tags **fRos** with 126 word-like sole `L0` tokens that IT does not place in this arm the same way. That transliteration gap is why compound cannot be stronger than PARTIAL.

### 3.4 Compound

| | Verdict |
|---|---|
| IT position | CONFOUND_SUPPORTED |
| ZL position | CONFOUND_PARTIAL |
| **Compound position** | **CONFOUND_PARTIAL** |
| Compound length | LENGTH_PARTIAL |

---

## 4. Verdict: CONFOUND_PARTIAL (IT supports; ZL softens)

**HYPOTHESIS (IT-primary, recorded):** inside `L0`, first tokens of multi-word labels are `ok+ot`-richer (~20%) than sole tokens (~5%). Gauntlet 2's type/position confound is real on IT. Short sole glyphs (`len<=2`, n=72) contribute 0% `ok+ot` and inflate the wound.

**HYPOTHESIS (control):** ZL does not call sole "weak" under the pre-registered ≤12% cut once fRos-heavy word-like `L0` soles are included; those soles sit near 25% `ok+ot`. The wound is **transliteration-sensitive**. Do not overclaim a corpus-wide OTHER failure.

**HYPOTHESIS (scope):** NAME sole remains ~32% `ok+ot` with `qo-` 0 in both IT and ZL. Nothing here widens or kills the NAME ban.

---

## 5. What SURVIVED / what is new

| Claim | Mark |
|---|---|
| NAME register (g5) | held |
| OTHER/`L0` uniformly label-poor | **wounded further as a uniform claim**; position + length + ZL/IT disagree |
| Gauntlet-2 unseparated confound | **partially separated**; IT supports |

**Still dead:** species readings; `keerodal`; plant ID; language ID; EVA-as-phonemes; merging OTHER into the label-register law.

---

## 6. What would still falsify

1. A locus-type remapping that moves fRos between IT and ZL into agreement and flips both arms to UNIFORM_WEAK or both to CONFOUND_SUPPORTED.
2. NAME sole `ok+ot` collapsing toward L0 sole rates under a better space model.
3. Showing `pos=initial` enrichment is only a length effect (→ gauntlet 8).

---

## 7. Next

Length-matched L0 sole vs NAME sole (gauntlet 8) - the direct leftover of LENGTH_PARTIAL / ZL LENGTH_CONFOUND.

**Not next:** folio walks; reading L0 tokens; promoting OTHER into the NAME ban.

---

## 8. Bottom line

No folio. No translation.

**IT L0: sole `ok+ot` 5.0% (n=120) vs initial 20.0% (n=30) → CONFOUND_SUPPORTED. Short sole glyphs 0% (n=72); wordlike sole 12.5% (n=48). ZL sole 17.5% / initial 31.0% → CONFOUND_PARTIAL (fRos tagging). Compound CONFOUND_PARTIAL. NAME contrast untouched. HYPOTHESIS only.**

Reproduce: `python3 scripts/other_l0_position_null.py /path/to/IT2a-n.txt /path/to/ZL3b-n.txt > results/gauntlet-7-other-l0-position.json`.
