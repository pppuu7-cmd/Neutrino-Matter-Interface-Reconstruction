#!/usr/bin/env python3
"""0105a6o1 prospectively frozen optimizer convergence diagnostic.

Uses exact 0105a6p central bytes and the exact 0105a6o central objective. This
is numerical-diagnostic-only and never performs publication-target or BSM
classification.
"""
from __future__ import annotations

import argparse, json
from pathlib import Path
import numpy as np
from scipy.optimize import minimize

from scripts.run_0105a6o_argon_tierb_central_null_reproduction_v2 import (
    A6P_MANIFEST_SHA256, q, sh, structural,
)

BENCHMARK = "NMIR-V2-0105A6O1"
PREREG_COMMIT = "1588298dbd04e4cc4c451b3993f43f61080d1339"
STARTS = [[128.,497.,33.,3152.],[159.,553.,10.,3131.],[0.,497.,33.,3152.],[256.,497.,33.,3152.]]
BOUNDS = [(0.,None)]*4


def mu_and_A(theta, s):
    A=np.column_stack([s["S"],s["P"],s["D"],s["B"]])
    x=np.asarray(theta,float)
    return A@x,A


def grad(theta,n,s,B0):
    x=np.asarray(theta,float); mu,A=mu_and_A(x,s)
    if np.any(mu<=0): return np.full(4,np.nan)
    g=2.*(A.T@(1.-n/mu))
    g += np.array([0.,2.*(x[1]-497.)/160.**2,2.*(x[2]-33.)/33.**2,2.*(x[3]-B0)/25.**2])
    return g


def hessian(theta,n,s,B0):
    mu,A=mu_and_A(theta,s)
    if np.any(mu<=0): return np.full((4,4),np.nan)
    H=2.*(A.T@((n/mu**2)[:,None]*A))
    H += np.diag([0.,2./160.**2,2./33.**2,2./25.**2])
    return (H+H.T)/2.


def kkt_inf(x,g,eps=1e-9):
    vals=[]
    for xi,gi in zip(x,g):
        vals.append(max(0.,-gi) if xi<=eps else abs(gi))
    return float(max(vals))


def run_one_anchor(n,s,B0):
    starts=[list(v) for v in STARTS]
    for v in starts: v[3]=B0
    original=[]
    for x0 in starts:
        r=minimize(q,np.asarray(x0,float),args=(n,s,B0,None),method="L-BFGS-B",bounds=BOUNDS,
                   options={"ftol":1e-12,"gtol":1e-9,"maxiter":20000})
        if r.success and np.isfinite(r.fun) and np.all(np.isfinite(r.x)):
            g=grad(r.x,n,s,B0)
            original.append({"x0":x0,"x":r.x.tolist(),"Q":float(r.fun),"grad_inf":float(np.max(np.abs(g))),"kkt_inf":kkt_inf(r.x,g),"nit":int(r.nit)})
    analytic=[]
    for x0 in starts:
        r=minimize(q,np.asarray(x0,float),args=(n,s,B0,None),jac=lambda x,*a: grad(x,*a),method="L-BFGS-B",bounds=BOUNDS,
                   options={"ftol":1e-15,"gtol":1e-11,"maxiter":50000})
        if r.success and np.isfinite(r.fun) and np.all(np.isfinite(r.x)):
            g=grad(r.x,n,s,B0)
            analytic.append({"x0":x0,"x":r.x.tolist(),"Q":float(r.fun),"grad_inf":float(np.max(np.abs(g))),"kkt_inf":kkt_inf(r.x,g),"nit":int(r.nit)})
    def spreads(rows):
        if not rows:return {"Q":None,"per_parameter":None}
        qs=np.array([r["Q"] for r in rows]); xs=np.array([r["x"] for r in rows])
        return {"Q":float(qs.max()-qs.min()),"per_parameter":(xs.max(axis=0)-xs.min(axis=0)).tolist()}
    chosen=min(analytic,key=lambda r:r["Q"]) if analytic else None
    slsqp=None; mineig=None
    if chosen:
        x=np.array(chosen["x"])
        H=hessian(x,n,s,B0); mineig=float(np.linalg.eigvalsh(H).min())
        r=minimize(q,x,args=(n,s,B0,None),jac=lambda xx,*a: grad(xx,*a),method="SLSQP",bounds=BOUNDS,
                   options={"ftol":1e-12,"maxiter":50000})
        if r.success and np.isfinite(r.fun):
            slsqp={"x":r.x.tolist(),"Q":float(r.fun),"dx_max":float(np.max(np.abs(r.x-x))),"dQ":abs(float(r.fun)-chosen["Q"]),"nit":int(r.nit)}
    osp=spreads(original); asp=spreads(analytic)
    c1=len(original)>=3
    bestoq=min([r["Q"] for r in original],default=np.inf)
    c2=bool(original) and all(abs(r["Q"]-bestoq)<=1e-4 for r in original)
    c3=bool(original) and all(r["grad_inf"]<=5e-3 for r in original)
    c4=len(analytic)==4
    c5=c4 and max(asp["per_parameter"])<=1e-5 and asp["Q"]<=1e-9
    c6=c4 and all(r["kkt_inf"]<=1e-6 for r in analytic)
    c7=mineig is not None and mineig>=-1e-10
    c8=slsqp is not None and slsqp["dx_max"]<=1e-4 and slsqp["dQ"]<=1e-8
    checks={"D1_success_count":c1,"D1_Q_spread":c2,"D1_gradient":c3,"D2_all_success":c4,"D2_agreement":c5,"D2_KKT_gradient":c6,"D2_Hessian_PSD":c7,"D3_SLSQP_agreement":c8}
    return {"B0":B0,"original":original,"original_spreads":osp,"analytic":analytic,"analytic_spreads":asp,"minimum_hessian_eigenvalue":mineig,"slsqp":slsqp,"checks":checks,"pass":all(checks.values())}


def execute(files_dir:Path):
    n,s,sums,sc=structural(files_dir)
    branches={k:run_one_anchor(n,s,b) for k,b in [("R3152",3152.),("R3154",3154.)]}
    passed=all(v["pass"] for v in branches.values())
    return {"benchmark":BENCHMARK,"preregistration_commit":PREREG_COMMIT,"structural_gate":{"template_sums":sums,"checks":sc,"pass":True},"branches":branches,"classification":"PASS_0105A6O1_SINGLE_CONVEX_OPTIMUM_NUMERICAL_TOLERANCE_ONLY_NONDISCOVERY" if passed else "BLOCKED_0105A6O1_OPTIMIZER_OR_OBJECTIVE_DIAGNOSTIC_UNRESOLVED","publication_target_classification_performed":False,"systematic_excursion_execution_performed":False,"observed_bsm_residual_permission_percent":0,"observed_bsm_residual_inspected":False}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--files-dir",required=True); ap.add_argument("--a6p-manifest",required=True); ap.add_argument("--output",required=True); ap.add_argument("--git-sha",required=True); a=ap.parse_args()
    mp=Path(a.a6p_manifest)
    if sh(mp)!=A6P_MANIFEST_SHA256: raise SystemExit("a6p manifest SHA mismatch")
    m=json.loads(mp.read_text())
    if not m.get("central_ready"): raise SystemExit("a6p central_ready false")
    try:
        r=execute(Path(a.files_dir)); r["git_sha"]=a.git_sha
    except Exception as e:
        r={"benchmark":BENCHMARK,"preregistration_commit":PREREG_COMMIT,"git_sha":a.git_sha,"classification":"BLOCKED_0105A6O1_OPTIMIZER_OR_OBJECTIVE_DIAGNOSTIC_UNRESOLVED","error_type":type(e).__name__,"error_message":str(e),"publication_target_classification_performed":False,"systematic_excursion_execution_performed":False,"observed_bsm_residual_permission_percent":0,"observed_bsm_residual_inspected":False}
    out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(r,indent=2,sort_keys=True)+"\n"); print(json.dumps(r,indent=2,sort_keys=True))

if __name__=="__main__": main()
