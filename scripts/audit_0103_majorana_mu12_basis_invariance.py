#!/usr/bin/env python3
"""Nonterminal basis-invariance audit for NMIR benchmark 0103.

This verifies the coordinate transformation for a single antisymmetric Majorana
mu_12 transition-moment fixture.  All numerical mixing parameters here are
synthetic test fixtures, not physical PMNS authority.
"""

from __future__ import annotations

import json
import numpy as np

TOL = 1.0e-12
EVOL_TOL = 1.0e-11


def _pmns_fixture() -> np.ndarray:
    t12, t13, t23, delta = 0.57, 0.15, 0.79, 1.17
    s12, c12 = np.sin(t12), np.cos(t12)
    s13, c13 = np.sin(t13), np.cos(t13)
    s23, c23 = np.sin(t23), np.cos(t23)
    em = np.exp(-1j * delta)
    ep = np.exp(1j * delta)
    return np.array(
        [
            [c12*c13, s12*c13, s13*em],
            [-s12*c23-c12*s23*s13*ep, c12*c23-s12*s23*s13*ep, s23*c13],
            [s12*s23-c12*c23*s13*ep, -c12*s23-s12*c23*s13*ep, c23*c13],
        ],
        dtype=np.complex128,
    )


def _block_diag(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    out = np.zeros((a.shape[0] + b.shape[0], a.shape[1] + b.shape[1]), dtype=np.complex128)
    out[: a.shape[0], : a.shape[1]] = a
    out[a.shape[0] :, a.shape[1] :] = b
    return out


def _assemble(hn: np.ndarray, ha: np.ndarray, m: np.ndarray) -> np.ndarray:
    return np.block([[hn, m], [m.conj().T, ha]]).astype(np.complex128)


def _propagator(h: np.ndarray, length: float) -> np.ndarray:
    vals, vecs = np.linalg.eigh(h)
    return (vecs * np.exp(-1j * vals * length)) @ vecs.conj().T


def run_audit() -> dict:
    u = _pmns_fixture()
    eye3 = np.eye(3, dtype=np.complex128)
    eye6 = np.eye(6, dtype=np.complex128)
    t6 = _block_diag(u, u.conj())

    d = np.diag([0.0, 0.13, 0.41]).astype(np.complex128)
    vf = np.diag([0.07, 0.0, 0.0]).astype(np.complex128)
    g = 0.025
    length = 3.7

    km = np.zeros((3, 3), dtype=np.complex128)
    km[0, 1] = 1.0
    km[1, 0] = -1.0
    mm = g * km

    hnu_m = d + u.conj().T @ vf @ u
    hanti_m = d - u.T @ vf @ u.conj()
    h6_m = _assemble(hnu_m, hanti_m, mm)

    hnu_f = u @ d @ u.conj().T + vf
    hanti_f = u.conj() @ d @ u.T - vf
    mf = u @ mm @ u.T
    h6_f_explicit = _assemble(hnu_f, hanti_f, mf)
    h6_f_similarity = t6 @ h6_m @ t6.conj().T

    raw = np.array(
        [1.0 + 0.2j, -0.3 + 0.7j, 0.4 - 0.1j, 0.2 + 0.5j, -0.6 + 0.1j, 0.3 - 0.4j],
        dtype=np.complex128,
    )
    psi_m0 = raw / np.linalg.norm(raw)
    psi_f0 = t6 @ psi_m0

    sm = _propagator(h6_m, length)
    sf = _propagator(h6_f_explicit, length)
    psi_m1 = sm @ psi_m0
    psi_f1_direct = sf @ psi_f0
    psi_f1_from_mass = t6 @ psi_m1

    # Zero-magnetic-coupling reduction from a neutrino-only state.
    h6_zero = _assemble(hnu_m, hanti_m, np.zeros((3, 3), dtype=np.complex128))
    psi_nu0 = np.zeros(6, dtype=np.complex128)
    psi_nu0[0] = 1.0
    psi_zero1 = _propagator(h6_zero, length) @ psi_nu0

    metrics = {
        "U_unitarity_residual": float(np.max(np.abs(u.conj().T @ u - eye3))),
        "T6_unitarity_residual": float(np.max(np.abs(t6.conj().T @ t6 - eye6))),
        "H6_mass_hermiticity_residual": float(np.max(np.abs(h6_m - h6_m.conj().T))),
        "H6_flavor_hermiticity_residual": float(np.max(np.abs(h6_f_explicit - h6_f_explicit.conj().T))),
        "flavor_similarity_residual": float(np.max(np.abs(h6_f_explicit - h6_f_similarity))),
        "magnetic_congruence_residual": float(np.max(np.abs(h6_f_explicit[:3, 3:] - u @ mm @ u.T))),
        "magnetic_antisymmetry_residual": float(np.max(np.abs(mf.T + mf))),
        "evolved_state_basis_residual": float(np.max(np.abs(psi_f1_direct - psi_f1_from_mass))),
        "probability_basis_residual": float(np.max(np.abs(np.abs(psi_f1_direct)**2 - np.abs(psi_f1_from_mass)**2))),
        "mass_norm_residual": float(abs(np.vdot(psi_m1, psi_m1).real - 1.0)),
        "flavor_norm_residual": float(abs(np.vdot(psi_f1_direct, psi_f1_direct).real - 1.0)),
        "zero_g_antineutrino_leakage": float(np.max(np.abs(psi_zero1[3:]))),
    }

    gates = {
        "U_is_unitary": metrics["U_unitarity_residual"] <= TOL,
        "T6_is_unitary": metrics["T6_unitarity_residual"] <= TOL,
        "H6_mass_is_hermitian": metrics["H6_mass_hermiticity_residual"] <= TOL,
        "H6_flavor_is_hermitian": metrics["H6_flavor_hermiticity_residual"] <= TOL,
        "explicit_flavor_equals_similarity_transform": metrics["flavor_similarity_residual"] <= TOL,
        "magnetic_block_uses_unitary_congruence": metrics["magnetic_congruence_residual"] <= TOL,
        "majorana_transition_matrix_stays_antisymmetric": metrics["magnetic_antisymmetry_residual"] <= TOL,
        "evolution_is_basis_invariant": metrics["evolved_state_basis_residual"] <= EVOL_TOL,
        "flavor_probabilities_are_basis_invariant": metrics["probability_basis_residual"] <= EVOL_TOL,
        "mass_evolution_conserves_norm": metrics["mass_norm_residual"] <= TOL,
        "flavor_evolution_conserves_norm": metrics["flavor_norm_residual"] <= TOL,
        "zero_magnetic_coupling_decouples_sectors": metrics["zero_g_antineutrino_leakage"] <= TOL,
    }

    passed = all(gates.values())
    return {
        "audit": "NMIR-0103-MAJORANA-MU12-BASIS-INVARIANCE",
        "status": (
            "PASS_0103_MAJORANA_MU12_BASIS_INVARIANCE_NONTERMINAL"
            if passed
            else "FAIL_0103_MAJORANA_MU12_BASIS_INVARIANCE"
        ),
        "gates": gates,
        "metrics": metrics,
        "interpretation": {
            "mass_to_flavor_magnetic_map": "M_f = U M_m U^T",
            "fixture_is_physical_PMNS_authority": False,
            "majorana_mu12_representation_interface_validated": passed,
            "terminal_parameter_authority_closed": False,
            "betelgeuse_pathwise_Bperp_authority_closed": False,
            "terminal_status_ceiling": "BLOCKED_0103_BETELGEUSE_PATHWISE_VECTOR_FIELD_AUTHORITY",
        },
    }


if __name__ == "__main__":
    print(json.dumps(run_audit(), indent=2, sort_keys=True))
