import math

from nmir.nuclear_current_loophole import (
    AXIAL_CHARGE_EXCESS_ANCHOR,
    ENU_MAX_MEV,
    M_E_MEV,
    induced_pseudoscalar_electron_scale,
    nuclear_current_loophole_diagnostic,
    one_body_component_scales,
    power_with_amplitude_ratio,
    qmax_zero_threshold_mev,
    required_extra_amplitude_ratio,
)


def test_qmax_zero_threshold_identity():
    assert qmax_zero_threshold_mev() == 2.0 * ENU_MAX_MEV + M_E_MEV


def test_induced_pseudoscalar_scale_is_small_for_electron_channel():
    scale = induced_pseudoscalar_electron_scale()
    assert 0.0 < scale < 1.0e-3


def test_one_body_frozen_ratio_is_conservative_but_order_unity():
    row = one_body_component_scales()
    assert row["frozen_one_body_amplitude_ratio"] > row["raw_omitted_to_leading_amplitude_ratio"]
    assert 1.0 < row["frozen_one_body_amplitude_ratio"] < 3.0


def test_power_amplitude_identity():
    p0 = 2.0
    assert math.isclose(power_with_amplitude_ratio(p0, 3.0), 32.0, rel_tol=0, abs_tol=0)


def test_required_amplitude_inverts_power_identity():
    p0 = 1.0e-8
    r = required_extra_amplitude_ratio(p0, 1.0)
    assert math.isclose(power_with_amplitude_ratio(p0, r), 1.0, rel_tol=1e-12)


def test_one_body_gate_is_strong_negative_scoped():
    out = nuclear_current_loophole_diagnostic()
    assert out["one_body_classification"] == "ONE_BODY_SUBLEADING_STRONG_NEGATIVE_SCOPED"
    assert out["one_body_power_w_per_kg"] < 1.0e-6


def test_two_body_data_distance_passes_preregistered_gap():
    out = nuclear_current_loophole_diagnostic()
    gap = out["bridge_to_anchor_amplitude_gaps"]["axial_charge_excess_0p61"]
    assert AXIAL_CHARGE_EXCESS_ANCHOR == 0.61
    assert gap > 1.0e4
    assert out["two_body_data_classification"] == "TWO_BODY_DATA_DISTANCE_STRONG_NEGATIVE"
    assert out["global_two_body_theorem"] == "OPEN"


def test_even_r1000_amplitude_stress_remains_below_one_watt_per_kg():
    out = nuclear_current_loophole_diagnostic()
    row = out["aggregate_amplitude_stress_rows"]["r_1000"]
    assert row["power_w_per_kg"] < 1.0
    assert row["deficit_to_1_w_per_kg"] > 100.0


def test_bridge_amplitude_is_enormous():
    out = nuclear_current_loophole_diagnostic()
    assert out["required_extra_amplitude_ratio_to_1_w_per_kg"] > 2.0e4
    assert out["required_generic_nlo_dimensionless_coefficient"] > 4.0e4
