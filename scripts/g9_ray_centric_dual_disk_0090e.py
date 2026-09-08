#!/usr/bin/env python3
from __future__ import annotations

import argparse
import functools
import json
import math
import os
from pathlib import Path
import urllib.request

import mpmath as mp
import numpy as np
from numpy.polynomial.legendre import leggauss as numpy_leggauss

import g9_radial_source_measure_0090a as radial
from g9_persistent_global_0090 import (
    MODEL_S_BLOB, MODEL_S_URL, R, CONTROLS, RECEIVERS_M, THETAS,
    git_blob_sha1, bulk_focal_factory, conformance,
)
from nmir.g9_continuous_projection import continuous_focal_distance_au
from nmir.gravity_extended import AU_CM, parse_model_s_text

CONTRACT = "c9d9e46860ef55bec2a5aaaafdac19f6e9de551b"
AMENDMENT = "c95fd80e7b2a54d04f83103e7678acbe8c51f6c6"
THETA_INDICES = (0, 12, 24)
DELTA_M = (0.0, 0.1, 100.0)
REPLICAS = {"L": (16, 32), "H": (32, 64)}  # angular, radial
REL_TOL = 0.005
ABS_SMALL_TOL = 1e-10
MAP_TOL = 2e-11
OVERLAP_SYM_TOL = 2e-14
OVERLAP_SCALE_TOL = 2e-13
MP_RATIO_TRIGGER = 1e-3
MP_DPS = 60


class Blocked(RuntimeError):
    pass


class ScientificFail(RuntimeError):
    pass


class InfrastructureFail(RuntimeError):
    pass


def rel(a: float, b: float) -> float:
    return abs(a-b)/max(abs(a),abs(b),1e-300)


@functools.lru_cache(maxsize=None)
def cached_leggauss(order: int):
    q,w=numpy_leggauss(int(order))
    q.setflags(write=False); w.setflags(write=False)
    return q,w

# Runtime-only optimization for inherited deterministic root-split helpers.
radial.leggauss = cached_leggauss


def _circle_overlap_mp(s: float, a: float, h: float) -> float:
    with mp.workdps(MP_DPS):
        ss=mp.mpf(s); aa=mp.mpf(a); hh=mp.mpf(h)
        c1=(hh*hh+ss*ss-aa*aa)/(2*hh*ss)
        c2=(hh*hh+aa*aa-ss*ss)/(2*hh*aa)
        c1=max(mp.mpf(-1),min(mp.mpf(1),c1))
        c2=max(mp.mpf(-1),min(mp.mpf(1),c2))
        rad=(-hh+ss+aa)*(hh+ss-aa)*(hh-ss+aa)*(hh+ss+aa)
        if rad < 0:
            rad=mp.mpf(0)
        out=ss*ss*mp.acos(c1)+aa*aa*mp.acos(c2)-mp.mpf('0.5')*mp.sqrt(rad)
        cap=mp.pi*min(ss,aa)**2
        tol=mp.mpf('1e-50')*max(cap,mp.mpf(1))
        if out < -tol or out > cap+tol or not mp.isfinite(out):
            raise ScientificFail("dual-disk high-precision overlap invariant")
        out=max(mp.mpf(0),min(cap,out))
        return float(out)


def _circle_overlap_double_partial(s: float, a: float, h: float) -> float | None:
    c1=(h*h+s*s-a*a)/(2.0*h*s)
    c2=(h*h+a*a-s*s)/(2.0*h*a)
    c1=min(1.0,max(-1.0,c1)); c2=min(1.0,max(-1.0,c2))
    rad=(-h+s+a)*(h+s-a)*(h-s+a)*(h+s+a)
    if rad < 0.0:
        return None
    out=s*s*math.acos(c1)+a*a*math.acos(c2)-0.5*math.sqrt(rad)
    cap=math.pi*min(s,a)**2
    eps=1e-13*max(cap,1.0)
    if not math.isfinite(out) or out < -eps or out > cap+eps:
        return None
    return min(cap,max(0.0,out))


def circle_overlap(s: float, a: float, h: float) -> float:
    s=float(s); a=float(a); h=float(h)
    if not (math.isfinite(s) and math.isfinite(a) and math.isfinite(h)):
        raise ScientificFail("non-finite dual-disk argument")
    if s<=0.0 or a<=0.0 or h<0.0:
        raise ScientificFail("invalid dual-disk argument")
    if h >= s+a:
        return 0.0
    if h <= abs(s-a):
        return math.pi*min(s,a)**2
    # Strict partial-overlap branch. Amendment 0090e-r1 freezes a
    # high-precision evaluation for disparate radii and as a deterministic
    # fallback when the direct IEEE-754 expression loses its exact range.
    ratio=min(s,a)/max(s,a,h)
    if ratio < MP_RATIO_TRIGGER:
        out=_circle_overlap_mp(s,a,h)
    else:
        out=_circle_overlap_double_partial(s,a,h)
        if out is None:
            out=_circle_overlap_mp(s,a,h)
    cap=math.pi*min(s,a)**2
    eps=1e-13*max(cap,1.0)
    if not math.isfinite(out) or out < -eps or out > cap+eps:
        raise ScientificFail("dual-disk overlap range invariant")
    return min(cap,max(0.0,out))


def overlap_fraction(s: float, a: float, h: float) -> float:
    return circle_overlap(s,a,h)/(math.pi*s*s)


def angular_split_points(y: float, s: float, d: float, a: float) -> tuple[float,...]:
    if y<=0.0 or d<=0.0:
        return (0.0,math.pi)
    pts=[0.0,math.pi]
    for t in (abs(s-a),s+a):
        if abs(y-d) <= t <= y+d:
            den=2.0*y*d
            c=(y*y+d*d-t*t)/den
            psi=math.acos(min(1.0,max(-1.0,c)))
            pts.append(psi)
    pts.sort()
    uniq=[]
    for x in pts:
        if not uniq or abs(x-uniq[-1]) > 8.0*math.ulp(max(1.0,abs(x),abs(uniq[-1]))):
            uniq.append(x)
    return tuple(uniq)


def angular_kernel(y: float, s: float, d: float, a: float, order: int) -> float:
    y=abs(float(y))
    if d==0.0:
        return overlap_fraction(s,a,y)
    if y==0.0:
        return overlap_fraction(s,a,d)
    q,w=cached_leggauss(order)
    total=0.0
    pts=angular_split_points(y,s,d,a)
    for lo,hi in zip(pts[:-1],pts[1:]):
        if hi<=lo:
            continue
        psi=0.5*(hi-lo)*q+0.5*(hi+lo)
        h=np.sqrt(np.maximum(0.0,y*y+d*d-2.0*y*d*np.cos(psi)))
        vals=np.array([overlap_fraction(s,a,float(hh)) for hh in h],dtype=np.float64)
        total += 0.5*(hi-lo)*float(np.dot(w,vals))
    k=total/math.pi
    cap=min(1.0,(a/s)**2)
    eps=1e-12*max(1.0,cap)
    if not math.isfinite(k) or k < -eps or k > cap+eps:
        raise ScientificFail("dual-disk angular kernel range invariant")
    return min(cap,max(0.0,k))


def radial_split_points(focal,z,turn: float,x0: float,s: float,d: float,a: float) -> tuple[float,...]:
    pts={radial.XMIN,float(turn),float(x0),radial.XMAX}
    t1=abs(s-a); t2=s+a
    targets={abs(d-t1),d+t1,abs(d-t2),d+t2}
    for target in sorted(targets):
        if not math.isfinite(target) or target<0.0:
            continue
        for lo,hi in radial.monotone_abs_segments(turn,x0):
            root=radial.threshold_root(focal,z,lo,hi,float(target))
            if root is not None:
                pts.add(float(root))
    return tuple(sorted(pts))


def ray_averaged_area(focal,z,turn: float,x0: float,a: float,s: float,d: float,
                      angular_order: int,radial_order: int) -> float:
    q,w=cached_leggauss(radial_order)
    total=0.0
    xs=radial_split_points(focal,z,turn,x0,s,d,a)
    for lo,hi in zip(xs[:-1],xs[1:]):
        if hi<=lo:
            continue
        x=0.5*(hi-lo)*q+0.5*(hi+lo)
        yy=radial.abs_y(focal,z,x)
        kval=np.array([angular_kernel(float(y),s,d,a,angular_order) for y in yy],dtype=np.float64)
        total += 0.5*(hi-lo)*float(np.dot(w,x*kval))
    area=2.0*math.pi*R*R*total
    cap=math.pi*R*R*(1.0+1e-9)
    if not math.isfinite(area) or area<0.0 or area>cap:
        raise ScientificFail("ray-centric accepted-area invariant")
    return area


def conv_metric(mu_l: float,mu_h: float) -> tuple[float,float]:
    el,eh=mu_l-1.0,mu_h-1.0
    if max(abs(el),abs(eh))>=ABS_SMALL_TOL:
        return abs(el-eh)/max(abs(el),abs(eh),1e-300),REL_TOL
    return abs(mu_l-mu_h),ABS_SMALL_TOL


def fixed_overlap_controls() -> dict:
    # Deterministic controls are scientific H1 checks, not fit points.
    disjoint=circle_overlap(2.0,3.0,5.0)
    containment=circle_overlap(2.0,3.0,0.5)
    if disjoint!=0.0 or containment!=math.pi*4.0:
        raise ScientificFail("dual-disk exact branch control")
    sym_cases=((2.0,3.0,2.5),(0.7,4.1,4.0),(5.0,1.2,5.3))
    max_sym=0.0
    for s,a,h in sym_cases:
        max_sym=max(max_sym,rel(circle_overlap(s,a,h),circle_overlap(a,s,h)))
    if max_sym>OVERLAP_SYM_TOL:
        raise ScientificFail("dual-disk symmetry control")
    base=(2.3,1.7,2.1); o0=circle_overlap(*base); max_scale=0.0
    for c in (1e-6,1.0,1e6):
        oc=circle_overlap(base[0]*c,base[1]*c,base[2]*c)/(c*c)
        max_scale=max(max_scale,rel(oc,o0))
    if max_scale>OVERLAP_SCALE_TOL:
        raise ScientificFail("dual-disk scale control")
    return {"disjoint":disjoint,"containment":containment,"max_symmetry_rel":max_sym,
            "max_scale_rel":max_scale}


def run_shard(ci: int,ri: int) -> dict:
    if ci not in (0,1,2) or ri not in (0,1,2):
        raise InfrastructureFail("invalid shard index")
    controls=fixed_overlap_controls()
    try:
        payload=urllib.request.urlopen(MODEL_S_URL,timeout=30).read()
    except Exception as e:
        raise InfrastructureFail(f"Model-S fetch failed: {e!r}") from e
    if git_blob_sha1(payload)!=MODEL_S_BLOB:
        raise InfrastructureFail("Model-S blob mismatch")
    profile=parse_model_s_text(payload.decode())
    focal=bulk_focal_factory(profile)
    x0,z_frozen,turn=CONTROLS[ci]
    z=continuous_focal_distance_au(profile,x0,R)
    focal_drift=rel(z,z_frozen)
    if focal_drift>MAP_TOL:
        raise ScientificFail("observer focal-distance drift")
    map_conf=conformance(profile,focal,z)
    if map_conf>MAP_TOL:
        raise ScientificFail("batch/scalar signed-map conformance")

    a=float(RECEIVERS_M[ri])*100.0
    point_area=radial.point_area_exact(focal,z,turn,x0,a)
    ref_area=radial.REFERENCE_AREAS_CM2[ci][a]
    point_rel=rel(point_area,ref_area)
    if point_rel>REL_TOL:
        raise Blocked(f"0089e point control mismatch rel={point_rel:.17g}")

    rows=[]; max_disc=0.0; point_limit_rel=None
    for ti in THETA_INDICES:
        theta=float(THETAS[ti]); s=z*AU_CM*theta
        if not (math.isfinite(s) and s>0.0):
            raise ScientificFail("invalid physical source radius")
        for dm in DELTA_M:
            d=dm*100.0
            try:
                area_l=ray_averaged_area(focal,z,turn,x0,a,s,d,*REPLICAS["L"])
                area_h=ray_averaged_area(focal,z,turn,x0,a,s,d,*REPLICAS["H"])
            except (Blocked,ScientificFail,InfrastructureFail):
                raise
            except Exception as e:
                raise InfrastructureFail(f"dual-disk evaluation failed at ti={ti},delta={dm}: {e!r}") from e
            mu_l=1.0+area_l/(math.pi*a*a)
            mu_h=1.0+area_h/(math.pi*a*a)
            if not (math.isfinite(mu_l) and math.isfinite(mu_h) and mu_l>=1.0 and mu_h>=1.0):
                raise ScientificFail("magnification invariant")
            disc,limit=conv_metric(mu_l,mu_h)
            max_disc=max(max_disc,disc)
            row={"theta_index":ti,"theta_rad":theta,"source_radius_cm":s,"delta_m":dm,
                 "area_l_cm2":area_l,"area_h_cm2":area_h,"mu_l":mu_l,"mu_h":mu_h,
                 "convergence":disc,"convergence_limit":limit}
            rows.append(row)
            if ti==0 and dm==0.0:
                point_limit_rel=rel(area_h,point_area) if point_area>0.0 else abs(area_h-point_area)
                row["point_limit_relative_error"]=point_limit_rel
                if point_limit_rel>REL_TOL:
                    raise Blocked(f"smallest-source aligned point-limit mismatch rel={point_limit_rel:.17g}")
            if disc>limit:
                raise Blocked(f"ray-centric L/H convergence miss ti={ti},delta_m={dm:g},metric={disc:.17g},limit={limit:.17g}")

    if len(rows)!=9:
        raise InfrastructureFail(f"shard row cardinality mismatch {len(rows)}")
    return {
        "status":"SHARD_PASS_G9_RAY_CENTRIC_DUAL_DISK",
        "contract":CONTRACT,"amendment":AMENDMENT,"head_sha":os.getenv("GITHUB_SHA"),"model_s_blob":MODEL_S_BLOB,
        "control_index":ci,"receiver_index":ri,"x0":x0,"z_au":z,"turn_x":turn,
        "receiver_m":float(RECEIVERS_M[ri]),"focal_drift":focal_drift,"batch_scalar_max_rel":map_conf,
        "overlap_controls":controls,
        "point_control":{"area_cm2":point_area,"reference_area_cm2":ref_area,"relative_error":point_rel,
                         "smallest_source_relative_error":point_limit_rel},
        "replicas":REPLICAS,"max_lh_discrepancy":max_disc,"rows":rows,
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--control",type=int,required=True)
    ap.add_argument("--receiver",type=int,required=True); ap.add_argument("--output",required=True)
    args=ap.parse_args()
    try:
        result=run_shard(args.control,args.receiver); exit_code=0
    except Blocked as e:
        result={"status":"BLOCKED_G9_RAY_CENTRIC_DUAL_DISK_CONVOLUTION","reason":str(e),
                "control_index":args.control,"receiver_index":args.receiver,"contract":CONTRACT,"amendment":AMENDMENT,"head_sha":os.getenv("GITHUB_SHA")}; exit_code=0
    except ScientificFail as e:
        result={"status":"SCIENTIFIC_FAIL_G9_DUAL_DISK_INVARIANT","reason":str(e),
                "control_index":args.control,"receiver_index":args.receiver,"contract":CONTRACT,"amendment":AMENDMENT,"head_sha":os.getenv("GITHUB_SHA")}; exit_code=1
    except Exception as e:
        result={"status":"INFRASTRUCTURE_FAIL_G9_0090E","reason":repr(e),
                "control_index":args.control,"receiver_index":args.receiver,"contract":CONTRACT,"amendment":AMENDMENT,"head_sha":os.getenv("GITHUB_SHA")}; exit_code=1
    Path(args.output).write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k!="rows"},indent=2,sort_keys=True))
    raise SystemExit(exit_code)


if __name__=="__main__":
    main()
