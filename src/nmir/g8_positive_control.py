"""Experimentally grounded G8 resonance positive controls.

This module is intentionally split between a genuine elementary-particle
Breit-Wigner resonance (Glashow) and the already validated narrow solar
Be7-line overlap with crossed Li7 capture.  They demonstrate different
notions of 'matching' and must not be multiplied together.
"""

from __future__ import annotations

import math

# Rounded control inputs matching the frozen literature benchmark.
M_W_GEV = 80.4
M_E_GEV = 0.00051099895
BR_W_ENU = 0.106
BR_W_HAD = 0.674
GEV2_TO_CM2 = 0.389379e-27

SOLAR_ENERGY_CEILING_MEV = 20.0
XE132_CEVNS_1MEV_CM2 = 2.404884e-41

# Frozen iteration-0023 GS98+MSW Li7 component authority.
LI7_TOTAL_RATE_SNU = 19.3488133336
LI7_TOTAL_ENERGY_SNU_MEV = 77.5070777600
LI7_BE7_RATE_SNU = 4.07166111
LI7_BE7_ENERGY_SNU_MEV = 3.51461158

# Literature concept control only, not a validated material realization.
H3_HE3_IDEALIZED_RESONANT_CM2 = 5.0e-32
H3_HE3_RESONANCE_KEV = 18.6


def glashow_resonance_energy_pev() -> float:
    e_gev = M_W_GEV**2 / (2.0 * M_E_GEV)
    return e_gev / 1.0e6


def glashow_hadronic_peak_cross_section_cm2() -> float:
    sigma_gev2 = 24.0 * math.pi * BR_W_ENU * BR_W_HAD / (M_W_GEV**2)
    return sigma_gev2 * GEV2_TO_CM2


def li7_be7_line_fractions() -> dict[str, float]:
    event_fraction = LI7_BE7_RATE_SNU / LI7_TOTAL_RATE_SNU
    energy_fraction = LI7_BE7_ENERGY_SNU_MEV / LI7_TOTAL_ENERGY_SNU_MEV
    return {
        "event_fraction": event_fraction,
        "energy_moment_fraction": energy_fraction,
        "event_to_energy_fraction_ratio": event_fraction / energy_fraction,
    }


def g8_positive_control() -> dict[str, object]:
    e_pev = glashow_resonance_energy_pev()
    sigma = glashow_hadronic_peak_cross_section_cm2()
    li7 = li7_be7_line_fractions()
    solar_ceiling_pev = SOLAR_ENERGY_CEILING_MEV / 1.0e9
    return {
        "glashow": {
            "resonance_energy_pev": e_pev,
            "hadronic_peak_cross_section_cm2": sigma,
            "relative_error_to_6p3_pev": abs(e_pev / 6.3 - 1.0),
            "relative_error_to_3p4e31": abs(sigma / 3.4e-31 - 1.0),
            "energy_mismatch_to_20_mev": e_pev / solar_ceiling_pev,
            "cross_scale_ratio_to_xe132_cevns_1mev": sigma / XE132_CEVNS_1MEV_CM2,
            "classification": "G8_REAL_RESONANCE_POSITIVE_CONTROL_PASS / SOLAR_APPLICATION_FAIL_KINEMATICS",
        },
        "li7_be7_narrow_line": {
            **li7,
            "classification": "NARROW_LINE_EVENT_GAIN_NOT_ENERGY_GAIN",
            "note": "Crossed threshold/line overlap, not a Breit-Wigner resonance.",
        },
        "h3_he3_mossbauer_concept": {
            "resonance_energy_kev": H3_HE3_RESONANCE_KEV,
            "idealized_peak_cross_section_cm2": H3_HE3_IDEALIZED_RESONANT_CM2,
            "classification": "THEORY_POSITIVE / MATERIAL_REALIZATION_UNVALIDATED",
        },
        "scope": (
            "Positive controls only. Peak resonance strength is not flux-integrated solar power. "
            "Glashow kinematics, Li7-Be7 line overlap and H3-He3 Mossbauer concepts are distinct channels."
        ),
    }
