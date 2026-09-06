import math

from nmir.finite_q_multipole_bound import (
    FROZEN_MULTIPOLE_SAFETY_FACTOR,
    RAW_ANGULAR_MULTIPOLE_FACTOR,
    SUBLEADING_CROSS_SECTION_STRESS,
    finite_q_leading_multipole_envelope,
)
from nmir.passive_allowed_bound import known_nuclei_allowed_stress_envelope


def test_safety_factor_exceeds_derived_angular_factor():
    assert math.isclose(RAW_ANGULAR_MULTIPOLE_FACTOR, 24.0 * math.pi, rel_tol=1e-15)
    assert FROZEN_MULTIPOLE_SAFETY_FACTOR > RAW_ANGULAR_MULTIPOLE_FACTOR


def test_uses_existing_allowed_envelope():
    allowed = known_nuclei_allowed_stress_envelope()
    result = finite_q_leading_multipole_envelope()
    assert math.isclose(
        float(result["allowed_0024_analytic_w_per_kg"]),
        float(allowed["analytic_allowed_bound_w_per_kg"]),
        rel_tol=1e-15,
    )


def test_leading_envelope_scaling_and_target_coverage():
    result = finite_q_leading_multipole_envelope()
    allowed = float(result["allowed_0024_analytic_w_per_kg"])
    leading = float(result["finite_q_leading_bound_w_per_kg"])
    assert math.isclose(leading / allowed, 128.0, rel_tol=1e-15)
    target_powers = (1.06589117e-21, 2.94006655e-22, 1.03091848e-22, 5.91482818e-23)
    assert all(leading > x for x in target_powers)


def test_classification_thresholds_are_applied_without_adjustment():
    result = finite_q_leading_multipole_envelope()
    leading = float(result["finite_q_leading_bound_w_per_kg"])
    extended = float(result["millionfold_subleading_stress_w_per_kg"])
    assert math.isclose(extended, leading * SUBLEADING_CROSS_SECTION_STRESS, rel_tol=1e-15)
    assert result["leading_classification"] == (
        "FINITE_Q_LEADING_STRONG_NEGATIVE" if leading < 1e-6 else "FINITE_Q_LEADING_NOT_STRONG_NEGATIVE"
    )
    assert result["stress_classification"] == (
        "MILLIONFOLD_SUBLEADING_STRESS_NEGATIVE" if extended < 1.0 else "MILLIONFOLD_SUBLEADING_STRESS_NOT_NEGATIVE"
    )
