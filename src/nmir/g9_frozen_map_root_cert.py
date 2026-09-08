"""Deterministic helpers for NMIR 0089a frozen-map piecewise root certification.

This module contains no Model-S physics and no area/kernel calculation. It only
implements the preregistered sign threshold, fixed probe meshes, sign-changing
root isolation and Q32/Q64 set matching.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Callable, Iterable


class RootCertificationBlocked(RuntimeError):
    pass


@dataclass(frozen=True)
class CertifiedRoot:
    root: float
    lo: float
    hi: float
    orientation: tuple[int, int]


def sign_with_tau(value: float, scale: float) -> int:
    if not math.isfinite(value) or not math.isfinite(scale) or scale <= 0.0:
        raise RootCertificationBlocked("nonfinite derivative/sign scale")
    tau = 2.0e-10 * max(1.0, scale)
    if abs(value) <= tau:
        return 0
    return -1 if value < 0.0 else 1


def base_fractions() -> tuple[float, ...]:
    vals = {j / 32.0 for j in range(1, 32)}
    vals.update((2.0**-16, 2.0**-14, 2.0**-12,
                 1.0-2.0**-12, 1.0-2.0**-14, 1.0-2.0**-16))
    return tuple(sorted(vals))


def stress_fractions() -> tuple[float, ...]:
    vals = set(base_fractions())
    vals.update(j / 64.0 for j in range(1, 64))
    return tuple(sorted(vals))


def stress_mid_fractions() -> tuple[float, ...]:
    return tuple((j + 0.5) / 64.0 for j in range(64))


def bisect_root(fn: Callable[[float], float], lo: float, hi: float,
                width: float = 1.0e-12) -> CertifiedRoot:
    fl, fh = fn(lo), fn(hi)
    if not (math.isfinite(fl) and math.isfinite(fh)) or fl == 0.0 or fh == 0.0 or fl * fh >= 0.0:
        raise RootCertificationBlocked("invalid sign-changing derivative bracket")
    orient = (-1 if fl < 0 else 1, -1 if fh < 0 else 1)
    while hi - lo > width:
        mid = 0.5 * (lo + hi)
        fm = fn(mid)
        if not math.isfinite(fm):
            raise RootCertificationBlocked("nonfinite derivative during bisection")
        if fm == 0.0:
            lo = hi = mid
            break
        if fl * fm < 0.0:
            hi, fh = mid, fm
        else:
            lo, fl = mid, fm
    return CertifiedRoot(0.5 * (lo + hi), lo, hi, orient)


def roots_from_probes(fn: Callable[[float], float], sign_fn: Callable[[float], int],
                      points: Iterable[float]) -> tuple[CertifiedRoot, ...]:
    xs = tuple(sorted(set(points)))
    signs = [sign_fn(x) for x in xs]
    candidate_brackets: list[tuple[float, float]] = []

    for x0, x1, s0, s1 in zip(xs, xs[1:], signs, signs[1:]):
        if s0 != 0 and s1 != 0 and s0 != s1:
            candidate_brackets.append((x0, x1))

    # A preregistered near-zero probe is allowed only when the nearest certified
    # signs on its two sides are opposite, in which case the entire certified
    # bracket is isolated deterministically. Otherwise fail closed.
    for i, s in enumerate(signs):
        if s != 0:
            continue
        left = next((j for j in range(i - 1, -1, -1) if signs[j] != 0), None)
        right = next((j for j in range(i + 1, len(xs)) if signs[j] != 0), None)
        if left is None or right is None or signs[left] == signs[right]:
            raise RootCertificationBlocked("unassociated near-zero derivative probe")
        candidate_brackets.append((xs[left], xs[right]))

    roots: list[CertifiedRoot] = []
    for lo, hi in sorted(set(candidate_brackets)):
        r = bisect_root(fn, lo, hi)
        if roots and abs(r.root - roots[-1].root) <= 1.0e-10:
            if r.orientation != roots[-1].orientation:
                raise RootCertificationBlocked("duplicate near-zero root has inconsistent orientation")
            # Keep the narrower deterministic bracket.
            if (r.hi - r.lo) < (roots[-1].hi - roots[-1].lo):
                roots[-1] = r
        else:
            roots.append(r)

    # Every zero-threshold probe must be uniquely associated with one root.
    for i, s in enumerate(signs):
        if s != 0:
            continue
        left = next(j for j in range(i - 1, -1, -1) if signs[j] != 0)
        right = next(j for j in range(i + 1, len(xs)) if signs[j] != 0)
        contained = [r for r in roots if xs[left] <= r.root <= xs[right]]
        if len(contained) != 1:
            raise RootCertificationBlocked("near-zero probe not uniquely associated with isolated root")

    roots.sort(key=lambda r: r.root)
    return tuple(roots)


def match_root_sets(a: tuple[CertifiedRoot, ...], b: tuple[CertifiedRoot, ...],
                    tol: float = 2.0e-10) -> None:
    if len(a) != len(b):
        raise RootCertificationBlocked("Q32/Q64 root-count mismatch")
    for x, y in zip(a, b):
        if abs(x.root - y.root) > tol or x.orientation != y.orientation:
            raise RootCertificationBlocked("Q32/Q64 root-set mismatch")


__all__ = [
    "RootCertificationBlocked", "CertifiedRoot", "sign_with_tau",
    "base_fractions", "stress_fractions", "stress_mid_fractions",
    "bisect_root", "roots_from_probes", "match_root_sets",
]
