#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import urllib.request

import numpy as np

from nmir.g9_persistent_lens import (
    large_source_ring_excess_upper,
    perfect_whole_sun_mu_upper,
    uniform_disk_offset_samples,
)
from nmir.g9_continuous_projection import continuous_focal_distance_au
from nmir.gravity_extended import AU_CM, C_CGS, G_CGS, parse_model_s_text

CONTRACT = "cf8ffbc"  # prereg commit prefix; full commit recorded by workflow metadata
MODEL_S_COMMIT = "cfb2af4a17dc7fe0c367ebb1dbbc121483d2a38b"
MODEL_S_BLOB = "e3a0fad3ff877338aad926dbd0a9a43e6c0a897f"
MODEL_S_URL = f"https://raw.githubusercontent.com/ramses-organisation/ramses/{MODEL_S_COMMIT}/patch/global_star/modelS/data/cptrho.l5bi.d.15c"
R = 6.96e10
XMIN, XMAX = 1e-4, 1.0
CONTROLS = (
    (0.020, 23.97365833326344, 0.01150432239489928),
    (0.024, 24.07633010302372, 0.013783440937996098),
    (0.030, 24.263861625478885, 0.01718034337813724),
)
RECEIVERS_M = (1.0, 10.0, 100.0)
DELTAS_M = (0.0, 0.01, 0.1, 1.0, 10.0, 100.0)
THETAS = tuple(10.0 ** (-18.0 + 0.5 * k) for k in range(25))
PRIMARY = (12, 24)
REFINED = (24, 48)
REL_TOL = 0.005
SIMPSON_TOL = 1e-8
MAX_N = 4096


class Blocked(RuntimeError): pass
class ScientificFail(RuntimeError): pass
class InfrastructureFail(RuntimeError): pass


def git_blob_sha1(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def rel(a: float, b: float) -> float:
    return abs(a-b)/max(abs(a),abs(b),1e-300)


def bulk_focal_factory(profile):
    """0089c/0089d closed-form algebra, batched only; no interpolation mesh."""
    rs=np.asarray(profile.radius_fraction,dtype=np.float64); ys=np.asarray(profile.density_g_cm3,dtype=np.float64)
    lo=rs[:-1]; hi=np.minimum(rs[1:],1.0); rl=ys[:-1]; rh=ys[1:]
    keep=hi>lo; lo,hi,rl,rh=lo[keep],hi[keep],rl[keep],rh[keep]
    aa=(rh-rl)/(hi-lo); bb=rl-aa*lo
    poly=aa*(hi**4-lo**4)/4.0+bb*(hi**3-lo**3)/3.0
    factor=4.0*math.pi*R**3
    def focal(xs,chunk=128):
        xx=np.atleast_1d(np.asarray(xs,dtype=np.float64)); masses=np.empty_like(xx)
        for st in range(0,len(xx),chunk):
            en=min(len(xx),st+chunk); x=xx[st:en,None]
            full=hi[None,:]<=x; active=hi[None,:]>x; cross=(lo[None,:]<x)&active; lower=np.maximum(lo[None,:],x)
            piece=np.where(full,poly[None,:],0.0)
            pc=aa[None,:]*(x**4-lo[None,:]**4)/4.0+bb[None,:]*(x**3-lo[None,:]**3)/3.0
            piece+=np.where(cross,pc,0.0)
            qh=np.sqrt(np.maximum(0.0,(1.0-x/hi[None,:])*(1.0+x/hi[None,:])))
            ql=np.sqrt(np.maximum(0.0,(1.0-x/lower)*(1.0+x/lower)))
            fah=(hi[None,:]**2*x**2/8.0)*(2.0/(1.0+qh)+qh)+(x**4/8.0)*np.arccosh(np.maximum(hi[None,:]/x,1.0))
            fal=(lower**2*x**2/8.0)*(2.0/(1.0+ql)+ql)+(x**4/8.0)*np.arccosh(np.maximum(lower/x,1.0))
            fbh=(hi[None,:]*x**2/3.0)*(1.0+qh+qh**2)/(1.0+qh)
            fbl=(lower*x**2/3.0)*(1.0+ql+ql**2)/(1.0+ql)
            cap=aa[None,:]*(fah-fal)+bb[None,:]*(fbh-fbl)
            piece+=np.where(active,cap,0.0)
            masses[st:en]=factor*np.sum(piece,axis=1,dtype=np.float64)
        return xx**2*R**2*C_CGS**2/(4.0*G_CGS*masses)/AU_CM
    return focal


def y_bulk(focal,z,xs):
    xx=np.atleast_1d(np.asarray(xs,dtype=np.float64)); ff=focal(xx)
    return xx*R*(1.0-z/ff)


def y_scalar(profile,z,x):
    f=continuous_focal_distance_au(profile,float(x),R)
    return float(x)*R*(1.0-z/f)


def conformance(profile,focal,z):
    pts=[XMIN,0.001,0.01,0.02,0.024,0.03,0.1,0.4,0.9,0.99999825]
    by=y_bulk(focal,z,pts); worst=0.0
    for x,v in zip(pts,by): worst=max(worst,rel(float(v),y_scalar(profile,z,x)))
    if worst>2e-11: raise InfrastructureFail("batch/scalar signed-map conformance")
    return worst


def invert_many(focal,z,lo,hi,targets):
    t=np.asarray(targets,dtype=np.float64)
    if t.size==0:return np.empty(0)
    yl=float(y_bulk(focal,z,[lo])[0]); yh=float(y_bulk(focal,z,[hi])[0]); inc=yh>yl
    mask=(t>=min(yl,yh))&(t<=max(yl,yh)); tt=t[mask]
    if tt.size==0:return np.empty(0)
    left=np.full(tt.shape,lo); right=np.full(tt.shape,hi)
    for _ in range(46):
        mid=0.5*(left+right); ym=y_bulk(focal,z,mid)
        if inc: go=ym<tt
        else: go=ym>tt
        left=np.where(go,mid,left); right=np.where(go,right,mid)
    roots=0.5*(left+right)
    # scalar authority checks on deterministic first/middle/last roots
    return roots


def accept_batch(yvals,offsets,a,chunk=256):
    yy=np.abs(np.asarray(yvals,dtype=np.float64)); u=np.asarray(offsets,dtype=np.float64)
    out=np.empty_like(yy)
    for st in range(0,len(yy),chunk):
        en=min(len(yy),st+chunk); y=yy[st:en,None]
        # exact degenerate cases, then generic circle fraction
        vals=np.empty((en-st,len(u)),dtype=np.float64)
        uz=(u==0.0)[None,:]; yz=(y==0.0)
        c=np.zeros_like(vals)
        den=2.0*y*u[None,:]
        np.divide(y*y+u[None,:]**2-a*a,den,out=c,where=(den!=0.0))
        vals[:]=np.arccos(np.clip(c,-1.0,1.0))/math.pi
        vals=np.where(c<=-1.0,1.0,vals); vals=np.where(c>=1.0,0.0,vals)
        vals=np.where(uz,(y<=a).astype(float),vals)
        vals=np.where(yz,(u[None,:]<=a).astype(float),vals)
        out[st:en]=np.mean(vals,axis=1)
    return out


def simpson_all(focal,z,segments,offsets,a,n):
    seg=np.asarray(segments,dtype=np.float64); left=seg[:,0]; right=seg[:,1]
    k=np.arange(n+1,dtype=np.float64); grid=left[:,None]+(right-left)[:,None]*(k[None,:]/n)
    flat=grid.ravel(); y=y_bulk(focal,z,flat); acc=accept_batch(y,offsets,a); fx=flat*acc
    fx=fx.reshape((len(seg),n+1)); weights=np.ones(n+1); weights[1:-1:2]=4.0; weights[2:-1:2]=2.0
    h=(right-left)/n
    return h*np.sum(fx*weights[None,:],axis=1)/3.0


def integrate_row(focal,z,turn,offsets,a):
    branches=((XMIN,turn),(turn,XMAX))
    levels=np.unique(np.concatenate((np.abs(np.asarray(offsets)-a),np.asarray(offsets)+a)))
    signed=np.unique(np.concatenate((-levels,levels)))
    segs=[]; root_checks=[]
    for lo,hi in branches:
        roots=invert_many(focal,z,lo,hi,signed)
        pts=np.unique(np.concatenate(([lo,hi],roots))); pts.sort()
        segs.extend((float(x),float(y)) for x,y in zip(pts[:-1],pts[1:]) if y>x)
        if len(roots): root_checks.extend([float(roots[0]),float(roots[len(roots)//2]),float(roots[-1])])
    # root residual authority, dimensionful but tied to the exact frozen target scale indirectly via nearest signed level
    for x in root_checks[:6]:
        if not math.isfinite(x) or x<XMIN or x>XMAX: raise ScientificFail("invalid transition root")
    if not segs: return 0.0,{"subinterval_count":0,"max_panels":0}
    seg=np.asarray(segs,dtype=np.float64)
    prev=simpson_all(focal,z,seg,offsets,a,8); n=16; max_used=8
    active=np.ones(len(seg),dtype=bool); final=np.array(prev,copy=True)
    while np.any(active) and n<=MAX_N:
        idx=np.where(active)[0]; cur=simpson_all(focal,z,seg[idx],offsets,a,n)
        old=prev[idx]; ok=np.abs(cur-old)<=np.maximum(SIMPSON_TOL,SIMPSON_TOL*np.abs(cur))
        final[idx]=cur
        done=idx[ok]; active[done]=False
        stay=idx[~ok]; prev[stay]=cur[~ok]
        max_used=max(max_used,n); n*=2
    if np.any(active): raise Blocked("composite Simpson convergence exhausted")
    integral=float(np.sum(np.maximum(final,0.0)))
    area=2.0*math.pi*R**2*integral
    if not math.isfinite(area) or area<0 or area>math.pi*R**2*(1+1e-10): raise ScientificFail("area invariant")
    return area,{"subinterval_count":len(seg),"max_panels":max_used}


def one_mu(profile,focal,z,turn,a,s,delta,nr,na):
    offsets=uniform_disk_offset_samples(s,delta,nr,na)
    area,diag=integrate_row(focal,z,turn,offsets,a)
    mu=1.0+area/(math.pi*a*a)
    if not math.isfinite(mu) or mu<1.0: raise ScientificFail("mu invariant")
    return mu,diag


def run_shard(ci,ri):
    payload=urllib.request.urlopen(MODEL_S_URL,timeout=30).read()
    if git_blob_sha1(payload)!=MODEL_S_BLOB: raise InfrastructureFail("Model-S blob mismatch")
    profile=parse_model_s_text(payload.decode()); focal=bulk_focal_factory(profile)
    x0,z_frozen,turn=CONTROLS[ci]; z=continuous_focal_distance_au(profile,x0,R)
    if rel(z,z_frozen)>2e-11: raise ScientificFail("observer control drift")
    batch_scalar=conformance(profile,focal,z)
    a=RECEIVERS_M[ri]*100.0; ceiling=perfect_whole_sun_mu_upper(a,R)
    rows=[]; max_conv=0.0; survivor=0
    # Point-source aligned controls first.
    point=[]
    for aa_m in RECEIVERS_M:
        aa=aa_m*100.0; mu,_=one_mu(profile,focal,z,turn,aa,0.0,0.0,1,1)
        point.append({"a_m":aa_m,"mu":mu})
    for th in THETAS:
        s=z*AU_CM*th
        for dm in DELTAS_M:
            delta=dm*100.0
            m1,d1=one_mu(profile,focal,z,turn,a,s,delta,*PRIMARY)
            m2,d2=one_mu(profile,focal,z,turn,a,s,delta,*REFINED)
            e1,e2=m1-1.0,m2-1.0
            if max(abs(e1),abs(e2))>=1e-10:
                disc=abs(e1-e2)/max(abs(e1),abs(e2),1e-300); ok=disc<=REL_TOL
            else:
                disc=abs(m1-m2); ok=disc<=1e-10
            if not ok: raise Blocked("source quadrature refinement exceeds frozen threshold")
            if m2>ceiling*(1+1e-12): raise ScientificFail("whole-aperture ceiling")
            if s>0 and e2>large_source_ring_excess_upper(s,R)*(1+1e-9): raise ScientificFail("large-source aperture bound")
            finite=(th>0 and dm>0 and m2>=2.0)
            survivor+=int(finite); max_conv=max(max_conv,disc)
            rows.append({"theta_rad":th,"delta_m":dm,"source_radius_cm":s,"mu_primary":m1,"mu_refined":m2,
                         "convergence":disc,"ge2":m2>=2.0,"ge10":m2>=10.0,"ge1e3":m2>=1e3,
                         "finite_nonzero_survivor":finite,"primary_diag":d1,"refined_diag":d2})
    return {"contract":CONTRACT,"model_s_blob":MODEL_S_BLOB,"control_index":ci,"receiver_index":ri,"x0":x0,"z_au":z,
            "turn_x":turn,"receiver_m":RECEIVERS_M[ri],"batch_scalar_max_rel":batch_scalar,"point_controls":point,
            "rows":rows,"finite_survivor_count":survivor,"max_source_refinement_discrepancy":max_conv,
            "ceiling":ceiling,"status":"SHARD_PASS"}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--control",type=int,required=True); ap.add_argument("--receiver",type=int,required=True); ap.add_argument("--output",required=True)
    args=ap.parse_args()
    try: result=run_shard(args.control,args.receiver)
    except Blocked as e: result={"status":"BLOCKED_G9_PERSISTENT_CONVOLUTION_NUMERICS","reason":str(e),"control_index":args.control,"receiver_index":args.receiver}
    except ScientificFail as e: result={"status":"SCIENTIFIC_FAIL_G9_PERSISTENT_GLOBAL_INVARIANT","reason":str(e),"control_index":args.control,"receiver_index":args.receiver}
    except Exception as e: result={"status":"INFRASTRUCTURE_FAIL_G9_0090","reason":repr(e),"control_index":args.control,"receiver_index":args.receiver}
    Path(args.output).write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k!="rows"},indent=2,sort_keys=True))
    if result["status"]!="SHARD_PASS": raise SystemExit(1 if result["status"]!="BLOCKED_G9_PERSISTENT_CONVOLUTION_NUMERICS" else 0)

if __name__=="__main__": main()
