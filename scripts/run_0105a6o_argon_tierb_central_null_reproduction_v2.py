#!/usr/bin/env python3
"""Execution-safe 0105a6o Tier-B COHERENT Ar central/null reproduction.

Implements the already-frozen preregistration. No BSM/model-agnostic residual is
constructed or inspected. Decimal coordinate centers are explicit literals so
exact numeric equality does not depend on np.arange accumulation.
"""
from __future__ import annotations

import argparse, hashlib, json, math
from pathlib import Path
import numpy as np
from scipy.optimize import brentq, minimize

BENCHMARK = "NMIR-V2-0105A6O"
PREREG_COMMIT = "a94cbdf5a65618545bd4b1fb4f9fd6c120ae340e"
A6P_MANIFEST_SHA256 = "5b1df47a50dd4dbb2a7fbd5ee64346c2854bdbad0540bfa6f16637eb10b6bada"
EXPECTED_SHA256 = {
 "datanobkgsub.txt":"dabf3d80f13959f4b94b77c9b56f7347a645105801e8cc177424e7ffcf7c7f66",
 "cevnspdf.txt":"3b1d5b25749e8d8e1cfdf5c32e48f026ce4aafec0a80632b3a63273e6e0e1f37",
 "brnpdf.txt":"02664ce6a84eca8c6146b6502497bc5d8165df945da132193622334ff4ff826f",
 "delbrnpdf.txt":"ebccca6c1650b0ace71fdbaade7a80ea289a99ff3c120266ae6ecf0083df5c63",
 "bkgpdf.txt":"36c89291dde3032a19ca7a8e64510d036d7b40c34b0805ce475a13ccfa739dd1",
 "LArParametersAnlA.yaml":"a206a77220436d0173c4783ae8fddeab97adf5e144f3d65005eff0870257693e",
}
E=[5.,15.,25.,35.,45.,55.,65.,75.,85.,95.,105.,115.]
F=[.525,.575,.625,.675,.725,.775,.825,.875]
T=[.15,.65,1.15,1.65,2.15,2.65,3.15,3.65,4.15,4.65]
EXPECTED_GRID=np.array([(e,f,t) for e in E for f in F for t in T],dtype=float)
TARGET={"NC":(159.,2.),"NP":(553.,3.),"ND":(10.,3.),"NB":(3131.,3.),"sigma_profile":(43.,2.),"Z_stat":(3.9,.15)}
ROBUST={"NC":1.,"NP":1.,"ND":1.,"Z_stat":.05,"sigma_profile":.5}


def sh(path:Path)->str:return hashlib.sha256(path.read_bytes()).hexdigest()

def parse(path:Path):
 a=np.loadtxt(path,dtype=float)
 if a.shape!=(960,4): raise ValueError(f"{path.name}: shape {a.shape} != (960,4)")
 if not np.array_equal(a[:,:3],EXPECTED_GRID): raise ValueError(f"{path.name}: frozen coordinate grid mismatch")
 if not np.isfinite(a).all() or np.any(a[:,3]<0): raise ValueError(f"{path.name}: invalid values")
 return a[:,3]

def structural(d:Path):
 for n,h in EXPECTED_SHA256.items():
  p=d/n
  if not p.exists() or sh(p)!=h: raise ValueError(f"exact byte identity failed: {n}")
 vals={n:parse(d/n) for n in ["datanobkgsub.txt","cevnspdf.txt","brnpdf.txt","delbrnpdf.txt","bkgpdf.txt"]}
 sums={n:float(v.sum()) for n,v in vals.items()}
 checks={
  "data_3752":abs(sums["datanobkgsub.txt"]-3752.)<=1e-9,
  "cevns_128":abs(sums["cevnspdf.txt"]-128.)<=.05,
  "prompt_497":abs(sums["brnpdf.txt"]-497.)<=.05,
  "delayed_33":abs(sums["delbrnpdf.txt"]-33.)<=.05,
  "steady_3152_or_3154":min(abs(sums["bkgpdf.txt"]-3152.),abs(sums["bkgpdf.txt"]-3154.))<=.05,
 }
 if not all(checks.values()): raise ValueError(f"frozen template-sum gate failed: {sums}; {checks}")
 shapes={"S":vals["cevnspdf.txt"]/sums["cevnspdf.txt"],"P":vals["brnpdf.txt"]/sums["brnpdf.txt"],"D":vals["delbrnpdf.txt"]/sums["delbrnpdf.txt"],"B":vals["bkgpdf.txt"]/sums["bkgpdf.txt"]}
 return vals["datanobkgsub.txt"],shapes,sums,checks

def q(theta,n,s,B0,fixed_nc=None):
 if fixed_nc is None: NC,NP,ND,NB=map(float,theta)
 else: NC=float(fixed_nc); NP,ND,NB=map(float,theta)
 if min(NC,NP,ND,NB)<0:return float("inf")
 mu=NC*s["S"]+NP*s["P"]+ND*s["D"]+NB*s["B"]
 if np.any((mu<=0)&(n>0)) or np.any(mu<0):return float("inf")
 term=mu.copy(); mask=n>0; term[mask]=mu[mask]-n[mask]*np.log(mu[mask])
 pen=((NP-497.)/160.)**2+((ND-33.)/33.)**2+((NB-B0)/25.)**2
 return float(2*term.sum()+pen)

def lbfgs(fun,x0,bounds,args):
 return minimize(fun,np.asarray(x0,float),args=args,method="L-BFGS-B",bounds=bounds,options={"ftol":1e-12,"gtol":1e-9,"maxiter":20000})
def bestfit(n,s,B0):
 starts=[[128,497,33,B0],[159,553,10,3131],[0,497,33,B0],[256,497,33,B0]]; ok=[]
 for x0 in starts:
  r=lbfgs(q,x0,[(0,None)]*4,(n,s,B0,None))
  if r.success and np.isfinite(r.fun):ok.append((x0,r))
 if not ok:raise RuntimeError("no successful L-BFGS-B start")
 bx0,b=min(ok,key=lambda z:z[1].fun)
 for _,r in ok:
  if np.max(np.abs(r.x-b.x))>1e-4 or abs(float(r.fun)-float(b.fun))>1e-7:raise RuntimeError("frozen multi-start stability gate failed")
 p=minimize(q,b.x,args=(n,s,B0,None),method="Powell",bounds=[(0,None)]*4,options={"xtol":1e-10,"ftol":1e-12,"maxiter":50000})
 if not p.success or np.max(np.abs(p.x-b.x))>.02 or abs(float(p.fun)-float(b.fun))>1e-5:raise RuntimeError("frozen Powell cross-check failed")
 return bx0,b,ok,p

def prof(n,s,B0,NC,start):
 rs=[]
 for x0 in [start,[497,33,B0]]:
  r=lbfgs(q,x0,[(0,None)]*3,(n,s,B0,NC))
  if r.success and np.isfinite(r.fun):rs.append(r)
 if not rs:raise RuntimeError(f"profile failure NC={NC}")
 return min(rs,key=lambda r:r.fun)
def branch(n,s,B0):
 bx0,b,allr,p=bestfit(n,s,B0); NC,NP,ND,NB=map(float,b.x); qb=float(b.fun); start=[NP,ND,NB]
 nul=prof(n,s,B0,0.,start); qn=float(nul.fun); q0=max(0.,qn-qb); Z=math.sqrt(q0)
 def delta(x):return float(prof(n,s,B0,float(x),start).fun-qb-1.)
 if NC<=0 or delta(0)<=0: lo=0.; boundary=True
 else:lo=float(brentq(delta,0.,NC,xtol=1e-6,rtol=1e-12,maxiter=200));boundary=False
 hi=max(NC+50,NC*1.5,50.)
 for _ in range(30):
  if delta(hi)>0:break
  hi*=1.5
 else:raise RuntimeError("upper profile bracket failure")
 up=float(brentq(delta,NC,hi,xtol=1e-6,rtol=1e-12,maxiter=200)); sig=(up-lo)/2
 v={"NC":NC,"NP":NP,"ND":ND,"NB":NB,"sigma_profile":sig,"Z_stat":Z}
 checks={k:abs(v[k]-tv)<=tol for k,(tv,tol) in TARGET.items()}
 return {"B0":B0,"best_fit":{**{k:v[k] for k in ["NC","NP","ND","NB"]},"Q":qb},"null_fit":{"NC":0.,"NP":float(nul.x[0]),"ND":float(nul.x[1]),"NB":float(nul.x[2]),"Q":qn},"q0":q0,"Z_stat":Z,"profile_1sigma":{"lower":lo,"upper":up,"half_width":sig,"lower_is_physical_boundary":boundary},"publication_checks":checks,"publication_pass":all(checks.values()),"lbfgsb_starts":[{"x0":x0,"x":[float(x) for x in r.x],"Q":float(r.fun),"nit":int(r.nit)} for x0,r in allr],"powell":{"x":[float(x) for x in p.x],"Q":float(p.fun),"nit":int(p.nit)}}
def execute(d:Path):
 n,s,sums,sc=structural(d); br={"R3152":branch(n,s,3152.),"R3154":branch(n,s,3154.)};a,b=br.values()
 dif={"NC":abs(a["best_fit"]["NC"]-b["best_fit"]["NC"]),"NP":abs(a["best_fit"]["NP"]-b["best_fit"]["NP"]),"ND":abs(a["best_fit"]["ND"]-b["best_fit"]["ND"]),"Z_stat":abs(a["Z_stat"]-b["Z_stat"]),"sigma_profile":abs(a["profile_1sigma"]["half_width"]-b["profile_1sigma"]["half_width"])}
 rc={k:dif[k]<=ROBUST[k] for k in ROBUST}; pp=all(x["publication_pass"] for x in br.values()); rp=all(rc.values());pas=pp and rp
 return {"benchmark":BENCHMARK,"preregistration_commit":PREREG_COMMIT,"tier":"release-consistent independent reproduction","tierA_exact_collaboration_internal_likelihood":"BLOCKED","structural_gate":{"template_sums":sums,"checks":sc,"pass":True},"branches":br,"dual_anchor_differences":dif,"dual_anchor_robustness_checks":rc,"dual_anchor_robustness_pass":rp,"both_publication_targets_pass":pp,"classification":"PASS_0105A6O_TIERB_ARGON_CENTRAL_NULL_REPRODUCTION_NONDISCOVERY" if pas else "BLOCKED_0105A6O_TIERB_ARGON_CENTRAL_NULL_REPRODUCTION_MISMATCH","systematic_excursion_preregistration_permission_percent":100 if pas else 0,"observed_bsm_residual_permission_percent":0,"observed_bsm_residual_inspected":False}
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--files-dir",required=True);ap.add_argument("--a6p-manifest",required=True);ap.add_argument("--output",required=True);ap.add_argument("--git-sha",required=True);a=ap.parse_args();mp=Path(a.a6p_manifest)
 if sh(mp)!=A6P_MANIFEST_SHA256:raise SystemExit("a6p manifest SHA mismatch")
 m=json.loads(mp.read_text());
 if not m.get("central_ready"):raise SystemExit("a6p central_ready false")
 try:r=execute(Path(a.files_dir));r["git_sha"]=a.git_sha
 except Exception as e:r={"benchmark":BENCHMARK,"preregistration_commit":PREREG_COMMIT,"git_sha":a.git_sha,"classification":"BLOCKED_0105A6O_TIERB_ARGON_CENTRAL_NULL_REPRODUCTION_EXECUTION_OR_STRUCTURAL_FAILURE","error_type":type(e).__name__,"error_message":str(e),"systematic_excursion_preregistration_permission_percent":0,"observed_bsm_residual_permission_percent":0,"observed_bsm_residual_inspected":False}
 out=Path(a.output);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(r,indent=2,sort_keys=True)+"\n");print(json.dumps(r,indent=2,sort_keys=True))
if __name__=="__main__":main()
