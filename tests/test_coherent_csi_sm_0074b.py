import math
from nmir.coherent_csi_sm_0074b import (
    QF, LIGHT_YIELD_PE_PER_KEVEE, PE_ANALYSIS_MIN, PE_ANALYSIS_MAX_EXCLUSIVE,
    acceptance_at_pe_center, calculate_events, poisson_acceptance,
    recoil_endpoint_gev, inverse_recoil_threshold_gev,
)


def test_recoil_endpoint_inverse_roundtrip():
    for e in (0.005, 0.02, 0.02979, 0.05):
        m = 120.0
        t = recoil_endpoint_gev(e, m)
        assert math.isclose(inverse_recoil_threshold_gev(t, m), e, rel_tol=2e-12, abs_tol=1e-15)


def test_acceptance_step_and_bounds():
    assert acceptance_at_pe_center(0) == 0.0
    assert acceptance_at_pe_center(4) == 0.0
    assert 0.0 < acceptance_at_pe_center(5) < acceptance_at_pe_center(6) < 1.0
    assert PE_ANALYSIS_MIN == 6
    assert PE_ANALYSIS_MAX_EXCLUSIVE == 30


def test_poisson_normalization_tail_independent_of_roi():
    for mu in (0.0, 0.5, 5.0, 20.0, 50.0):
        total, tail = poisson_acceptance(
            mu,
            apply_acceptance=False,
            pe_max_exclusive=160,
            restrict_analysis_window=False,
        )
        assert abs(total + tail - 1.0) < 1e-12
        assert tail <= 1e-8


def test_roi_selection_is_strictly_smaller_than_full_poisson_support():
    roi, _ = poisson_acceptance(30.0, apply_acceptance=False, restrict_analysis_window=True)
    all_pe, _ = poisson_acceptance(30.0, apply_acceptance=False, restrict_analysis_window=False)
    assert 0.0 < roi < all_pe <= 1.0


def test_components_nonnegative_and_refinement():
    coarse = calculate_events(n_t=1000)
    fine = calculate_events(n_t=4000)
    assert all(math.isfinite(v) and v >= 0 for k, v in fine.items() if k != "max_poisson_tail")
    assert abs(fine["total"] - coarse["total"]) / fine["total"] <= 0.005
    assert fine["max_poisson_tail"] <= 1e-8


def test_monotonic_guards():
    base = calculate_events(n_t=1000)
    no_acc = calculate_events(n_t=1000, apply_acceptance=False)
    no_ff = calculate_events(n_t=1000, form_factor=False)
    qf_up = calculate_events(n_t=1000, qf=QF * 1.01)
    ly_up = calculate_events(n_t=1000, light_yield=LIGHT_YIELD_PE_PER_KEVEE * 1.01)
    assert no_acc["total"] >= base["total"]
    assert no_ff["total"] >= base["total"]
    assert qf_up["total"] >= base["total"]
    assert ly_up["total"] >= base["total"]
