#!/usr/bin/env python3
"""Parser guards for IVTFF readers (no corpus download required)."""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from line_position_null import page_permutation, read_loci


class TestReadLociGuards(unittest.TestCase):
    def test_orphan_continuation_does_not_crash(self) -> None:
        raw = "# comment\n/orphaned continuation with no locus yet\n"
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.txt"
            path.write_text(raw, encoding="latin-1")
            loci = read_loci(str(path))
        self.assertEqual(loci, [])

    def test_continuation_appends_to_prior_locus(self) -> None:
        # IVTFF `/` lines are mid-word wraps: append without inserting a break.
        raw = (
            "<f1r>      <! $Q=A $L=A>\n"
            "<f1r.1,@P0>       alpha.be\n"
            "/ta.delta\n"
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "ok.txt"
            path.write_text(raw, encoding="latin-1")
            loci = read_loci(str(path))
        self.assertEqual(len(loci), 1)
        self.assertEqual(loci[0]["tokens"], ["alpha", "beta", "delta"])



class TestPagePermutationGuards(unittest.TestCase):
    def test_empty_l_does_not_divide_by_zero(self) -> None:
        import numpy as np

        rng = np.random.default_rng(0)
        out = page_permutation([], {}, lambda t: t.startswith("qo"), 50, rng)
        self.assertEqual(out["n_L"], 0)
        self.assertIsNone(out["obs_rate"])
        self.assertEqual(out.get("error"), "empty_L")


if __name__ == "__main__":
    unittest.main()
