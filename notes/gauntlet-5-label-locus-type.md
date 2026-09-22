# Voynich gauntlet 5 - label prefix register by locus-type family (not a translation)

**For:** Pitchfork-and-Torch
**Date:** 22 Sep 2026 (ET)
**Status:** corpus-wide structural test. No folio opened. **STRICT_NULL** for the herbal/pharma NAME family (`Lf`/`Lc`/`Lp`). Soft "any L" `qo-` ban is honestly narrowed. **No verified full translation of Beinecke MS 408 exists.** Nothing below is a decipherment. Every gloss is marked **HYPOTHESIS**. No plant is identified. No language is identified. EVA letters are not phonemes. Do not grind `keerodal`.

Sources on disk this cycle: `/workspace/voynich-src/IT2a-n.txt`, `ZL3b-n.txt`. Scorer: `scripts/label_locus_type_null.py`. Results: `results/gauntlet-5-label-locus-type.json`.

---

## 0. Why this test

The rollup and README already say: `qo-` is **0** on `Lf` / `Lc` / `Lp`, while the known corpus `qo-` labels sit on other locus types (`L0`, `Ls`, `Lz`, `Ln`, `Lt`). That inventory was never scored as a pre-registered family test with a decision rule for `ok+ot` enrichment inside the NAME family alone.

Gauntlet 4 left "label-locus-type narrowing" as the next named leftover. This cycle runs it. No folio opens.

---

## 1. Source transcription (citation + URL)

Same as gauntlet 4 / series default. IT primary, ZL control. Sanity: 34,486 P / 1,038 L.

**What this is not:** a language ID, EVA-as-phonemes, a plant ID, a reading of any token, or a public post.

---

## 2. Pre-registered families and decision rule

Written before the scorer ran:

| Family | IVTFF locus types | Role in English (HYPOTHESIS, structural only) |
|---|---|---|
| **NAME** | `Lf`, `Lc`, `Lp` | plant / container / plant-caption labels |
| **FIGURE** | `Ln`, `Lt` | nymph / tub-tube labels (balneo) |
| **ZODIAC** | `Lz` | zodiac labels |
| **STARISH** | `Ls` | star / circular-diagram labels |
| **OTHER** | `L0`, `La`, `Lx` | stand-alone / rare / unknown |

**Load-bearing claim:** the *strict* herbal/pharma `qo-` ban and `ok+ot` enrichment hold on **NAME**.

- **STRICT_NULL:** NAME `qo-` = 0 **and** NAME `ok+ot` ≥ 22% **and** (if page-matched n ≥ 50) within-page perm p_le(`qo-`) < 0.001 and p_ge(`ok+ot`) < 0.001.
- **STRICT_HIT:** NAME `qo-` ≥ 1% **or** NAME `ok+ot` ≤ 18% **or** (when n_pm ≥ 50) either perm p > 0.01.
- **STRICT_PARTIAL:** anything else.

**Narrowing supported (secondary, recorded):** NAME has 0 `qo-` tokens **and** at least one non-NAME `qo-` token exists in IT. That means the soft "any L" wording in older notes overclaims; the honest held ban is NAME-scoped.

Other families are descriptive. FIGURE / ZODIAC may still be `ok+ot`-rich; that does not widen the strict ban.

---

## 3. Results (IT primary; ZL agrees)

### 3.1 Families

| Family | n | page-matched | `qo-` | `ok+ot` | perm p_le qo | perm p_ge ok+ot | `qo-` types present |
|---|---|---|---|---|---|---|---|
| **NAME** | **260** | **257** | **0.0%** | **29.6%** | **< 1e-5** | **< 1e-5** | *(none)* |
| FIGURE | 123 | 123 | 2.4% | 42.3% | < 1e-5 | < 1e-5 | `qokal`, `qoted`, `qotedy` |
| ZODIAC | 367 | 0 | 0.3% | 44.1% | n/a (L0 pages) | n/a | `qokeoly` |
| STARISH | 82 | 67 | 1.2% | 37.8% | 0.098 | < 0.001 | `qotoear` |
| OTHER | 206 | 185 | 1.9% | **10.2%** | < 0.001 | 0.70 | `qokal`, `qolsa`, `qor`, `qotesy` |

Corpus L `qo-` types this parse (8 types / matches the known inventory as types; token count in rollup was 9 because `qokal` appears twice):  
`qokal`, `qokeoly`, `qolsa`, `qor`, `qoted`, `qotedy`, `qotesy`, `qotoear`.

**All of them are outside NAME.** NAME `qo-` token list is empty in IT and in ZL first-alt.

### 3.2 By raw locus type (IT)

| ltype | n | `qo-` | `ok+ot` | family |
|---|---|---|---|---|
| Lf | 216 | 0 | 29.2% | NAME |
| Lc | 40 | 0 | 32.5% | NAME |
| Lp | 4 | 0 | 25.0% | NAME |
| Ln | 68 | 2.9% | 36.8% | FIGURE |
| Lt | 55 | 1.8% | 49.1% | FIGURE |
| Lz | 367 | 0.3% | 44.1% | ZODIAC |
| Ls | 82 | 1.2% | 37.8% | STARISH |
| L0 | 196 | 2.0% | 8.7% | OTHER |
| La / Lx | 7 / 3 | 0 | ~33-43% | OTHER |

---

## 4. Verdict: STRICT_NULL + narrowing supported

| Clause | Observed | Result |
|---|---|---|
| NAME `qo-` = 0 | 0 / 260 | met |
| NAME `ok+ot` ≥ 22% | 29.6% | met |
| page-matched perm both p < 0.001 | p < 1e-5 both | met |
| ZL NAME | same direction, 0 `qo-` | agrees |
| **compound NAME** | | **STRICT_NULL** |
| non-NAME `qo-` exists | 8 types | **narrowing supported** |

**HYPOTHESIS (compounded, narrowed):** the strict label ban on `qo-` and the `ok-`/`ot-` enrichment that the series can defend without overclaim are properties of the herbal/pharma NAME locus family (`Lf`/`Lc`/`Lp`), not of every locus whose flag contains `L`.

**HYPOTHESIS (recorded):** FIGURE and ZODIAC remain `ok+ot`-rich even with a few `qo-` tokens; OTHER (`L0` especially) is *not* `ok+ot`-rich (~10%). Do not merge OTHER into the label-register law.

This is not a plant-name claim. It is a register-scope claim.

---

## 5. What SURVIVED / what is revised

| Claim | Mark |
|---|---|
| NAME family is label-shaped vs same-page P | **STRICT_NULL / compounded** |
| Soft wording "`qo-` banned on all labels" | **narrowed** - still useful as a corpus-level description (0.9%), but the clean zero is NAME |
| `ok+ot` enrichment on all L | **wounded for OTHER/L0**; still strong on NAME / FIGURE / ZODIAC / STARISH |
| Gauntlets 2-4 compound law | held; scope language should say NAME when claiming a *ban* |

**Still dead:** species readings; `keerodal` grind; plant ID; language ID; EVA-as-phonemes; f75v as a test of the *NAME* ban (its `qo-` labels are `Ln`/`Lt`, already classified FIGURE).

---

## 6. What would still falsify

1. A clean `Lf` / `Lc` / `Lp` token starting with `qo-` in IT or ZL under this tokenisation.
2. NAME `ok+ot` collapsing toward P rates under a better space model that reassigns locus types.
3. A third transliteration that moves the nine `qo-` tokens into NAME flags.
4. Treating FIGURE `qo-` tokens as a break of the *NAME* ban (they are not).

---

## 7. Next

**Idle on folio walks.** Structural leftovers that remain weakly tried:

- Secondary section `T` from gauntlet 4 (HIT-shaped, 2 pages) - needs floors or an explicit tiny-n rule.
- OTHER/`L0` low `ok+ot` - descriptive; could be a first-token vs later-token split inside multi-word labels (gauntlet 2 already noted the confound).

**Not next:** `keerodal` grind; f75v as NAME-ban test; opening herbal pages; promoting FIGURE `qo-` into a cracked reading.

---

## 8. Bottom line

No folio. No translation. No plant ID. No language ID.

**IT NAME (`Lf`+`Lc`+`Lp`, n=260): `qo-` 0%, `ok+ot` 29.6%, page-matched perm p < 1e-5 both ways vs same-page P. All corpus L `qo-` types sit outside NAME. ZL agrees. STRICT_NULL for the NAME register; soft "any L" ban honestly narrowed. HYPOTHESIS only.**

Reproduce: `python3 scripts/label_locus_type_null.py /path/to/IT2a-n.txt /path/to/ZL3b-n.txt > results/gauntlet-5-label-locus-type.json`.
