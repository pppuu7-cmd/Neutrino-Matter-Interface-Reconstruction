#!/usr/bin/env python3
import json
import numpy as np

SCOPE="NONPHYSICAL_INTERFACE_ONLY"


def pmns_fixture():
    th12,th13,th23,delta=0.57,0.15,0.79,1.17
    c12,s12=np.cos(th12),np.sin(th12)
    c13,s13=np.cos(th13),np.sin(th13)
    c23,s23=np.cos(th23),np.sin(th23)
    ep=np.exp(1j*delta); em=np.exp(-1j*delta)
    return np.array([
        [c12*c13,s12*c13,s13*em],
        [-s12*c23-c12*s23*s13*ep,c12*c23-s12*s23*s13*ep,s23*c13],
        [s12*s23-c12*c23*s13*ep,-c12*s23-s12*c23*s13*ep,c23*c13],
    ],dtype=complex)


def transform6(U):
    T=np.zeros((6,6),dtype=complex)
    T[:3,:3]=U; T[3:,3:]=U.conj()
    return T


def hamiltonian_mass(s,g,U):
    Hv=np.diag([0.0,0.4,1.1]).astype(complex)
    v=0.6*np.exp(-2.0*s)+0.05
    Vf=np.diag([v,0.0,0.0]).astype(complex)
    Hn=Hv+U.conj().T@Vf@U
    Hb=Hv-U.T@Vf@U.conj()
    K=np.zeros((3,3),dtype=complex); K[0,1]=1.0; K[1,0]=-1.0
    b=np.sin(np.pi*s)**2
    M=g*b*K
    return np.block([[Hn,M],[M.conj().T,Hb]])


def propagate(g,N,basis="mass"):
    U=pmns_fixture(); T=transform6(U)
    psi_f=np.zeros(6,dtype=complex); psi_f[0]=1.0
    psi=T.conj().T@psi_f if basis=="mass" else psi_f.copy()
    ds=1.0/N; max_herm=0.0
    for i in range(N):
        s=(i+0.5)*ds
        H=hamiltonian_mass(s,g,U)
        if basis=="flavor": H=T@H@T.conj().T
        max_herm=max(max_herm,float(np.max(np.abs(H-H.conj().T))))
        w,V=np.linalg.eigh(H)
        psi=V@(np.exp(-1j*w*ds)*(V.conj().T@psi))
    return psi,U,T,max_herm


def run_audit():
    U=pmns_fixture(); T=transform6(U)
    ures=float(np.max(np.abs(U.conj().T@U-np.eye(3))))
    tres=float(np.max(np.abs(T.conj().T@T-np.eye(6))))

    p400_m,_,_,h_m=propagate(0.35,400,"mass")
    p400_f,_,_,h_f=propagate(0.35,400,"flavor")
    p200_m,_,_,_=propagate(0.35,200,"mass")
    p400_repeat,_,_,_=propagate(0.35,400,"mass")
    pzero,_,_,h0=propagate(0.0,400,"mass")

    final_f_from_m=T@p400_m
    p200_f=T@p200_m
    repeat_f=T@p400_repeat
    zero_f=T@pzero

    state_basis_res=float(np.max(np.abs(final_f_from_m-p400_f)))
    prob_basis_res=float(np.max(np.abs(np.abs(final_f_from_m)**2-np.abs(p400_f)**2)))
    convergence=float(np.max(np.abs(np.abs(final_f_from_m)**2-np.abs(p200_f)**2)))
    repeat_res=float(np.max(np.abs(np.abs(final_f_from_m)**2-np.abs(repeat_f)**2)))
    norm_res=float(abs(np.vdot(p400_m,p400_m).real-1.0))
    zero_leak=float(np.sum(np.abs(zero_f[3:])**2))
    positive_antinu=float(np.sum(np.abs(final_f_from_m[3:])**2))
    herm=max(h_m,h_f,h0)

    metrics={
        "scope":SCOPE,
        "unitarity_U_residual":ures,
        "unitarity_T6_residual":tres,
        "hamiltonian_hermiticity_residual":herm,
        "zero_g_antineutrino_leakage":zero_leak,
        "norm_residual":norm_res,
        "mass_flavor_state_residual":state_basis_res,
        "mass_flavor_probability_residual":prob_basis_res,
        "step_200_400_probability_residual":convergence,
        "positive_control_antineutrino_probability":positive_antinu,
        "repeat_probability_residual":repeat_res,
        "final_probabilities":np.abs(final_f_from_m).tolist(),
    }
    gates={
        "U_unitary":ures<=1e-12,
        "T6_unitary":tres<=1e-12,
        "hamiltonian_hermitian":herm<=1e-12,
        "zero_control":zero_leak<=1e-13,
        "norm_conserved":norm_res<=1e-12,
        "basis_state_invariance":state_basis_res<=1e-11,
        "basis_probability_invariance":prob_basis_res<=1e-11,
        "step_halving_convergence":convergence<=1e-5,
        "positive_control":positive_antinu>1e-6,
        "deterministic_repeat":repeat_res<=1e-14,
        "scope_guard":SCOPE=="NONPHYSICAL_INTERFACE_ONLY",
    }
    out={"audit":"NMIR-0103E-END-TO-END-SURROGATE-SPIN-FLAVOR","metrics":metrics,"gates":gates}
    out["status"]="PASS_0103E_END_TO_END_INTERFACE_NONPHYSICAL" if all(gates.values()) else "FAIL_0103E_END_TO_END_INTERFACE"
    return out


if __name__=="__main__":
    out=run_audit(); print(json.dumps(out,indent=2,sort_keys=True))
    if not all(out["gates"].values()): raise SystemExit(1)
