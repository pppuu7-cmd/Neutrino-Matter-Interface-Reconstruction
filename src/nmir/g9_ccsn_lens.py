"""G9 distant-CCSN transparent-Sun lens utility controls.

The scientific distinction in this module is deliberate:
1. a local annular receiver calculation demonstrates a real, finite receiver-integrated
   magnification around a validated extended-Sun focal ring;
2. a separate whole-solar-disk perfect-collection ceiling bounds occurrence-weighted
   utility without relying on the detailed caustic strength.

The ceiling is intentionally impossible/optimistic: every neutrino crossing the full
solar disk is granted perfect redirection into the receiver.  If even that aperture
ceiling fails the preregistered duty-weighted utility threshold, the physical lens fails it.
"""

from __future__ import annotations

import math
from typing import Callable

AU_CM = 1.495978707e13
KPC_CM = 3.0856775814913673e21
R_SUN_CM = 6.96e10


def all_flavour_totals(
    n_nue: float,
    n_anue: float,
    n_nux_per_species: float,
    e_nue_erg: float,
    e_anue_erg: float,
    e_nux_per_species_erg: float,
) -> tuple[float, float]:
    """Return all-flavour N and energy, with four heavy-lepton species."""
    if min(n_nue, n_anue, n_nux_per_species, e_nue_erg, e_anue_erg, e_nux_per_species_erg) < 0:
        raise ValueError("emission totals must be non-negative")
    return (
        n_nue + n_anue + 4.0 * n_nux_per_species,
        e_nue_erg + e_anue_erg + 4.0 * e_nux_per_species_erg,
    )


def isotropic_fluence(total_number: float, distance_kpc: float) -> float:
    if total_number < 0.0 or distance_kpc <= 0.0:
        raise ValueError("invalid total_number or distance")
    d_cm = distance_kpc * KPC_CM
    return total_number / (4.0 * math.pi * d_cm * d_cm)


def source_angular_radius_rad(source_radius_km: float, distance_kpc: float) -> float:
    if source_radius_km < 0.0 or distance_kpc <= 0.0:
        raise ValueError("invalid source size or distance")
    return source_radius_km * 1.0e5 / (distance_kpc * KPC_CM)


def source_footprint_cm(source_radius_km: float, distance_kpc: float, observer_au: float) -> float:
    return source_angular_radius_rad(source_radius_km, distance_kpc) * observer_au * AU_CM


def exact_cap_probability(theta_rad: float) -> float:
    """Isotropic random-direction probability inside an angular cap."""
    if not 0.0 <= theta_rad <= math.pi:
        raise ValueError("theta must lie in [0,pi]")
    return 0.5 * (1.0 - math.cos(theta_rad))


def stable_small_cap_probability(theta_rad: float) -> float:
    """Numerically stable equivalent of (1-cos(theta))/2."""
    if not 0.0 <= theta_rad <= math.pi:
        raise ValueError("theta must lie in [0,pi]")
    return math.sin(0.5 * theta_rad) ** 2


def perfect_solar_aperture_mu_ceiling(receiver_radius_cm: float, solar_radius_cm: float = R_SUN_CM) -> float:
    """Impossible best-case instantaneous magnification from full solar-disk collection."""
    if receiver_radius_cm <= 0.0 or solar_radius_cm <= 0.0:
        raise ValueError("radii must be positive")
    return (solar_radius_cm / receiver_radius_cm) ** 2


def alignment_theta_upper_rad(
    receiver_radius_cm: float,
    source_footprint_cm_value: float,
    observer_au: float,
) -> float:
    """Optimistic centre-alignment tolerance granting any source/receiver overlap."""
    if receiver_radius_cm <= 0.0 or source_footprint_cm_value < 0.0 or observer_au <= 0.0:
        raise ValueError("invalid geometry")
    return (receiver_radius_cm + source_footprint_cm_value) / (observer_au * AU_CM)


def expected_multiplier_upper_isotropic(
    receiver_radius_cm: float,
    source_footprint_cm_value: float,
    observer_au: float,
    solar_radius_cm: float = R_SUN_CM,
) -> tuple[float, float, float]:
    """Return (mu_ceiling, alignment probability, expected multiplier ceiling).

    The comparison baseline is the same detector without requiring solar alignment,
    so E[mu] = (1-p)*1 + p*mu.
    """
    mu = perfect_solar_aperture_mu_ceiling(receiver_radius_cm, solar_radius_cm)
    theta = alignment_theta_upper_rad(receiver_radius_cm, source_footprint_cm_value, observer_au)
    p = stable_small_cap_probability(theta)
    return mu, p, 1.0 + p * (mu - 1.0)


def focal_map_offset_cm(
    b_fraction: float,
    solar_radius_cm: float,
    observer_au: float,
    focal_distance_au_fn: Callable[[float], float],
) -> float:
    """Signed on-axis focal-plane radius y=b*(1-z/F(b)) for a distant source."""
    if not 0.0 < b_fraction <= 1.0:
        raise ValueError("b_fraction must lie in (0,1]")
    if solar_radius_cm <= 0.0 or observer_au <= 0.0:
        raise ValueError("invalid geometry")
    f_au = focal_distance_au_fn(b_fraction)
    if f_au <= 0.0:
        raise ValueError("focal distance must be positive")
    b_cm = b_fraction * solar_radius_cm
    return b_cm * (1.0 - observer_au / f_au)


def _find_abs_offset_boundary(
    root_b_fraction: float,
    direction: int,
    target_radius_cm: float,
    solar_radius_cm: float,
    observer_au: float,
    focal_distance_au_fn: Callable[[float], float],
    initial_step: float = 1.0e-8,
    max_step: float = 0.05,
) -> float:
    if direction not in (-1, 1):
        raise ValueError("direction must be +/-1")
    if target_radius_cm <= 0.0:
        raise ValueError("target radius must be positive")

    def h(x: float) -> float:
        return abs(focal_map_offset_cm(x, solar_radius_cm, observer_au, focal_distance_au_fn)) - target_radius_cm

    root_h = h(root_b_fraction)
    if root_h > 1.0e-5 * max(1.0, target_radius_cm):
        raise ValueError("supplied root is not sufficiently focused at observer distance")

    step = initial_step
    inner = root_b_fraction
    outer = root_b_fraction + direction * step
    while 0.0 < outer < 1.0 and h(outer) <= 0.0 and step < max_step:
        inner = outer
        step *= 2.0
        outer = root_b_fraction + direction * step
    if not 0.0 < outer < 1.0 or h(outer) <= 0.0:
        raise ValueError("failed to bracket receiver boundary")

    lo, hi = sorted((inner, outer))
    # One endpoint is inside and one outside. Preserve only interval geometry;
    # convergence target is much finer than any receiver scale used by 0061.
    for _ in range(90):
        mid = 0.5 * (lo + hi)
        inside = h(mid) <= 0.0
        if direction < 0:
            # outside is at lower b; inside is toward root at higher b
            if inside:
                hi = mid
            else:
                lo = mid
        else:
            # inside is at lower b; outside at higher b
            if inside:
                lo = mid
            else:
                hi = mid
    return 0.5 * (lo + hi)


def annular_point_source_receiver_mu(
    root_b_fraction: float,
    receiver_radius_cm: float,
    solar_radius_cm: float,
    focal_distance_au_fn: Callable[[float], float],
) -> tuple[float, float, float, float]:
    """Receiver-integrated point-source magnification for one resolved focal ring.

    Observer distance is frozen to F(root).  The returned tuple is
    (observer_au, b_low, b_high, magnification), where magnification is the
    incident annulus area divided by receiver area.  Other roots/images are
    deliberately omitted, so this is a conservative physical contribution.
    """
    if receiver_radius_cm <= 0.0:
        raise ValueError("receiver radius must be positive")
    z_au = focal_distance_au_fn(root_b_fraction)
    b_lo = _find_abs_offset_boundary(
        root_b_fraction, -1, receiver_radius_cm, solar_radius_cm, z_au, focal_distance_au_fn
    )
    b_hi = _find_abs_offset_boundary(
        root_b_fraction, +1, receiver_radius_cm, solar_radius_cm, z_au, focal_distance_au_fn
    )
    area_annulus = math.pi * solar_radius_cm**2 * (b_hi * b_hi - b_lo * b_lo)
    area_receiver = math.pi * receiver_radius_cm**2
    return z_au, b_lo, b_hi, area_annulus / area_receiver


def finite_source_mu_bracket(
    root_b_fraction: float,
    receiver_radius_cm: float,
    source_footprint_cm_value: float,
    solar_radius_cm: float,
    focal_distance_au_fn: Callable[[float], float],
) -> tuple[float, float, float]:
    """Rigorous triangle-inequality bracket for a uniform finite source.

    Rays mapping within a-s are accepted for every source point (lower bound),
    while no accepted ray can originate outside a+s (upper bound).  For 0061
    the 10-kpc CCSN footprint at ~24 AU is sub-mm, making this bracket tight for
    metre-class receivers while avoiding a point-caustic approximation.
    """
    if not 0.0 <= source_footprint_cm_value < receiver_radius_cm:
        raise ValueError("source footprint must satisfy 0 <= s < receiver radius")
    z1, _, _, mu_lo = annular_point_source_receiver_mu(
        root_b_fraction,
        receiver_radius_cm - source_footprint_cm_value,
        solar_radius_cm,
        focal_distance_au_fn,
    )
    z2, _, _, mu_hi_raw = annular_point_source_receiver_mu(
        root_b_fraction,
        receiver_radius_cm + source_footprint_cm_value,
        solar_radius_cm,
        focal_distance_au_fn,
    )
    # Both annulus areas above are normalized to their temporary disks. Convert
    # back to the physical receiver area a^2.
    mu_lo *= ((receiver_radius_cm - source_footprint_cm_value) / receiver_radius_cm) ** 2
    mu_hi = mu_hi_raw * ((receiver_radius_cm + source_footprint_cm_value) / receiver_radius_cm) ** 2
    if abs(z1 - z2) > 1e-12:
        raise AssertionError("observer distance changed unexpectedly")
    return z1, mu_lo, mu_hi
