import math

from nmir.finite_horizon_mitigation import (
    G0053,
    background_ceiling,
    build_budget,
    equal_factor,
    projection_reduction,
    required_other_rejection,
)


def test_frozen_background_ceiling():
    assert math.isclose(background_ceiling(10.0), 1.0806120114381677, rel_tol=2e-12)


def test_time_branches_and_full_acceptance_identity():
    stress = projection_reduction(3.0 * 365.25)
    assert stress > 100.0
    for time_factor in (100.0, stress):
        expected = G0053 / time_factor
        for restored in (False, True):
            got = required_other_rejection(
                time_factor, 1.0, restore_signal_with_exposure=restored
            )
            assert math.isclose(got, expected, rel_tol=2e-12)


def test_acceptance_penalty_monotone():
    for time_factor in (100.0, projection_reduction(3.0 * 365.25)):
        for restored in (False, True):
            values = [
                required_other_rejection(
                    time_factor, eps, restore_signal_with_exposure=restored
                )
                for eps in (1.0, 0.9, 0.8, 0.7, 0.5, 0.3)
            ]
            assert all(b >= a for a, b in zip(values, values[1:]))


def test_restored_exposure_exact_law():
    for time_factor in (100.0, projection_reduction(3.0 * 365.25)):
        for eps in (1.0, 0.9, 0.8, 0.7, 0.5, 0.3):
            got = required_other_rejection(
                time_factor, eps, restore_signal_with_exposure=True
            )
            assert math.isclose(got, G0053 / (time_factor * eps), rel_tol=2e-12)


def test_equal_factor_reconstructs_requirement():
    requirement = G0053 / 100.0
    for n in (2, 3, 4, 5):
        factor = equal_factor(requirement, n)
        assert math.isclose(factor**n, requirement, rel_tol=2e-12)


def test_budget_is_finite_positive():
    budget = build_budget()
    assert budget["bmax_s10_5sigma_delta30"] > 0
    for scenario in budget["time_scenarios"].values():
        assert scenario["time_reduction"] > 0
        assert scenario["residual_requirement_full_acceptance"] > 0
        assert math.isfinite(scenario["residual_decades_full_acceptance"])
        for row in scenario["acceptance_budget"].values():
            assert row["fixed_exposure"] > 0
            assert row["signal_restored_exposure"] > 0
