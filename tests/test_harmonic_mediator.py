import pytest

from nmir.harmonic_mediator import (
    completed_square_hamiltonian,
    effective_pair_scale,
    field_energy_at_minimum,
    induced_energy_magnitude,
    mediator_hamiltonian,
    minimizing_displacement,
    per_particle_energy_gain,
)


def test_completion_of_square_identity():
    args = dict(n=1234.0, o=0.4, g0=1.2, gamma=0.37, kappa=2.3)
    x = 7.1
    direct = mediator_hamiltonian(x=x, **args)
    completed = completed_square_hamiltonian(x=x, **args)
    assert abs(direct - completed) / max(abs(direct), 1e-300) <= 1e-15


def test_field_and_induced_energy_match_at_minimum():
    args = dict(n=1e5, o=0.5, g0=2.0, gamma=0.5, kappa=3.0)
    field = field_energy_at_minimum(**args)
    induced = induced_energy_magnitude(**args)
    assert abs(field / induced - 1.0) <= 1e-15
    x = minimizing_displacement(**args)
    assert mediator_hamiltonian(x=x, **args) == pytest.approx(-induced)


@pytest.mark.parametrize("gamma", [0.0, 0.25, 0.5, 0.75])
def test_per_particle_scaling(gamma):
    n1, n2 = 1e3, 1e6
    e1 = induced_energy_magnitude(n1, 0.5, 1.0, gamma, 2.0) / n1
    e2 = induced_energy_magnitude(n2, 0.5, 1.0, gamma, 2.0) / n2
    assert e2 / e1 == pytest.approx(per_particle_energy_gain(n1, n2, gamma), rel=1e-12)


def test_dicke_scaling_pair_coefficient_is_inverse_n():
    n1, n2 = 1e3, 1e6
    j1 = effective_pair_scale(n1, 1.0, 0.5, 2.0)
    j2 = effective_pair_scale(n2, 1.0, 0.5, 2.0)
    assert j2 / j1 == pytest.approx(n1 / n2, rel=1e-12)
