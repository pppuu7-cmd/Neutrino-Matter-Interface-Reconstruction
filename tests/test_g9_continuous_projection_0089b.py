import math

from nmir.g9_continuous_projection import (
    continuous_focal_distance_au,
    continuous_projected_mass_derivative_g_per_x,
    continuous_projected_mass_g,
)
from nmir.gravity_extended import RadialDensityProfile, uniform_sphere_projected_fraction


def rel(a, b):
    return abs(a - b) / max(abs(a), abs(b), 1e-300)


def test_constant_density_matches_uniform_sphere_projection_exactly():
    profile = RadialDensityProfile((0.0, 0.25, 0.7, 1.0), (3.0, 3.0, 3.0, 3.0))
    r = 7.0
    total = 4.0 * math.pi * r**3 * 3.0 / 3.0
    for x in (1e-4, 0.02, 0.17, 0.5, 0.91, 1.0):
        got = continuous_projected_mass_g(profile, x, r)
        want = total * uniform_sphere_projected_fraction(x)
        assert rel(got, want) < 2e-12


def test_continuous_mass_is_monotone_and_positive_for_linear_profile():
    profile = RadialDensityProfile((0.0, 0.2, 0.6, 1.0), (8.0, 5.0, 2.0, 0.2))
    vals = [continuous_projected_mass_g(profile, x, 5.0) for x in (1e-4, 0.01, 0.1, 0.3, 0.7, 0.99, 1.0)]
    assert all(math.isfinite(v) and v > 0 for v in vals)
    assert all(a < b for a, b in zip(vals, vals[1:]))


def test_analytic_mass_derivative_matches_five_point_difference_on_toy_profile():
    profile = RadialDensityProfile((0.0, 0.15, 0.4, 0.75, 1.0), (9.0, 7.0, 4.0, 1.5, 0.3))
    r = 11.0
    for x in (0.03, 0.19, 0.52, 0.83):
        h = 2e-6
        f = lambda t: continuous_projected_mass_g(profile, t, r)
        fd = (-f(x + 2*h) + 8*f(x + h) - 8*f(x - h) + f(x - 2*h)) / (12*h)
        exact = continuous_projected_mass_derivative_g_per_x(profile, x, r)
        assert rel(fd, exact) < 2e-7


def test_derivative_is_finite_at_density_knots_for_continuous_map():
    profile = RadialDensityProfile((0.0, 0.2, 0.55, 1.0), (7.0, 4.0, 1.0, 0.1))
    for x in (0.2, 0.55):
        d = continuous_projected_mass_derivative_g_per_x(profile, x, 3.0)
        assert math.isfinite(d) and d > 0


def test_focal_distance_is_finite_positive():
    profile = RadialDensityProfile((0.0, 0.3, 1.0), (5.0, 2.0, 0.1))
    for x in (1e-4, 0.02, 0.4, 1.0):
        f = continuous_focal_distance_au(profile, x, 6.96e10)
        assert math.isfinite(f) and f > 0
