from pathlib import Path

from nmir.cevns_be7_profile import (
    cevns_sigma_above_threshold_cm2,
    load_profile,
    profile_fraction_above,
    profile_norm,
    threshold_row,
)

PROFILE = Path("data/be7_bahcall1994_ground_profile.csv")


def test_frozen_profile_is_normalized():
    profile = load_profile(PROFILE)
    assert abs(profile_norm(profile) - 1.0) <= 1e-12


def test_40ev_reproduces_iteration_0041_source_threshold():
    profile = load_profile(PROFILE)
    row = threshold_row(profile, 40.0)
    expected = 0.8628609380456526
    assert abs(row["source_min_energy_mev"] / expected - 1.0) <= 1e-12


def test_40ev_is_true_profile_boundary_not_step_function():
    profile = load_profile(PROFILE)
    row = threshold_row(profile, 40.0)
    assert 0.0 < row["profile_fraction_above_emin"] < 1.0
    assert 0.0 < row["profile_average_above_threshold_sigma_cm2"] < row["profile_average_total_sigma_cm2"]
    assert row["ideal_events_per_kg_day"] > 0.0


def test_threshold_zero_retains_all_cross_section():
    profile = load_profile(PROFILE)
    row = threshold_row(profile, 0.0)
    assert abs(row["retained_cross_section_fraction"] - 1.0) <= 1e-12
    assert row["profile_fraction_above_emin"] == 1.0


def test_rate_and_cross_section_are_monotone_with_threshold():
    profile = load_profile(PROFILE)
    thresholds = [0.0, 10.0, 20.0, 30.0, 35.0, 38.0, 39.0, 40.0]
    rows = [threshold_row(profile, t) for t in thresholds]
    sigmas = [r["profile_average_above_threshold_sigma_cm2"] for r in rows]
    rates = [r["ideal_events_per_kg_day"] for r in rows]
    assert all(b <= a for a, b in zip(sigmas[:-1], sigmas[1:]))
    assert all(b <= a for a, b in zip(rates[:-1], rates[1:]))


def test_cross_section_rejects_unphysical_inputs():
    try:
        cevns_sigma_above_threshold_cm2(0.0, 1.0)
        raise AssertionError("expected ValueError")
    except ValueError:
        pass
    try:
        cevns_sigma_above_threshold_cm2(1.0, -1.0)
        raise AssertionError("expected ValueError")
    except ValueError:
        pass


def test_profile_fraction_limits():
    profile = load_profile(PROFILE)
    assert profile_fraction_above(profile, profile[0][0] - 1.0) == 1.0
    assert profile_fraction_above(profile, profile[-1][0] + 1.0) == 0.0
