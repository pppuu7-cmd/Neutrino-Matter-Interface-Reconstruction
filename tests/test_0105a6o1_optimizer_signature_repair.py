import numpy as np

from scripts.run_0105a6o1_argon_optimizer_convergence_diagnostic_v2 import grad


def test_grad_accepts_parent_objective_fixed_nc_slot_without_changing_value():
    n = np.array([2.0])
    s = {
        "S": np.array([1.0]),
        "P": np.array([0.0]),
        "D": np.array([0.0]),
        "B": np.array([0.0]),
    }
    theta = [2.0, 497.0, 33.0, 3152.0]
    g4 = grad(theta, n, s, 3152.0)
    g5 = grad(theta, n, s, 3152.0, None)
    assert np.array_equal(g4, g5)
    assert np.allclose(g5, np.zeros(4), atol=1e-12)
