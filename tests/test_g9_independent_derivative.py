import math

import pytest

from nmir.g9_independent_derivative import (
    adaptive_simpson,
    continuous_mass_and_derivative,
    fixed_dyadic_points,
    isolate_sign_roots,
)
from nmir.gravity_extended import RadialDensityProfile


def test_adaptive_simpson_polynomial():
    got = adaptive_simpson(lambda x: x**4, 0.0, 1.0)
    assert got == pytest.approx(0.2, rel=1e-11, abs=1e-12)


def test_uniform_sphere_projection_and_derivative():
    p = RadialDensityProfile((0.0, 1.0), (1.0, 1.0))
    x = 0.37
    mass, dmass = continuous_mass_and_derivative(p, x, 1.0)
    expected_mass = 4.0 * math.pi / 3.0 * (1.0 - (1.0 - x*x)**1.5)
    expected_derivative = 4.0 * math.pi * x * math.sqrt(1.0 - x*x)
    assert mass == pytest.approx(expected_mass, rel=2e-9)
    assert dmass == pytest.approx(expected_derivative, rel=2e-9)


def test_known_multi_turn_root_set():
    grid = tuple((i + 0.37) / 100.0 for i in range(100))
    fn = lambda x: (x - 0.2) * (x - 0.5) * (x - 0.8)
    roots = isolate_sign_roots(fn, grid)
    assert [r.root for r in roots] == pytest.approx([0.2, 0.5, 0.8], abs=1e-11)


def test_fixed_dyadic_mesh_is_result_independent():
    grid = (0.0, 1.0, 2.0)
    pts = fixed_dyadic_points(grid, 0.25, 1.25)
    assert pts == pytest.approx((0.375, 0.5, 0.625, 0.75, 0.875, 1.125))
