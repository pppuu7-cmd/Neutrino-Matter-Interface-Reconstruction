"""Global finite-source convolution primitives for NMIR G9 iteration 0090.

This module contains no solar-model authority and discovers no turning points.
Callers supply an already-certified monotone signed radial map and its branch
boundaries.  The source/offset semantics are inherited from iteration 0075.
"""
from __future__ import annotations

import math
from typing import Callable, Sequence

from .g9_persistent_lens import point_receiver_azimuth_fraction, uniform_disk_offset_samples


class PersistentConvolutionBlocked(RuntimeError):
    pass


class PersistentConvolutionScientificFail(RuntimeError):
    pass


def simpson_fixed(f: Callable[[float], float], a: float, b: float, n: int) -> float:
    if b <= a:
        return 0.0
    if n <= 0 or n % 2:
        raise ValueError("Simpson panel count must be positive and even")
    h = (b - a) / n
    vals = [f(a), f(b)]
    odd = math.fsum(f(a + i * h) for i in range(1, n, 2))
    even = math.fsum(f(a + i * h) for i in range(2, n, 2))
    return h * (vals[0] + vals[1] + 4.0 * odd + 2.0 * even) / 3.0


def converged_simpson(
    f: Callable[[float], float],
    a: float,
    b: float,
    *,
    tol: float = 1e-8,
    start_n: int = 8,
    max_n: int = 4096,
) -> tuple[float, int]:
    """Deterministic successive-composite-Simpson convergence contract."""
    if b <= a:
        return 0.0, 0
    n = start_n
    prev = simpson_fixed(f, a, b, n)
    while n < max_n:
        n *= 2
        cur = simpson_fixed(f, a, b, n)
        if abs(cur - prev) <= max(tol, tol * abs(cur)):
            return cur, n
        prev = cur
    raise PersistentConvolutionBlocked("composite Simpson convergence exhausted")


def branch_target_root(
    yfn: Callable[[float], float],
    lo: float,
    hi: float,
    target: float,
    *,
    width: float = 1e-12,
) -> float | None:
    """Invert one certified monotone signed branch when target is in its range."""
    yl, yh = yfn(lo), yfn(hi)
    if not (math.isfinite(yl) and math.isfinite(yh)) or yl == yh:
        raise PersistentConvolutionBlocked("invalid certified branch endpoint map")
    low, high = min(yl, yh), max(yl, yh)
    if target < low or target > high:
        return None
    if target == yl:
        return lo
    if target == yh:
        return hi
    increasing = yh > yl
    left, right = lo, hi
    for _ in range(256):
        if right - left <= width:
            return 0.5 * (left + right)
        mid = 0.5 * (left + right)
        ym = yfn(mid)
        if not math.isfinite(ym):
            raise PersistentConvolutionBlocked("nonfinite branch inversion value")
        if (ym < target) == increasing:
            left = mid
        else:
            right = mid
    raise PersistentConvolutionBlocked("branch inversion iteration exhausted")


def transition_points_for_offsets(
    yfn: Callable[[float], float],
    branches: Sequence[tuple[float, float]],
    offsets_cm: Sequence[float],
    receiver_radius_cm: float,
) -> tuple[float, ...]:
    """All frozen f_phi piece-transition b values for one source quadrature."""
    a = float(receiver_radius_cm)
    if a <= 0.0:
        raise ValueError("receiver radius must be positive")
    levels = sorted(set([abs(float(u) - a) for u in offsets_cm] + [float(u) + a for u in offsets_cm]))
    points: list[float] = []
    for lo, hi in branches:
        points.extend((lo, hi))
        for level in levels:
            for target in (-level, level):
                root = branch_target_root(yfn, lo, hi, target)
                if root is not None and lo < root < hi:
                    points.append(root)
    points.sort()
    unique: list[float] = []
    for x in points:
        if not unique or abs(x - unique[-1]) > 2e-13:
            unique.append(x)
    return tuple(unique)


def accepted_area_for_offsets(
    yfn: Callable[[float], float],
    branches: Sequence[tuple[float, float]],
    offsets_cm: Sequence[float],
    receiver_radius_cm: float,
    solar_radius_cm: float,
    *,
    tol: float = 1e-8,
    max_n: int = 4096,
) -> tuple[float, dict]:
    """Average accepted incident annular area over deterministic source samples."""
    if not offsets_cm:
        raise ValueError("offset sample set is empty")
    a = float(receiver_radius_cm)
    r_sun = float(solar_radius_cm)
    points = transition_points_for_offsets(yfn, branches, offsets_cm, a)
    point_source = all(float(u) == 0.0 for u in offsets_cm)
    total_integral = 0.0
    max_panels = 0
    subintervals = 0
    branch_terms = [0.0 for _ in branches]

    def accept(x: float) -> float:
        y = abs(yfn(x))
        return math.fsum(point_receiver_azimuth_fraction(y, u, a) for u in offsets_cm) / len(offsets_cm)

    for bi, (blo, bhi) in enumerate(branches):
        local = [x for x in points if blo <= x <= bhi]
        if not local or local[0] != blo:
            local.insert(0, blo)
        if local[-1] != bhi:
            local.append(bhi)
        local = sorted(set(local))
        for left, right in zip(local, local[1:]):
            if right <= left:
                continue
            if point_source:
                # For u=0, f_phi is exactly the indicator |y|<=a.  The
                # transition splitter already put every |y|=a root on an
                # interval boundary, so the midpoint classifies the entire
                # open subinterval and its x dx integral is analytic.  This
                # avoids asking Simpson to converge across an endpoint jump;
                # it changes no frozen 0090 physics or tolerance.
                inside = abs(yfn(0.5 * (left + right))) <= a
                val = 0.5 * (right * right - left * left) if inside else 0.0
                panels = 0
            else:
                # 2*pi*R^2*x dx is applied outside the normalized Simpson integral.
                val, panels = converged_simpson(lambda x: x * accept(x), left, right, tol=tol, max_n=max_n)
            if val < -1e-18 or not math.isfinite(val):
                raise PersistentConvolutionScientificFail("negative/nonfinite accepted integral")
            val = max(0.0, val)
            branch_terms[bi] += val
            total_integral += val
            max_panels = max(max_panels, panels)
            subintervals += 1
    area = 2.0 * math.pi * r_sun**2 * total_integral
    if not math.isfinite(area) or area < 0.0 or area > math.pi * r_sun**2 * (1.0 + 1e-10):
        raise PersistentConvolutionScientificFail("accepted-area aperture invariant failed")
    return area, {
        "transition_point_count": len(points),
        "subinterval_count": subintervals,
        "max_simpson_panels": max_panels,
        "branch_integrals": branch_terms,
    }


def finite_source_mu(
    yfn: Callable[[float], float],
    branches: Sequence[tuple[float, float]],
    receiver_radius_cm: float,
    source_radius_cm: float,
    centre_error_cm: float,
    solar_radius_cm: float,
    *,
    n_radial: int,
    n_azimuth: int,
    tol: float = 1e-8,
    max_n: int = 4096,
) -> tuple[float, dict]:
    offsets = uniform_disk_offset_samples(source_radius_cm, centre_error_cm, n_radial, n_azimuth)
    area, diag = accepted_area_for_offsets(
        yfn, branches, offsets, receiver_radius_cm, solar_radius_cm, tol=tol, max_n=max_n
    )
    mu = 1.0 + area / (math.pi * receiver_radius_cm**2)
    if not math.isfinite(mu) or mu < 1.0:
        raise PersistentConvolutionScientificFail("invalid magnification")
    diag = dict(diag)
    diag["accepted_area_cm2"] = area
    diag["source_sample_count"] = len(offsets)
    return mu, diag


__all__ = [
    "PersistentConvolutionBlocked",
    "PersistentConvolutionScientificFail",
    "simpson_fixed",
    "converged_simpson",
    "branch_target_root",
    "transition_points_for_offsets",
    "accepted_area_for_offsets",
    "finite_source_mu",
]
