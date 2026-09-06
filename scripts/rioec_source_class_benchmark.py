#!/usr/bin/env python3
import json

from nmir.rioec_gate import resonance_area_numeric, smooth_profile_overlap_ratio, source_flavor_factor

B0 = 1.0
payload = {
    "classification_expected": "RIOEC_B16_FLAVOR_NO_GO_PASS / RIOEC_AREA_PROFILE_PASS / G8_TARGET_SPECIFIC_OPEN",
    "b16_nu_e_factor": source_flavor_factor("nu_e"),
    "rioec_antinu_e_factor": source_flavor_factor("anti-nu_e"),
    "area_ratio_gamma_1e-3": resonance_area_numeric(0.1, 1e-3, B0) / B0,
    "area_ratio_gamma_1e-9": resonance_area_numeric(0.1, 1e-9, B0) / B0,
    "smooth_overlap_gamma_over_source_1e-5": smooth_profile_overlap_ratio(1e-5),
    "smooth_overlap_gamma_over_source_1e-3": smooth_profile_overlap_ratio(1e-3),
    "note": "B16 thermonuclear solar sources are neutrinos, not antineutrinos; thermal solar pair-process antineutrinos remain a separate source class for target-specific G8 follow-up.",
}
print(json.dumps(payload, indent=2, sort_keys=True))
