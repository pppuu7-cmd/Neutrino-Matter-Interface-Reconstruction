"""Subleading nuclear weak-current diagnostics for NMIR G3.

Part A is a deliberately generous one-body recoil/induced-current cap within
an admitted nucleonic/nonrelativistic sector.  Part B compares the amplitude
needed to bridge the frozen finite-q leading-current power envelope to
literature-calibrated two-body/current correction scales.  The latter is a
data-distance diagnostic, not a universal two-body theorem.
"""

from __future__ import annotations

import math

from .finite_q_multipole_bound import finite_q_leading_multipole_envelope

M_N_MEV = 938.918
M_E_MEV = 0.51099895
M_PI_CHARGED_MEV = 139.57039
G_V = 1.0
G_A = 1.2754
G_M_ANOM_ISOVECTOR = 3.706
ENU_MAX_MEV = 20.0
BETA_NUCLEON_CAP = 1.0
ONE_BODY_COMPONENT_SAFETY = 2.0

# Literature-calibrated amplitude-scale anchors.  These are not universal maxima.
TWO_BODY_TYPICAL_ANCHOR = 0.03
TWO_BODY_SUPPRESSED_GT_ANCHOR = 0.30
AXIAL_CHARGE_EXCESS_ANCHOR = 0.61

# Deliberately extreme amplitude stresses; still not physical bounds.
AGGREGATE_AMPLITUDE_STRESSES = (10.0, 100.0, 1000.0)


def qmax_zero_threshold_mev(enu_max_mev: float = ENU_MAX_MEV) -> float:
    """Conservative zero-threshold |q| cap E_nu + p_e <= 2 E_nu + m_e."""
    if enu_max_mev < 0:
        raise ValueError("enu_max_mev must be non-negative")
    return 2.0 * enu_max_mev + M_E_MEV


def induced_pseudoscalar_electron_scale(
    endpoint_mev: float = ENU_MAX_MEV + M_E_MEV,
) -> float:
    """Electron-channel beta/neutrino scale m_e E0 / m_pi^2."""
    if endpoint_mev < 0:
        raise ValueError("endpoint_mev must be non-negative")
    return M_E_MEV * endpoint_mev / (M_PI_CHARGED_MEV**2)


def one_body_component_scales() -> dict[str, float]:
    """Return frozen triangle-count coefficient scales for LO and omitted 1b pieces."""
    qmax = qmax_zero_threshold_mev()
    leading = G_V + 3.0 * G_A
    axial_charge = G_A * BETA_NUCLEON_CAP
    convection = 3.0 * G_V * BETA_NUCLEON_CAP
    weak_magnetism = 3.0 * (G_V + G_M_ANOM_ISOVECTOR) * qmax / (2.0 * M_N_MEV)
    induced_pseudoscalar = 3.0 * G_A * induced_pseudoscalar_electron_scale()
    omitted = axial_charge + convection + weak_magnetism + induced_pseudoscalar
    raw_ratio = omitted / leading
    frozen_ratio = ONE_BODY_COMPONENT_SAFETY * raw_ratio
    return {
        "qmax_mev": qmax,
        "leading_component_scale": leading,
        "axial_charge_component_scale": axial_charge,
        "convection_component_scale": convection,
        "weak_magnetism_component_scale": weak_magnetism,
        "induced_pseudoscalar_component_scale": induced_pseudoscalar,
        "omitted_component_scale": omitted,
        "raw_omitted_to_leading_amplitude_ratio": raw_ratio,
        "frozen_one_body_amplitude_ratio": frozen_ratio,
    }


def power_with_amplitude_ratio(power_leading_w_per_kg: float, ratio: float) -> float:
    if power_leading_w_per_kg < 0:
        raise ValueError("power_leading_w_per_kg must be non-negative")
    if ratio < 0:
        raise ValueError("ratio must be non-negative")
    return power_leading_w_per_kg * (1.0 + ratio) ** 2


def required_extra_amplitude_ratio(
    power_leading_w_per_kg: float,
    target_w_per_kg: float = 1.0,
) -> float:
    if power_leading_w_per_kg <= 0:
        raise ValueError("power_leading_w_per_kg must be positive")
    if target_w_per_kg <= 0:
        raise ValueError("target_w_per_kg must be positive")
    if power_leading_w_per_kg >= target_w_per_kg:
        return 0.0
    return math.sqrt(target_w_per_kg / power_leading_w_per_kg) - 1.0


def nuclear_current_loophole_diagnostic() -> dict[str, object]:
    baseline = finite_q_leading_multipole_envelope()
    leading_power = float(baseline["finite_q_leading_bound_w_per_kg"])
    scales = one_body_component_scales()
    r_1b = scales["frozen_one_body_amplitude_ratio"]
    one_body_power = power_with_amplitude_ratio(leading_power, r_1b)
    r_bridge = required_extra_amplitude_ratio(leading_power)

    anchors = {
        "two_body_typical_0p03": TWO_BODY_TYPICAL_ANCHOR,
        "two_body_suppressed_gt_0p30": TWO_BODY_SUPPRESSED_GT_ANCHOR,
        "axial_charge_excess_0p61": AXIAL_CHARGE_EXCESS_ANCHOR,
    }
    anchor_gaps = {name: r_bridge / value for name, value in anchors.items()}
    stress_rows = {
        f"r_{int(r)}": {
            "amplitude_ratio": r,
            "power_w_per_kg": power_with_amplitude_ratio(leading_power, r),
            "deficit_to_1_w_per_kg": 1.0 / power_with_amplitude_ratio(leading_power, r),
        }
        for r in AGGREGATE_AMPLITUDE_STRESSES
    }

    one_body_class = (
        "ONE_BODY_SUBLEADING_STRONG_NEGATIVE_SCOPED"
        if one_body_power < 1.0e-6
        else "ONE_BODY_SUBLEADING_NOT_STRONG_NEGATIVE"
    )
    two_body_data_class = (
        "TWO_BODY_DATA_DISTANCE_STRONG_NEGATIVE"
        if anchor_gaps["axial_charge_excess_0p61"] > 1.0e4
        else "TWO_BODY_DATA_DISTANCE_NOT_STRONG_NEGATIVE"
    )

    q_over_lambda = 0.5
    required_nlo_coefficient = r_bridge / q_over_lambda

    return {
        "leading_finite_q_power_w_per_kg": leading_power,
        "one_body_scales": scales,
        "one_body_power_w_per_kg": one_body_power,
        "one_body_deficit_to_1_w_per_kg": 1.0 / one_body_power,
        "one_body_classification": one_body_class,
        "required_extra_amplitude_ratio_to_1_w_per_kg": r_bridge,
        "literature_amplitude_anchors": anchors,
        "bridge_to_anchor_amplitude_gaps": anchor_gaps,
        "two_body_data_classification": two_body_data_class,
        "global_two_body_theorem": "OPEN",
        "aggregate_amplitude_stress_rows": stress_rows,
        "eft_naturalness_q_over_lambda": q_over_lambda,
        "required_generic_nlo_dimensionless_coefficient": required_nlo_coefficient,
        "scope": (
            "Part A: one-body SM recoil/induced currents with p/M<=1 and frozen component safety; "
            "Part B: literature-calibrated two-body/current distance diagnostics only. Genuine universal "
            "two-body/higher-body operator bound, resonances and engineered media remain open."
        ),
    }
