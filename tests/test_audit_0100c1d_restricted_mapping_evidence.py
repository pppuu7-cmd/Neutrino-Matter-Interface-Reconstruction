#!/usr/bin/env python3
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.audit_0100c1d_restricted_mapping_evidence import CANDIDATES, matching_windows


class RestrictedMappingEvidenceTests(unittest.TestCase):
    def test_exact_allowlist_has_six_members(self):
        self.assertEqual(len(CANDIDATES), 6)
        self.assertEqual(
            sorted(CANDIDATES),
            sorted([
                "pre_sn_neutrino/README.rst",
                "pre_sn_neutrino/history_columns.list",
                "pre_sn_neutrino/profile_columns.list",
                "pre_sn_neutrino/inlist_common",
                "pre_sn_neutrino/inlist_to_cc",
                "pre_sn_neutrino/src/run_star_extras.f90",
            ]),
        )

    def test_candidate_requires_all_three_token_families_in_fixed_window(self):
        positive = "neutrino spectrum\nfoo\nmodel_number\nfoo\nstep"
        self.assertGreater(len(matching_windows(positive)), 0)
        self.assertEqual(matching_windows("neutrino spectrum\nstep\ntime"), [])
        self.assertEqual(matching_windows("profile_number\nstep\nhistory"), [])

    def test_far_separated_tokens_do_not_form_candidate(self):
        text = "spectrum\n" + "\n".join(["filler"] * 20) + "\nprofile_number\nstep\n"
        self.assertEqual(matching_windows(text), [])


if __name__ == "__main__":
    unittest.main()
