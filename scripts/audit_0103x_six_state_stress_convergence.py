#!/usr/bin/env python3
import csv
import json
from pathlib import Path
import numpy as np

SCOPE = "NONTERMINAL_SYNTHETIC_NUMERICAL_STRESS_ONLY"
G_VALUES = [0.0, 1e-3, 1e-2, 1e-1, 1.0]
N_VALUES = [64, 128, 256, 512, 1024]
N_REF = 4096


def pmns_fixture():
    th12, th13, th23, delta = 0.57, 0.15, 0.79, 1.17
    c12, s12 = np.cos(th12), np.sin(th12)
    c13, s13 = np.cos(th13), np.sin(th13)
    c23, s23 = np.cos(th23), np.sin(th23)
    ep, em = np.exp(1j*delta), np.exp(-1j*delta)
    return np.array([
        [c12*c13, s12*c13, s13*em],
        [-s12*c23-c12*s23*s13*ep, c12*c23-s12*s23*s13*ep, s23*c13],
        [s12*s23-c12*c23*s13*ep, -c12*s23-s12*c23*s13*ep, c23*c13],
    ], dtype=complex)


def transform6(U):
    T = np.zeros((6,6), dtype=complex)
    T[:3,:3] = U
    T[3:,3:] = U.conj()
    return T


def hamiltonian(s, g, U):
    Hv = np.array([
        [0.0, 0.03+0.01j, 0.015-0.008j],
        [0.03-0.01j, 0.45, 0.025+0.012j],
        [0.015+0.008j, 0.025-0.012j, 1.2],
    ], dtype=complex)
    v = 0.55*(1.0 + 0.3*np.sin(2*np.pi*s) + 0.1*np.cos(5*np.pi*s))
    Vf = np.diag([v,0.0,0.0]).astype(complex)
    Hn = Hv + U.conj().T @ Vf @ U
    Hb = Hv.conj() - U.T @ Vf @ U.conj()
    amp = 0.55 + 0.25*np.sin(3*np.pi*s) + 0.1*np.cos(7*np.pi*s)
    phase = 0.8*np.sin(2*np.pi*s) + 0.35*np.cos(3*np.pi*s)
    b = amp*np.exp(1j*phase)
    K = np.zeros((3,3), dtype=complex)
    K[0,1], K[1,0] = 1.0, -1.0
    M = g*b*K
    return np.block([[Hn,M],[M.conj().T,Hb]])


def propagate(g, N):
    U = pmns_fixture(); T = transform6(U)
    psi_f = np.zeros(6, dtype=complex); psi_f[0] = 1.0
    psi = T.conj().T @ psi_f
    ds = 1.0/N; max_herm = 0.0
    for i in range(N):
        s = (i+0.5)*ds
        H = hamiltonian(s,g,U)
        max_herm = max(max_herm, float(np.max(np.abs(H-H.conj().T))))
        w,V = np.linalg.eigh(H)
        psi = V @ (np.exp(-1j*w*ds) * (V.conj().T @ psi))
    psi_f = T @ psi
    p = np.abs(psi_f)**2
    return p, float(abs(np.vdot(psi_f,psi_f).real-1.0)), max_herm


def run_audit():
    rows=[]; max_herm=0.0; max_norm=0.0; max_psum=0.0; max1024=0.0
    bounded=True; zero_leak=0.0; convergence_improves=True; positive=0.0
    refs={g: propagate(g,N_REF)[0] for g in G_VALUES}
    for g in G_VALUES:
        e64=None
        for N in N_VALUES:
            p,norm,herm=propagate(g,N)
            err=float(np.max(np.abs(p-refs[g])))
            anti=float(np.sum(p[3:]))
            if N==64: e64=err
            if N==1024:
                max1024=max(max1024,err)
                if g!=0.0: convergence_improves = convergence_improves and (err < e64)
            if g==0.0: zero_leak=max(zero_leak,anti)
            else: positive=max(positive,anti)
            max_herm=max(max_herm,herm); max_norm=max(max_norm,norm)
            max_psum=max(max_psum,float(abs(np.sum(p)-1.0)))
            bounded = bounded and bool(np.all(np.isfinite(p)) and np.min(p)>=-1e-12 and np.max(p)<=1+1e-12)
            rows.append({"g":g,"N":N,"linf_probability_error_vs_Nref":err,"norm_residual":norm,"probability_sum_residual":float(abs(np.sum(p)-1.0)),"hermiticity_residual":herm,"antineutrino_probability":anti})
    p1,_,_=propagate(1.0,1024); p2,_,_=propagate(1.0,1024)
    repeat=float(np.max(np.abs(p1-p2)))
    metrics={
        "scope":SCOPE,"couplings":G_VALUES,"resolutions":N_VALUES,"reference_resolution":N_REF,
        "max_hamiltonian_hermiticity_residual":max_herm,
        "max_norm_residual":max_norm,"max_probability_sum_residual":max_psum,
        "max_1024_probability_error_vs_reference":max1024,
        "zero_g_max_antineutrino_leakage":zero_leak,
        "max_nonzero_g_antineutrino_probability":positive,
        "convergence_improves_64_to_1024_for_each_nonzero_g":bool(convergence_improves),
        "repeat_1024_probability_residual":repeat,
    }
    gates={
        "hamiltonian_hermitian":max_herm<=1e-12,
        "norm_conserved":max_norm<=1e-10,
        "probability_sum":max_psum<=1e-10,
        "finite_bounded_probabilities":bool(bounded),
        "zero_control":zero_leak<=1e-12,
        "refinement_improves":bool(convergence_improves),
        "1024_accuracy":max1024<=1e-6,
        "deterministic_repeat":repeat<=1e-14,
        "positive_control":positive>1e-8,
        "scope_guard":SCOPE=="NONTERMINAL_SYNTHETIC_NUMERICAL_STRESS_ONLY",
    }
    out={"audit":"NMIR-0103X-SIX-STATE-STRESS-CONVERGENCE","metrics":metrics,"gates":gates}
    out["status"]="PASS_0103X_SIX_STATE_STRESS_CONVERGENCE_NONTERMINAL" if all(gates.values()) else "FAIL_0103X_SIX_STATE_STRESS_CONVERGENCE"
    return out,rows


def write_csv(rows,path):
    with Path(path).open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)


if __name__=="__main__":
    out,rows=run_audit()
    write_csv(rows,"0103x_convergence_matrix.csv")
    print(json.dumps(out,indent=2,sort_keys=True))
    if not all(out["gates"].values()):
        raise SystemExit(1)
