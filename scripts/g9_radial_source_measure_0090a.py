#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import os
from pathlib import Path
import urllib.request

import numpy as np
from numpy.polynomial.legendre import leggauss

from g9_persistent_global_0090 import (
    MODEL_S_BLOB,
    MODEL_S_URL,
    R,
    XMIN,
    XMAX,
    CONTROLS,
    RECEIVERS_M,
    DELTAS_M,
    THETAS,
    git_blob_sha1,
    bulk_focal_factory,
    y_bulk,
    conformance,
)
from nmir.g9_continuous_projection import continuous_focal_distance_au
from nmir.gravity_extended import AU_CM, parse_model_s_text

CONTRACT = "fb4aad7d1ffe23fb4863d09e26c0c3b20f47364c"
ORDERS = (32, 64)
THETA_INDICES = (0, 6, 12, 18, 24)
REL_TOL = 0.005
NORM_TOL = 2e-10
MAP_TOL = 2e-11

REFERENCE_0089E = {
    "run": 34227872401,
    "job": 102066360966,
    "artifact": 10061342281,
    "zip_sha256": "d76b3937a9ea0fcced50769c8098642b96e1345dd1f5b77bbd1754f53c104bb3",
    "json_sha256": "010a9f55c11c9bb7c7020293f2ebef9ce3e00b4dc8401ade700a417c327ba56e",
}
REFERENCE_AREAS_CM2 = {
    0: {100.0: 89603387150718.505626122216462361306689896924504029,
        1000.0: 896033874366433.44608527755138163715935203488917499,
        10000.0: 8960341602650288.2731453480626673137684942466225575},
    1: {100.0: 75413795300055.545733581322971620931795363473709321,
        1000.0: 754137953799252.78502926500138849650133246383029423,
        10000.0: 7541380336361811.3548610233212145292519349034602974},
    2: {100.0: 61412376211279.143724259938491785705633497236858798,
        1000.0: 614123762287926.58687309644010362472213205020299952,
        10000.0: 6141237797984624.7601542407982892513052384309387309},
}


class Blocked(RuntimeError):
    pass


class ScientificFail(RuntimeError):
    pass


class InfrastructureFail(RuntimeError):
    pass


def rel(a: float, b: float) -> float:
    return abs(a-b)/max(abs(a),abs(b),1e-300)


def phi_fraction(y: np.ndarray, u: np.ndarray, a: float) -> np.ndarray:
    """Fraction of an incident ring at |y| accepted by receiver disk radius a."""
    yy=np.asarray(y,dtype=np.float64)
    uu=np.asarray(u,dtype=np.float64)
    Y,U=np.broadcast_arrays(yy,uu)
    out=np.zeros_like(Y)
    yz=Y==0.0; uz=U==0.0
    out=np.where(yz,(U<=a).astype(float),out)
    out=np.where(uz,(Y<=a).astype(float),out)
    generic=~(yz|uz)
    if np.any(generic):
        c=np.empty_like(Y)
        c[generic]=(Y[generic]**2+U[generic]**2-a*a)/(2.0*Y[generic]*U[generic])
        vals=np.zeros_like(Y)
        vals[generic]=np.arccos(np.clip(c[generic],-1.0,1.0))/math.pi
        vals=np.where(generic&(c<=-1.0),1.0,vals)
        vals=np.where(generic&(c>=1.0),0.0,vals)
        out=np.where(generic,vals,out)
    return out


def omega(u: np.ndarray, s: float, d: float) -> np.ndarray:
    """Angular measure of source-disk circumference at radial source offset u."""
    uu=np.asarray(u,dtype=np.float64)
    out=np.zeros_like(uu)
    if s<=0.0:
        return out
    if d==0.0:
        return np.where((uu>=0.0)&(uu<=s),2.0*math.pi,0.0)
    if d<s:
        full=(uu>=0.0)&(uu<=s-d)
        out=np.where(full,2.0*math.pi,out)
    partial=(uu>abs(s-d))&(uu<s+d)&(uu>0.0)
    if np.any(partial):
        c=(uu[partial]**2+d*d-s*s)/(2.0*uu[partial]*d)
        out[partial]=2.0*np.arccos(np.clip(c,-1.0,1.0))
    return out


def radial_density(u: np.ndarray, s: float, d: float) -> np.ndarray:
    return np.asarray(u,dtype=np.float64)*omega(u,s,d)/(math.pi*s*s)


def source_support(s: float, d: float) -> tuple[float,float]:
    if d==0.0:
        return 0.0,s
    return max(0.0,d-s),d+s


def source_intervals(s: float, d: float, a: float) -> list[tuple[float,float]]:
    lo,hi=source_support(s,d)
    candidates=[lo,hi,0.0,max(0.0,s-d),abs(s-d),s+d,a]
    pts=sorted({float(x) for x in candidates if lo<=x<=hi})
    if not pts or pts[0]!=lo: pts.insert(0,lo)
    if pts[-1]!=hi: pts.append(hi)
    return [(x,y) for x,y in zip(pts[:-1],pts[1:]) if y>x]


def gauss_integral(func, lo: float, hi: float, order: int) -> float:
    if hi<=lo: return 0.0
    q,w=leggauss(order)
    x=0.5*(hi-lo)*q+0.5*(hi+lo)
    return 0.5*(hi-lo)*float(np.dot(w,np.asarray(func(x),dtype=np.float64)))


def abs_y(focal,z,xs):
    return np.abs(y_bulk(focal,z,xs))


def monotone_abs_segments(turn: float, x0: float) -> tuple[tuple[float,float],...]:
    pts=sorted({XMIN,float(turn),float(x0),XMAX})
    return tuple((a,b) for a,b in zip(pts[:-1],pts[1:]) if b>a)


def threshold_root(focal,z,lo: float,hi: float,target: float) -> float | None:
    yl=float(abs_y(focal,z,[lo])[0])-target
    yh=float(abs_y(focal,z,[hi])[0])-target
    scale=max(target,1.0)
    eps=2e-13*scale
    if abs(yl)<=eps: return lo
    if abs(yh)<=eps: return hi
    if yl*yh>0.0: return None
    left,right=lo,hi
    fl=yl
    for _ in range(58):
        mid=0.5*(left+right)
        fm=float(abs_y(focal,z,[mid])[0])-target
        if fm==0.0:
            left=right=mid; break
        if fl*fm<=0.0:
            right=mid
        else:
            left=mid; fl=fm
    return 0.5*(left+right)


def b_intervals(focal,z,turn,x0,u: float,a: float) -> list[tuple[float,float]]:
    pts={XMIN,float(turn),float(x0),XMAX}
    for target in (abs(u-a),u+a):
        for lo,hi in monotone_abs_segments(turn,x0):
            root=threshold_root(focal,z,lo,hi,float(target))
            if root is not None: pts.add(float(root))
    xs=sorted(pts)
    return [(lo,hi) for lo,hi in zip(xs[:-1],xs[1:]) if hi>lo]


def area_at_u(focal,z,turn,x0,u: float,a: float,order: int) -> float:
    total=0.0
    for lo,hi in b_intervals(focal,z,turn,x0,u,a):
        def integrand(x):
            yy=abs_y(focal,z,x)
            return x*phi_fraction(yy,np.full_like(yy,u),a)
        total += gauss_integral(integrand,lo,hi,order)
    area=2.0*math.pi*R*R*total
    if not math.isfinite(area) or area<0.0 or area>math.pi*R*R*(1+1e-10):
        raise ScientificFail("accepted-area invariant")
    return area


def point_area_exact(focal,z,turn,x0,a: float) -> float:
    pts={XMIN,float(turn),float(x0),XMAX}
    for lo,hi in monotone_abs_segments(turn,x0):
        root=threshold_root(focal,z,lo,hi,a)
        if root is not None: pts.add(float(root))
    xs=sorted(pts); area=0.0
    for lo,hi in zip(xs[:-1],xs[1:]):
        mid=0.5*(lo+hi)
        if float(abs_y(focal,z,[mid])[0])<=a:
            area += math.pi*R*R*(hi*hi-lo*lo)
    if not math.isfinite(area) or area<0.0 or area>math.pi*R*R*(1+1e-10):
        raise ScientificFail("point area invariant")
    return area


def radial_normalization(s: float,d: float,a: float,order: int) -> float:
    return sum(gauss_integral(lambda u: radial_density(u,s,d),lo,hi,order)
               for lo,hi in source_intervals(s,d,a))


def averaged_area(focal,z,turn,x0,a: float,s: float,d: float,order: int) -> float:
    total=0.0
    q,w=leggauss(order)
    for lo,hi in source_intervals(s,d,a):
        us=0.5*(hi-lo)*q+0.5*(hi+lo)
        pd=radial_density(us,s,d)
        areas=np.array([area_at_u(focal,z,turn,x0,float(u),a,order) for u in us])
        total += 0.5*(hi-lo)*float(np.dot(w,pd*areas))
    if not math.isfinite(total) or total<0.0 or total>math.pi*R*R*(1+1e-9):
        raise ScientificFail("source-averaged area invariant")
    return total


def convergence(mu_l: float,mu_h: float) -> float:
    el,eh=mu_l-1.0,mu_h-1.0
    if max(abs(el),abs(eh))>=1e-10:
        return abs(el-eh)/max(abs(el),abs(eh),1e-300)
    return abs(mu_l-mu_h)


def run_shard(ci: int,ri: int) -> dict:
    payload=urllib.request.urlopen(MODEL_S_URL,timeout=30).read()
    if git_blob_sha1(payload)!=MODEL_S_BLOB:
        raise InfrastructureFail("Model-S blob mismatch")
    profile=parse_model_s_text(payload.decode())
    focal=bulk_focal_factory(profile)
    x0,z_frozen,turn=CONTROLS[ci]
    z=continuous_focal_distance_au(profile,x0,R)
    focal_drift=rel(z,z_frozen)
    if focal_drift>MAP_TOL: raise ScientificFail("observer focal drift")
    batch_scalar=conformance(profile,focal,z)
    if batch_scalar>MAP_TOL: raise ScientificFail("batch/scalar signed-map conformance")

    a=RECEIVERS_M[ri]*100.0
    point_area=point_area_exact(focal,z,turn,x0,a)
    ref_area=REFERENCE_AREAS_CM2[ci][a]
    point_rel=rel(point_area,ref_area)
    if point_rel>REL_TOL: raise Blocked("0089e aligned point-control mismatch")

    rows=[]; max_norm=0.0; max_conv=0.0
    for ti in THETA_INDICES:
        theta=THETAS[ti]
        s=z*AU_CM*theta
        for dm in DELTAS_M:
            d=dm*100.0
            n_h=radial_normalization(s,d,a,ORDERS[1])
            nerr=abs(n_h-1.0)
            max_norm=max(max_norm,nerr)
            if nerr>NORM_TOL: raise Blocked("radial source normalization exceeds frozen threshold")
            area_l=averaged_area(focal,z,turn,x0,a,s,d,ORDERS[0])
            area_h=averaged_area(focal,z,turn,x0,a,s,d,ORDERS[1])
            mu_l=1.0+area_l/(math.pi*a*a)
            mu_h=1.0+area_h/(math.pi*a*a)
            if not (math.isfinite(mu_l) and math.isfinite(mu_h) and mu_l>=1.0 and mu_h>=1.0):
                raise ScientificFail("magnification invariant")
            disc=convergence(mu_l,mu_h); max_conv=max(max_conv,disc)
            limit=REL_TOL if max(abs(mu_l-1.0),abs(mu_h-1.0))>=1e-10 else 1e-10
            if disc>limit: raise Blocked("L/H radial-source quadrature exceeds frozen threshold")
            rows.append({"theta_index":ti,"theta_rad":theta,"source_radius_cm":s,"delta_m":dm,
                         "normalization_h":n_h,"normalization_abs_error":nerr,
                         "area_l_cm2":area_l,"area_h_cm2":area_h,"mu_l":mu_l,"mu_h":mu_h,
                         "convergence":disc})
    return {"status":"SHARD_PASS","contract":CONTRACT,"head_sha":os.getenv("GITHUB_SHA"),
            "model_s_blob":MODEL_S_BLOB,"reference_0089e":REFERENCE_0089E,
            "control_index":ci,"receiver_index":ri,"x0":x0,"z_au":z,"turn_x":turn,
            "receiver_m":RECEIVERS_M[ri],"focal_drift":focal_drift,"batch_scalar_max_rel":batch_scalar,
            "point_control":{"area_cm2":point_area,"reference_area_cm2":ref_area,"relative_error":point_rel},
            "max_normalization_abs_error":max_norm,"max_lh_discrepancy":max_conv,"rows":rows}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--control",type=int,required=True)
    ap.add_argument("--receiver",type=int,required=True); ap.add_argument("--output",required=True)
    args=ap.parse_args()
    try:
        result=run_shard(args.control,args.receiver)
    except Blocked as e:
        result={"status":"BLOCKED_G9_RADIAL_SOURCE_MEASURE_QUADRATURE","reason":str(e),"control_index":args.control,"receiver_index":args.receiver,"contract":CONTRACT,"head_sha":os.getenv("GITHUB_SHA")}
    except ScientificFail as e:
        result={"status":"SCIENTIFIC_FAIL_G9_RADIAL_SOURCE_MEASURE_INVARIANT","reason":str(e),"control_index":args.control,"receiver_index":args.receiver,"contract":CONTRACT,"head_sha":os.getenv("GITHUB_SHA")}
    except Exception as e:
        result={"status":"INFRASTRUCTURE_FAIL_G9_0090A","reason":repr(e),"control_index":args.control,"receiver_index":args.receiver,"contract":CONTRACT,"head_sha":os.getenv("GITHUB_SHA")}
    Path(args.output).write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k!="rows"},indent=2,sort_keys=True))
    if result["status"] in ("INFRASTRUCTURE_FAIL_G9_0090A","SCIENTIFIC_FAIL_G9_RADIAL_SOURCE_MEASURE_INVARIANT"):
        raise SystemExit(1)

if __name__=="__main__": main()
