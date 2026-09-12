#!/usr/bin/env python3
"""NMIR 0103M: synthetic co-registered 3-D magneto-matter engineering audit."""
from __future__ import annotations
import json
import numpy as np

TOL=1e-12

def pmns():
    t12,t13,t23,d=0.57,0.15,0.79,1.17
    s12,c12=np.sin(t12),np.cos(t12); s13,c13=np.sin(t13),np.cos(t13); s23,c23=np.sin(t23),np.cos(t23)
    em=np.exp(-1j*d); ep=np.exp(1j*d)
    return np.array([[c12*c13,s12*c13,s13*em],[-s12*c23-c12*s23*s13*ep,c12*c23-s12*s23*s13*ep,s23*c13],[s12*s23-c12*c23*s13*ep,-c12*s23-s12*c23*s13*ep,c23*c13]],complex)

def grid_state(n=21):
    a=np.linspace(-1,1,n); x,y,z=np.meshgrid(a,a,a,indexing='ij')
    bx=0.7+0.2*y+0.1*z; by=-0.3+0.15*x-0.05*z; bz=0.4+0.1*x*y
    rho=1.0+0.25*np.exp(-(x*x+y*y+z*z))+0.08*z
    ye=0.47+0.03*x-0.02*y
    return a,(bx,by,bz,rho,ye)

def interp3(a,f,p):
    q=(np.asarray(p)-a[0])/(a[-1]-a[0])*(len(a)-1)
    i=np.floor(q).astype(int); t=q-i
    i=np.clip(i,0,len(a)-2); t=np.where(q>=len(a)-1,1.0,t)
    out=0.0
    for dx in (0,1):
      for dy in (0,1):
       for dz in (0,1):
        w=(t[0] if dx else 1-t[0])*(t[1] if dy else 1-t[1])*(t[2] if dz else 1-t[2])
        out += w*f[i[0]+dx,i[1]+dy,i[2]+dz]
    return float(out)

def H6(u,rho,ye,bperp,g):
    d=np.diag([0.0,0.13,0.41]).astype(complex)
    vf=np.diag([0.055*rho*ye,0.0,0.0]).astype(complex)
    hn=d+u.conj().T@vf@u; ha=d-u.T@vf@u.conj()
    k=np.zeros((3,3),complex); k[0,1]=1; k[1,0]=-1
    m=(g*bperp)*k
    return np.block([[hn,m],[m.conj().T,ha]])

def prop(h,ds):
    w,v=np.linalg.eigh(h); return (v*np.exp(-1j*w*ds))@v.conj().T

def evolve(nstep,g):
    a,fields=grid_state(); bx,by,bz,rho3,ye3=fields
    shapes=[f.shape for f in fields]
    p0=np.array([-0.78,-0.52,-0.66]); p1=np.array([0.72,0.61,0.74]); vec=p1-p0; L=float(np.linalg.norm(vec)); nh=vec/L
    u=pmns(); psi=np.zeros(6,complex); psi[0]=1
    max_herm=max_proj=0.0; rhos=[]; yes=[]; bps=[]
    ds=L/nstep
    for j in range(nstep):
        p=p0+(j+0.5)/nstep*vec
        b=np.array([interp3(a,bx,p),interp3(a,by,p),interp3(a,bz,p)])
        rr=interp3(a,rho3,p); yy=interp3(a,ye3,p)
        para=float(b@nh); bp2=max(0.0,float(b@b)-para*para); bp=np.sqrt(bp2)
        max_proj=max(max_proj,abs(bp2-(float(b@b)-para*para)))
        h=H6(u,rr,yy,bp,g); max_herm=max(max_herm,float(np.max(np.abs(h-h.conj().T))))
        psi=prop(h,ds)@psi; rhos.append(rr); yes.append(yy); bps.append(bp)
    return psi,{"shapes":shapes,"max_hermiticity":max_herm,"max_projection_residual":max_proj,"rho_min":min(rhos),"ye_min":min(yes),"ye_max":max(yes),"bperp_min":min(bps),"bperp_max":max(bps),"ray_inside":bool(np.all(p0>=-1)&np.all(p0<=1)&np.all(p1>=-1)&np.all(p1<=1))}

def run_audit():
    p256,m256=evolve(256,0.02); p512,m512=evolve(512,0.02); p0,m0=evolve(512,0.0)
    probs256=np.abs(p256)**2; probs512=np.abs(p512)**2
    metrics={"co_registered_shapes":len(set(m512['shapes']))==1,"rho_min":m512['rho_min'],"ye_min":m512['ye_min'],"ye_max":m512['ye_max'],"ray_inside":m512['ray_inside'],"Bperp_projection_residual":m512['max_projection_residual'],"H6_hermiticity_residual":m512['max_hermiticity'],"norm_residual":float(abs(np.vdot(p512,p512).real-1)),"zero_g_antineutrino_leakage":float(np.max(np.abs(p0[3:]))),"probability_refinement_residual_256_512":float(np.max(np.abs(probs256-probs512))),"antineutrino_probability":float(np.sum(probs512[3:])),"bperp_range":[m512['bperp_min'],m512['bperp_max']]}
    gates={"co_registered":metrics['co_registered_shapes'],"matter_physical_fixture":metrics['rho_min']>0 and 0<metrics['ye_min']<metrics['ye_max']<1,"ray_inside_domain":metrics['ray_inside'],"Bperp_projection":metrics['Bperp_projection_residual']<=1e-12,"H6_hermitian":metrics['H6_hermiticity_residual']<=1e-12,"norm_conserved":metrics['norm_residual']<=1e-10,"zero_g_decouples":metrics['zero_g_antineutrino_leakage']<=1e-12,"refinement_converged":metrics['probability_refinement_residual_256_512']<=2e-4}
    passed=all(gates.values())
    return {"audit":"NMIR-0103M-COHERENT-MAGNETO-MATTER","status":"PASS_0103M_COHERENT_MAGNETO_MATTER_NONTERMINAL" if passed else "FAIL_0103M_COHERENT_MAGNETO_MATTER","gates":gates,"metrics":metrics,"interpretation":{"synthetic_fixture":True,"closes_engineering_interface_only":passed,"betelgeuse_authority_closed":False,"terminal_status_ceiling":"BLOCKED_0103_BETELGEUSE_COHERENT_MAGNETO_MATTER_STATE_AUTHORITY"}}

if __name__=='__main__': print(json.dumps(run_audit(),indent=2,sort_keys=True))
