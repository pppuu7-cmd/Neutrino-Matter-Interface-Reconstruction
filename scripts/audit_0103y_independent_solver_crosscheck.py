#!/usr/bin/env python3
import json
import numpy as np

SCOPE="NONTERMINAL_SYNTHETIC_NUMERICAL_CROSSCHECK_ONLY"
G_VALUES=[0.0,1e-2,1e-1,1.0]
N=4096

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

def midpoint(g,N):
    U=pmns_fixture(); psi,T=initial(U); ds=1/N; mh=0.0
    for i in range(N):
        H=hamiltonian((i+0.5)*ds,g,U); mh=max(mh,float(np.max(np.abs(H-H.conj().T))))
        w,V=np.linalg.eigh(H); psi=V@(np.exp(-1j*w*ds)*(V.conj().T@psi))
    pf=T@psi; return pf,mh

def rk4(g,N):
    U=pmns_fixture(); psi,T=initial(U); ds=1/N; mh=0.0
    def f(s,x):
        nonlocal mh
        H=hamiltonian(s,g,U); mh=max(mh,float(np.max(np.abs(H-H.conj().T))))
        return -1j*(H@x)
    for i in range(N):
        s=i*ds; k1=f(s,psi); k2=f(s+ds/2,psi+ds*k1/2); k3=f(s+ds/2,psi+ds*k2/2); k4=f(s+ds,psi+ds*k3)
        psi=psi+ds*(k1+2*k2+2*k3+k4)/6
    return T@psi,mh

def run_audit():
    rows=[]; maxpd=maxrk=maxmid=maxherm=zeroleak=positive=0.0; bounded=True
    for g in G_VALUES:
        a,ha=midpoint(g,N); b,hb=rk4(g,N); pa=np.abs(a)**2; pb=np.abs(b)**2
        pd=float(np.max(np.abs(pa-pb))); nrka=float(abs(np.vdot(b,b).real-1)); nmida=float(abs(np.vdot(a,a).real-1))
        maxpd=max(maxpd,pd); maxrk=max(maxrk,nrka); maxmid=max(maxmid,nmida); maxherm=max(maxherm,ha,hb)
        if g==0: zeroleak=max(zeroleak,float(np.sum(pa[3:])),float(np.sum(pb[3:])))
        else: positive=max(positive,float(np.sum(pa[3:])),float(np.sum(pb[3:])))
        bounded=bounded and bool(np.all(np.isfinite(pa)) and np.all(np.isfinite(pb)) and np.min(pa)>=-1e-10 and np.min(pb)>=-1e-10 and np.max(pa)<=1+1e-10 and np.max(pb)<=1+1e-10)
        rows.append({"g":g,"probability_linf":pd,"midpoint_norm_residual":nmida,"rk4_norm_residual":nrka})
    gates={"hamiltonian_hermitian":maxherm<=1e-12,"solver_probability_agreement":maxpd<=5e-6,"rk4_norm":maxrk<=5e-8,"midpoint_norm":maxmid<=1e-10,"zero_control":zeroleak<=1e-12,"positive_control":positive>1e-8,"bounded_probabilities":bounded,"scope_guard":SCOPE=="NONTERMINAL_SYNTHETIC_NUMERICAL_CROSSCHECK_ONLY"}
    out={"audit":"NMIR-0103Y-INDEPENDENT-SOLVER-CROSSCHECK","metrics":{"scope":SCOPE,"couplings":G_VALUES,"N":N,"max_probability_linf":maxpd,"max_rk4_norm_residual":maxrk,"max_midpoint_norm_residual":maxmid,"max_hermiticity_residual":maxherm,"zero_g_max_antineutrino_leakage":zeroleak,"max_nonzero_g_antineutrino_probability":positive,"rows":rows},"gates":gates}
    out["status"]="PASS_0103Y_INDEPENDENT_SOLVER_CROSSCHECK_NONTERMINAL" if all(gates.values()) else "FAIL_0103Y_INDEPENDENT_SOLVER_CROSSCHECK"
    return out

if __name__=="__main__":
    r=run_audit(); print(json.dumps(r,indent=2,sort_keys=True)); raise SystemExit(0 if all(r["gates"].values()) else 1)
