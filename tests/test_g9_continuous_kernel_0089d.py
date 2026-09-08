from __future__ import annotations

import math

import pytest

from nmir.g9_continuous_kernel import (
    KernelScientificFail,
    accepted_branch_interval,
    annular_area_cm2,
    branch_crossings,
    merge_adjacent_with_parents,
)


def test_one_turn_two_branch_toy():
    # y=(x-0.4)^2-0.04: one certified turn at x=0.4.
    y = lambda x: (x - 0.4) ** 2 - 0.04
    r = 0.01
    intervals = []
    for parent, (lo, hi) in enumerate(((0.0, 0.4), (0.4, 1.0))):
        roots = branch_crossings(y, lo, hi, r)
        iv = accepted_branch_interval(y, lo, hi, r, roots)
        if iv is not None:
            intervals.append((*iv, parent))
    merged = merge_adjacent_with_parents(intervals)
    assert len(merged) == 2
    # exact boundaries solve (x-.4)^2 in [.03,.05]
    expected = [
        (0.4 - math.sqrt(0.05), 0.4 - math.sqrt(0.03)),
        (0.4 + math.sqrt(0.03), 0.4 + math.sqrt(0.05)),
    ]
    for got, exp in zip(merged, expected):
        assert got["lo"] == pytest.approx(exp[0], abs=2e-12)
        assert got["hi"] == pytest.approx(exp[1], abs=2e-12)


def test_tangent_boundary_zero_measure_does_not_duplicate_area():
    y = lambda x: (x - 0.5) ** 2
    intervals = []
    for parent, (lo, hi) in enumerate(((0.0, 0.5), (0.5, 1.0))):
        roots = branch_crossings(y, lo, hi, 0.0)
        iv = accepted_branch_interval(y, lo, hi, 0.0, roots)
        if iv is not None and iv[1] > iv[0]:
            intervals.append((*iv, parent))
    assert intervals == []
    assert annular_area_cm2([], 10.0) == 0.0


def test_adjacent_intervals_merge_but_positive_overlap_fails():
    merged = merge_adjacent_with_parents([(0.1, 0.2, 0), (0.2 + 1e-12, 0.3, 1)])
    assert len(merged) == 1
    assert merged[0]["parents"] == [0, 1]
    with pytest.raises(KernelScientificFail):
        merge_adjacent_with_parents([(0.1, 0.25, 0), (0.2, 0.3, 1)])


def test_narrow_preimage_is_constructed_without_scan():
    y = lambda x: 1e9 * (x - 0.7)
    r = 1.0
    roots = branch_crossings(y, 0.0, 1.0, r)
    iv = accepted_branch_interval(y, 0.0, 1.0, r, roots)
    assert iv is not None
    assert iv[1] - iv[0] == pytest.approx(2e-9, rel=0, abs=2e-12)
