#!/usr/bin/env python3
"""Machine-checkable medium-transfer audit for NMIR benchmark 0102.

This is an authority/interface audit, not a terminal NSI fit.  It formalizes why
an Earth-effective epsilon matrix cannot in general be reused in a stellar
medium, while an electron-only vector NSI maps exactly onto the already-frozen
0102 constant-epsilon Hamiltonian.
"""

from __future__ import annotations

import json

import numpy as np

TOL = 1.0e-12
YN_EARTH_REFERENCE = 1.051  # documented comparison fixture, not a fitted NMIR input


def neutron_to_electron_ratio(ye: float) -> float:
    """Return N_n/N_e for electrically neutral nucleonic matter.

    With N_e=N_p and Ye=N_e/(N_p+N_n), Y_n=N_n/N_e=(1-Ye)/Ye.
    """
    if not 0.0 < ye <= 1.0:
        raise ValueError("require 0 < Ye <= 1")
    return (1.0 - ye) / ye


def effective_vector_epsilon(
    epsilon_e: np.ndarray,
    epsilon_u: np.ndarray,
    epsilon_d: np.ndarray,
    ye: float,
) -> np.ndarray:
    """Map charged-fermion vector NSI coefficients into propagation epsilon.

    In electrically neutral matter:
      N_u/N_e = 2 + Y_n
      N_d/N_e = 1 + 2 Y_n
    so epsilon_eff = epsilon_e + (2+Y_n) epsilon_u
                                 + (1+2Y_n) epsilon_d.
    """
    yn = neutron_to_electron_ratio(ye)
    e = np.asarray(epsilon_e, dtype=np.complex128)
    u = np.asarray(epsilon_u, dtype=np.complex128)
    d = np.asarray(epsilon_d, dtype=np.complex128)
    if e.shape != (3, 3) or u.shape != (3, 3) or d.shape != (3, 3):
        raise ValueError("epsilon_e/u/d must each be 3x3")
    return e + (2.0 + yn) * u + (1.0 + 2.0 * yn) * d


def _fixture_matrix() -> np.ndarray:
    eps = np.zeros((3, 3), dtype=np.complex128)
    eps[0, 0] = 0.05
    eps[2, 2] = -0.02
    z = 0.01 * np.exp(1j * np.pi / 5.0)
    eps[0, 1] = z
    eps[1, 0] = np.conjugate(z)
    return eps


def run_audit() -> dict:
    zeros = np.zeros((3, 3), dtype=np.complex128)
    eps_e = _fixture_matrix()

    # Gate 1: electron-only vector NSI is composition-independent and therefore
    # exactly matches the frozen constant-epsilon 0102 interface.
    ye_grid = [0.20, 0.35, 0.50, 0.70, 1.00]
    electron_maps = [effective_vector_epsilon(eps_e, zeros, zeros, ye) for ye in ye_grid]
    electron_only_max_spread = max(
        float(np.max(np.abs(m - eps_e))) for m in electron_maps
    )

    # Gate 2: quark NSI generically changes with composition.
    eps_u = 0.04 * np.eye(3, dtype=np.complex128)
    eps_d = -0.015 * np.eye(3, dtype=np.complex128)
    q_lo = effective_vector_epsilon(zeros, eps_u, eps_d, 0.35)
    q_hi = effective_vector_epsilon(zeros, eps_u, eps_d, 0.70)
    quark_composition_change = float(np.max(np.abs(q_lo - q_hi)))

    # Gate 3: an Earth-effective epsilon does not uniquely identify the
    # underlying charged-fermion operator.  Construct two operator-level models
    # with identical epsilon_eff at the Earth reference composition, then show
    # they separate in a different medium.
    target = np.zeros((3, 3), dtype=np.complex128)
    target[0, 0] = 0.10

    # Model A: electron-only.
    a_e, a_u, a_d = target, zeros, zeros
    # Model B: up-quark-only, normalized to reproduce the same Earth effective
    # coefficient at Y_n^Earth=1.051.
    b_e = zeros
    b_u = target / (2.0 + YN_EARTH_REFERENCE)
    b_d = zeros

    ye_earth_reference = 1.0 / (1.0 + YN_EARTH_REFERENCE)
    a_earth = effective_vector_epsilon(a_e, a_u, a_d, ye_earth_reference)
    b_earth = effective_vector_epsilon(b_e, b_u, b_d, ye_earth_reference)
    earth_degeneracy_error = float(np.max(np.abs(a_earth - b_earth)))

    ye_other = 0.70
    a_other = effective_vector_epsilon(a_e, a_u, a_d, ye_other)
    b_other = effective_vector_epsilon(b_e, b_u, b_d, ye_other)
    other_medium_separation = float(np.max(np.abs(a_other - b_other)))

    # Gate 4: Ye <-> Yn algebra is self-consistent for the declared neutral
    # nucleonic matter convention.
    yn_roundtrip_errors = []
    for ye in ye_grid:
        yn = neutron_to_electron_ratio(ye)
        ye_back = 1.0 / (1.0 + yn)
        yn_roundtrip_errors.append(abs(ye_back - ye))
    ye_yn_roundtrip_max_error = max(yn_roundtrip_errors)

    gates = {
        "electron_only_is_constant_epsilon": electron_only_max_spread <= TOL,
        "quark_nsi_is_composition_dependent": quark_composition_change > 1.0e-6,
        "same_earth_effective_can_hide_operator_degeneracy": earth_degeneracy_error <= TOL,
        "operator_degeneracy_breaks_in_other_medium": other_medium_separation > 1.0e-6,
        "ye_to_yn_roundtrip": ye_yn_roundtrip_max_error <= TOL,
    }

    return {
        "audit": "NMIR-0102-NSI-MEDIUM-TRANSFER-AUTHORITY",
        "status": (
            "PASS_0102_MEDIUM_TRANSFER_INTERFACE_AUDIT_NONTERMINAL"
            if all(gates.values())
            else "FAIL_0102_MEDIUM_TRANSFER_INTERFACE_AUDIT"
        ),
        "gates": gates,
        "metrics": {
            "electron_only_max_spread": electron_only_max_spread,
            "quark_fixture_composition_change": quark_composition_change,
            "earth_effective_operator_degeneracy_error": earth_degeneracy_error,
            "other_medium_operator_separation": other_medium_separation,
            "ye_yn_roundtrip_max_error": ye_yn_roundtrip_max_error,
            "earth_reference_Yn": YN_EARTH_REFERENCE,
            "earth_reference_Ye": ye_earth_reference,
            "other_medium_Ye": ye_other,
        },
        "interpretation": {
            "electron_only_vector_maps_to_frozen_0102": True,
            "earth_effective_epsilon_transferable_without_operator_identity": False,
            "quark_vector_nsi_requires_composition_mapping": True,
            "source_profile_rho_Ye_is_sufficient_to_compute_Yn_under_declared_neutral_nucleonic_convention": True,
            "terminal_parameter_authority_closed": False,
            "terminal_status_ceiling": "BLOCKED_0102_NSI_PARAMETER_AUTHORITY_UNPINNED",
        },
    }


if __name__ == "__main__":
    print(json.dumps(run_audit(), indent=2, sort_keys=True))
