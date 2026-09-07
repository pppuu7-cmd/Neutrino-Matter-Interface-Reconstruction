from scripts.calibrate_esseili_kribs_bbn_axes_0081a import (
    FIT_TOL_DECADE,
    CROSS_TOL_DECADE,
    fit_axis,
    ols,
    transform_difference,
    unique_by_exponent,
)


def test_ols_and_loo_scale_is_well_below_frozen_tolerance_for_exact_log_axis():
    ticks = [{"xc": float(i), "exponent": e} for i, e in enumerate(range(-6, 4))]
    fit = fit_axis(ticks, "xc")
    assert fit["max_abs_residual_decade"] < 1e-12
    assert fit["max_abs_loo_decade"] < 1e-12
    assert fit["max_abs_residual_decade"] <= FIT_TOL_DECADE


def test_duplicate_axis_exponent_fails_unique_recovery():
    expected = list(range(-6, 4))
    candidates = [{"exponent": e, "xc": float(e)} for e in expected]
    candidates.append({"exponent": -3, "xc": 999.0})
    unique, ordered, multiplicity = unique_by_exponent(candidates, expected)
    assert unique is False
    assert multiplicity["-3"] == 2
    assert len(ordered) == 9


def test_cross_panel_difference_detects_transform_shift():
    a = {"a": 0.1, "b": -2.0}
    b = {"a": 0.1, "b": -2.0 + 2 * CROSS_TOL_DECADE}
    diffs = transform_difference(a, b, [1.0, 2.0, 3.0])
    assert max(map(abs, diffs)) > CROSS_TOL_DECADE


def test_ols_rejects_zero_coordinate_variance():
    try:
        ols([1.0, 1.0], [0.0, 1.0])
    except ValueError as exc:
        assert "zero coordinate variance" in str(exc)
    else:
        raise AssertionError("expected zero-variance ValueError")
