"""Global radial preimage kernel for the transparent-Sun G9 lens (iteration 0076).

Unlike the local one-ring helper used by 0061/0075, this module never continues a
monotone branch through a turn.  It scans the full validated impact-parameter domain,
refines every detected signed-map zero, inserts those roots explicitly, then solves the
set |y(b)| <= r as disjoint b intervals.  Each interval is integrated once by annular
area, so multiple images/turns are handled without semantic relabeling or double count.
"""
from __future__ import annotations

import math
from typing import Callable, Sequence


def signed_map_cm(
    b_fraction: float,
    observer_au: float,
    focal_distance_au_fn: Callable[[float], float],
    solar_radius_cm: float,
) -> float:
    if not 0.0 < b_fraction <= 1.0 or observer_au <= 0.0 or solar_radius_cm <= 0.0:
        raise ValueError("invalid lens geometry")
    f = focal_distance_au_fn(b_fraction)
    if f <= 0.0:
        raise ValueError("non-positive focal distance")
    return b_fraction * solar_radius_cm * (1.0 - observer_au / f)


def _bisect_zero(fn: Callable[[float], float], lo: float, hi: float, iterations: int = 70) -> float:
    flo, fhi = fn(lo), fn(hi)
    if flo == 0.0:
        return lo
    if fhi == 0.0:
        return hi
    if flo * fhi > 0.0:
        raise ValueError("root is not bracketed")
    for _ in range(iterations):
        mid = 0.5 * (lo + hi)
        fm = fn(mid)
        if fm == 0.0:
            return mid
        if flo * fm <= 0.0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return 0.5 * (lo + hi)


def refine_grid_once(grid: Sequence[float]) -> tuple[float, ...]:
    if len(grid) < 2:
        raise ValueError("grid too short")
    out = [grid[0]]
    for a, b in zip(grid, grid[1:]):
        if not a < b:
            raise ValueError("grid must be strictly increasing")
        out.extend((0.5 * (a + b), b))
    return tuple(out)


def find_signed_roots(
    observer_au: float,
    focal_distance_au_fn: Callable[[float], float],
    solar_radius_cm: float,
    scan_grid: Sequence[float],
    explicit_roots: Sequence[float] = (),
) -> tuple[float, ...]:
    """Find all sign-change roots and merge preregistered generating roots."""
    if len(scan_grid) < 2:
        raise ValueError("scan grid too short")
    fn = lambda b: signed_map_cm(b, observer_au, focal_distance_au_fn, solar_radius_cm)
    vals = [fn(b) for b in scan_grid]
    roots: list[float] = []
    for a, b, fa, fb in zip(scan_grid, scan_grid[1:], vals, vals[1:]):
        if fa == 0.0:
            roots.append(a)
        if fa * fb < 0.0:
            roots.append(_bisect_zero(fn, a, b))
    if vals[-1] == 0.0:
        roots.append(scan_grid[-1])
    for root in explicit_roots:
        if not scan_grid[0] <= root <= scan_grid[-1]:
            raise ValueError("explicit root outside validated domain")
        # Explicit roots are authority controls only if they truly map to zero.
        if abs(fn(root)) > 1.0e-5:
            raise ValueError("explicit root does not map to observer axis")
        roots.append(root)
    roots.sort()
    unique: list[float] = []
    for root in roots:
        if not unique or abs(root - unique[-1]) > 1.0e-11:
            unique.append(root)
    return tuple(unique)


def accepted_preimage_intervals(
    output_radius_cm: float,
    observer_au: float,
    focal_distance_au_fn: Callable[[float], float],
    solar_radius_cm: float,
    scan_grid: Sequence[float],
    signed_roots: Sequence[float],
) -> tuple[tuple[float, float], ...]:
    """Return disjoint b/R intervals satisfying |y(b)| <= output_radius_cm."""
    if output_radius_cm <= 0.0:
        raise ValueError("output radius must be positive")
    lo_domain, hi_domain = scan_grid[0], scan_grid[-1]
    yfn = lambda b: signed_map_cm(b, observer_au, focal_distance_au_fn, solar_radius_cm)
    hfn = lambda b: abs(yfn(b)) - output_radius_cm

    # Explicit zero roots force a negative h node inside every narrow caustic interval.
    nodes = sorted(set(tuple(scan_grid) + tuple(signed_roots)))
    vals = [hfn(b) for b in nodes]
    crossings: list[float] = []
    for a, b, fa, fb in zip(nodes, nodes[1:], vals, vals[1:]):
        if fa == 0.0:
            crossings.append(a)
        if fa * fb < 0.0:
            crossings.append(_bisect_zero(hfn, a, b))
    if vals[-1] == 0.0:
        crossings.append(nodes[-1])

    boundaries = sorted(set((lo_domain, hi_domain) + tuple(crossings) + tuple(signed_roots)))
    accepted: list[tuple[float, float]] = []
    for a, b in zip(boundaries, boundaries[1:]):
        if b <= a:
            continue
        mid = 0.5 * (a + b)
        if hfn(mid) <= 0.0:
            if accepted and abs(a - accepted[-1][1]) <= 2e-14:
                accepted[-1] = (accepted[-1][0], b)
            else:
                accepted.append((a, b))
    return tuple(accepted)


def annular_area_cm2(intervals: Sequence[tuple[float, float]], solar_radius_cm: float) -> float:
    if solar_radius_cm <= 0.0:
        raise ValueError("solar radius must be positive")
    total = 0.0
    last_hi = -1.0
    for lo, hi in sorted(intervals):
        if not 0.0 <= lo < hi <= 1.0:
            raise ValueError("invalid impact interval")
        if lo < last_hi - 1e-14:
            raise ValueError("overlapping impact intervals would double count")
        total += math.pi * solar_radius_cm**2 * (hi * hi - lo * lo)
        last_hi = hi
    return total


def cumulative_kernel_point(
    output_radius_cm: float,
    observer_au: float,
    focal_distance_au_fn: Callable[[float], float],
    solar_radius_cm: float,
    scan_grid: Sequence[float],
    signed_roots: Sequence[float],
) -> tuple[float, float, tuple[tuple[float, float], ...]]:
    intervals = accepted_preimage_intervals(
        output_radius_cm, observer_au, focal_distance_au_fn, solar_radius_cm, scan_grid, signed_roots
    )
    area = annular_area_cm2(intervals, solar_radius_cm)
    receiver_area = math.pi * output_radius_cm**2
    return area, area / receiver_area, intervals
