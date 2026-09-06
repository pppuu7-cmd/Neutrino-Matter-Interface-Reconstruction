import math

import pytest

from nmir.gravity_extended import (
    RadialDensityProfile,
    focal_distance_au_from_projected_mass,
    parse_model_s_text,
    projected_mass_g,
    shell_cylinder_fraction,
    total_mass_g,
    uniform_sphere_projected_fraction,
)


def uniform_profile(n: int = 12001, rho: float = 3.0) -> RadialDensityProfile:
    rs = tuple(i / (n - 1) for i in range(n))
    return RadialDensityProfile(rs, tuple(rho for _ in rs))


def test_parse_model_s_orders_and_inserts_center():
    text = """
# r/R c rho ...
 1.0001 1.0 1e-9 0 0 0
 0.8 1.0 0.2 0 0 0
 0.2 1.0 5.0 0 0 0
"""
    p = parse_model_s_text(text)
    assert p.radius_fraction == (0.0, 0.2, 0.8)
    assert p.density_g_cm3[0] == 5.0


def test_uniform_sphere_total_mass():
    p = uniform_profile()
    radius = 2.0e10
    rho = p.density_g_cm3[0]
    numeric = total_mass_g(p, radius)
    exact = 4.0 * math.pi * radius**3 * rho / 3.0
    assert abs(numeric / exact - 1.0) < 2e-8


@pytest.mark.parametrize("bfrac", [0.01, 0.024, 0.05, 0.2, 0.5, 0.9])
def test_uniform_sphere_projected_mass(bfrac):
    p = uniform_profile()
    radius = 1.0e10
    total = total_mass_g(p, radius)
    numeric_fraction = projected_mass_g(p, bfrac, radius) / total
    exact_fraction = uniform_sphere_projected_fraction(bfrac)
    rel = abs(numeric_fraction / exact_fraction - 1.0)
    assert rel <= 2e-3


def test_shell_fraction_and_focal_input_guards():
    assert shell_cylinder_fraction(2.0, 1.0) == 1.0
    assert 0.0 < shell_cylinder_fraction(1.0, 2.0) < 1.0
    with pytest.raises(ValueError):
        focal_distance_au_from_projected_mass(0.0, 0.1, 1.0)
    with pytest.raises(ValueError):
        projected_mass_g(uniform_profile(20), 0.0, 1.0)
