import math

from nmir.g9_continuous_projection import (
    _derivative_shell_tspace,
    _ja,
    _jb,
    continuous_focal_distance_au,
    continuous_projected_mass_derivative_g_per_x,
    continuous_projected_mass_g,
)
from nmir.gravity_extended import RadialDensityProfile


def rel(a, b):
    return abs(a - b) / max(abs(a), abs(b), 1e-300)


def stable_uniform_sphere_projected_fraction(x):
    if x == 1.0:
        return 1.0
    return -math.expm1(1.5 * math.log1p(-x * x))


def test_constant_density_matches_uniform_sphere_projection_exactly():
    profile = RadialDensityProfile((0.0, 0.25, 0.7, 1.0), (3.0, 3.0, 3.0, 3.0))
    r = 7.0
    total = 4.0 * math.pi * r**3 * 3.0 / 3.0
    for x in (1e-4, 0.02, 0.17, 0.5, 0.91, 1.0):
        got = continuous_projected_mass_g(profile, x, r)
        want = total * stable_uniform_sphere_projected_fraction(x)
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


def test_endpoint_centered_shell_matches_prior_closed_form_when_well_conditioned():
    x, lo, hi = 0.37, 0.22, 0.81
    rho_lo, rho_hi = 4.2, 0.7
    lower = max(lo, x)
    a = (rho_hi - rho_lo) / (hi - lo)
    b = rho_lo - a * lo
    old = a * (_ja(hi, x) - _ja(lower, x)) + b * (_jb(hi, x) - _jb(lower, x))
    new = _derivative_shell_tspace(x, lo, hi, rho_lo, rho_hi)
    assert rel(old, new) < 2e-14


def test_endpoint_centered_shell_stays_finite_near_surface():
    value = _derivative_shell_tspace(
        0.99999825,
        0.9999965,
        1.0,
        2.0253139e-7,
        1.9979759e-7,
    )
    assert math.isfinite(value) and value > 0.0
