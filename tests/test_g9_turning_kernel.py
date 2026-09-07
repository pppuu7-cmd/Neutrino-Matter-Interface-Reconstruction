import math

import pytest

from nmir.g9_turning_kernel import (
    accepted_intervals_monotone,
    cumulative_kernel_point_monotone,
    derivative_surrogate,
    find_turning_points,
    monotone_segments,
    solve_segment_targets,
)
from nmir.g9_global_kernel import signed_map_cm


def linear_focal(b: float) -> float:
    # z=1, R=1 -> y=b-0.2 exactly.
    return b / 0.2


def curved_focal(b: float) -> float:
    # z=1, R=1 -> y=0.01*(b-0.2)*(b-0.5), with one turn at b=0.35.
    y = 0.01 * (b - 0.2) * (b - 0.5)
    return 1.0 / (1.0 - y / b)


def test_derivative_surrogate_linear():
    d = derivative_surrogate(0.3, 1.0, linear_focal, 1.0, (0.01, 0.9))
    assert d == pytest.approx(1.0, rel=2e-9)


def test_turning_point_and_monotone_segments_curved():
    grid = tuple(0.01 + 0.89 * i / 300.0 for i in range(301))
    turns = find_turning_points(1.0, curved_focal, 1.0, grid)
    assert len(turns) == 1
    assert turns[0] == pytest.approx(0.35, abs=2e-7)
    segments = monotone_segments(1.0, curved_focal, 1.0, grid, 0.2)
    assert len(segments) == 3  # generating root additionally partitions the first monotone branch
    assert [s[2] for s in segments] == [-1, -1, 1]


def test_all_zero_targets_are_solved_without_scan_acceptance():
    grid = tuple(0.01 + 0.89 * i / 300.0 for i in range(301))
    segments = monotone_segments(1.0, curved_focal, 1.0, grid, 0.2)
    yfn = lambda b: signed_map_cm(b, 1.0, curved_focal, 1.0)
    roots = solve_segment_targets(segments, (0.0,), yfn)[0.0]
    assert roots == pytest.approx((0.2, 0.5), abs=1e-9)


def test_two_disjoint_preimages_are_recovered():
    grid = tuple(0.01 + 0.89 * i / 300.0 for i in range(301))
    intervals = accepted_intervals_monotone(1.0e-4, 1.0, curved_focal, 1.0, grid, 0.2)
    assert len(intervals) == 2
    assert intervals[0][0] < 0.2 < intervals[0][1]
    assert intervals[1][0] < 0.5 < intervals[1][1]
    area, mu, same = cumulative_kernel_point_monotone(1.0e-4, 1.0, curved_focal, 1.0, grid, 0.2)
    assert same == intervals
    expected = math.pi * sum(hi * hi - lo * lo for lo, hi in intervals)
    assert area == pytest.approx(expected, rel=1e-12)
    assert mu > 0.0


def test_half_derivative_step_keeps_toy_turning_point():
    grid = tuple(0.01 + 0.89 * i / 300.0 for i in range(301))
    t1 = find_turning_points(1.0, curved_focal, 1.0, grid, step_scale=1.0)
    t2 = find_turning_points(1.0, curved_focal, 1.0, grid, step_scale=0.5)
    assert t1 == pytest.approx(t2, abs=2e-7)
