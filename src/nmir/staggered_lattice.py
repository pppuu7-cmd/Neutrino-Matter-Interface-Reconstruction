"""Toy structure-factor utilities for staggered-layer NMIR studies."""

from __future__ import annotations

import cmath
import math
from typing import Iterable, Sequence, Tuple

Position2D = Tuple[float, float]  # (x, z) in meters
HC_EV_M = 1.239841984e-6


def staggered_layer_positions(
    n_layers: int,
    layer_spacing_m: float,
    lateral_shift_m: float,
    lattice_period_m: float | None = None,
) -> list[Position2D]:
    """Return one representative scatterer per layer in an x-z toy stack.

    If ``lattice_period_m`` is supplied, lateral positions are wrapped into
    one transverse unit cell. The routine is intentionally geometrical; it
    does not claim that each representative point is an independent atom of
    a real 3-D crystal.
    """
    if n_layers <= 0:
        raise ValueError("n_layers must be positive")
    if layer_spacing_m <= 0:
        raise ValueError("layer_spacing_m must be positive")
    if lattice_period_m is not None and lattice_period_m <= 0:
        raise ValueError("lattice_period_m must be positive")

    out: list[Position2D] = []
    for ell in range(n_layers):
        x = ell * lateral_shift_m
        if lattice_period_m is not None:
            x %= lattice_period_m
        out.append((x, ell * layer_spacing_m))
    return out


def elastic_structure_factor(qx_inv_m: float, qz_inv_m: float, positions: Iterable[Position2D]) -> complex:
    """F(q)=sum_j exp(i q.r_j) for a 2-D toy stack."""
    total = 0.0j
    for x, z in positions:
        total += cmath.exp(1j * (qx_inv_m * x + qz_inv_m * z))
    return total


def normalized_directional_gain(qx_inv_m: float, qz_inv_m: float, positions: Sequence[Position2D]) -> float:
    """Return |F|^2/N, i.e. directional coherent intensity vs incoherent N.

    This can reach N at an exactly coherent direction. It is *not* an
    angle-integrated opacity gain.
    """
    if not positions:
        raise ValueError("positions must be non-empty")
    f = elastic_structure_factor(qx_inv_m, qz_inv_m, positions)
    return abs(f) ** 2 / len(positions)


def geometric_nuclear_covering_per_layer(nuclear_radius_m: float, transverse_lattice_spacing_m: float) -> float:
    """Naive hard-disk projected nuclear area fraction for a square cell.

    This is only a sanity check. Weak-interaction opacity is much smaller
    than nuclear geometric opacity and must not be inferred from this value.
    """
    if nuclear_radius_m <= 0 or transverse_lattice_spacing_m <= 0:
        raise ValueError("lengths must be positive")
    return math.pi * nuclear_radius_m**2 / transverse_lattice_spacing_m**2


def layers_for_geometric_covering(nuclear_radius_m: float, transverse_lattice_spacing_m: float) -> float:
    """Optimistic number of perfectly non-overlapping shifted layers for unity hard-disk coverage."""
    f = geometric_nuclear_covering_per_layer(nuclear_radius_m, transverse_lattice_spacing_m)
    return 1.0 / f


def neutrino_wavelength_m(energy_mev: float) -> float:
    """Relativistic de Broglie wavelength h c / E for E in MeV."""
    if energy_mev <= 0:
        raise ValueError("energy_mev must be positive")
    return HC_EV_M / (energy_mev * 1.0e6)


def first_order_bragg_angle_deg(energy_mev: float, plane_spacing_m: float) -> float:
    """Return theta in 2 d sin(theta)=lambda for first-order Bragg diffraction.

    The physical scattering-angle convention is often 2*theta. This helper
    only reports the Bragg theta used in the equation.
    """
    if plane_spacing_m <= 0:
        raise ValueError("plane_spacing_m must be positive")
    wavelength = neutrino_wavelength_m(energy_mev)
    x = wavelength / (2.0 * plane_spacing_m)
    if x > 1.0:
        raise ValueError("first-order Bragg condition is not kinematically available")
    return math.degrees(math.asin(x))
