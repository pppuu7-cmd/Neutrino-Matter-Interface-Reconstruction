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
    CONTROLS,
    DELTAS_M,
    THETAS,
    git_blob_sha1,
)
from nmir.g9_continuous_projection import continuous_focal_distance_au
from nmir.gravity_extended import AU_CM, parse_model_s_text

CONTRACT = "19245cf8a119e010ef161ebaeb4113a74d083158"
THETA_INDICES = (0, 6, 12, 18, 24)
REPLICAS = {"L": (16, 32), "H": (32, 64)}
ID_TOL = 2e-14
GEOM_RESID_TOL = 5e-15
FOCAL_TOL = 2e-11
EPS = np.finfo(float).eps
D_CONTROLS = (0.0, 0.1, 0.5, 0.9, 1.0, 1.1, 2.0, 10.0, 1e6)


class Blocked(RuntimeError):
    pass


class ScientificFail(RuntimeError):
    pass


class InfrastructureFail(RuntimeError):
    pass


def rel(a: float, b: float) -> float:
    return abs(a-b)/max(abs(a), abs(b), 1e-300)


def product_nodes(nq: int, nphi: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    q0, w0 = leggauss(nq)
    q = 0.5*(q0+1.0)
    wq = 0.5*w0
    phi = 2.0*math.pi*(np.arange(nphi, dtype=np.float64)+0.5)/nphi
    qq, pp = np.meshgrid(q, phi, indexing="ij")
    ww = np.broadcast_to(wq[:, None]/nphi, qq.shape).copy()
    return qq.ravel(), pp.ravel(), ww.ravel()


def evaluate_replica(s: float, d: float, nq: int, nphi: int) -> dict:
    if not (math.isfinite(s) and s > 0.0 and math.isfinite(d) and d >= 0.0):
        raise ScientificFail("invalid source geometry")
    q, phi, w = product_nodes(nq, nphi)
    sq = np.sqrt(q)
    r = s*sq
    c = np.cos(phi); sn = np.sin(phi)
    xi = sq*c
    eta = sq*sn
    x = d + r*c
    y = r*sn
    u = np.hypot(x, y)

    if not (np.all(np.isfinite(r)) and np.all(np.isfinite(x)) and np.all(np.isfinite(y)) and np.all(np.isfinite(u))):
        raise ScientificFail("non-finite source-coordinate geometry")
    if np.any(r < 0.0) or np.any(r > s*(1.0+2e-14)):
        raise ScientificFail("source-radius support invariant")

    t = 64.0*EPS*max(d, s, 1.0)
    lower = np.maximum(0.0, d-r)-t
    upper = d+r+t
    if np.any(u < lower) or np.any(u > upper):
        raise ScientificFail("triangle-support invariant")

    rhs = x*x+y*y
    lhs = u*u
    resid = np.abs(lhs-rhs)/np.maximum.reduce([lhs, rhs, np.ones_like(lhs)])
    max_resid = float(np.max(resid))
    if max_resid > GEOM_RESID_TOL:
        raise ScientificFail("hypot/cartesian residual invariant")

    def mean(v: np.ndarray) -> float:
        return float(np.dot(w, np.asarray(v, dtype=np.float64)))

    moments = {
        "norm": float(np.sum(w, dtype=np.float64)),
        "xi": mean(xi),
        "eta": mean(eta),
        "xi2": mean(xi*xi),
        "eta2": mean(eta*eta),
        "xieta": mean(xi*eta),
        "rho2": mean(xi*xi+eta*eta),
    }
    errors = {
        "norm": abs(moments["norm"]-1.0),
        "xi": abs(moments["xi"]),
        "eta": abs(moments["eta"]),
        "xi2": abs(moments["xi2"]-0.25),
        "eta2": abs(moments["eta2"]-0.25),
        "xieta": abs(moments["xieta"]),
        "rho2": abs(moments["rho2"]-0.5),
    }
    if max(errors.values()) > ID_TOL:
        raise Blocked("source-centric exact-measure identity exceeds frozen threshold")

    return {
        "nq": nq,
        "nphi": nphi,
        "moments": moments,
        "errors": errors,
        "max_geometry_residual": max_resid,
        "u_min_cm": float(np.min(u)),
        "u_max_cm": float(np.max(u)),
    }


def evaluate_geometry(s: float, d: float, label: str) -> dict:
    reps = {name: evaluate_replica(s, d, *orders) for name, orders in REPLICAS.items()}
    keys = ("norm", "xi", "eta", "xi2", "eta2", "xieta", "rho2")
    agreement = {k: abs(reps["L"]["moments"][k]-reps["H"]["moments"][k]) for k in keys}
    if max(agreement.values()) > ID_TOL:
        raise Blocked("source-centric L/H moment agreement exceeds frozen threshold")
    return {
        "label": label,
        "s_cm": float(s),
        "d_cm": float(d),
        "d_over_s": float(d/s),
        "replicas": reps,
        "lh_agreement": agreement,
    }


def run() -> dict:
    try:
        payload = urllib.request.urlopen(MODEL_S_URL, timeout=30).read()
    except Exception as e:
        raise InfrastructureFail(f"Model-S source fetch failed: {e!r}") from e
    if git_blob_sha1(payload) != MODEL_S_BLOB:
        raise InfrastructureFail("Model-S blob mismatch")
    profile = parse_model_s_text(payload.decode())

    focal_rows=[]
    z_values=[]
    for ci,(x0,z_frozen,_turn) in enumerate(CONTROLS):
        z=continuous_focal_distance_au(profile,x0,R)
        drift=rel(z,z_frozen)
        if drift > FOCAL_TOL:
            raise ScientificFail("observer focal-distance drift")
        focal_rows.append({"control_index":ci,"x0":x0,"z_au":z,"z_frozen_au":z_frozen,"relative_drift":drift})
        z_values.append(z)

    controls=[evaluate_geometry(1.0, D, f"D={D:g}") for D in D_CONTROLS]
    physical=[]
    for ci,z in enumerate(z_values):
        for ti in THETA_INDICES:
            theta=float(THETAS[ti])
            s=z*AU_CM*theta
            if not (math.isfinite(s) and s > 0.0):
                raise ScientificFail("non-positive physical source radius")
            for dm in DELTAS_M:
                row=evaluate_geometry(s, float(dm)*100.0, f"control={ci},theta_index={ti},delta_m={dm:g}")
                row.update({"control_index":ci,"theta_index":ti,"theta_rad":theta,"delta_m":float(dm)})
                physical.append(row)
    if len(physical) != 90 or len(controls) != 9:
        raise InfrastructureFail(f"fixed-set cardinality mismatch controls={len(controls)} physical={len(physical)}")

    all_rows=controls+physical
    max_identity=0.0
    max_lh=0.0
    max_geom=0.0
    for row in all_rows:
        for rep in row["replicas"].values():
            max_identity=max(max_identity,max(rep["errors"].values()))
            max_geom=max(max_geom,rep["max_geometry_residual"])
        max_lh=max(max_lh,max(row["lh_agreement"].values()))

    return {
        "status":"PASS_G9_SOURCE_CENTRIC_EXACT_MEASURE_AUTHORITY",
        "contract":CONTRACT,
        "head_sha":os.getenv("GITHUB_SHA"),
        "model_s_blob":MODEL_S_BLOB,
        "replicas":REPLICAS,
        "thresholds":{"identity":ID_TOL,"geometry_residual":GEOM_RESID_TOL,"focal_drift":FOCAL_TOL},
        "focal_rows":focal_rows,
        "control_count":len(controls),
        "physical_count":len(physical),
        "max_identity_abs_error":max_identity,
        "max_lh_abs":max_lh,
        "max_geometry_residual":max_geom,
        "controls":controls,
        "physical":physical,
    }


def main() -> None:
    ap=argparse.ArgumentParser(); ap.add_argument("--output",required=True); args=ap.parse_args()
    try:
        result=run(); exit_code=0
    except Blocked as e:
        result={"status":"BLOCKED_G9_SOURCE_CENTRIC_EXACT_MEASURE","reason":str(e),"contract":CONTRACT,"head_sha":os.getenv("GITHUB_SHA")}; exit_code=0
    except ScientificFail as e:
        result={"status":"SCIENTIFIC_FAIL_G9_SOURCE_CENTRIC_GEOMETRY","reason":str(e),"contract":CONTRACT,"head_sha":os.getenv("GITHUB_SHA")}; exit_code=1
    except Exception as e:
        result={"status":"INFRASTRUCTURE_FAIL_G9_0090C","reason":repr(e),"contract":CONTRACT,"head_sha":os.getenv("GITHUB_SHA")}; exit_code=1
    Path(args.output).write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k not in ("controls","physical")},indent=2,sort_keys=True))
    raise SystemExit(exit_code)


if __name__ == "__main__":
    main()
