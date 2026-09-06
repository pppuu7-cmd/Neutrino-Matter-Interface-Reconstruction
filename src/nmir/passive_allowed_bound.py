"""Conservative passive-target upper bounds for allowed solar-neutrino capture.

This module implements the preregistered first-stage G3 target-space bound.
It is intentionally *not* a realistic nuclear model.  It combines:

* a correlation-independent operator-norm strength cap,
* a rigorous point-Coulomb phase-space inequality,
* zero threshold/excitation when maximizing phase space,
* deliberately generous solar-energy and target-count inputs.

Forbidden multipoles, resonant line capture, collective engineered media and
BSM interactions are outside this module's scope.
"""

from __future__ import annotations

import math

from .capture_metrics import AVOGADRO

GF_GEV_M2 = 1.1663787e-5
VUD = 0.97420
G_A = 1.2754
ALPHA = 1.0 / 137.035999084
M_E_MEV = 0.510998950
GEV_M2_TO_CM2 = 0.389379338e-27

# Preregistered known-nuclei stress domain.
DEFAULT_A_MAX = 300
DEFAULT_Z_DAUGHTER_MAX = 119
DEFAULT_ENU_MAX_MEV = 20.0
DEFAULT_NEUTRINO_ENERGY_FLUX_W_M2 = 2000.0
DEFAULT_TARGET_COUNT_SAFETY = 1.02
DEFAULT_OMITTED_PHYSICS_STRESS = 1.0e6


def point_coulomb_pef_ratio_bound(z_daughter: int) -> float:
    """Return C such that p*E*F_pc <= C*E^2 for attractive point Coulomb.

    For x=2*pi*alpha*Z*E/p and F=x/(1-exp(-x)), exp(x)>=1+x gives
    F<=1+x.  Since p<=E, p*E*F <= (1+2*pi*alpha*Z)*E^2.
    """
    if z_daughter <= 0:
        raise ValueError("z_daughter must be positive")
    return 1.0 + 2.0 * math.pi * ALPHA * z_daughter


def allowed_strength_operator_norm_bound(a_mass: int, *, g_a: float = G_A) -> float:
    """Intentionally loose one-body closure bound B(F)+g_A^2 B(GT).

    Triangle/operator-norm inequalities give S_F<=A^2 and S_GT<=3A^2,
    independent of nuclear correlations.  This is a cap, not a prediction.
    """
    if a_mass <= 0:
        raise ValueError("a_mass must be positive")
    if g_a <= 0:
        raise ValueError("g_a must be positive")
    return float(a_mass * a_mass) * (1.0 + 3.0 * g_a * g_a)


def allowed_sigma_operator_norm_bound_cm2(
    enu_mev: float,
    a_mass: int,
    z_daughter: int,
    *,
    g_a: float = G_A,
) -> float:
    """Upper bound on leading allowed CC capture cross section in cm^2.

    Threshold and excitation are set to zero to maximize outgoing-electron
    phase space: E_e <= m_e + E_nu.  The point-Coulomb p E F factor is then
    bounded analytically and multiplied by the operator-norm strength cap.
    """
    if enu_mev < 0:
        raise ValueError("enu_mev must be non-negative")
    electron_total_gev = (M_E_MEV + enu_mev) * 1.0e-3
    weak_prefactor = GF_GEV_M2**2 * VUD**2 / math.pi
    phase_bound = point_coulomb_pef_ratio_bound(z_daughter) * electron_total_gev**2
    strength_bound = allowed_strength_operator_norm_bound(a_mass, g_a=g_a)
    return weak_prefactor * phase_bound * strength_bound * GEV_M2_TO_CM2


def target_nuclei_per_kg_upper(a_mass: int, *, count_safety: float = DEFAULT_TARGET_COUNT_SAFETY) -> float:
    """Conservative target-count cap based on A g/mol with an upward margin."""
    if a_mass <= 0:
        raise ValueError("a_mass must be positive")
    if count_safety < 1.0:
        raise ValueError("count_safety must be at least one")
    return count_safety * 1000.0 * AVOGADRO / float(a_mass)


def passive_allowed_power_bound_w_per_kg(
    *,
    a_mass: int,
    z_daughter: int,
    enu_max_mev: float,
    neutrino_energy_flux_w_m2: float,
    count_safety: float = DEFAULT_TARGET_COUNT_SAFETY,
) -> float:
    """Bound neutrino-supplied power using sigma_max times energy flux.

    Since sigma(E)<=sigma_max over the admitted energy range,
    N_T * integral Phi(E) sigma(E) E dE <= N_T sigma_max F_nu.
    """
    if neutrino_energy_flux_w_m2 < 0:
        raise ValueError("neutrino_energy_flux_w_m2 must be non-negative")
    sigma_max = allowed_sigma_operator_norm_bound_cm2(enu_max_mev, a_mass, z_daughter)
    flux_w_cm2 = neutrino_energy_flux_w_m2 / 1.0e4
    return target_nuclei_per_kg_upper(a_mass, count_safety=count_safety) * sigma_max * flux_w_cm2


def known_nuclei_allowed_stress_envelope() -> dict[str, float | int | str]:
    """Return the preregistered A<=300/Z_f<=119 allowed-current envelope."""
    analytic = passive_allowed_power_bound_w_per_kg(
        a_mass=DEFAULT_A_MAX,
        z_daughter=DEFAULT_Z_DAUGHTER_MAX,
        enu_max_mev=DEFAULT_ENU_MAX_MEV,
        neutrino_energy_flux_w_m2=DEFAULT_NEUTRINO_ENERGY_FLUX_W_M2,
    )
    stressed = analytic * DEFAULT_OMITTED_PHYSICS_STRESS
    if stressed < 1.0e-3:
        classification = "STRONG_NEGATIVE_SCOPED"
    elif analytic < 1.0:
        classification = "NEGATIVE_SCOPED"
    else:
        classification = "NO_NEGATIVE_BOUND"
    return {
        "a_max": DEFAULT_A_MAX,
        "z_daughter_max": DEFAULT_Z_DAUGHTER_MAX,
        "enu_max_mev": DEFAULT_ENU_MAX_MEV,
        "neutrino_energy_flux_w_m2": DEFAULT_NEUTRINO_ENERGY_FLUX_W_M2,
        "target_count_safety": DEFAULT_TARGET_COUNT_SAFETY,
        "analytic_allowed_bound_w_per_kg": analytic,
        "omitted_physics_stress_multiplier": DEFAULT_OMITTED_PHYSICS_STRESS,
        "stressed_bound_w_per_kg": stressed,
        "analytic_deficit_to_1_w_per_kg": 1.0 / analytic,
        "stressed_deficit_to_1_w_per_kg": 1.0 / stressed,
        "classification": classification,
    }
