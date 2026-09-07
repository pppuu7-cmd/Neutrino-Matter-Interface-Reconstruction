"""G9 persistent/known-direction transparent-Sun lens controls (iteration 0075).

The calculation keeps the already validated radial lens map y(b) but replaces the
random-direction duty penalty of 0061 by an explicit finite source disk and transverse
observer-position error.  A deterministic equal-area source quadrature is convolved
with a circular receiver.  The accepted incident annulus is then integrated in b, so
there is no point-caustic divergence.
"""
from __future__ import annotations

import math
from typing import Callable, Sequence

AU_CM = 1.495978707e13
R_SUN_CM = 6.96e10


def point_receiver_azimuth_fraction(image_radius_cm: float, source_offset_cm: float, receiver_radius_cm: float) -> float:
    """Azimuth fraction of a circular image ring accepted by an offset receiver tube."""
    y = abs(image_radius_cm)
    u = abs(source_offset_cm)
    a = receiver_radius_cm
    if a <= 0.0 or y < 0.0 or u < 0.0:
        raise ValueError("invalid radius")
    if y == 0.0:
        return 1.0 if u <= a else 0.0
    if u == 0.0:
        return 1.0 if y <= a else 0.0
    c = (y * y + u * u - a * a) / (2.0 * y * u)
    if c <= -1.0:
        return 1.0
    if c >= 1.0:
        return 0.0
    return math.acos(c) / math.pi


def uniform_disk_offset_samples(source_radius_cm: float, centre_error_cm: float, n_radial: int = 6, n_azimuth: int = 12) -> tuple[float, ...]:
    """Deterministic equal-area samples of |centre_error + source-disk point|."""
    if source_radius_cm < 0.0 or centre_error_cm < 0.0:
        raise ValueError("source radius and error must be non-negative")
    if n_radial <= 0 or n_azimuth <= 0:
        raise ValueError("quadrature counts must be positive")
    if source_radius_cm == 0.0:
        return (centre_error_cm,)
    out = []
    for ir in range(n_radial):
        r = source_radius_cm * math.sqrt((ir + 0.5) / n_radial)
        for ip in range(n_azimuth):
            phi = 2.0 * math.pi * (ip + 0.5) / n_azimuth
            out.append(math.sqrt(max(0.0, centre_error_cm**2 + r**2 + 2.0 * centre_error_cm * r * math.cos(phi))))
    return tuple(out)


def build_local_branch_grid(
    root_b_fraction: float,
    max_image_radius_cm: float,
    focal_distance_au_fn: Callable[[float], float],
    solar_radius_cm: float = R_SUN_CM,
    points_per_decade: int = 24,
) -> tuple[float, tuple[tuple[float, float], ...]]:
    """Sample the real extended-Sun map around one focal ring on a geometric b grid.

    The grid expands independently on each side of the exact focal root until the
    mapped radius safely exceeds the largest blur required by the frozen class map.
    """
    if not 0.0 < root_b_fraction < 1.0 or max_image_radius_cm <= 0.0 or points_per_decade < 8:
        raise ValueError("invalid branch-grid arguments")
    z_au = focal_distance_au_fn(root_b_fraction)

    def y(b: float) -> float:
        f = focal_distance_au_fn(b)
        return abs(b * solar_radius_cm * (1.0 - z_au / f))

    rows: list[tuple[float, float]] = [(root_b_fraction, 0.0)]
    factor = 10.0 ** (1.0 / points_per_decade)
    for direction in (-1.0, 1.0):
        db = 1.0e-14
        last_y = 0.0
        side: list[tuple[float, float]] = []
        for _ in range(600):
            b = root_b_fraction + direction * db
            if not 0.0 < b < 1.0:
                break
            yy = y(b)
            side.append((b, yy))
            # Require enough support beyond the largest source+position+receiver blur.
            if yy >= 1.25 * max_image_radius_cm:
                break
            # The frozen branches are local monotone focal roots.  A turn before the
            # requested support would make the existing model insufficient, not a
            # license to jump to another image after seeing the result.
            if len(side) > 5 and yy < last_y * (1.0 - 1.0e-8):
                raise ValueError("local focal branch turned before requested support")
            last_y = yy
            db *= factor
        else:
            raise ValueError("failed to terminate local branch grid")
        if not side or side[-1][1] < 1.05 * max_image_radius_cm:
            raise ValueError("insufficient local branch support")
        rows.extend(side)
    rows.sort(key=lambda p: p[0])
    return z_au, tuple(rows)


def one_ring_receiver_mu(
    branch_grid: Sequence[tuple[float, float]],
    receiver_radius_cm: float,
    source_radius_cm: float,
    centre_error_cm: float,
    solar_radius_cm: float = R_SUN_CM,
    n_radial: int = 6,
    n_azimuth: int = 12,
) -> float:
    """Return 1 + the finite-source accepted contribution of one resolved focal ring.

    The additive 1 is the unlensed comparison baseline.  The ring term is obtained
    from the incident annulus area averaged over the uniform source disk.  It tends
    to zero as the source/position blur becomes very large, so the total tends to 1.
    """
    if receiver_radius_cm <= 0.0 or source_radius_cm < 0.0 or centre_error_cm < 0.0:
        raise ValueError("invalid physical radius")
    if len(branch_grid) < 3:
        raise ValueError("branch grid too short")
    samples = uniform_disk_offset_samples(source_radius_cm, centre_error_cm, n_radial, n_azimuth)

    def accept(y: float) -> float:
        return sum(point_receiver_azimuth_fraction(y, u, receiver_radius_cm) for u in samples) / len(samples)

    integral = 0.0
    b0, y0 = branch_grid[0]
    p0 = accept(y0)
    for b1, y1 in branch_grid[1:]:
        p1 = accept(y1)
        integral += 0.5 * (b0 * p0 + b1 * p1) * (b1 - b0)
        b0, p0 = b1, p1
    ring_mu = 2.0 * solar_radius_cm**2 * integral / receiver_radius_cm**2
    if ring_mu < -1.0e-10 or not math.isfinite(ring_mu):
        raise AssertionError("non-finite/negative ring contribution")
    return 1.0 + max(0.0, ring_mu)


def perfect_whole_sun_mu_upper(receiver_radius_cm: float, solar_radius_cm: float = R_SUN_CM) -> float:
    """Impossible duty=1 upper ceiling: unlensed baseline plus full solar aperture."""
    if receiver_radius_cm <= 0.0 or solar_radius_cm <= 0.0:
        raise ValueError("radii must be positive")
    return 1.0 + (solar_radius_cm / receiver_radius_cm) ** 2


def large_source_ring_excess_upper(source_radius_cm: float, solar_radius_cm: float = R_SUN_CM) -> float:
    """Aperture-only asymptotic bound proving the finite-source ring excess -> 0."""
    if source_radius_cm <= 0.0 or solar_radius_cm <= 0.0:
        raise ValueError("radii must be positive")
    return (solar_radius_cm / source_radius_cm) ** 2
