# Voynich gauntlet 6 - section T tiny-n length-floor redesign (not a translation)

**For:** Pitchfork-and-Torch
**Date:** 22 Sep 2026 (ET)
**Status:** corpus-wide structural test. No folio opened. **TINY_HIT** under an explicit tiny-n rule (section T still not load-bearing). **No verified full translation of Beinecke MS 408 exists.** Nothing below is a decipherment. Every gloss is marked **HYPOTHESIS**. No plant is identified. No language is identified. EVA letters are not phonemes. Do not grind `keerodal`.

Sources on disk this cycle: `/workspace/voynich-src/IT2a-n.txt`, `ZL3b-n.txt`. Scorer: `scripts/section_t_tiny_null.py`. Results: `results/gauntlet-6-section-t-tiny.json`.

---

## 0. Why this test

Gauntlet 4 recorded secondary section `T` as HIT-shaped (`qo-` 6.8%, `ok+ot` 1.7%) on 2 both-band pages and refused to promote it. Gauntlet 5 §7 left it as a leftover that "needs floors or an explicit tiny-n rule." Inventory showed the raw slice is dominated by single-glyph `L0` tokens on f66r / f76r (mean length 2.24). This cycle pre-registers a **word-like length floor** and an explicit tiny-n decision rule. It does **not** make `T` load-bearing.

---

## 1. Source transcription

Same as gauntlets 4-5 / series default. IT primary, ZL control. Sanity: 34,486 P / 1,038 L.

**What this is not:** a language ID, EVA-as-phonemes, a plant ID, a reading of any token, a folio walk of f66r, or a public post.

---

## 2. Pre-registered rule (written before the scorer ran)

| Knob | Value |
|---|---|
| Section | `T` only, page-matched both-band pages (gauntlet-4 secondary scope) |
| Primary filter | `len(token) >= 3` (word-like) |
| Sensitivity | `len >= 4` (reported, not verdict) |
| Tiny-n floor | `n_filtered >= 10` else `TINY_UNDERPOWERED` |
| Load-bearing | **false** (still 1-2 pages; gauntlet-4 floors unmet) |

**Verdict (tiny-n only):**

- **TINY_HIT:** `qo-` ≥ 5% **and** `ok+ot` ≤ 18% after `len>=3`
- **TINY_NULL:** `qo-` ≤ 3% **and** `ok+ot` ≥ 22% after `len>=3`
- **TINY_PARTIAL:** anything else with floors met
- Compound: TINY_HIT if either IT or ZL is TINY_HIT; TINY_NULL only if both are

---

## 3. Results (IT primary; ZL agrees)

### 3.1 Calibration (unfiltered, page-matched T)

| | n_L | pages | `qo-` | `ok+ot` | mean_len |
|---|---|---|---|---|---|
| Raw T L | 59 | f66r, f76r | 6.8% | 1.7% | 2.24 |

Short discarded (`len<3`): **40** tokens (almost all single glyphs; f76r contributes 9/9).

### 3.2 After `len>=3` (verdict-bearing)

| | n | pages | `qo-` | `ok+ot` | `qo-` tokens | Verdict |
|---|---|---|---|---|---|---|
| **IT** | **19** | **f66r only** | **21.1%** | **5.3%** | `qor`, `qotesy`, `qokal`, `qolsa` | **TINY_HIT** |
| **ZL** | **19** | **f66r only** | **21.1%** | **5.3%** | same four | **TINY_HIT** |
| Sensitivity `len>=4` | 17 | f66r | 17.6% | 5.9% | drops `qor` | TINY_HIT |

Compound: **TINY_HIT**.

The four `qo-` tokens are exactly the known f66r `L0` set already inventoried in the rollup / gauntlet 5 (outside NAME). The sole `ok+ot` hit is `otcheo` (IT) / `otcheodaiin` (ZL first-alt on the `Lx` locus).

---

## 4. Verdict: TINY_HIT (secondary confirmed; not load-bearing)

| Clause | Result |
|---|---|
| HIT shape survives word-like filter | yes |
| T becomes load-bearing | **no** (1 page after filter; floors still unmet) |
| NAME law touched | **no** |
| ZL control | agrees |

**HYPOTHESIS (recorded, not promoted):** section `T`'s disagreement with the label register is not an artifact of single-glyph noise alone. Among the 19 word-like `L` tokens on f66r, `qo-` stays high and `ok+ot` stays low. That is consistent with gauntlet 5's OTHER/`L0` wound and with the series' refusal to treat every `L` flag as NAME.

**HYPOTHESIS (scope):** this is a tiny-n, one-page secondary observation. It does not kill the corpus NAME law. It does not open f66r as a folio walk. Promote only if a future gate meets load-bearing floors without fishing.

---

## 5. What SURVIVED / what is new

| Claim | Mark |
|---|---|
| NAME `qo-` ban / `ok+ot` enrichment (g5) | untouched |
| Soft "any L" ban | still narrowed; f66r `L0` `qo-` remain the known non-NAME set |
| Gauntlet-4 secondary T HIT-shape | **confirmed under length floor** (TINY_HIT) |

**Still dead:** species readings; `keerodal` grind; plant ID; language ID; EVA-as-phonemes; promoting T without floors; reading the four `qo-` tokens.

---

## 6. What would still falsify

1. A redesign that gives section `T` ≥5 both-band pages with word-like L and still meets TINY_NULL (unlikely without new transcription scope).
2. A third transliteration that moves the four f66r `qo-` tokens into NAME flags (would also break gauntlet 5).
3. Showing the 19 tokens are mistagged `P` under IVTFF (parser / flag audit) - not scored here.

---

## 7. Next

Named leftovers after this cycle: OTHER/`L0` sole-vs-multi / length confound (gauntlet 7).

**Not next:** f66r folio walk; reading `qokal`/`qolsa`/`qor`/`qotesy`; promoting T to load-bearing; `keerodal`.

---

## 8. Bottom line

No folio. No translation. No plant ID. No language ID.

**IT section T after `len>=3`: n=19 on f66r, `qo-` 21.1%, `ok+ot` 5.3%, four known `L0` `qo-` tokens retained. ZL agrees. TINY_HIT under the explicit tiny-n rule; section T remains secondary. HYPOTHESIS only.**

Reproduce: `python3 scripts/section_t_tiny_null.py /path/to/IT2a-n.txt /path/to/ZL3b-n.txt > results/gauntlet-6-section-t-tiny.json`.
