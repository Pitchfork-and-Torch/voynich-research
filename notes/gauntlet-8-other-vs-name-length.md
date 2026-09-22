# Voynich gauntlet 8 - length-matched L0 sole vs NAME sole (not a translation)

**For:** Pitchfork-and-Torch
**Date:** 22 Sep 2026 (ET)
**Status:** corpus-wide structural test. No folio opened. **IT: STILL_WOUNDED**; **ZL: LENGTH_EXPLAINS**; **compound PARTIAL**. **No verified full translation of Beinecke MS 408 exists.** Nothing below is a decipherment. Every gloss is marked **HYPOTHESIS**. No plant is identified. No language is identified. EVA letters are not phonemes. Do not grind `keerodal`.

Sources on disk this cycle: `/workspace/voynich-src/IT2a-n.txt`, `ZL3b-n.txt`. Scorer: `scripts/other_vs_name_length_null.py`. Results: `results/gauntlet-8-other-vs-name-length.json`.

---

## 0. Why this test

Gauntlet 7 left IT at LENGTH_PARTIAL (wordlike L0 sole `ok+ot` 12.5%) and ZL at LENGTH_CONFOUND (wordlike 24.7%). The named next question: once short glyphs are removed, does `L0` sole still lack enrichment relative to **NAME** sole at the same length floor?

---

## 1. Source transcription

Same as series default. IT primary, ZL control.

**What this is not:** a language ID, EVA-as-phonemes, a plant ID, a reading of any token, or a public post.

---

## 2. Pre-registered rule (written before the scorer ran)

| Arm | Definition |
|---|---|
| L0 sole wordlike | `ltype=L0`, `pos=sole`, `len>=3` |
| NAME sole wordlike | `ltype in {Lf,Lc,Lp}`, `pos=sole`, `len>=3` |
| Floors | both arms n ≥ 30 |

**Verdict:**

- **STILL_WOUNDED:** L0 `ok+ot` ≤ 15% **and** NAME `ok+ot` ≥ 25% **and** Fisher two-sided p < 0.01
- **LENGTH_EXPLAINS:** L0 `ok+ot` ≥ 22%
- **PARTIAL:** else
- Compound: agree → that label; disagree → PARTIAL (do not overclaim the wound)

---

## 3. Results

| | n_L0 | L0 `ok+ot` | n_NAME | NAME `ok+ot` | Fisher `ok+ot` | Verdict |
|---|---|---|---|---|---|---|
| **IT** | **48** | **12.5%** | **211** | **31.8%** | **0.0073** | **STILL_WOUNDED** |
| **ZL** | **174** | **24.7%** | **227** | **32.6%** | 0.097 | **LENGTH_EXPLAINS** |

Compound: **PARTIAL**.

IT L0 wordlike sole pages (top): f66r 16, f67r2 14, f67v1 9, f57v 5. ZL adds **fRos 126**, which is why ZL's L0 arm reaches 24.7% and crosses the LENGTH_EXPLAINS line.

Both arms keep `qo-` near zero on NAME; IT L0 wordlike sole still carries the four f66r `qo-` types (rate 8.3%).

---

## 4. Verdict: PARTIAL (IT wounded; ZL length-explains via fRos)

**HYPOTHESIS (IT-primary):** after removing short glyphs, IT `L0` sole tokens remain `ok+ot`-poor versus NAME sole at the same length floor (12.5% vs 31.8%, Fisher p=0.007). The gauntlet-5 OTHER wound is **not only** single-glyph noise on IT.

**HYPOTHESIS (control):** ZL's much larger wordlike `L0` sole pool (fRos-dominated) sits at 24.7% and meets LENGTH_EXPLAINS. The IT wound does not replicate under ZL tagging. Honest compound is PARTIAL.

**HYPOTHESIS (scope):** NAME sole enrichment holds in both transliterations (~32%). Do not merge OTHER into the NAME register law. Do not treat fRos `L0` as a cracked reading.

---

## 5. What SURVIVED / what is new

| Claim | Mark |
|---|---|
| NAME sole `ok+ot` enrichment | held (IT+ZL) |
| OTHER/`L0` wound = short glyphs only | **rejected on IT**; **plausible on ZL** |
| Soft any-L register | still narrowed to NAME when claiming a ban |

**Still dead:** species readings; `keerodal`; plant ID; language ID; EVA-as-phonemes; folio fishing on fRos / f66r.

---

## 6. What would still falsify

1. An IVTFF flag audit that aligns IT and ZL `L0` membership on fRos and flips both arms the same way.
2. NAME sole `ok+ot` ≤ 15% under a revised tokenisation.
3. A third transliteration that lands between IT and ZL and is pre-registered as tie-break (not this cycle).

---

## 7. Next

**Structural leftovers now thin.** Honest idle candidates:

- IVTFF `L0` / fRos tagging audit (IT vs ZL) as a *parser* gate, not a folio walk.
- Stop. Do not open folios without a new named gate.

**Not next:** `keerodal`; f75v as NAME-ban test; reading f66r `qo-` tokens; X posts.

---

## 8. Bottom line

No folio. No translation.

**IT: L0 sole `len>=3` `ok+ot` 12.5% (n=48) vs NAME sole 31.8% (n=211), Fisher p=0.007 → STILL_WOUNDED. ZL: L0 24.7% (n=174, fRos-heavy) → LENGTH_EXPLAINS. Compound PARTIAL. HYPOTHESIS only.**

Reproduce: `python3 scripts/other_vs_name_length_null.py /path/to/IT2a-n.txt /path/to/ZL3b-n.txt > results/gauntlet-8-other-vs-name-length.json`.
