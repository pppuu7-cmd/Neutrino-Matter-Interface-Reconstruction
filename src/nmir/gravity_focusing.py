"""Baseline gravitational focusing utilities for ultrarelativistic neutrinos.

These functions implement geometric-optics weak-field benchmarks only.  They do
not model an extended transparent lens, finite source size, wave optics, or
strong-field capture.  Those are separate NMIR gates.
"""

from __future__ import annotations

import math

G_SI = 6.67430e-11
C_SI = 299_792_458.0
AU_M = 1.495978707e11
M_SUN_KG = 1.98847e30
R_SUN_M = 6.957e8


def null_deflection_rad(mass_kg: float, impact_parameter_m: float) -> float:
    """Leading Schwarzschild deflection 4GM/(bc^2)."""
    if mass_kg <= 0:
        raise ValueError("mass_kg must be positive")
    if impact_parameter_m <= 0:
        raise ValueError("impact_parameter_m must be positive")
    return 4.0 * G_SI * mass_kg / (impact_parameter_m * C_SI**2)


def focal_distance_m(mass_kg: float, impact_parameter_m: float) -> float:
    """Axis-crossing distance b/alpha in the weak point-lens approximation."""
    alpha = null_deflection_rad(mass_kg, impact_parameter_m)
    return impact_parameter_m / alpha


def solar_limb_focal_distance_au() -> float:
    """Reference focal distance for a ray grazing the solar limb."""
    return focal_distance_m(M_SUN_KG, R_SUN_M) / AU_M


def point_lens_magnification(u: float) -> float:
    """Total geometric-optics magnification for a point source and point lens.

    u = beta/theta_E.  The point-source formula diverges at u=0 and must not be
    interpreted as an infinite physical flux.  Finite source size, detector
    size, wave optics and alignment regularize the caustic.
    """
    if u <= 0:
        raise ValueError("u must be positive; use a finite-source model near u=0")
    return (u * u + 2.0) / (u * math.sqrt(u * u + 4.0))


def required_lensing_gain(current_power_w_per_kg: float, target_power_w_per_kg: float) -> float:
    """Lensing magnification required if *nothing else* in capture physics changes."""
    if current_power_w_per_kg <= 0:
        raise ValueError("current_power_w_per_kg must be positive")
    if target_power_w_per_kg < 0:
        raise ValueError("target_power_w_per_kg must be non-negative")
    return target_power_w_per_kg / current_power_w_per_kg
