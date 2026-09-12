#!/usr/bin/env python3
"""NMIR 0103X: six-state Majorana stress/convergence audit."""
from __future__ import annotations
import json
import numpy as np

COUPLINGS=[0.0,0.002,0.01,0.05]
RESOLUTIONS=[128,256,512,1024]

def pmns():
    t12,t13,t23,d=0.57,0.15,0.79,1.17
    s12,c12=np.sin(t12),np.cos(t12); s13,c13=np.sin(t13),np.cos(t13); s23,c23=np.sin(t23),np.cos(t23)
    em=np.exp(-1j*d); ep=np.exp(1j*d)
    return np.array([[c12*c13,s12*c13,s13*em],[-s12*c23-c12*s23*s13*ep,c12*c23-s12*s23*s13*ep,s23*c13],[s12*s23-c12*c23*s13*ep,-c12*s23-s12*c23*s13*ep,c23*c13]],complex)

def h6(x,g):
    u=pmns(); d=np.diag([0.0,0.13,0.41]).astype(complex)
    rho=1.0+0.25*np.exp(-2.0*(x-0.5)**2)+0.05*np.sin(2*np.pi*x)
    ye=0.47+0.02*np.cos(2*np.pi*x)
    vf=np.diag([0.055*rho*ye,0,0]).astype(complex)
    hn=d+u.conj().T@vf@u; ha=d-u.T@vf@u.conj()
    bp=0.72+0.18*np.sin(2*np.pi*x)+0.08*np.cos(4*np.pi*x)
    k=np.zeros((3,3),complex); k[0,1]=1; k[1,0]=-1
    m=g*bp*k
    return np.block([[hn,m],[m.conj().T,ha]])

def run_case(g,n):
    psi=np.zeros(6,complex); psi[0]=1
    total=np.eye(6,dtype=complex); mh=0.0
    ds=1.0/n
    for j in range(n):
        h=h6((j+0.5)/n,g); mh=max(mh,float(np.max(np.abs(h-h.conj().T))))
        w,v=np.linalg.eigh(h); s=(v*np.exp(-1j*w*ds))@v.conj().T
        psi=s@psi; total=s@total
    probs=np.abs(psi)**2
    return {"probs":probs,"norm_residual":float(abs(np.vdot(psi,psi).real-1)),"anti_leakage_amplitude":float(np.max(np.abs(psi[3:]))),"hermiticity_residual":mh,"unitarity_residual":float(np.max(np.abs(total.conj().T@total-np.eye(6))))}

def run_audit():
    cases={}; max_h=max_norm=max_zero=max_conv=max_unit=0.0
    for g in COUPLINGS:
      cases[str(g)]={}
      for n in RESOLUTIONS:
        r=run_case(g,n); cases[str(g)][str(n)]={k:(v.tolist() if isinstance(v,np.ndarray) else v) for k,v in r.items()}
        max_h=max(max_h,r['hermiticity_residual']); max_norm=max(max_norm,r['norm_residual'])
        if g==0: max_zero=max(max_zero,r['anti_leakage_amplitude'])
      a=np.array(cases[str(g)]['512']['probs']); b=np.array(cases[str(g)]['1024']['probs'])
      max_conv=max(max_conv,float(np.max(np.abs(a-b))))
      max_unit=max(max_unit,float(cases[str(g)]['1024']['unitarity_residual']))
    metrics={"max_hermiticity_residual":max_h,"max_norm_residual":max_norm,"max_zero_g_antineutrino_leakage":max_zero,"max_probability_refinement_residual_512_1024":max_conv,"max_cumulative_unitarity_residual_1024":max_unit}
    gates={"all_H6_hermitian":max_h<=1e-12,"all_norms_conserved":max_norm<=1e-10,"zero_g_decouples":max_zero<=1e-12,"fine_grid_converged":max_conv<=1e-4,"cumulative_propagator_unitary":max_unit<=1e-10}
    passed=all(gates.values())
    return {"audit":"NMIR-0103X-SIX-STATE-STRESS-CONVERGENCE","status":"PASS_0103X_STRESS_CONVERGENCE_NONTERMINAL" if passed else "FAIL_0103X_STRESS_CONVERGENCE","gates":gates,"metrics":metrics,"cases":cases,"interpretation":{"synthetic_fixture":True,"monotonicity_in_g_required":False,"betelgeuse_authority_closed":False}}

if __name__=='__main__': print(json.dumps(run_audit(),indent=2,sort_keys=True))
