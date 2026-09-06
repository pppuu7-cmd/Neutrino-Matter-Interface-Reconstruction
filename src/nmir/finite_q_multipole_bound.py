"""Finite-q leading-current multipole envelope for NMIR G3.

This module deliberately reuses the iteration-0024 passive allowed-current
stress domain, then applies the prospectively frozen multipole/kinematic safety
factor.  It does not claim a rigorous bound for recoil/weak-magnetism/axial-
charge/induced-pseudoscalar corrections; those receive a separately labeled
non-theorem millionfold stress diagnostic.
"""

from __future__ import annotations

import math

from .passive_allowed_bound import known_nuclei_allowed_stress_envelope

RAW_ANGULAR_MULTIPOLE_FACTOR = 24.0 * math.pi
FROZEN_MULTIPOLE_SAFETY_FACTOR = 128.0
SUBLEADING_CROSS_SECTION_STRESS = 1.0e6


def finite_q_leading_multipole_envelope() -> dict[str, float | str]:
    allowed = known_nuclei_allowed_stress_envelope()
    allowed_power = float(allowed["analytic_allowed_bound_w_per_kg"])
    if FROZEN_MULTIPOLE_SAFETY_FACTOR <= RAW_ANGULAR_MULTIPOLE_FACTOR:
        raise RuntimeError("frozen multipole safety must exceed 24*pi")
    leading = FROZEN_MULTIPOLE_SAFETY_FACTOR * allowed_power
    stressed = SUBLEADING_CROSS_SECTION_STRESS * leading
    leading_class = (
        "FINITE_Q_LEADING_STRONG_NEGATIVE"
        if leading < 1.0e-6
        else "FINITE_Q_LEADING_NOT_STRONG_NEGATIVE"
    )
    stress_class = (
        "MILLIONFOLD_SUBLEADING_STRESS_NEGATIVE"
        if stressed < 1.0
        else "MILLIONFOLD_SUBLEADING_STRESS_NOT_NEGATIVE"
    )
    return {
        "allowed_0024_analytic_w_per_kg": allowed_power,
        "raw_angular_multipole_factor_24pi": RAW_ANGULAR_MULTIPOLE_FACTOR,
        "frozen_multipole_safety_factor": FROZEN_MULTIPOLE_SAFETY_FACTOR,
        "finite_q_leading_bound_w_per_kg": leading,
        "finite_q_leading_deficit_to_1_w_per_kg": 1.0 / leading,
        "subleading_cross_section_stress_multiplier": SUBLEADING_CROSS_SECTION_STRESS,
        "millionfold_subleading_stress_w_per_kg": stressed,
        "millionfold_subleading_stress_deficit_to_1_w_per_kg": 1.0 / stressed,
        "leading_classification": leading_class,
        "stress_classification": stress_class,
        "scope": "leading finite-q vector-charge plus axial-spin one-body current; subleading-current x1e6 result is diagnostic only",
    }
