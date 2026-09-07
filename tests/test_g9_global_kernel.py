import math

import pytest

from nmir.g9_global_kernel import (
    accepted_preimage_intervals,
    annular_area_cm2,
    cumulative_kernel_point,
    find_signed_roots,
    refine_grid_once,
    signed_map_cm,
)


def toy_focal(b: float) -> float:
    # With z=1, R=1 and b0=0.2 this gives y=b-b0 exactly.
    return b / 0.2


def test_signed_map_toy_is_linear():
    assert signed_map_cm(0.3, 1.0, toy_focal, 1.0) == pytest.approx(0.1, abs=1e-14)
    assert signed_map_cm(0.1, 1.0, toy_focal, 1.0) == pytest.approx(-0.1, abs=1e-14)


def test_global_preimage_recovers_toy_root_and_interval():
    grid = tuple(i / 100.0 for i in range(1, 101))
    roots = find_signed_roots(1.0, toy_focal, 1.0, grid, explicit_roots=(0.2,))
    assert roots == pytest.approx((0.2,), abs=1e-12)
    intervals = accepted_preimage_intervals(0.03, 1.0, toy_focal, 1.0, grid, roots)
    assert len(intervals) == 1
    assert intervals[0][0] == pytest.approx(0.17, abs=1e-12)
    assert intervals[0][1] == pytest.approx(0.23, abs=1e-12)
    area, mu, _ = cumulative_kernel_point(0.03, 1.0, toy_focal, 1.0, grid, roots)
    expected_area = math.pi * (0.23**2 - 0.17**2)
    assert area == pytest.approx(expected_area, rel=1e-11)
    assert mu == pytest.approx(expected_area / (math.pi * 0.03**2), rel=1e-11)


def test_annular_area_rejects_overlap():
    with pytest.raises(ValueError):
        annular_area_cm2(((0.1, 0.3), (0.2, 0.4)), 1.0)


def test_refine_grid_preserves_endpoints_and_order():
    refined = refine_grid_once((0.1, 0.2, 0.5))
    assert refined == pytest.approx((0.1, 0.15, 0.2, 0.35, 0.5))


def test_bad_geometry_fails_closed():
    with pytest.raises(ValueError):
        signed_map_cm(0.0, 1.0, toy_focal, 1.0)
    with pytest.raises(ValueError):
        accepted_preimage_intervals(0.0, 1.0, toy_focal, 1.0, (0.1, 0.2), (0.2,))
