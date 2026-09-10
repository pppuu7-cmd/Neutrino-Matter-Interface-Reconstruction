import inspect

import mpmath as mp

import scripts.run_0105a6o2_argon_strict_convexity_high_precision_certificate as m


def test_frozen_prereg_and_amendment_ids():
    assert m.PREREG_COMMIT == "07a61181b7fb2b8f7041250c3b9bf1de1aeee0e4"
    assert m.AMENDMENT_COMMIT == "29c529ccdf1c4d586367e0dd1f7822e1e6999291"


def test_simple_objective_gradient_stationarity_and_positive_hessian():
    mp.mp.dps = 50
    n = [mp.mpf("2")]
    shapes = {
        "S": [mp.mpf("1")],
        "P": [mp.mpf("0")],
        "D": [mp.mpf("0")],
        "B": [mp.mpf("0")],
    }
    theta = mp.matrix([mp.mpf("2"), mp.mpf("497"), mp.mpf("33"), mp.mpf("3152")])
    _, gradient, hessian = m.qgh(theta, n, shapes, mp.mpf("3152"))
    assert m.infinity_norm(gradient) == 0
    assert all(value > 0 for value in m.leading_principal_minors(hessian))


def test_strict_convexity_algebra_used_not_sampled_grid():
    source = inspect.getsource(m.load_exact)
    assert "positive_count_positive_signal_overlap_bins" in source
    assert "algebraic_strict_convexity_certified" in source


def test_precision_levels_and_thresholds_are_frozen_in_code():
    source = inspect.getsource(m.execute)
    assert '80, "1e-50"' in source
    assert '200, "1e-80"' in source
    assert 'mp.mpf("1e-60")' in source
    assert 'mp.mpf("1e-40")' in source
    assert 'mp.mpf("1e-70")' in source


def test_no_publication_systematic_or_bsm_permission_is_granted():
    source = inspect.getsource(m.execute)
    assert '"publication_target_classification_performed": False' in source
    assert '"systematic_excursion_execution_performed": False' in source
    assert '"observed_bsm_residual_permission_percent": 0' in source
    assert '"observed_bsm_residual_inspected": False' in source
