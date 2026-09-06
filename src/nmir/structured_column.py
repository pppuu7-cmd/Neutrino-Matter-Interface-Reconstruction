"""G10 geometry-only/fixed-column structured-matter bounds for NMIR."""

from __future__ import annotations

import math
from collections.abc import Iterable

from .finite_q_multipole_bound import FROZEN_MULTIPOLE_SAFETY_FACTOR
from .nuclear_current_loophole import one_body_component_scales
from .passive_allowed_bound import (
    DEFAULT_A_MAX,
    DEFAULT_ENU_MAX_MEV,
    DEFAULT_Z_DAUGHTER_MAX,
    allowed_sigma_operator_norm_bound_cm2,
)

ANGSTROM_CM = 1.0e-8
LATTICE_SPACING_ANGSTROM = 2.0


def absorption_from_optical_depth(tau: float) -> float:
    if tau < 0:
        raise ValueError("tau must be non-negative")
    return -math.expm1(-tau)


def layered_absorption(taus: Iterable[float]) -> float:
    values = tuple(float(t) for t in taus)
    if any(t < 0 for t in values):
        raise ValueError("all optical depths must be non-negative")
    return absorption_from_optical_depth(sum(values))


def mass_specific_optical_depth_coefficient(
    weights: Iterable[float],
    sigma_over_mass: Iterable[float],
) -> float:
    w = tuple(float(x) for x in weights)
    k = tuple(float(x) for x in sigma_over_mass)
    if len(w) != len(k) or not w:
        raise ValueError("weights and sigma_over_mass must have equal nonzero length")
    if any(x < 0 for x in w) or any(x < 0 for x in k):
        raise ValueError("weights and coefficients must be non-negative")
    if not math.isclose(sum(w), 1.0, rel_tol=0.0, abs_tol=1.0e-12):
        raise ValueError("weights must sum to one")
    return sum(wi * ki for wi, ki in zip(w, k, strict=True))


def tilted_capture_factor(face_on_tau: float, cos_theta: float) -> float:
    """Total captured-power factor for fixed slab face area, up to common flux*area."""
    if face_on_tau < 0:
        raise ValueError("face_on_tau must be non-negative")
    if not 0 < cos_theta <= 1:
        raise ValueError("cos_theta must lie in (0,1]")
    return cos_theta * absorption_from_optical_depth(face_on_tau / cos_theta)


def stressed_atomic_layer_geometry() -> dict[str, float]:
    """Illustrative staggered-layer scale using the frozen huge weak cross-section stress."""
    sigma_allowed = allowed_sigma_operator_norm_bound_cm2(
        DEFAULT_ENU_MAX_MEV,
        DEFAULT_A_MAX,
        DEFAULT_Z_DAUGHTER_MAX,
    )
    sigma_leading = FROZEN_MULTIPOLE_SAFETY_FACTOR * sigma_allowed
    r1b = float(one_body_component_scales()["frozen_one_body_amplitude_ratio"])
    sigma_stress = sigma_leading * (1.0 + r1b) ** 2
    spacing_cm = LATTICE_SPACING_ANGSTROM * ANGSTROM_CM
    cell_area_cm2 = spacing_cm**2
    tau_per_layer = sigma_stress / cell_area_cm2
    layers_tau_one = 1.0 / tau_per_layer
    thickness_cm = layers_tau_one * spacing_cm
    return {
        "allowed_sigma_operator_norm_cm2": sigma_allowed,
        "finite_q_leading_sigma_stress_cm2": sigma_leading,
        "one_body_subleading_sigma_stress_cm2": sigma_stress,
        "lattice_spacing_angstrom": LATTICE_SPACING_ANGSTROM,
        "cell_area_cm2": cell_area_cm2,
        "tau_per_ideal_dense_layer": tau_per_layer,
        "layers_for_tau_one": layers_tau_one,
        "thickness_for_tau_one_m": thickness_cm / 100.0,
        "effective_interaction_radius_m": math.sqrt(sigma_stress / math.pi) * 1.0e-2,
    }


def structured_column_gate() -> dict[str, object]:
    geom = stressed_atomic_layer_geometry()
    return {
        "layer_order_formula": "A=1-exp(-sum_j tau_j)",
        "mixture_formula": "sum_i w_i kappa_i <= max_i kappa_i, kappa_i=sigma_i/m_i",
        "tilt_formula": "C(c)=c[1-exp(-tau/c)] <= C(1)",
        "stressed_atomic_geometry": geom,
        "classification": "G10_GEOMETRY_ONLY_STRONG_NEGATIVE / FIXED_COLUMN_MIXTURE_THEOREM_PASS",
        "scope": (
            "Independent passive events at fixed microscopic cross sections. Any structure-induced change "
            "of sigma through coherence, resonance, polarization, active pumping or BSM is outside this theorem."
        ),
    }
