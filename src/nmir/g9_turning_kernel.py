"""Turning-point / monotone-segment radial kernel for NMIR G9 iteration 0077.

The frozen 0077 method uses the scan grid only to bracket turning points of the
continuous signed radial map.  All accepted preimage boundaries are then solved
inside independently audited monotone segments; scan nodes are never used as
accept/reject samples for |y| <= r.
"""
from __future__ import annotations

import math
from typing import Callable, Sequence

from nmir.g9_global_kernel import annular_area_cm2, refine_grid_once, signed_map_cm


def derivative_surrogate(
    b: float,
    observer_au: float,
    focal_distance_au_fn: Callable[[float], float],
    solar_radius_cm: float,
    domain: tuple[float, float],
    step_scale: float = 1.0,
) -> float:
    """Frozen finite-difference derivative surrogate from preregistration 0077."""
    lo, hi = domain
    if not lo <= b <= hi or not 0.0 < step_scale <= 1.0:
        raise ValueError("invalid derivative-surrogate request")
    base_h = max(1.0e-9, 1.0e-5 * b) * step_scale
    left = max(lo, b - base_h)
    right = min(hi, b + base_h)
    if not left < right:
        raise ValueError("collapsed derivative stencil")
    y = lambda x: signed_map_cm(x, observer_au, focal_distance_au_fn, solar_radius_cm)
    if left < b < right:
        return (y(right) - y(left)) / (right - left)
    if b <= lo:
        return (y(right) - y(b)) / (right - b)
    return (y(b) - y(left)) / (b - left)


def _bisect_target(fn: Callable[[float], float], target: float, lo: float, hi: float, iterations: int = 90) -> float:
    flo = fn(lo) - target
    fhi = fn(hi) - target
    if flo == 0.0:
        return lo
    if fhi == 0.0:
        return hi
    if flo * fhi > 0.0:
        raise ValueError("target is not bracketed on monotone segment")
    for _ in range(iterations):
        mid = 0.5 * (lo + hi)
        fm = fn(mid) - target
        if fm == 0.0:
            return mid
        if flo * fm <= 0.0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return 0.5 * (lo + hi)


def _bisect_derivative_zero(
    observer_au: float,
    focal_distance_au_fn: Callable[[float], float],
    solar_radius_cm: float,
    domain: tuple[float, float],
    lo: float,
    hi: float,
    step_scale: float,
    iterations: int = 90,
) -> float:
    d = lambda x: derivative_surrogate(x, observer_au, focal_distance_au_fn, solar_radius_cm, domain, step_scale)
    dlo, dhi = d(lo), d(hi)
    if dlo == 0.0:
        return lo
    if dhi == 0.0:
        return hi
    if dlo * dhi > 0.0:
        raise ValueError("derivative reversal is not bracketed")
    for _ in range(iterations):
        mid = 0.5 * (lo + hi)
        dm = d(mid)
        if dm == 0.0:
            return mid
        if dlo * dm <= 0.0:
            hi, dhi = mid, dm
        else:
            lo, dlo = mid, dm
    return 0.5 * (lo + hi)


def find_turning_points(
    observer_au: float,
    focal_distance_au_fn: Callable[[float], float],
    solar_radius_cm: float,
    scan_grid: Sequence[float],
    step_scale: float = 1.0,
) -> tuple[float, ...]:
    if len(scan_grid) < 2 or any(a >= b for a, b in zip(scan_grid, scan_grid[1:])):
        raise ValueError("scan grid must be strictly increasing")
    domain = (scan_grid[0], scan_grid[-1])
    derivs = [derivative_surrogate(x, observer_au, focal_distance_au_fn, solar_radius_cm, domain, step_scale) for x in scan_grid]
    turns: list[float] = []
    for a, b, da, db in zip(scan_grid, scan_grid[1:], derivs, derivs[1:]):
        if da == 0.0:
            turns.append(a)
        if da * db < 0.0:
            turns.append(_bisect_derivative_zero(observer_au, focal_distance_au_fn, solar_radius_cm, domain, a, b, step_scale))
    if derivs[-1] == 0.0:
        turns.append(scan_grid[-1])
    turns.sort()
    unique: list[float] = []
    for x in turns:
        if domain[0] < x < domain[1] and (not unique or abs(x - unique[-1]) > 1.0e-12):
            unique.append(x)
    return tuple(unique)


def _dedupe_sorted(values: Sequence[float], tol: float = 1.0e-12) -> tuple[float, ...]:
    out: list[float] = []
    for x in sorted(values):
        if not out or abs(x - out[-1]) > tol:
            out.append(x)
    return tuple(out)


def monotone_segments(
    observer_au: float,
    focal_distance_au_fn: Callable[[float], float],
    solar_radius_cm: float,
    scan_grid: Sequence[float],
    generating_root: float,
    step_scale: float = 1.0,
) -> tuple[tuple[float, float, int], ...]:
    domain = (scan_grid[0], scan_grid[-1])
    if not domain[0] <= generating_root <= domain[1]:
        raise ValueError("generating root outside validated domain")
    turns = find_turning_points(observer_au, focal_distance_au_fn, solar_radius_cm, scan_grid, step_scale)
    bounds = _dedupe_sorted((domain[0], domain[1], generating_root, *turns))
    segments: list[tuple[float, float, int]] = []
    for lo, hi in zip(bounds, bounds[1:]):
        if hi - lo <= 1.0e-14:
            continue
        # Nine fixed Chebyshev-like interior controls, independent of scan nodes.
        controls = sorted(0.5 * (lo + hi) + 0.5 * (hi - lo) * math.cos(math.pi * k / 10.0) for k in range(1, 10))
        ds = [derivative_surrogate(x, observer_au, focal_distance_au_fn, solar_radius_cm, domain, step_scale) for x in controls]
        signs = [1 if v > 0.0 else -1 if v < 0.0 else 0 for v in ds]
        nonzero = [s for s in signs if s != 0]
        if len(nonzero) != len(signs) or not nonzero or any(s != nonzero[0] for s in nonzero):
            raise ValueError("unresolved derivative sign reversal in monotonicity audit")
        segments.append((lo, hi, nonzero[0]))
    if not segments:
        raise ValueError("no validated monotone segments")
    return tuple(segments)


def solve_segment_targets(
    segments: Sequence[tuple[float, float, int]],
    targets: Sequence[float],
    yfn: Callable[[float], float],
) -> dict[float, tuple[float, ...]]:
    solved: dict[float, list[float]] = {float(t): [] for t in targets}
    for lo, hi, _ in segments:
        ylo, yhi = yfn(lo), yfn(hi)
        low_y, high_y = min(ylo, yhi), max(ylo, yhi)
        for target in solved:
            if low_y <= target <= high_y:
                solved[target].append(_bisect_target(yfn, target, lo, hi))
    return {t: _dedupe_sorted(xs, 1.0e-11) for t, xs in solved.items()}


def accepted_intervals_monotone(
    output_radius_cm: float,
    observer_au: float,
    focal_distance_au_fn: Callable[[float], float],
    solar_radius_cm: float,
    scan_grid: Sequence[float],
    generating_root: float,
    step_scale: float = 1.0,
) -> tuple[tuple[float, float], ...]:
    if output_radius_cm <= 0.0:
        raise ValueError("output radius must be positive")
    segments = monotone_segments(observer_au, focal_distance_au_fn, solar_radius_cm, scan_grid, generating_root, step_scale)
    yfn = lambda b: signed_map_cm(b, observer_au, focal_distance_au_fn, solar_radius_cm)
    targets = solve_segment_targets(segments, (0.0, output_radius_cm, -output_radius_cm), yfn)
    accepted: list[tuple[float, float]] = []
    for lo, hi, _ in segments:
        nodes = _dedupe_sorted((lo, hi, *(x for xs in targets.values() for x in xs if lo <= x <= hi)), 1.0e-12)
        for a, b in zip(nodes, nodes[1:]):
            if b - a <= 1.0e-14:
                continue
            mid = 0.5 * (a + b)
            if abs(yfn(mid)) <= output_radius_cm:
                if accepted and abs(a - accepted[-1][1]) <= 2.0e-12:
                    accepted[-1] = (accepted[-1][0], b)
                else:
                    accepted.append((a, b))
    return tuple(accepted)


def cumulative_kernel_point_monotone(
    output_radius_cm: float,
    observer_au: float,
    focal_distance_au_fn: Callable[[float], float],
    solar_radius_cm: float,
    scan_grid: Sequence[float],
    generating_root: float,
    step_scale: float = 1.0,
) -> tuple[float, float, tuple[tuple[float, float], ...]]:
    intervals = accepted_intervals_monotone(
        output_radius_cm, observer_au, focal_distance_au_fn, solar_radius_cm,
        scan_grid, generating_root, step_scale,
    )
    area = annular_area_cm2(intervals, solar_radius_cm)
    return area, area / (math.pi * output_radius_cm**2), intervals


__all__ = [
    "accepted_intervals_monotone",
    "cumulative_kernel_point_monotone",
    "derivative_surrogate",
    "find_turning_points",
    "monotone_segments",
    "refine_grid_once",
    "solve_segment_targets",
]
