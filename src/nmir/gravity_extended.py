"""Extended transparent-Sun lens controls for NMIR G9.

This module projects a spherical density profile into the lens plane and computes
small-angle focal distances for ultrarelativistic rays.  It is deliberately
stdlib-only so the hosted validation is reproducible without a numerical stack.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Iterable, Sequence

G_CGS = 6.67430e-8
C_CGS = 2.99792458e10
AU_CM = 1.495978707e13


@dataclass(frozen=True)
class RadialDensityProfile:
    radius_fraction: tuple[float, ...]
    density_g_cm3: tuple[float, ...]

    def __post_init__(self) -> None:
        if len(self.radius_fraction) != len(self.density_g_cm3):
            raise ValueError("radius and density arrays must have equal length")
        if len(self.radius_fraction) < 2:
            raise ValueError("profile needs at least two points")
        if any(r < 0.0 or r > 1.0 for r in self.radius_fraction):
            raise ValueError("radius fractions must lie in [0,1]")
        if any(r1 >= r2 for r1, r2 in zip(self.radius_fraction, self.radius_fraction[1:])):
            raise ValueError("radius fractions must be strictly increasing")
        if any(rho < 0.0 for rho in self.density_g_cm3):
            raise ValueError("density must be non-negative")


def parse_model_s_text(text: str) -> RadialDensityProfile:
    """Parse the pinned Model-S cptrho table and retain 0 <= r/R <= 1.

    Only columns 1 (r/R) and 3 (rho in g/cm^3) are consumed.  The published
    table is ordered surface-to-centre, so rows are sorted before integration.
    A centre point is inserted by constant extrapolation if not explicitly
    present; its contribution vanishes as r^2 and stabilizes quadrature.
    """
    rows: list[tuple[float, float]] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        fields = line.split()
        if len(fields) < 3:
            continue
        try:
            rfrac = float(fields[0])
            rho = float(fields[2])
        except ValueError:
            continue
        if 0.0 <= rfrac <= 1.0 and rho >= 0.0:
            rows.append((rfrac, rho))
    if len(rows) < 2:
        raise ValueError("no usable Model-S density profile found")

    # De-duplicate exact radii deterministically, then sort centre -> surface.
    by_r: dict[float, float] = {}
    for rfrac, rho in rows:
        by_r[rfrac] = rho
    ordered = sorted(by_r.items())
    if ordered[0][0] > 0.0:
        ordered.insert(0, (0.0, ordered[0][1]))
    return RadialDensityProfile(
        tuple(r for r, _ in ordered),
        tuple(rho for _, rho in ordered),
    )


def _interp_density(profile: RadialDensityProfile, rfrac: float) -> float:
    rs = profile.radius_fraction
    ys = profile.density_g_cm3
    if rfrac <= rs[0]:
        return ys[0]
    if rfrac >= rs[-1]:
        return ys[-1]
    lo, hi = 0, len(rs) - 1
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if rs[mid] <= rfrac:
            lo = mid
        else:
            hi = mid
    t = (rfrac - rs[lo]) / (rs[hi] - rs[lo])
    return ys[lo] + t * (ys[hi] - ys[lo])


def _augmented_grid(profile: RadialDensityProfile, split_rfrac: float | None = None) -> list[tuple[float, float]]:
    points = list(zip(profile.radius_fraction, profile.density_g_cm3))
    if split_rfrac is not None and 0.0 < split_rfrac < points[-1][0]:
        if split_rfrac not in profile.radius_fraction:
            points.append((split_rfrac, _interp_density(profile, split_rfrac)))
            points.sort(key=lambda p: p[0])
    return points


def _trapz(points: Sequence[tuple[float, float]]) -> float:
    total = 0.0
    for (x0, y0), (x1, y1) in zip(points, points[1:]):
        total += 0.5 * (y0 + y1) * (x1 - x0)
    return total


def total_mass_g(profile: RadialDensityProfile, radius_cm: float) -> float:
    if radius_cm <= 0.0:
        raise ValueError("radius_cm must be positive")
    integrand = []
    for x, rho in _augmented_grid(profile):
        r = x * radius_cm
        integrand.append((r, 4.0 * math.pi * r * r * rho))
    return _trapz(integrand)


def shell_cylinder_fraction(b_cm: float, r_cm: float) -> float:
    """Fraction of a thin spherical shell projected inside cylinder radius b."""
    if b_cm < 0.0 or r_cm < 0.0:
        raise ValueError("radii must be non-negative")
    if r_cm == 0.0 or r_cm <= b_cm:
        return 1.0
    x = b_cm / r_cm
    # Algebraically stable and clipped for roundoff near x=1.
    return 1.0 - math.sqrt(max(0.0, 1.0 - x * x))


def projected_mass_g(
    profile: RadialDensityProfile,
    b_fraction: float,
    radius_cm: float,
) -> float:
    """Mass inside a lens-plane cylinder of radius b_fraction * radius_cm."""
    if not 0.0 < b_fraction <= 1.0:
        raise ValueError("b_fraction must lie in (0,1]")
    if radius_cm <= 0.0:
        raise ValueError("radius_cm must be positive")
    b_cm = b_fraction * radius_cm
    integrand: list[tuple[float, float]] = []
    for x, rho in _augmented_grid(profile, b_fraction):
        r = x * radius_cm
        frac = shell_cylinder_fraction(b_cm, r)
        integrand.append((r, 4.0 * math.pi * r * r * rho * frac))
    return _trapz(integrand)


def uniform_sphere_projected_fraction(b_fraction: float) -> float:
    if not 0.0 <= b_fraction <= 1.0:
        raise ValueError("b_fraction must lie in [0,1]")
    return 1.0 - (1.0 - b_fraction * b_fraction) ** 1.5


def focal_distance_au_from_projected_mass(
    projected_mass_g_value: float,
    b_fraction: float,
    radius_cm: float,
) -> float:
    if projected_mass_g_value <= 0.0:
        raise ValueError("projected mass must be positive")
    if not 0.0 < b_fraction <= 1.0:
        raise ValueError("b_fraction must lie in (0,1]")
    if radius_cm <= 0.0:
        raise ValueError("radius_cm must be positive")
    b_cm = b_fraction * radius_cm
    focal_cm = b_cm * b_cm * C_CGS * C_CGS / (4.0 * G_CGS * projected_mass_g_value)
    return focal_cm / AU_CM


def focal_distance_au(profile: RadialDensityProfile, b_fraction: float, radius_cm: float) -> float:
    return focal_distance_au_from_projected_mass(
        projected_mass_g(profile, b_fraction, radius_cm), b_fraction, radius_cm
    )


def combined_scan_grid() -> tuple[float, ...]:
    """Frozen dense log+linear impact grid spanning 1e-4 <= b/R <= 1."""
    log_grid = [10.0 ** (-4.0 + 3.0 * i / 1200.0) for i in range(1201)]  # 1e-4 .. 1e-1
    lin_grid = [0.1 + 0.9 * i / 1800.0 for i in range(1801)]
    return tuple(sorted(set(log_grid + lin_grid)))


def scan_focal_profile(
    profile: RadialDensityProfile,
    radius_cm: float,
    b_grid: Iterable[float] | None = None,
) -> list[tuple[float, float, float]]:
    grid = tuple(b_grid) if b_grid is not None else combined_scan_grid()
    result: list[tuple[float, float, float]] = []
    for bfrac in grid:
        mproj = projected_mass_g(profile, bfrac, radius_cm)
        f_au = focal_distance_au_from_projected_mass(mproj, bfrac, radius_cm)
        result.append((bfrac, mproj, f_au))
    return result
