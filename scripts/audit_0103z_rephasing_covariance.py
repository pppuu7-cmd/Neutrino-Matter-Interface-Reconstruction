#!/usr/bin/env python3
import json
import numpy as np

SCOPE="NONTERMINAL_SYNTHETIC_REPHASING_COVARIANCE_ONLY"
G_VALUES=[0.0,0.1,1.0]
N=1024
PHASE_SETS=[
    [0.13,-0.71,1.11,0.52,-1.37,2.03],
    [1.7,0.2,-2.2,-0.4,0.9,2.6],
    [-2.8,1.3,0.44,2.1,-0.77,0.31],
]

def pmns_fixture():
    th12,th13,th23,delta=0.57,0.15,0.79,1.17
    c12,s12=np.cos(th12),np.sin(th12); c13,s13=np.cos(th13),np.sin(th13); c23,s23=np.cos(th23),np.sin(th23)
    ep,em=np.exp(1j*delta),np.exp(-1j*delta)
    return np.array([[c12*c13,s12*c13,s13*em],[-s12*c23-c12*s23*s13*ep,c12*c23-s12*s23*s13*ep,s23*c13],[s12*s23-c12*c23*s13*ep,-c12*s23-s12*c23*s13*ep,c23*c13]],complex)

def transform6(U):
    T=np.zeros((6,6),complex); T[:3,:3]=U; T[3:,3:]=U.conj(); return T

def hamiltonian(s,g,U):
    Hv=np.array([[0,0.03+0.01j,0.015-0.008j],[0.03-0.01j,0.45,0.025+0.012j],[0.015+0.008j,0.025-0.012j,1.2]],complex)
    v=0.55*(1+0.3*np.sin(2*np.pi*s)+0.1*np.cos(5*np.pi*s)); Vf=np.diag([v,0,0]).astype(complex)
    Hn=Hv+U.conj().T@Vf@U; Hb=Hv.conj()-U.T@Vf@U.conj()
    amp=0.55+0.25*np.sin(3*np.pi*s)+0.1*np.cos(7*np.pi*s); phase=0.8*np.sin(2*np.pi*s)+0.35*np.cos(3*np.pi*s)
    K=np.zeros((3,3),complex); K[0,1]=1; K[1,0]=-1; M=g*amp*np.exp(1j*phase)*K
    return np.block([[Hn,M],[M.conj().T,Hb]])

def initial(U):
    T=transform6(U); pf=np.zeros(6,complex); pf[0]=1; return T.conj().T@pf,T

def propagate(g,N,D=None):
    U=pmns_fixture(); psi,T=initial(U); ds=1/N; mh=0.0
    if D is not None: psi=D@psi
    for i in range(N):
        H=hamiltonian((i+0.5)*ds,g,U)
        if D is not None: H=D@H@D.conj().T
        mh=max(mh,float(np.max(np.abs(H-H.conj().T))))
        w,V=np.linalg.eigh(H); psi=V@(np.exp(-1j*w*ds)*(V.conj().T@psi))
    if D is not None: psi=D.conj().T@psi
    return psi,T,mh

def run_audit():
    maxDu=maxH=maxState=maxProb=maxNorm=zeroLeak=0.0
    rows=[]
    for phases in PHASE_SETS:
        D=np.diag(np.exp(1j*np.array(phases)))
        maxDu=max(maxDu,float(np.max(np.abs(D.conj().T@D-np.eye(6)))))
        for g in G_VALUES:
            a,T,ha=propagate(g,N,None); b,_,hb=propagate(g,N,D)
            af=T@a; bf=T@b
            sr=float(np.max(np.abs(a-b))); pr=float(np.max(np.abs(np.abs(af)**2-np.abs(bf)**2)))
            na=float(abs(np.vdot(a,a).real-1)); nb=float(abs(np.vdot(b,b).real-1))
            maxH=max(maxH,ha,hb); maxState=max(maxState,sr); maxProb=max(maxProb,pr); maxNorm=max(maxNorm,na,nb)
            if g==0: zeroLeak=max(zeroLeak,float(np.sum(np.abs(af[3:])**2)),float(np.sum(np.abs(bf[3:])**2)))
            rows.append({"g":g,"state_residual":sr,"probability_residual":pr,"norm_residual":max(na,nb)})
    gates={"D_unitary":maxDu<=1e-14,"hamiltonian_hermitian":maxH<=1e-12,"state_covariance":maxState<=2e-12,"probability_invariance":maxProb<=2e-12,"norm_conserved":maxNorm<=1e-10,"zero_control":zeroLeak<=1e-12,"scope_guard":SCOPE=="NONTERMINAL_SYNTHETIC_REPHASING_COVARIANCE_ONLY"}
    out={"audit":"NMIR-0103Z-SIX-STATE-REPHASING-COVARIANCE","metrics":{"scope":SCOPE,"couplings":G_VALUES,"N":N,"phase_sets":PHASE_SETS,"max_D_unitarity_residual":maxDu,"max_hamiltonian_hermiticity_residual":maxH,"max_recovered_state_residual":maxState,"max_probability_residual":maxProb,"max_norm_residual":maxNorm,"zero_g_max_antineutrino_leakage":zeroLeak,"rows":rows},"gates":gates}
    out["status"]="PASS_0103Z_SIX_STATE_REPHASING_COVARIANCE_NONTERMINAL" if all(gates.values()) else "FAIL_0103Z_SIX_STATE_REPHASING_COVARIANCE"
    return out

if __name__=="__main__":
    r=run_audit(); print(json.dumps(r,indent=2,sort_keys=True)); raise SystemExit(0 if all(r["gates"].values()) else 1)
