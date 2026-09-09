#!/usr/bin/env python3
"""Mathematical preflights for NMIR known-model benchmarks 0101--0104.

These calculations intentionally use frozen synthetic fixtures for code-path and
known-limit validation. They are non-terminal until each benchmark's external
parameter/source authorities are prospectively pinned.
"""

from __future__ import annotations

import json
import math

import numpy as np

from scripts.benchmark_0100_standard_3flavor_msw import (
    NUFIT61_NO,
    PHASE_COEFF,
    effective_mass_squared_flavor,
    evolve_constant_density,
    mass_squared_eigenvalues,
    matter_a_eV2,
    pmns_matrix,
    probability_vector,
    pure_flavor,
)

TOL = 1.0e-12
MU_B_EV_PER_T = 5.7883818060e-5
N_A = 6.02214076e23
INV_CM_TO_EV = 1.973269804e-5
INV_CM3_TO_EV3 = INV_CM_TO_EV ** 3


def evolve_hermitian(state: np.ndarray, m2_eff: np.ndarray, length_km: float, energy_MeV: float) -> np.ndarray:
    if length_km < 0 or energy_MeV <= 0:
        raise ValueError("require L>=0 and E>0")
    evals, evecs = np.linalg.eigh(np.asarray(m2_eff, dtype=np.complex128))
    phases = np.exp(-1j * PHASE_COEFF * evals * length_km / (energy_MeV / 1000.0))
    state = np.asarray(state, dtype=np.complex128)
    return evecs @ (phases * (evecs.conjugate().T @ state))


def hermiticity_error(matrix: np.ndarray) -> float:
    return float(np.max(np.abs(matrix - matrix.conjugate().T)))


def rotation4(i: int, j: int, theta: float) -> np.ndarray:
    r = np.eye(4, dtype=np.complex128)
    c, s = math.cos(theta), math.sin(theta)
    r[i, i] = c
    r[j, j] = c
    r[i, j] = s
    r[j, i] = -s
    return r


def mixing_3p1(theta14: float, theta24: float, theta34: float, antineutrino: bool = False) -> np.ndarray:
    u3 = pmns_matrix(NUFIT61_NO, antineutrino=False)
    base = np.eye(4, dtype=np.complex128)
    base[:3, :3] = u3
    u4 = rotation4(2, 3, theta34) @ rotation4(1, 3, theta24) @ rotation4(0, 3, theta14) @ base
    return u4.conjugate() if antineutrino else u4


def effective_3p1(
    energy_MeV: float,
    rho_g_cm3: float,
    ye: float,
    theta14: float,
    theta24: float,
    theta34: float,
    dm41_eV2: float,
    antineutrino: bool = False,
) -> np.ndarray:
    if not 0.0 < ye <= 1.0:
        raise ValueError("0101 requires 0<Ye<=1")
    u4 = mixing_3p1(theta14, theta24, theta34, antineutrino=antineutrino)
    m2 = np.concatenate([mass_squared_eigenvalues(NUFIT61_NO), [dm41_eV2]])
    out = u4 @ np.diag(m2) @ u4.conjugate().T
    acc = matter_a_eV2(rho_g_cm3, ye, energy_MeV, antineutrino=antineutrino)
    out[0, 0] += acc
    out[3, 3] += acc * (1.0 - ye) / (2.0 * ye)
    return out


def run_0101() -> dict:
    e, rho, ye, L = 5.0, 80.0, 0.5, 1234.5
    t14 = math.asin(math.sqrt(0.02))
    t24 = math.asin(math.sqrt(0.01))
    t34 = 0.0
    dm41 = 1.0

    u4 = mixing_3p1(t14, t24, t34)
    unitary = float(np.max(np.abs(u4.conjugate().T @ u4 - np.eye(4))))
    h = effective_3p1(e, rho, ye, t14, t24, t34, dm41)
    herm = hermiticity_error(h)
    psi4 = np.zeros(4, dtype=np.complex128)
    psi4[0] = 1.0
    out = evolve_hermitian(psi4, h, L, e)
    probs = probability_vector(out)
    norm = abs(float(np.sum(probs)) - 1.0)

    h_dec = effective_3p1(e, rho, ye, 0.0, 0.0, 0.0, dm41)
    out_dec = evolve_hermitian(psi4, h_dec, L, e)
    p_dec = probability_vector(out_dec)
    p_0100 = probability_vector(evolve_constant_density(pure_flavor(0), L, NUFIT61_NO, e, rho, ye))
    dec_active = float(np.max(np.abs(p_dec[:3] - p_0100)))
    dec_sterile = float(p_dec[3])

    h_nu = effective_3p1(e, rho, ye, t14, t24, t34, dm41, False)
    h_nu0 = effective_3p1(e, 0.0, ye, t14, t24, t34, dm41, False)
    h_an = effective_3p1(e, rho, ye, t14, t24, t34, dm41, True)
    h_an0 = effective_3p1(e, 0.0, ye, t14, t24, t34, dm41, True)
    matter_sign = (
        np.real(h_nu[0, 0] - h_nu0[0, 0]) > 0
        and np.real(h_an[0, 0] - h_an0[0, 0]) < 0
        and np.real(h_nu[3, 3] - h_nu0[3, 3]) > 0
        and np.real(h_an[3, 3] - h_an0[3, 3]) < 0
    )

    gates = {
        "u4_unitarity": unitary <= TOL,
        "hamiltonian_hermiticity": herm <= TOL,
        "probability_normalization": norm <= TOL,
        "zero_sterile_active_recovery": dec_active <= TOL,
        "zero_sterile_no_leakage": dec_sterile <= TOL,
        "nonzero_fixture_sterile_leakage": float(probs[3]) > 1.0e-10,
        "finite_outputs": bool(np.all(np.isfinite(probs))),
        "antineutrino_matter_sign": bool(matter_sign),
    }
    return {
        "benchmark": "NMIR-BENCHMARK-0101",
        "status": "PASS_0101_3P1_MATHEMATICAL_PREFLIGHT_NONTERMINAL" if all(gates.values()) else "FAIL_0101_MATHEMATICAL_PREFLIGHT",
        "gates": gates,
        "metrics": {
            "u4_unitarity_max_abs": unitary,
            "hermiticity_max_abs": herm,
            "normalization_abs_error": norm,
            "decoupling_active_probability_max_abs": dec_active,
            "decoupling_sterile_probability": dec_sterile,
            "synthetic_sterile_probability": float(probs[3]),
        },
        "terminal_physics_execution_allowed": False,
        "terminal_status_ceiling": "BLOCKED_0101_STERILE_PARAMETER_AUTHORITY_UNPINNED",
    }


def epsilon_fixture() -> np.ndarray:
    eps = np.zeros((3, 3), dtype=np.complex128)
    eps[0, 0] = 0.05
    eps[2, 2] = -0.02
    z = 0.01 * np.exp(1j * math.pi / 5.0)
    eps[0, 1] = z
    eps[1, 0] = np.conjugate(z)
    return eps


def effective_nsi(energy_MeV: float, rho: float, ye: float, eps: np.ndarray, antineutrino: bool = False) -> np.ndarray:
    u = pmns_matrix(NUFIT61_NO, antineutrino=antineutrino)
    vacuum = u @ np.diag(mass_squared_eigenvalues(NUFIT61_NO)) @ u.conjugate().T
    a = matter_a_eV2(rho, ye, energy_MeV, antineutrino=antineutrino)
    eps_eff = np.asarray(eps, dtype=np.complex128).conjugate() if antineutrino else np.asarray(eps, dtype=np.complex128)
    matter = np.diag([1.0, 0.0, 0.0]).astype(np.complex128) + eps_eff
    return vacuum + a * matter


def run_0102() -> dict:
    e, rho, ye, L = 5.0, 80.0, 0.5, 1234.5
    eps = epsilon_fixture()
    h = effective_nsi(e, rho, ye, eps)
    herm = hermiticity_error(h)
    out = evolve_hermitian(pure_flavor(0), h, L, e)
    p = probability_vector(out)
    norm = abs(float(np.sum(p)) - 1.0)

    h0 = effective_nsi(e, rho, ye, np.zeros((3, 3), complex))
    p0 = probability_vector(evolve_hermitian(pure_flavor(0), h0, L, e))
    p0100 = probability_vector(evolve_constant_density(pure_flavor(0), L, NUFIT61_NO, e, rho, ye))
    zero_recovery = float(np.max(np.abs(p0 - p0100)))

    eps_shift = eps + 0.2 * np.eye(3)
    p_shift = probability_vector(evolve_hermitian(pure_flavor(0), effective_nsi(e, rho, ye, eps_shift), L, e))
    identity_invariance = float(np.max(np.abs(p - p_shift)))
    nontrivial = float(np.max(np.abs(p - p0100)))

    hnu = effective_nsi(e, rho, ye, eps, False)
    hnu0 = effective_nsi(e, 0.0, ye, eps, False)
    han = effective_nsi(e, rho, ye, eps, True)
    han0 = effective_nsi(e, 0.0, ye, eps, True)
    sign_ok = np.real(hnu[0, 0] - hnu0[0, 0]) > 0 and np.real(han[0, 0] - han0[0, 0]) < 0

    gates = {
        "hamiltonian_hermiticity": herm <= TOL,
        "probability_normalization": norm <= TOL,
        "zero_nsi_recovery": zero_recovery <= TOL,
        "identity_shift_invariance": identity_invariance <= TOL,
        "nonzero_fixture_nontrivial": nontrivial > 1.0e-10,
        "finite_outputs": bool(np.all(np.isfinite(p))),
        "antineutrino_matter_sign": bool(sign_ok),
    }
    return {
        "benchmark": "NMIR-BENCHMARK-0102",
        "status": "PASS_0102_NSI_MATHEMATICAL_PREFLIGHT_NONTERMINAL" if all(gates.values()) else "FAIL_0102_MATHEMATICAL_PREFLIGHT",
        "gates": gates,
        "metrics": {
            "hermiticity_max_abs": herm,
            "normalization_abs_error": norm,
            "zero_nsi_probability_max_abs": zero_recovery,
            "identity_shift_probability_max_abs": identity_invariance,
            "synthetic_vs_standard_probability_max_abs": nontrivial,
        },
        "terminal_physics_execution_allowed": False,
        "terminal_status_ceiling": "BLOCKED_0102_NSI_PARAMETER_AUTHORITY_UNPINNED",
    }


def magnetic_transition_matrix() -> np.ndarray:
    t = np.zeros((3, 3), dtype=np.complex128)
    t[0, 1] = 1.0
    t[1, 0] = -1.0
    return t


def effective_spin_flavor(
    energy_MeV: float,
    rho: float,
    ye: float,
    mu_over_muB: float,
    b_perp_T: float,
    coupling_phase: float = 0.0,
) -> np.ndarray:
    hnu = effective_mass_squared_flavor(NUFIT61_NO, energy_MeV, rho, ye, antineutrino=False)
    hbar = effective_mass_squared_flavor(NUFIT61_NO, energy_MeV, rho, ye, antineutrino=True)
    energy_eV = energy_MeV * 1.0e6
    strength = 2.0 * energy_eV * mu_over_muB * MU_B_EV_PER_T * b_perp_T
    c = strength * np.exp(1j * coupling_phase) * magnetic_transition_matrix()
    out = np.block([[hnu, c], [c.conjugate().T, hbar]])
    return out


def run_0103() -> dict:
    e, rho, ye, L = 5.0, 80.0, 0.5, 0.001
    mu, b = 1.0e-11, 1.0e8
    psi = np.zeros(6, dtype=np.complex128)
    psi[0] = 1.0

    h = effective_spin_flavor(e, rho, ye, mu, b)
    herm = hermiticity_error(h)
    p = probability_vector(evolve_hermitian(psi, h, L, e))
    norm = abs(float(np.sum(p)) - 1.0)
    spin_transfer = float(np.sum(p[3:]))

    h_zero_mu = effective_spin_flavor(e, rho, ye, 0.0, b)
    p_zero_mu = probability_vector(evolve_hermitian(psi, h_zero_mu, L, e))
    p0100 = probability_vector(evolve_constant_density(pure_flavor(0), L, NUFIT61_NO, e, rho, ye))
    dec_mu = max(float(np.max(np.abs(p_zero_mu[:3] - p0100))), float(np.max(np.abs(p_zero_mu[3:]))))

    h_zero_b = effective_spin_flavor(e, rho, ye, mu, 0.0)
    p_zero_b = probability_vector(evolve_hermitian(psi, h_zero_b, L, e))
    dec_b = max(float(np.max(np.abs(p_zero_b[:3] - p0100))), float(np.max(np.abs(p_zero_b[3:]))))

    p_phase = probability_vector(evolve_hermitian(psi, effective_spin_flavor(e, rho, ye, mu, b, math.pi / 3.0), L, e))
    phase_total_spin = abs(float(np.sum(p_phase[3:])) - spin_transfer)

    gates = {
        "six_state_hermiticity": herm <= TOL,
        "probability_normalization": norm <= TOL,
        "zero_mu_decoupling": dec_mu <= TOL,
        "zero_field_decoupling": dec_b <= TOL,
        "nonzero_spin_flavor_transfer": spin_transfer > 1.0e-10,
        "global_coupling_phase_spin_invariance": phase_total_spin <= TOL,
        "finite_outputs": bool(np.all(np.isfinite(p))),
    }
    return {
        "benchmark": "NMIR-BENCHMARK-0103",
        "status": "PASS_0103_MAGNETIC_SPIN_FLAVOR_MATHEMATICAL_PREFLIGHT_NONTERMINAL" if all(gates.values()) else "FAIL_0103_MATHEMATICAL_PREFLIGHT",
        "gates": gates,
        "metrics": {
            "hermiticity_max_abs": herm,
            "normalization_abs_error": norm,
            "zero_mu_decoupling_max_abs": dec_mu,
            "zero_field_decoupling_max_abs": dec_b,
            "synthetic_spin_transfer_probability": spin_transfer,
            "coupling_phase_total_spin_abs_error": phase_total_spin,
        },
        "terminal_physics_execution_allowed": False,
        "terminal_status_ceiling": "BLOCKED_0103_MAGNETIC_AND_FIELD_AUTHORITY_UNPINNED",
    }


def light_mediator_a_eV2(
    rho_g_cm3: float,
    y_f: float,
    energy_MeV: float,
    coupling_product: float,
    mediator_mass_eV: float,
    antineutrino: bool = False,
) -> float:
    if rho_g_cm3 < 0 or not 0.0 <= y_f <= 1.0 or energy_MeV <= 0 or mediator_mass_eV <= 0:
        raise ValueError("invalid 0104 matter parameters")
    number_density_cm3 = N_A * rho_g_cm3 * y_f
    number_density_eV3 = number_density_cm3 * INV_CM3_TO_EV3
    vx_eV = coupling_product * number_density_eV3 / (mediator_mass_eV ** 2)
    a = 2.0 * energy_MeV * 1.0e6 * vx_eV
    return -a if antineutrino else a


def effective_light_mediator(
    energy_MeV: float,
    rho: float,
    ye: float,
    coupling_product: float,
    mediator_mass_eV: float,
    antineutrino: bool = False,
) -> np.ndarray:
    base = effective_mass_squared_flavor(NUFIT61_NO, energy_MeV, rho, ye, antineutrino=antineutrino)
    out = np.array(base, copy=True)
    out[0, 0] += light_mediator_a_eV2(rho, ye, energy_MeV, coupling_product, mediator_mass_eV, antineutrino)
    return out


def run_0104() -> dict:
    e, rho, ye, L = 5.0, 80.0, 0.5, 1234.5
    gprod, mx = 1.0e-12, 1.0e6
    h = effective_light_mediator(e, rho, ye, gprod, mx)
    herm = hermiticity_error(h)
    p = probability_vector(evolve_hermitian(pure_flavor(0), h, L, e))
    norm = abs(float(np.sum(p)) - 1.0)

    p_zero = probability_vector(evolve_hermitian(pure_flavor(0), effective_light_mediator(e, rho, ye, 0.0, mx), L, e))
    p0100 = probability_vector(evolve_constant_density(pure_flavor(0), L, NUFIT61_NO, e, rho, ye))
    zero_recovery = float(np.max(np.abs(p_zero - p0100)))
    nontrivial = float(np.max(np.abs(p - p0100)))

    a1 = abs(light_mediator_a_eV2(rho, ye, e, gprod, mx))
    a2 = abs(light_mediator_a_eV2(rho, ye, e, gprod, 2.0 * mx))
    heavy_ratio = a2 / a1 if a1 else float("nan")
    anu = light_mediator_a_eV2(rho, ye, e, gprod, mx, False)
    aan = light_mediator_a_eV2(rho, ye, e, gprod, mx, True)

    gates = {
        "hamiltonian_hermiticity": herm <= TOL,
        "probability_normalization": norm <= TOL,
        "zero_coupling_recovery": zero_recovery <= TOL,
        "heavy_mediator_inverse_square_scaling": abs(heavy_ratio - 0.25) <= 1.0e-15,
        "nonzero_fixture_nontrivial": nontrivial > 1.0e-10,
        "antineutrino_potential_sign": abs(anu + aan) <= 1.0e-18,
        "finite_outputs": bool(np.all(np.isfinite(p))),
    }
    return {
        "benchmark": "NMIR-BENCHMARK-0104",
        "status": "PASS_0104_LIGHT_MEDIATOR_MATHEMATICAL_PREFLIGHT_NONTERMINAL" if all(gates.values()) else "FAIL_0104_MATHEMATICAL_PREFLIGHT",
        "gates": gates,
        "metrics": {
            "hermiticity_max_abs": herm,
            "normalization_abs_error": norm,
            "zero_coupling_probability_max_abs": zero_recovery,
            "synthetic_vs_standard_probability_max_abs": nontrivial,
            "heavy_mass_scaling_ratio": heavy_ratio,
            "synthetic_Ax_eV2": a1,
        },
        "terminal_physics_execution_allowed": False,
        "terminal_status_ceiling": "BLOCKED_0104_MEDIATOR_PARAMETER_AND_RANGE_AUTHORITY_UNPINNED",
    }


def run_all() -> dict:
    results = {"0101": run_0101(), "0102": run_0102(), "0103": run_0103(), "0104": run_0104()}
    all_pass = all(v["status"].startswith("PASS_") for v in results.values())
    return {
        "suite": "NMIR-KNOWN-MODEL-PREFLIGHT-0101-0104",
        "preflight_all_pass": all_pass,
        "terminal_physics_execution_allowed": False,
        "results": results,
    }


if __name__ == "__main__":
    print(json.dumps(run_all(), indent=2, sort_keys=True))
