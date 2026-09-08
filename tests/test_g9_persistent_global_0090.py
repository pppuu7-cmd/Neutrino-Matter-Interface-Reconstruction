from __future__ import annotations

import math

from nmir.g9_persistent_global import (
    branch_target_root,
    finite_source_mu,
    transition_points_for_offsets,
)


def test_branch_target_root_increasing_and_decreasing():
    inc = lambda x: 3.0 * x - 1.0
    dec = lambda x: 2.0 - 4.0 * x
    assert abs(branch_target_root(inc, 0.0, 1.0, 0.5) - 0.5) < 2e-12
    assert abs(branch_target_root(dec, 0.0, 1.0, 0.0) - 0.5) < 2e-12
    assert branch_target_root(inc, 0.0, 1.0, 3.0) is None


def test_transition_points_include_receiver_edges():
    y = lambda x: 10.0 * (x - 0.5)
    pts = transition_points_for_offsets(y, ((0.0, 0.5), (0.5, 1.0)), (0.0,), 1.0)
    # |y|=1 occurs at x=.4,.6; branch endpoints are also retained.
    assert any(abs(x - 0.4) < 2e-12 for x in pts)
    assert any(abs(x - 0.6) < 2e-12 for x in pts)
    assert 0.0 in pts and 0.5 in pts and 1.0 in pts


def test_linear_map_point_source_matches_exact_annulus():
    # y = K(x-x0), one monotone branch. For u=0 the accepted interval is exact.
    k = 10.0
    x0 = 0.5
    a = 0.2
    r_sun = 7.0
    y = lambda x: k * (x - x0)
    mu, _ = finite_source_mu(
        y, ((0.0, 1.0),), a, 0.0, 0.0, r_sun,
        n_radial=12, n_azimuth=24, tol=1e-10,
    )
    lo, hi = x0 - a / k, x0 + a / k
    area = math.pi * r_sun**2 * (hi**2 - lo**2)
    expected = 1.0 + area / (math.pi * a**2)
    assert abs(mu - expected) / expected < 1e-9


def test_finite_source_refinement_toy_converges():
    # Smooth global toy with one turn, deliberately nonzero source and offset.
    y = lambda x: 8.0 * ((x - 0.45) ** 2 - 0.04)
    branches = ((0.0, 0.45), (0.45, 1.0))
    args = (y, branches, 0.25, 0.08, 0.03, 5.0)
    m1, _ = finite_source_mu(*args, n_radial=12, n_azimuth=24, tol=1e-9)
    m2, _ = finite_source_mu(*args, n_radial=24, n_azimuth=48, tol=1e-9)
    assert math.isfinite(m1) and math.isfinite(m2) and m1 >= 1.0 and m2 >= 1.0
    assert abs((m1 - 1.0) - (m2 - 1.0)) / max(abs(m1 - 1.0), abs(m2 - 1.0), 1e-15) < 5e-3
