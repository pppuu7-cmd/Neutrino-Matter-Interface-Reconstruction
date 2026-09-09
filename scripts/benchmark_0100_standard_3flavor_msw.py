#!/usr/bin/env python3
"""NMIR benchmark 0100: standard three-flavor + MSW preflight.

This module implements only the mathematical control model frozen in
research/prereg/0100_known_model_benchmark_standard_3flavor_msw.md.
It does not contain a terminal Betelgeuse source profile or source spectrum.
Synthetic profiles are test fixtures only.
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from typing import Iterable

import numpy as np

# exp[-i m^2 L/(2E)] = exp[-i * PHASE_COEFF * m^2[eV^2] * L[km] / E[GeV]]
PHASE_COEFF = 2.53386535
# A_CC = 2 E V_CC in eV^2, with E in MeV, rho in g cm^-3, explicit Ye.
A_CC_COEFF = 1.52588e-7


@dataclass(frozen=True)
class OscillationParameters:
    ordering: str
    sin2_theta12: float
    sin2_theta23: float
    sin2_theta13: float
    delta_cp_deg: float
    dm21_eV2: float
    dm3l_eV2: float


# NuFIT 6.1 (2025), IC24 with SK atmospheric data, retrieved/frozen 2026-09-09.
NUFIT61_NO = OscillationParameters(
    ordering="NO",
    sin2_theta12=0.3088,
    sin2_theta23=0.470,
    sin2_theta13=0.02248,
    delta_cp_deg=212.0,
    dm21_eV2=7.537e-5,
    dm3l_eV2=2.511e-3,  # dm31 for NO
)

NUFIT61_IO = OscillationParameters(
    ordering="IO",
    sin2_theta12=0.3088,
    sin2_theta23=0.550,
    sin2_theta13=0.02262,
    delta_cp_deg=274.0,
    dm21_eV2=7.537e-5,
    dm3l_eV2=-2.483e-3,  # NuFIT convention: dm32 for IO
)


def pmns_matrix(p: OscillationParameters, antineutrino: bool = False) -> np.ndarray:
    s12, s23, s13 = map(math.sqrt, (p.sin2_theta12, p.sin2_theta23, p.sin2_theta13))
    c12, c23, c13 = map(math.sqrt, (1.0 - p.sin2_theta12, 1.0 - p.sin2_theta23, 1.0 - p.sin2_theta13))
    delta = math.radians(p.delta_cp_deg)
    e_pos = np.exp(1j * delta)
    e_neg = np.exp(-1j * delta)

    u = np.array(
        [
            [c12 * c13, s12 * c13, s13 * e_neg],
            [
                -s12 * c23 - c12 * s23 * s13 * e_pos,
                c12 * c23 - s12 * s23 * s13 * e_pos,
                s23 * c13,
            ],
            [
                s12 * s23 - c12 * c23 * s13 * e_pos,
                -c12 * s23 - s12 * c23 * s13 * e_pos,
                c23 * c13,
            ],
        ],
        dtype=np.complex128,
    )
    return u.conjugate() if antineutrino else u


def mass_squared_eigenvalues(p: OscillationParameters) -> np.ndarray:
    if p.ordering == "NO":
        dm31 = p.dm3l_eV2
    elif p.ordering == "IO":
        # NuFIT supplies dm32 for IO. Since dm31 = dm32 + dm21:
        dm31 = p.dm3l_eV2 + p.dm21_eV2
    else:
        raise ValueError(f"unsupported ordering: {p.ordering}")
    # Any common additive mass^2 shift is an unobservable global phase.
    return np.array([0.0, p.dm21_eV2, dm31], dtype=float)


def matter_a_eV2(rho_g_cm3: float, ye: float, energy_MeV: float, antineutrino: bool = False) -> float:
    if rho_g_cm3 < 0 or not 0.0 <= ye <= 1.0 or energy_MeV <= 0:
        raise ValueError("require rho>=0, 0<=Ye<=1, E>0")
    a = A_CC_COEFF * rho_g_cm3 * ye * energy_MeV
    return -a if antineutrino else a


def effective_mass_squared_flavor(
    p: OscillationParameters,
    energy_MeV: float,
    rho_g_cm3: float = 0.0,
    ye: float = 0.5,
    antineutrino: bool = False,
) -> np.ndarray:
    u = pmns_matrix(p, antineutrino=antineutrino)
    m2 = u @ np.diag(mass_squared_eigenvalues(p)) @ u.conjugate().T
    out = np.array(m2, copy=True)
    out[0, 0] += matter_a_eV2(rho_g_cm3, ye, energy_MeV, antineutrino)
    return out


def evolve_constant_density(
    state: np.ndarray,
    length_km: float,
    p: OscillationParameters,
    energy_MeV: float,
    rho_g_cm3: float = 0.0,
    ye: float = 0.5,
    antineutrino: bool = False,
) -> np.ndarray:
    if length_km < 0:
        raise ValueError("length must be non-negative")
    m2 = effective_mass_squared_flavor(p, energy_MeV, rho_g_cm3, ye, antineutrino)
    evals, evecs = np.linalg.eigh(m2)
    energy_GeV = energy_MeV / 1000.0
    phases = np.exp(-1j * PHASE_COEFF * evals * length_km / energy_GeV)
    return evecs @ (phases * (evecs.conjugate().T @ np.asarray(state, dtype=np.complex128)))


def propagate_profile(
    state: np.ndarray,
    radius_km: Iterable[float],
    rho_g_cm3: Iterable[float],
    ye: Iterable[float],
    p: OscillationParameters,
    energy_MeV: float,
    antineutrino: bool = False,
) -> np.ndarray:
    r = np.asarray(list(radius_km), dtype=float)
    rho = np.asarray(list(rho_g_cm3), dtype=float)
    y = np.asarray(list(ye), dtype=float)
    if not (len(r) == len(rho) == len(y)) or len(r) < 2:
        raise ValueError("profile arrays must have equal length >=2")
    if np.any(np.diff(r) <= 0):
        raise ValueError("radius must be strictly increasing")

    psi = np.asarray(state, dtype=np.complex128)
    for i in range(len(r) - 1):
        length = r[i + 1] - r[i]
        rho_mid = 0.5 * (rho[i + 1] + rho[i])
        ye_mid = 0.5 * (y[i + 1] + y[i])
        psi = evolve_constant_density(psi, length, p, energy_MeV, rho_mid, ye_mid, antineutrino)
    return psi


def vacuum_probability_direct(
    alpha: int,
    beta: int,
    length_km: float,
    p: OscillationParameters,
    energy_MeV: float,
    antineutrino: bool = False,
) -> float:
    u = pmns_matrix(p, antineutrino=antineutrino)
    m2 = mass_squared_eigenvalues(p)
    energy_GeV = energy_MeV / 1000.0
    phases = np.exp(-1j * PHASE_COEFF * m2 * length_km / energy_GeV)
    amp = np.sum(u[beta, :] * np.conjugate(u[alpha, :]) * phases)
    return float(abs(amp) ** 2)


def pure_flavor(alpha: int) -> np.ndarray:
    state = np.zeros(3, dtype=np.complex128)
    state[alpha] = 1.0
    return state


def probability_vector(state: np.ndarray) -> np.ndarray:
    return np.abs(np.asarray(state)) ** 2


def relativistic_mass_correction_scale(mass_eV: float, energy_MeV: float) -> float:
    """Leading ultra-relativistic scale m^2/(2E^2), not a new ray calculation."""
    if mass_eV < 0 or energy_MeV <= 0:
        raise ValueError("require m>=0, E>0")
    energy_eV = energy_MeV * 1.0e6
    return 0.5 * (mass_eV / energy_eV) ** 2


def synthetic_profile(n_segments: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if n_segments < 1:
        raise ValueError("n_segments must be positive")
    r = np.linspace(0.0, 10000.0, n_segments + 1)
    rho = 1.0e4 * np.exp(-r / 1500.0) + 1.0
    ye = np.full_like(r, 0.5)
    return r, rho, ye


def run_preflight() -> dict:
    results: dict[str, object] = {
        "benchmark": "NMIR-BENCHMARK-0100",
        "scope": "mathematical_preflight_only",
        "terminal_source_profile_pinned": False,
        "terminal_physics_execution_allowed": False,
    }

    unitary_errors = {}
    normalization_errors = {}
    vacuum_errors = {}
    anti_sign_ok = True
    finite_ok = True
    bounded_ok = True

    for p in (NUFIT61_NO, NUFIT61_IO):
        u = pmns_matrix(p)
        unitary_errors[p.ordering] = float(np.max(np.abs(u.conjugate().T @ u - np.eye(3))))

        max_norm = 0.0
        max_vac = 0.0
        for alpha in range(3):
            out = evolve_constant_density(pure_flavor(alpha), 1234.5, p, 5.0, rho_g_cm3=0.0)
            probs = probability_vector(out)
            max_norm = max(max_norm, abs(float(np.sum(probs)) - 1.0))
            finite_ok = finite_ok and bool(np.all(np.isfinite(probs)))
            bounded_ok = bounded_ok and bool(np.all(probs >= -1e-12) and np.all(probs <= 1.0 + 1e-12))
            for beta in range(3):
                p_direct = vacuum_probability_direct(alpha, beta, 1234.5, p, 5.0)
                max_vac = max(max_vac, abs(float(probs[beta]) - p_direct))
        normalization_errors[p.ordering] = max_norm
        vacuum_errors[p.ordering] = max_vac

        h_nu = effective_mass_squared_flavor(p, 5.0, rho_g_cm3=100.0, ye=0.5, antineutrino=False)
        h_anu = effective_mass_squared_flavor(p, 5.0, rho_g_cm3=100.0, ye=0.5, antineutrino=True)
        h_nu_vac = effective_mass_squared_flavor(p, 5.0, rho_g_cm3=0.0, ye=0.5, antineutrino=False)
        h_anu_vac = effective_mass_squared_flavor(p, 5.0, rho_g_cm3=0.0, ye=0.5, antineutrino=True)
        anti_sign_ok = anti_sign_ok and (np.real(h_nu[0, 0] - h_nu_vac[0, 0]) > 0)
        anti_sign_ok = anti_sign_ok and (np.real(h_anu[0, 0] - h_anu_vac[0, 0]) < 0)

    vacuum_scale = float(np.max(np.abs(mass_squared_eigenvalues(NUFIT61_NO))))
    matter_scale = abs(matter_a_eV2(1.0e10, 0.5, 5.0, False))
    high_density_ratio = matter_scale / vacuum_scale

    psi0 = pure_flavor(0)
    r32, rho32, ye32 = synthetic_profile(3200)
    r64, rho64, ye64 = synthetic_profile(6400)
    p32 = probability_vector(propagate_profile(psi0, r32, rho32, ye32, NUFIT61_NO, 5.0))
    p64 = probability_vector(propagate_profile(psi0, r64, rho64, ye64, NUFIT61_NO, 5.0))
    convergence = float(np.max(np.abs(p32 - p64)))

    mass_guard = relativistic_mass_correction_scale(0.46, 0.5)

    gates = {
        "pmns_unitarity": max(unitary_errors.values()) <= 1e-12,
        "probability_normalization": max(normalization_errors.values()) <= 1e-12,
        "vacuum_reduction": max(vacuum_errors.values()) <= 1e-12,
        "antineutrino_matter_sign": bool(anti_sign_ok),
        "high_density_qualitative": high_density_ratio >= 1.0e4,
        "step_convergence": convergence < 1.0e-4,
        "finite_outputs": bool(finite_ok),
        "probability_bounds": bool(bounded_ok),
        "g9_mass_scale_guard": mass_guard < 5.0e-13,
    }

    results.update(
        {
            "unitarity_max_abs": unitary_errors,
            "normalization_abs_error": normalization_errors,
            "vacuum_probability_max_abs_error": vacuum_errors,
            "high_density_matter_to_vacuum_ratio": high_density_ratio,
            "synthetic_step_convergence_max_abs": convergence,
            "g9_mass_correction_guard_scale": mass_guard,
            "gates": gates,
            "preflight_all_pass": bool(all(gates.values())),
            "terminal_status_ceiling": "BLOCKED_0100_SOURCE_PROFILE_UNPINNED",
        }
    )
    return results


if __name__ == "__main__":
    print(json.dumps(run_preflight(), indent=2, sort_keys=True))
