#!/usr/bin/env python3
import json, math
from pathlib import Path

N_N = 1.7659857664161126e36
E_GEV = 1500.0
FASER_NU_MU_CC_COEFF_LOWER = 0.3e-38  # cm^2 / GeV, frozen central-minus-1sigma
SIGMA_CC_LOWER = FASER_NU_MU_CC_COEFF_LOWER * E_GEV
TAU_CC_LOWER = N_N * SIGMA_CC_LOWER
T0_UPPER = math.exp(-TAU_CC_LOWER)

result = {
    "schema": "nmir.g9.cross_section_authority.0092a.v1",
    "prereg": "research/prereg/0092a_g9_cross_section_authority.md",
    "frozen_column": {"nucleon_column_cm2": N_N},
    "ngc1068_low_endpoint": {
        "energy_GeV": E_GEV,
        "authority": "FASER Collaboration, PRL 133, 021802 (2024), arXiv:2403.12520",
        "reported_numu_cc_sigma_over_E_central_cm2_GeV": 0.5e-38,
        "reported_numu_cc_sigma_over_E_1sigma_cm2_GeV": 0.2e-38,
        "frozen_conservative_lower_coeff_cm2_GeV": FASER_NU_MU_CC_COEFF_LOWER,
        "sigma_cc_lower_cm2": SIGMA_CC_LOWER,
        "tau_cc_lower": TAU_CC_LOWER,
        "T0_upper_from_cc_lower": T0_UPPER,
        "classification": "SCIENTIFIC_FAIL_G9_TRANSPARENT_SUN_ASSUMPTION",
        "reason": "authority-backed conservative CC lower optical depth exceeds unity at 1.5 TeV"
    },
    "txs_290TeV": {
        "classification": "BLOCKED_G9_0092A_HIGH_ENERGY_AUTHORITY",
        "reason": "exact numerical 290-TeV cross-section authority not yet frozen in machine-readable form; no post-result extrapolation used"
    },
    "ccsn_5_50MeV": {
        "classification": "BLOCKED_G9_0092A_MEV_TOTAL_CROSS_SECTION_AUTHORITY",
        "reason": "conservative total low-energy interaction upper bound requires prospectively frozen solar composition plus coherent/incoherent channel accounting"
    },
    "gate_classification": "BLOCKED_G9_0092A_CROSS_SECTION_AUTHORITY_MIXED",
    "guards": [
        "TeV opacity result applies only to the frozen b/Rsun=0.024 ray/source regime",
        "no DIS extrapolation into MeV",
        "no claim that TeV opacity invalidates CCSN MeV focusing",
        "no detector/material/BSM gain fold"
    ]
}

assert TAU_CC_LOWER >= 1.0
assert T0_UPPER < math.exp(-1.0)

out = Path("g9_0092a_cross_section_authority.json")
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(out.read_text(), end="")
