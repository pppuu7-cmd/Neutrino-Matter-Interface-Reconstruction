import math

from nmir.time_likelihood import (
    HORIZON_DAYS,
    background_rate_day,
    build_time_likelihood_map,
    evaluate_branch,
    stable_h,
)


def test_stable_h_matches_direct_away_from_zero():
    for x in (1e-3, 0.1, 1.0, 10.0):
        direct = (1.0 + x) * math.log1p(x) - x
        assert math.isclose(stable_h(x), direct, rel_tol=2e-14, abs_tol=1e-16)


def test_frozen_end_reductions():
    auth = background_rate_day(0.0, "authority_capped_900d") / background_rate_day(
        HORIZON_DAYS, "authority_capped_900d"
    )
    stress = background_rate_day(0.0, "stress_3y") / background_rate_day(
        HORIZON_DAYS, "stress_3y"
    )
    assert math.isclose(auth, 100.0, rel_tol=1e-14)
    assert stress > 100.0
    assert math.isclose(stress, 272.27013080779125, rel_tol=2e-14)


def test_time_shape_beats_count_only_but_remains_million_scale():
    for branch in ("authority_capped_900d", "stress_3y"):
        row = evaluate_branch(branch, n=4096)
        assert row["rejection_time_5sigma"] < row["rejection_count_5sigma"]
        assert row["rejection_time_5sigma"] > 1e6
        assert row["time_shape_rejection_advantage"] > 1.0
        assert row["unsuppressed_time_z"] < 0.01


def test_exact_rejection_grid_convergence():
    for branch in ("authority_capped_900d", "stress_3y"):
        coarse = evaluate_branch(branch, n=4096)
        fine = evaluate_branch(branch, n=8192)
        for key in ("rejection_time_5sigma", "rejection_count_5sigma"):
            assert math.isclose(coarse[key], fine[key], rel_tol=1e-8)


def test_fisher_is_local_only_and_matches_unsuppressed_weak_signal():
    for branch in ("authority_capped_900d", "stress_3y"):
        row = evaluate_branch(branch, n=4096)
        assert math.isclose(
            row["fisher_local_q"], row["unsuppressed_time_q"], rel_tol=2e-6
        )


def test_map_finite_positive():
    result = build_time_likelihood_map(n=4096)
    assert result["horizon_days"] == HORIZON_DAYS
    assert result["signal_total"] == 30.0
    for row in result["branches"].values():
        assert all(math.isfinite(value) and value > 0 for value in row.values())
