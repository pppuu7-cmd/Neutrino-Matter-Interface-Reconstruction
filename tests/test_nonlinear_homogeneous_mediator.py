import math

import pytest

from nmir.nonlinear_homogeneous_mediator import (
    analytic_per_particle_gain,
    collective_scaling_energy,
    extensive_gamma,
    scalar_equilibrium,
)


@pytest.mark.parametrize("p", [2.0, 3.0, 4.0, 6.0])
def test_euler_energy_identity(p):
    out = scalar_equilibrium(p=p, kappa=1.7, source=2.3)
    scale = max(1.0, abs(out["source_work"]))
    assert abs(out["stationarity_residual"]) / scale < 1e-12
    assert math.isclose(out["induced_to_stored_ratio"], p - 1.0, rel_tol=1e-12, abs_tol=1e-12)
    assert math.isclose(out["work_to_stored_ratio"], p, rel_tol=1e-12, abs_tol=1e-12)


@pytest.mark.parametrize("p", [2.0, 3.0, 4.0, 6.0])
def test_extensive_scaling_has_constant_energy_per_particle(p):
    n1, n2 = 1.0e3, 1.0e6
    gamma = extensive_gamma(p)
    a = collective_scaling_energy(n=n1, p=p, gamma=gamma)
    b = collective_scaling_energy(n=n2, p=p, gamma=gamma)
    assert math.isclose(b["stored_per_particle"] / a["stored_per_particle"], 1.0, rel_tol=1e-12)
    assert math.isclose(b["induced_per_particle"] / a["induced_per_particle"], 1.0, rel_tol=1e-12)


@pytest.mark.parametrize("p", [2.0, 3.0, 4.0, 6.0])
def test_unscaled_collective_source_matches_analytic_superextensive_gain(p):
    n1, n2 = 1.0e3, 1.0e6
    gamma = 0.0
    a = collective_scaling_energy(n=n1, p=p, gamma=gamma)
    b = collective_scaling_energy(n=n2, p=p, gamma=gamma)
    expected = analytic_per_particle_gain(n1=n1, n2=n2, p=p, gamma=gamma)
    assert math.isclose(b["stored_per_particle"] / a["stored_per_particle"], expected, rel_tol=1e-12)
    assert math.isclose(b["induced_per_particle"] / a["induced_per_particle"], expected, rel_tol=1e-12)


def test_harmonic_and_quartic_controls():
    assert extensive_gamma(2.0) == 0.5
    assert extensive_gamma(4.0) == 0.25
    quartic = scalar_equilibrium(p=4.0, kappa=1.0, source=2.0)
    assert math.isclose(quartic["induced_to_stored_ratio"], 3.0, rel_tol=1e-12)


def test_invalid_inputs_fail_closed():
    with pytest.raises(ValueError):
        scalar_equilibrium(p=1.0, kappa=1.0, source=1.0)
    with pytest.raises(ValueError):
        scalar_equilibrium(p=2.0, kappa=0.0, source=1.0)
