"""Gravitational focusing utilities for ultrarelativistic neutrinos.

The transparent-Sun helpers reproduce a published interior focal-scale benchmark.
Finite-source helpers are explicit Liouville/surface-brightness controls; they do
not replace a full extended-Sun caustic calculation.
"""

from __future__ import annotations

import math

G_SI = 6.67430e-11
C_SI = 299_792_458.0
AU_M = 1.495978707e11
M_SUN_KG = 1.98847e30
R_SUN_M = 6.957e8


def null_deflection_rad(mass_kg: float, impact_parameter_m: float) -> float:
    if mass_kg <= 0:
        raise ValueError("mass_kg must be positive")
    if impact_parameter_m <= 0:
        raise ValueError("impact_parameter_m must be positive")
    return 4.0 * G_SI * mass_kg / (impact_parameter_m * C_SI**2)


def focal_distance_m(mass_kg: float, impact_parameter_m: float) -> float:
    return impact_parameter_m / null_deflection_rad(mass_kg, impact_parameter_m)


def solar_limb_focal_distance_au() -> float:
    return focal_distance_m(M_SUN_KG, R_SUN_M) / AU_M


def transparent_sun_rounded_check_au(
    impact_fraction: float = 0.024,
    projected_mass_fraction: float = 0.0137,
) -> float:
    """Patla-Nemiroff rounded interior check for the ~23.5 AU minimum focus."""
    if not 0 < impact_fraction <= 1:
        raise ValueError("impact_fraction must lie in (0,1]")
    if not 0 < projected_mass_fraction <= 1:
        raise ValueError("projected_mass_fraction must lie in (0,1]")
    return focal_distance_m(
        projected_mass_fraction * M_SUN_KG,
        impact_fraction * R_SUN_M,
    ) / AU_M


def point_lens_magnification(u: float) -> float:
    if u <= 0:
        raise ValueError("u must be positive; use a finite-source model near u=0")
    return (u * u + 2.0) / (u * math.sqrt(u * u + 4.0))


def on_axis_uniform_disk_magnification(rho: float) -> float:
    """Exact geometric-optics magnification for an on-axis uniform disk.

    rho is source angular radius / Einstein angular radius.  The divergence of
    the point-source formula is integrable and the finite source gain is finite.
    """
    if rho <= 0:
        raise ValueError("rho must be positive")
    return math.sqrt(rho * rho + 4.0) / rho


def numerical_uniform_disk_magnification(rho: float, intervals: int = 20000) -> float:
    """Midpoint area-average of point-source magnification over an on-axis disk."""
    if rho <= 0:
        raise ValueError("rho must be positive")
    if intervals < 10:
        raise ValueError("intervals must be >=10")
    dr = rho / intervals
    total = 0.0
    for i in range(intervals):
        u = (i + 0.5) * dr
        total += point_lens_magnification(u) * u * dr
    return 2.0 * total / (rho * rho)


def surface_brightness_flux_gain(image_solid_angle: float, source_solid_angle: float) -> float:
    """Liouville control: conserved specific intensity => flux gain = area gain."""
    if image_solid_angle <= 0 or source_solid_angle <= 0:
        raise ValueError("solid angles must be positive")
    return image_solid_angle / source_solid_angle


def required_lensing_gain(current_power_w_per_kg: float, target_power_w_per_kg: float) -> float:
    if current_power_w_per_kg <= 0:
        raise ValueError("current_power_w_per_kg must be positive")
    if target_power_w_per_kg < 0:
        raise ValueError("target_power_w_per_kg must be non-negative")
    return target_power_w_per_kg / current_power_w_per_kg
