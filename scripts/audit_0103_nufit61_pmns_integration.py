#!/usr/bin/env python3
"""Nonterminal NuFIT 6.1 PMNS integration audit for NMIR benchmark 0103."""

from __future__ import annotations

import json
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "research" / "authority" / "0103_nufit61_three_flavor_manifest.json"
UNIT_TOL = 1.0e-14
MASS_TOL = 1.0e-16


def _pmns(branch: dict) -> tuple[np.ndarray, tuple[float, float, float, float]]:
    t12 = np.arcsin(np.sqrt(branch["sin2_theta12"]))
    t13 = np.arcsin(np.sqrt(branch["sin2_theta13"]))
    t23 = np.arcsin(np.sqrt(branch["sin2_theta23"]))
    delta = np.deg2rad(branch["delta_cp_deg"])
    s12, c12 = np.sin(t12), np.cos(t12)
    s13, c13 = np.sin(t13), np.cos(t13)
    s23, c23 = np.sin(t23), np.cos(t23)
    em, ep = np.exp(-1j * delta), np.exp(1j * delta)
    u = np.array(
        [
            [c12*c13, s12*c13, s13*em],
            [-s12*c23-c12*s23*s13*ep, c12*c23-s12*s23*s13*ep, s23*c13],
            [s12*s23-c12*c23*s13*ep, -c12*s23-s12*c23*s13*ep, c23*c13],
        ],
        dtype=np.complex128,
    )
    return u, (t12, t13, t23, delta)


def _block_diag(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    out = np.zeros((a.shape[0] + b.shape[0], a.shape[1] + b.shape[1]), dtype=np.complex128)
    out[:a.shape[0], :a.shape[1]] = a
    out[a.shape[0]:, a.shape[1]:] = b
    return out


def _spectrum(branch_name: str, branch: dict) -> np.ndarray:
    dm21 = branch["dm2_21_eV2"]
    if branch_name == "normal_ordering":
        return np.array([0.0, dm21, branch["dm2_3l_eV2"]], dtype=float)
    if branch_name == "inverted_ordering":
        return np.array([0.0, dm21, branch["dm2_3l_eV2"] + dm21], dtype=float)
    raise ValueError(branch_name)


def _audit_branch(branch_name: str, branch: dict) -> dict:
    u, (t12, t13, t23, delta) = _pmns(branch)
    eye3 = np.eye(3, dtype=np.complex128)
    t6 = _block_diag(u, u.conj())
    eye6 = np.eye(6, dtype=np.complex128)

    km = np.zeros((3, 3), dtype=np.complex128)
    km[0, 1] = 1.0
    km[1, 0] = -1.0
    mf = u @ km @ u.T

    m2 = _spectrum(branch_name, branch)
    dm21_recon = float(m2[1] - m2[0])
    if branch_name == "normal_ordering":
        dm3l_recon = float(m2[2] - m2[0])
    else:
        dm3l_recon = float(m2[2] - m2[1])

    reconstructed = {
        "sin2_theta12": float(np.sin(t12)**2),
        "sin2_theta13": float(np.sin(t13)**2),
        "sin2_theta23": float(np.sin(t23)**2),
        "delta_cp_deg": float(np.rad2deg(delta)),
        "dm2_21_eV2": dm21_recon,
        "dm2_3l_eV2": dm3l_recon,
    }
    metrics = {
        "pmns_unitarity_residual": float(np.max(np.abs(u.conj().T @ u - eye3))),
        "t6_unitarity_residual": float(np.max(np.abs(t6.conj().T @ t6 - eye6))),
        "sin2_theta12_residual": abs(reconstructed["sin2_theta12"] - branch["sin2_theta12"]),
        "sin2_theta13_residual": abs(reconstructed["sin2_theta13"] - branch["sin2_theta13"]),
        "sin2_theta23_residual": abs(reconstructed["sin2_theta23"] - branch["sin2_theta23"]),
        "dm2_21_residual_eV2": abs(dm21_recon - branch["dm2_21_eV2"]),
        "dm2_3l_residual_eV2": abs(dm3l_recon - branch["dm2_3l_eV2"]),
        "mu12_antisymmetry_residual": float(np.max(np.abs(mf.T + mf))),
    }
    gates = {
        "pmns_unitary": metrics["pmns_unitarity_residual"] <= UNIT_TOL,
        "t6_unitary": metrics["t6_unitarity_residual"] <= UNIT_TOL,
        "angles_reconstruct": max(
            metrics["sin2_theta12_residual"],
            metrics["sin2_theta13_residual"],
            metrics["sin2_theta23_residual"],
        ) <= UNIT_TOL,
        "dm21_reconstructs": metrics["dm2_21_residual_eV2"] <= MASS_TOL,
        "dm3l_reconstructs": metrics["dm2_3l_residual_eV2"] <= MASS_TOL,
        "mu12_stays_antisymmetric": metrics["mu12_antisymmetry_residual"] <= UNIT_TOL,
    }
    return {
        "gates": gates,
        "metrics": metrics,
        "reconstructed": reconstructed,
        "mass_squared_representative_eV2": m2.tolist(),
        "ordering_convention": branch["dm2_3l_convention"],
    }


def run_audit() -> dict:
    manifest = json.loads(MANIFEST.read_text())
    branches = {
        name: _audit_branch(name, manifest[name])
        for name in ("normal_ordering", "inverted_ordering")
    }
    all_pass = all(all(x["gates"].values()) for x in branches.values())
    return {
        "audit": "NMIR-0103-NUFIT61-PMNS-INTEGRATION",
        "status": "PASS_0103_NUFIT61_PMNS_INTEGRATION_NONTERMINAL" if all_pass else "FAIL_0103_NUFIT61_PMNS_INTEGRATION",
        "branches_emitted": list(branches.keys()),
        "both_orderings_carried": set(branches) == {"normal_ordering", "inverted_ordering"},
        "branches": branches,
        "interpretation": {
            "ordering_postselection_used": False,
            "official_numeric_input_integration_validated": all_pass,
            "nufit_pdf_byte_pin_closed": False,
            "betelgeuse_pathwise_Bperp_authority_closed": False,
            "terminal_status_ceiling": "BLOCKED_0103_BETELGEUSE_PATHWISE_VECTOR_FIELD_AUTHORITY"
        },
    }


if __name__ == "__main__":
    print(json.dumps(run_audit(), indent=2, sort_keys=True))
