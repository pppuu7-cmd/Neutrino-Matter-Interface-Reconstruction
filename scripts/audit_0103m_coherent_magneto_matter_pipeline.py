#!/usr/bin/env python3
import csv
import json
import math
from pathlib import Path
import numpy as np

SCOPE = "NONTERMINAL_SYNTHETIC_ENGINEERING_ONLY"
STATE_ID = "0103M_SYNTHETIC_COREGISTERED_STATE_V1"


def pmns_fixture():
    th12, th13, th23, delta = 0.57, 0.15, 0.79, 1.17
    c12, s12 = np.cos(th12), np.sin(th12)
    c13, s13 = np.cos(th13), np.sin(th13)
    c23, s23 = np.cos(th23), np.sin(th23)
    ep, em = np.exp(1j * delta), np.exp(-1j * delta)
    return np.array([
        [c12*c13, s12*c13, s13*em],
        [-s12*c23-c12*s23*s13*ep, c12*c23-s12*s23*s13*ep, s23*c13],
        [s12*s23-c12*c23*s13*ep, -c12*s23-s12*c23*s13*ep, c23*c13],
    ], dtype=complex)


def transform6(U):
    T = np.zeros((6, 6), dtype=complex)
    T[:3, :3] = U
    T[3:, 3:] = U.conj()
    return T


def analytic_channels(x, y, z):
    bx = 0.7 + 0.2*x - 0.15*y + 0.1*z + 0.05*x*y - 0.04*x*z + 0.03*y*z + 0.02*x*y*z
    by = -0.3 + 0.1*x + 0.25*y - 0.2*z - 0.03*x*y + 0.06*x*z + 0.01*y*z - 0.015*x*y*z
    bz = 0.4 - 0.12*x + 0.08*y + 0.18*z + 0.02*x*y + 0.03*x*z - 0.05*y*z + 0.01*x*y*z
    rho = 1.4 + 0.12*x - 0.08*y + 0.06*z + 0.03*x*y - 0.02*x*z + 0.015*y*z + 0.01*x*y*z
    ye = 0.45 + 0.025*x + 0.02*y - 0.015*z + 0.008*x*y + 0.004*x*z - 0.005*y*z + 0.003*x*y*z
    return np.array([bx, by, bz, rho, ye], dtype=float)


def build_state():
    axis = np.linspace(-1.0, 1.0, 9)
    data = np.empty((9, 9, 9, 5), dtype=float)
    for i, x in enumerate(axis):
        for j, y in enumerate(axis):
            for k, z in enumerate(axis):
                data[i, j, k] = analytic_channels(x, y, z)
    return axis, data


def trilinear(axis, data, p):
    idx, frac = [], []
    for q in p:
        if q < axis[0] or q > axis[-1]:
            raise ValueError("ray extrapolation is forbidden")
        i = int(np.searchsorted(axis, q, side="right") - 1)
        i = min(max(i, 0), len(axis)-2)
        idx.append(i)
        frac.append(float((q-axis[i])/(axis[i+1]-axis[i])))
    i, j, k = idx
    tx, ty, tz = frac
    out = np.zeros(data.shape[-1], dtype=float)
    for di in (0, 1):
        wx = tx if di else 1.0-tx
        for dj in (0, 1):
            wy = ty if dj else 1.0-ty
            for dk in (0, 1):
                wz = tz if dk else 1.0-tz
                out += wx*wy*wz*data[i+di, j+dj, k+dk]
    return out


def geometry():
    p0 = np.array([-0.75, -0.60, -0.55])
    p1 = np.array([0.72, 0.65, 0.58])
    ray = p1-p0
    n = ray/np.linalg.norm(ray)
    anchor = np.array([0.0, 0.0, 1.0]) if abs(n[2]) < 0.9 else np.array([0.0, 1.0, 0.0])
    e1 = np.cross(n, anchor); e1 /= np.linalg.norm(e1)
    e2 = np.cross(n, e1)
    return p0, p1, ray, n, e1, e2


def sample_state(s, axis, data):
    p0, _, ray, n, e1, e2 = geometry()
    p = p0 + s*ray
    q = trilinear(axis, data, p)
    B = q[:3]
    bperp = B - np.dot(B, n)*n
    bcomplex = np.dot(bperp, e1) + 1j*np.dot(bperp, e2)
    return p, q, bperp, bcomplex


def hamiltonian(s, g, axis, data, U):
    _, q, _, bcomplex = sample_state(s, axis, data)
    rho, ye = q[3], q[4]
    Hv = np.diag([0.0, 0.4, 1.1]).astype(complex)
    v = 0.15*rho*ye
    Vf = np.diag([v, 0.0, 0.0]).astype(complex)
    Hn = Hv + U.conj().T @ Vf @ U
    Hb = Hv - U.T @ Vf @ U.conj()
    K = np.zeros((3, 3), dtype=complex)
    K[0, 1], K[1, 0] = 1.0, -1.0
    M = g*bcomplex*K
    return np.block([[Hn, M], [M.conj().T, Hb]])


def propagate(g, N, axis, data):
    U = pmns_fixture(); T = transform6(U)
    psi_f = np.zeros(6, dtype=complex); psi_f[0] = 1.0
    psi = T.conj().T @ psi_f
    ds = 1.0/N; max_herm = 0.0
    for i in range(N):
        s = (i+0.5)*ds
        H = hamiltonian(s, g, axis, data, U)
        max_herm = max(max_herm, float(np.max(np.abs(H-H.conj().T))))
        w, V = np.linalg.eigh(H)
        psi = V @ (np.exp(-1j*w*ds) * (V.conj().T @ psi))
    psi_f = T @ psi
    return psi_f, max_herm


def ray_rows(axis, data):
    _, _, _, n, _, _ = geometry()
    rows = []
    for s in np.linspace(0.0, 1.0, 257):
        p, q, bp, bc = sample_state(float(s), axis, data)
        exact = analytic_channels(*p)
        rows.append({
            "s": float(s), "x": float(p[0]), "y": float(p[1]), "z": float(p[2]),
            "Bx": float(q[0]), "By": float(q[1]), "Bz": float(q[2]),
            "rho": float(q[3]), "Ye": float(q[4]),
            "Bperp_x": float(bp[0]), "Bperp_y": float(bp[1]), "Bperp_z": float(bp[2]),
            "Bperp_abs": float(abs(bc)),
            "interp_residual": float(np.max(np.abs(q-exact))),
            "orthogonality_residual": float(abs(np.dot(n, bp))),
            "bperp_magnitude_residual": float(abs(np.linalg.norm(bp)-math.sqrt(max(0.0, np.dot(q[:3], q[:3])-np.dot(q[:3], n)**2))))
        })
    return rows


def run_audit():
    axis, data = build_state()
    rows = ray_rows(axis, data)
    pos, herm_pos = propagate(0.35, 512, axis, data)
    zero, herm_zero = propagate(0.0, 512, axis, data)
    repeat, _ = propagate(0.35, 512, axis, data)
    pp = np.abs(pos)**2; p0 = np.abs(zero)**2; pr = np.abs(repeat)**2
    interp = max(r["interp_residual"] for r in rows)
    orth = max(r["orthogonality_residual"] for r in rows)
    mag = max(r["bperp_magnitude_residual"] for r in rows)
    norm = float(abs(np.vdot(pos, pos).real-1.0))
    psum = float(abs(np.sum(pp)-1.0))
    zero_leak = float(np.sum(p0[3:]))
    positive = float(np.sum(pp[3:]))
    repeat_res = float(np.max(np.abs(pp-pr)))
    finite_bounded = bool(np.all(np.isfinite(pp)) and np.min(pp) >= -1e-12 and np.max(pp) <= 1+1e-12)
    no_extrap = all(np.all(np.abs(np.array([r["x"],r["y"],r["z"]])) <= 1.0+1e-15) for r in rows)
    metrics = {
        "scope": SCOPE, "state_id": STATE_ID, "grid_shape": [9,9,9], "ray_samples": len(rows),
        "common_state_grid_ray": True, "no_extrapolation": no_extrap,
        "max_trilinear_interpolation_residual": interp,
        "max_bperp_orthogonality_residual": orth,
        "max_bperp_magnitude_residual": mag,
        "max_hamiltonian_hermiticity_residual": max(herm_pos, herm_zero),
        "norm_residual": norm, "probability_sum_residual": psum,
        "zero_g_antineutrino_leakage": zero_leak,
        "positive_control_antineutrino_probability": positive,
        "repeat_probability_residual": repeat_res,
        "final_probabilities": pp.tolist(),
    }
    gates = {
        "coregistered_identity": bool(metrics["common_state_grid_ray"] and no_extrap),
        "trilinear_exactness": interp <= 1e-12,
        "bperp_orthogonality": orth <= 1e-12,
        "bperp_magnitude_consistency": mag <= 1e-12,
        "hamiltonian_hermitian": metrics["max_hamiltonian_hermiticity_residual"] <= 1e-12,
        "norm_conserved": norm <= 1e-10,
        "probability_sum": psum <= 1e-10,
        "finite_bounded_probabilities": finite_bounded,
        "zero_control": zero_leak <= 1e-12,
        "deterministic_repeat": repeat_res <= 1e-14,
        "positive_control": positive > 1e-8,
        "scope_guard": SCOPE == "NONTERMINAL_SYNTHETIC_ENGINEERING_ONLY",
    }
    out = {"audit":"NMIR-0103M-COHERENT-SYNTHETIC-MAGNETO-MATTER-PIPELINE", "metrics":metrics, "gates":gates}
    out["status"] = "PASS_0103M_COHERENT_SYNTHETIC_MAGNETO_MATTER_PIPELINE_NONTERMINAL" if all(gates.values()) else "FAIL_0103M_COHERENT_SYNTHETIC_MAGNETO_MATTER_PIPELINE"
    return out, rows


def write_csv(rows, path):
    with Path(path).open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)


if __name__ == "__main__":
    out, rows = run_audit()
    write_csv(rows, "0103m_ray_samples.csv")
    print(json.dumps(out, indent=2, sort_keys=True))
    if not all(out["gates"].values()):
        raise SystemExit(1)
