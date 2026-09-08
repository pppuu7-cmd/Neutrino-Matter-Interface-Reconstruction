#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import urllib.request

import g9_ray_centric_dual_disk_0090e as dual
import g9_radial_source_measure_0090a as radial
from g9_persistent_global_0090 import (
    MODEL_S_BLOB, MODEL_S_URL, R, CONTROLS, RECEIVERS_M, DELTAS_M, THETAS,
    git_blob_sha1, bulk_focal_factory, conformance,
)
from nmir.g9_continuous_projection import continuous_focal_distance_au
from nmir.g9_persistent_lens import large_source_ring_excess_upper, perfect_whole_sun_mu_upper
from nmir.gravity_extended import AU_CM, parse_model_s_text

CONTRACT = "fc277e3695ebeb2628d133b9385e7d7d2e12a5d5"
PARENT_CONTRACT = "c9d9e46860ef55bec2a5aaaafdac19f6e9de551b"
PARENT_AMENDMENT = "c95fd80e7b2a54d04f83103e7678acbe8c51f6c6"
PARENT_EVALUATOR_BLOB = "4bedc9431b428292f1b09613f603bea82597f9b5"
ANGULAR_ORDER = 32
RADIAL_ORDER = 64
MAP_TOL = 2e-11
POINT_TOL = 0.005


class ScientificFail(RuntimeError):
    pass


class InfrastructureFail(RuntimeError):
    pass


def rel(a: float, b: float) -> float:
    return abs(a-b)/max(abs(a),abs(b),1e-300)


def blob_sha1_bytes(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode()+data).hexdigest()


def parent_evaluator_blob() -> str:
    p=Path(dual.__file__)
    if p.suffix==".pyc":
        p=p.with_suffix(".py")
    return blob_sha1_bytes(p.read_bytes())


def run_shard(ci: int, ri: int) -> dict:
    if ci not in (0,1,2) or ri not in (0,1,2):
        raise InfrastructureFail("invalid shard index")
    if dual.CONTRACT != PARENT_CONTRACT or dual.AMENDMENT != PARENT_AMENDMENT:
        raise InfrastructureFail("0090e parent contract/amendment mismatch")
    pblob=parent_evaluator_blob()
    if pblob != PARENT_EVALUATOR_BLOB:
        raise InfrastructureFail(f"0090e evaluator blob mismatch: {pblob}")

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
    if point_rel>POINT_TOL:
        raise ScientificFail(f"0089e point-control mismatch rel={point_rel:.17g}")

    ceiling=perfect_whole_sun_mu_upper(a,R)
    rows=[]
    survivor_count=0
    ge2_count=0; ge10_count=0; ge1e3_count=0
    nonzero_ge2=0; nonzero_ge10=0; nonzero_ge1e3=0
    mu_min=math.inf; mu_max=-math.inf

    for ti,theta in enumerate(THETAS):
        theta=float(theta)
        s=z*AU_CM*theta
        if not (math.isfinite(s) and s>0.0):
            raise ScientificFail("invalid source radius")
        lsb=large_source_ring_excess_upper(s,R)
        for dm in DELTAS_M:
            dm=float(dm); d=dm*100.0
            try:
                area=dual.ray_averaged_area(focal,z,turn,x0,a,s,d,ANGULAR_ORDER,RADIAL_ORDER)
            except dual.ScientificFail as e:
                raise ScientificFail(str(e)) from e
            except Exception as e:
                raise InfrastructureFail(f"full-grid evaluation failed ti={ti},delta={dm}: {e!r}") from e
            mu=1.0+area/(math.pi*a*a)
            if not math.isfinite(mu) or mu<1.0:
                raise ScientificFail("magnification invariant")
            if mu>ceiling*(1.0+1e-12):
                raise ScientificFail(f"whole-aperture ceiling ti={ti},delta={dm}")
            if (mu-1.0)>lsb*(1.0+1e-9):
                raise ScientificFail(f"large-source aperture bound ti={ti},delta={dm}")
            ge2=mu>=2.0; ge10=mu>=10.0; ge1e3=mu>=1e3
            finite=(theta>0.0 and dm>0.0 and ge2)
            ge2_count += int(ge2); ge10_count += int(ge10); ge1e3_count += int(ge1e3)
            if dm>0.0:
                nonzero_ge2 += int(ge2); nonzero_ge10 += int(ge10); nonzero_ge1e3 += int(ge1e3)
            survivor_count += int(finite)
            mu_min=min(mu_min,mu); mu_max=max(mu_max,mu)
            rows.append({
                "control_index":ci,"observer_x0":x0,"z_au":z,
                "receiver_index":ri,"receiver_m":float(RECEIVERS_M[ri]),
                "theta_index":ti,"theta_rad":theta,"source_radius_cm":s,
                "delta_m":dm,"area_h_cm2":area,"mu":mu,
                "ge2":ge2,"ge10":ge10,"ge1e3":ge1e3,
                "finite_nonzero_survivor":finite,
            })

    if len(rows)!=150:
        raise InfrastructureFail(f"shard row cardinality mismatch {len(rows)}")
    return {
        "status":"SHARD_PASS_G9_FULL_RAY_CENTRIC_SCAN",
        "contract":CONTRACT,"head_sha":os.getenv("GITHUB_SHA"),
        "parent_contract":PARENT_CONTRACT,"parent_amendment":PARENT_AMENDMENT,
        "parent_evaluator_blob":pblob,"model_s_blob":MODEL_S_BLOB,
        "control_index":ci,"receiver_index":ri,"x0":x0,"z_au":z,"turn_x":turn,
        "receiver_m":float(RECEIVERS_M[ri]),"focal_drift":focal_drift,
        "batch_scalar_max_rel":map_conf,
        "point_control":{"area_cm2":point_area,"reference_area_cm2":ref_area,"relative_error":point_rel},
        "whole_aperture_ceiling":ceiling,
        "row_count":len(rows),"finite_nonzero_survivor_count":survivor_count,
        "ge2_count":ge2_count,"ge10_count":ge10_count,"ge1e3_count":ge1e3_count,
        "nonzero_offset_ge2_count":nonzero_ge2,"nonzero_offset_ge10_count":nonzero_ge10,
        "nonzero_offset_ge1e3_count":nonzero_ge1e3,
        "mu_min":mu_min,"mu_max":mu_max,"rows":rows,
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--control",type=int,required=True)
    ap.add_argument("--receiver",type=int,required=True); ap.add_argument("--output",required=True)
    args=ap.parse_args()
    try:
        result=run_shard(args.control,args.receiver); code=0
    except ScientificFail as e:
        result={"status":"SCIENTIFIC_FAIL_G9_FULL_RAY_CENTRIC_INVARIANT","reason":str(e),
                "control_index":args.control,"receiver_index":args.receiver,"contract":CONTRACT,"head_sha":os.getenv("GITHUB_SHA")}; code=1
    except Exception as e:
        result={"status":"INFRASTRUCTURE_FAIL_G9_0090F","reason":repr(e),
                "control_index":args.control,"receiver_index":args.receiver,"contract":CONTRACT,"head_sha":os.getenv("GITHUB_SHA")}; code=1
    Path(args.output).write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k!="rows"},indent=2,sort_keys=True))
    raise SystemExit(code)

if __name__=="__main__":
    main()
