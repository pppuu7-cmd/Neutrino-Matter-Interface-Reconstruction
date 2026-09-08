#!/usr/bin/env python3
from __future__ import annotations

from functools import lru_cache
import hashlib, json, math
from pathlib import Path
import urllib.request

from nmir.g9_ccsn_lens import annular_point_source_receiver_mu
from nmir.g9_global_kernel import signed_map_cm, refine_grid_once
from nmir.g9_turning_kernel import derivative_surrogate
from nmir.g9_independent_derivative import (
    RootCertificationBlocked, fixed_dyadic_points, independent_derivative,
    isolate_sign_roots,
)
from nmir.gravity_extended import combined_scan_grid, focal_distance_au, parse_model_s_text

MODEL_S_COMMIT="cfb2af4a17dc7fe0c367ebb1dbbc121483d2a38b"
MODEL_S_BLOB="e3a0fad3ff877338aad926dbd0a9a43e6c0a897f"
MODEL_S_URL="https://raw.githubusercontent.com/ramses-organisation/ramses/"+MODEL_S_COMMIT+"/patch/global_star/modelS/data/cptrho.l5bi.d.15c"
CONTRACT="7471acdf876e5a990505369db8a6888225052913"
R=6.96e10; X0S=(0.020,0.024,0.030); RADII=tuple(10.0**i for i in range(10))
STEPS=(1.0,0.5,0.25); TOL=1e-11; TIGHT=TOL/4.0


def blob_sha(data: bytes)->str:
    return hashlib.sha1(f"blob {len(data)}\0".encode()+data).hexdigest()

def rel(a,b):
    return abs(a-b)/max(abs(a),abs(b),1e-300)

def sgn(x): return -1 if x<0 else (1 if x>0 else 0)

def bisect(fn,lo,hi,tol=1e-12):
    fl,fh=fn(lo),fn(hi)
    if fl==0:return lo
    if fh==0:return hi
    if fl*fh>0: raise RootCertificationBlocked("original-map FD bracket has no sign reversal")
    while hi-lo>tol:
        m=(lo+hi)/2; fm=fn(m)
        if fm==0:return m
        if fl*fm<=0:hi,fh=m,fm
        else:lo,fl=m,fm
    return (lo+hi)/2

def dedup(xs,tol=1e-10):
    out=[]
    for x in sorted(xs):
        if not out or abs(x-out[-1])>tol:out.append(x)
    return out

def solve_target(yfn,lo,hi,target):
    fl,fh=yfn(lo)-target,yfn(hi)-target
    if abs(fl)<1e-15:return lo
    if abs(fh)<1e-15:return hi
    if fl*fh>0:return None
    return bisect(lambda x:yfn(x)-target,lo,hi)

def intervals_for_radius(yfn,segments,radius):
    cuts=[segments[0][0],segments[-1][1]]
    for lo,hi,_ in segments:
        cuts.extend((lo,hi))
        for t in (-radius,radius):
            r=solve_target(yfn,lo,hi,t)
            if r is not None:cuts.append(r)
    cuts=dedup(cuts,1e-11); accepted=[]
    for a,b in zip(cuts,cuts[1:]):
        if abs(yfn((a+b)/2))<=radius: accepted.append((a,b))
    merged=[]
    for a,b in accepted:
        if merged and a<=merged[-1][1]+1e-11: merged[-1]=(merged[-1][0],max(b,merged[-1][1]))
        else: merged.append((a,b))
    return merged

def area_for(yfn,segments,radius):
    iv=intervals_for_radius(yfn,segments,radius)
    area=math.pi*R*R*sum(b*b-a*a for a,b in iv)
    return area,iv

def certify(profile,focal,grid,x0):
    z=focal(x0)
    d=lambda x: independent_derivative(profile,x,z,R,TOL)
    dt=lambda x: independent_derivative(profile,x,z,R,TIGHT)
    roots=isolate_sign_roots(d,grid); tight=isolate_sign_roots(dt,grid)
    if len(roots)!=len(tight) or any(abs(a.root-b.root)>1e-9 for a,b in zip(roots,tight)):
        raise RootCertificationBlocked("independent derivative root set unstable under 4x tighter quadrature")
    fd_roots={s:[] for s in STEPS}
    confirmations=[]
    for rb in roots:
        ds=(sgn(d(rb.lo)),sgn(d(rb.hi)))
        row={"independent_root":rb.root,"bracket":[rb.lo,rb.hi],"fd":{}}
        for step in STEPS:
            fn=lambda x,step=step: derivative_surrogate(x,z,focal,R,(grid[0],grid[-1]),step)
            fs=(sgn(fn(rb.lo)),sgn(fn(rb.hi)))
            if 0 in fs or fs[0]==fs[1] or fs!=ds:
                raise RootCertificationBlocked(f"original-map FD sign reversal disagrees at step {step}")
            rr=bisect(fn,rb.lo,rb.hi)
            if abs(rr-rb.root)>1e-8:
                raise RootCertificationBlocked(f"original-map FD root disagrees at step {step}")
            fd_roots[step].append(rr); row["fd"][str(step)]=rr
        confirmations.append(row)
    # Independent roots are authoritative only for partition proposal; add generating root.
    bounds=dedup([grid[0],grid[-1],x0]+[r.root for r in roots],1e-11)
    yfn=lambda x:signed_map_cm(x,z,focal,R)
    segments=[]; audit_count=0
    for lo,hi in zip(bounds,bounds[1:]):
        if hi-lo<=1e-12:continue
        orient=sgn(yfn(hi)-yfn(lo))
        if orient==0:raise RootCertificationBlocked("zero-orientation certified segment")
        for x in fixed_dyadic_points(grid,lo,hi):
            signs=[]
            for step in STEPS:
                signs.append(sgn(derivative_surrogate(x,z,focal,R,(grid[0],grid[-1]),step)))
            audit_count+=1
            if 0 in signs or len(set(signs))!=1 or signs[0]!=orient:
                raise RootCertificationBlocked("fixed dyadic original-map derivative audit disagreement")
        segments.append((lo,hi,orient))
    # Generating root and all y=0 roots.
    zeros=[]
    for lo,hi,_ in segments:
        r=solve_target(yfn,lo,hi,0.0)
        if r is not None: zeros.append(r)
    zeros=dedup(zeros,1e-9)
    if not zeros or min(abs(r-x0) for r in zeros)>1e-10:
        raise RootCertificationBlocked("generating root not recovered")
    areas=[]; prev=-1.0; ceiling=math.pi*R*R
    for radius in RADII:
        a,iv=area_for(yfn,segments,radius)
        if not math.isfinite(a) or a<0 or a+1e-10*ceiling<prev or a>ceiling*(1+1e-10):
            raise RuntimeError("area invariant failure")
        prev=a; areas.append({"radius_cm":radius,"area_cm2":a,"intervals":iv})
    return {"x0":x0,"observer_au":z,"roots":[r.root for r in roots],"confirmations":confirmations,
            "fd_roots":fd_roots,"segments":segments,"dyadic_audit_points":audit_count,"zero_roots":zeros,"areas":areas}

def main():
    try:
        payload=urllib.request.urlopen(MODEL_S_URL,timeout=30).read(); blob=blob_sha(payload)
        if blob!=MODEL_S_BLOB: raise RootCertificationBlocked("pinned Model-S blob mismatch")
        profile=parse_model_s_text(payload.decode())
        @lru_cache(maxsize=None)
        def focal(x): return focal_distance_au(profile,x,R)
        grid=combined_scan_grid(); fine=refine_grid_once(grid)
        base=[certify(profile,focal,grid,x0) for x0 in X0S]
        fine_rows=[certify(profile,focal,fine,x0) for x0 in X0S]
        max_grid=0.0; max_step=0.0; local=[]
        for b,f in zip(base,fine_rows):
            for p,q in zip(b["areas"],f["areas"]): max_grid=max(max_grid,rel(p["area_cm2"],q["area_cm2"]))
            # Step-specific certified root partitions as validation replicas.
            for step in (0.5,0.25):
                bounds=dedup([grid[0],grid[-1],b["x0"]]+b["fd_roots"][step],1e-11)
                yfn=lambda x,z=b["observer_au"]:signed_map_cm(x,z,focal,R)
                seg=[(a,c,sgn(yfn(c)-yfn(a))) for a,c in zip(bounds,bounds[1:])]
                for p in b["areas"]:
                    a,_=area_for(yfn,seg,p["radius_cm"]); max_step=max(max_step,rel(p["area_cm2"],a))
        row=base[1]; yfn=lambda x:signed_map_cm(x,row["observer_au"],focal,R)
        for rc in (100.0,1000.0,10000.0):
            a,ivs=area_for(yfn,row["segments"],rc); global_mu=a/(math.pi*rc*rc)
            exact=annular_point_source_receiver_mu(0.024,rc,R,focal)[3]
            containing=[iv for iv in ivs if iv[0]<=0.024<=iv[1]]
            lm=None if len(containing)!=1 else R*R*(containing[0][1]**2-containing[0][0]**2)/(rc*rc)
            local.append({"radius_cm":rc,"global_mu":global_mu,"exact_one_ring_mu":exact,"local_mu":lm,
                          "rel":float("inf") if lm is None else rel(lm,exact),"contains":global_mu+1e-12>=exact})
        local_ok=all(x["contains"] and x["rel"]<=0.005 for x in local)
        passed=max_grid<=0.005 and max_step<=0.005 and local_ok
        status="PASS_G9_INDEPENDENT_DERIVATIVE_ROOT_CERTIFIED_KERNEL" if passed else "SCIENTIFIC_FAIL_G9_ROOT_CERTIFIED_KERNEL"
        result={"status":status,"contract_commit":CONTRACT,"model_s_git_blob_sha1":blob,"branches":base,
                "max_grid_area_rel":max_grid,"max_step_area_rel":max_step,"one_ring":local,
                "criteria":{"grid_0p5pct":max_grid<=0.005,"step_0p5pct":max_step<=0.005,"one_ring_0p5pct":local_ok},
                "scope":"G9 transparent-Sun radial numerical geometry only; no persistent-source convolution or BSM"}
    except RootCertificationBlocked as exc:
        result={"status":"BLOCKED_G9_ROOT_CERTIFICATION","reason":str(exc),"contract_commit":CONTRACT,
                "model_s_git_blob_sha1":locals().get("blob"),"scope":"G9 numerical root certification only"}
    except (OSError,urllib.error.URLError) as exc:
        result={"status":"INFRASTRUCTURE_FAIL_G9_ROOT_CERTIFICATION","reason":str(exc),"contract_commit":CONTRACT}
    except Exception as exc:
        result={"status":"SCIENTIFIC_FAIL_G9_ROOT_CERTIFIED_KERNEL","reason":str(exc),"contract_commit":CONTRACT,
                "model_s_git_blob_sha1":locals().get("blob")}
    Path("g9_0088_result.json").write_text(json.dumps(result,indent=2,sort_keys=True,default=str)+"\n")
    print(json.dumps(result,indent=2,sort_keys=True,default=str))
    if result["status"] in ("SCIENTIFIC_FAIL_G9_ROOT_CERTIFIED_KERNEL","INFRASTRUCTURE_FAIL_G9_ROOT_CERTIFICATION"):
        raise SystemExit(1)

if __name__=="__main__": main()
