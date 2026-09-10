import inspect

import mpmath as mp

import scripts.run_0105a6o3_argon_certified_central_null_reproduction as m


def test_original_publication_thresholds_are_unchanged():
    assert m.ORIGINAL_A6O_PREREG_COMMIT == "a94cbdf5a65618545bd4b1fb4f9fd6c120ae340e"
    assert m.PUB_TARGETS["NC"] == (mp.mpf("159"), mp.mpf("2.0"))
    assert m.PUB_TARGETS["NP"] == (mp.mpf("553"), mp.mpf("3.0"))
    assert m.PUB_TARGETS["ND"] == (mp.mpf("10"), mp.mpf("3.0"))
    assert m.PUB_TARGETS["NB"] == (mp.mpf("3131"), mp.mpf("3.0"))
    assert m.PUB_TARGETS["sigma_profile"] == (mp.mpf("43"), mp.mpf("2.0"))
    assert m.PUB_TARGETS["Z_stat"] == (mp.mpf("3.9"), mp.mpf("0.15"))


def test_original_dual_anchor_thresholds_are_unchanged():
    assert m.ROBUSTNESS == {
        "NC": mp.mpf("1.0"),
        "NP": mp.mpf("1.0"),
        "ND": mp.mpf("1.0"),
        "Z_stat": mp.mpf("0.05"),
        "sigma_profile": mp.mpf("0.5"),
    }


def test_simple_profile_gradient_stationarity():
    mp.mp.dps = 50
    rows = [(mp.mpf("2"), mp.mpf("1"), mp.mpf("0"), mp.mpf("0"), mp.mpf("0"))]
    Q, g, H = m.profile_qgh([mp.mpf("497"), mp.mpf("33"), mp.mpf("3152")], mp.mpf("2"), rows, mp.mpf("3152"))
    assert Q is not None
    assert m.inf_norm(g) == 0
    assert all(value > 0 for value in m.principal_minors_3(H))


def test_profile_solver_is_frozen_to_100_digit_newton_and_1e_minus_50_gradient():
    source = inspect.getsource(m.solve_profile)
    parent = inspect.getsource(m.load_exact)
    assert "mp.mp.dps = 100" in parent
    assert 'mp.mpf("1e-50")' in source
    assert "range(81)" in source
    assert "range(201)" in source


def test_residual_permission_remains_zero():
    source = inspect.getsource(m.execute)
    assert '"observed_bsm_residual_permission_percent": 0' in source
    assert '"observed_bsm_residual_inspected": False' in source
    assert '"tierA_exact_collaboration_internal_likelihood": "BLOCKED"' in source
