#!/usr/bin/env python3
from __future__ import annotations

import argparse
import functools
import json
import math
import os
from pathlib import Path
import urllib.request

import numpy as np
from numpy.polynomial.legendre import leggauss as numpy_leggauss

import g9_radial_source_measure_0090a as radial
from g9_persistent_global_0090 import (
    MODEL_S_BLOB, MODEL_S_URL, R, CONTROLS, RECEIVERS_M, THETAS,
    git_blob_sha1, bulk_focal_factory, conformance,
)
from nmir.g9_continuous_projection import continuous_focal_distance_au
from nmir.gravity_extended import AU_CM, parse_model_s_text

CONTRACT = "44a9f2d9a28d7169da6166eef0634df91121434a"
THETA_INDICES = (0, 12, 24)
DELTA_M = (0.0, 0.1, 100.0)
SOURCE_REPLICAS = {"L": (8, 16, 32), "H": (16, 32, 64)}
REL_TOL = 0.005
ABS_SMALL_TOL = 1e-10
MAP_TOL = 2e-11


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

# Pure runtime optimization only: inherited 0090a gauss_integral receives the
# same numpy nodes/weights, but avoids recomputing them for every root-split interval.
radial.leggauss = cached_leggauss


def source_nodes(s: float, d: float, nq: int, nphi: int) -> tuple[np.ndarray,np.ndarray]:
    q0,w0=cached_leggauss(nq)
    q=0.5*(q0+1.0); wq=0.5*w0
    phi=2.0*math.pi*(np.arange(nphi,dtype=np.float64)+0.5)/nphi
    qq,pp=np.meshgrid(q,phi,indexing="ij")
    ww=np.broadcast_to(wq[:,None]/nphi,qq.shape)
    r=s*np.sqrt(qq)
    u=np.hypot(d+r*np.cos(pp),r*np.sin(pp))
    if not np.all(np.isfinite(u)) or np.any(u<0.0):
        raise ScientificFail("source-coordinate offset invariant")
    return u.ravel(),ww.ravel()


def source_averaged_area(focal,z,turn,x0,a: float,s: float,d: float,nq: int,nphi: int,b_order: int) -> float:
    us,w=source_nodes(s,d,nq,nphi)
    # Reuse only bit-identical u values; no rounding/merging of distinct nodes.
    vals={}
    areas=np.empty_like(us)
    for i,u0 in enumerate(us):
        key=float(u0)
        area=vals.get(key)
        if area is None:
            area=radial.area_at_u(focal,z,turn,x0,key,a,b_order)
            vals[key]=area
        areas[i]=area
    total=float(np.dot(w,areas))
    cap=math.pi*R*R*(1.0+1e-9)
    if not math.isfinite(total) or total<0.0 or total>cap:
        raise ScientificFail("source-averaged accepted-area invariant")
    return total


def conv_metric(mu_l: float,mu_h: float) -> tuple[float,float]:
    el,eh=mu_l-1.0,mu_h-1.0
    if max(abs(el),abs(eh))>=ABS_SMALL_TOL:
        return abs(el-eh)/max(abs(el),abs(eh),1e-300),REL_TOL
    return abs(mu_l-mu_h),ABS_SMALL_TOL


def run_shard(ci: int,ri: int) -> dict:
    if ci not in (0,1,2) or ri not in (0,1,2):
        raise InfrastructureFail("invalid shard index")
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
                area_l=source_averaged_area(focal,z,turn,x0,a,s,d,*SOURCE_REPLICAS["L"])
                area_h=source_averaged_area(focal,z,turn,x0,a,s,d,*SOURCE_REPLICAS["H"])
            except (Blocked,ScientificFail,InfrastructureFail):
                raise
            except Exception as e:
                raise InfrastructureFail(f"finite-source evaluation failed at ti={ti},delta={dm}: {e!r}") from e
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
                raise Blocked(f"source-centric L/H convergence miss ti={ti},delta_m={dm:g},metric={disc:.17g},limit={limit:.17g}")

    if len(rows)!=9:
        raise InfrastructureFail(f"shard row cardinality mismatch {len(rows)}")
    return {
        "status":"SHARD_PASS_G9_SOURCE_CENTRIC_FINITE_SOURCE",
        "contract":CONTRACT,"head_sha":os.getenv("GITHUB_SHA"),"model_s_blob":MODEL_S_BLOB,
        "control_index":ci,"receiver_index":ri,"x0":x0,"z_au":z,"turn_x":turn,
        "receiver_m":float(RECEIVERS_M[ri]),"focal_drift":focal_drift,"batch_scalar_max_rel":map_conf,
        "point_control":{"area_cm2":point_area,"reference_area_cm2":ref_area,"relative_error":point_rel,
                         "smallest_source_relative_error":point_limit_rel},
        "source_replicas":SOURCE_REPLICAS,"max_lh_discrepancy":max_disc,"rows":rows,
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--control",type=int,required=True)
    ap.add_argument("--receiver",type=int,required=True); ap.add_argument("--output",required=True)
    args=ap.parse_args()
    try:
        result=run_shard(args.control,args.receiver); exit_code=0
    except Blocked as e:
        result={"status":"BLOCKED_G9_SOURCE_CENTRIC_FINITE_SOURCE_CONVOLUTION","reason":str(e),
                "control_index":args.control,"receiver_index":args.receiver,"contract":CONTRACT,"head_sha":os.getenv("GITHUB_SHA")}; exit_code=0
    except ScientificFail as e:
        result={"status":"SCIENTIFIC_FAIL_G9_SOURCE_CENTRIC_FINITE_SOURCE_INVARIANT","reason":str(e),
                "control_index":args.control,"receiver_index":args.receiver,"contract":CONTRACT,"head_sha":os.getenv("GITHUB_SHA")}; exit_code=1
    except Exception as e:
        result={"status":"INFRASTRUCTURE_FAIL_G9_0090D","reason":repr(e),
                "control_index":args.control,"receiver_index":args.receiver,"contract":CONTRACT,"head_sha":os.getenv("GITHUB_SHA")}; exit_code=1
    Path(args.output).write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k!="rows"},indent=2,sort_keys=True))
    raise SystemExit(exit_code)


if __name__=="__main__":
    main()
