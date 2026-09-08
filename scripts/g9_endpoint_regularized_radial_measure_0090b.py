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

CONTRACT = "c46110eecf6fae9719d37f8f3a378206c2706324"
ORDERS = (32, 64)
THETA_INDICES = (0, 6, 12, 18, 24)
NORM_TOL = 2e-10
CENTER_TOL = 2e-14
SCALE_TOL = 2e-12
FOCAL_TOL = 2e-11
DIAG_N = 257


class Blocked(RuntimeError):
    pass


class ScientificFail(RuntimeError):
    pass


class InfrastructureFail(RuntimeError):
    pass


def rel(a: float, b: float) -> float:
    return abs(a-b)/max(abs(a), abs(b), 1e-300)


def omega_partial(u: np.ndarray, s: float, d: float) -> np.ndarray:
    """Partial-overlap angular measure; caller supplies d>0 and interior u."""
    uu = np.asarray(u, dtype=np.float64)
    if not (s > 0.0 and d > 0.0):
        raise ValueError("omega_partial requires s>0,d>0")
    den = 2.0*uu*d
    c = (uu*uu + d*d - s*s)/den
    return 2.0*np.arccos(np.clip(c, -1.0, 1.0))


def transformed_u(t: np.ndarray, s: float, d: float) -> np.ndarray:
    tt = np.asarray(t, dtype=np.float64)
    rad = d*d + s*s - 2.0*d*s*np.cos(tt)
    return np.sqrt(np.maximum(rad, 0.0))


def transformed_normalization(s: float, d: float, order: int) -> float:
    """0090b authority formula: no direct GL integration in source radius u."""
    s = float(s); d = float(d)
    if not (math.isfinite(s) and math.isfinite(d) and s > 0.0 and d >= 0.0):
        raise ScientificFail("invalid source geometry")
    if d == 0.0:
        return 1.0

    full = ((s-d)/s)**2 if d < s else 0.0
    q, w = leggauss(order)
    t = 0.5*math.pi*(q + 1.0)
    u = transformed_u(t, s, d)
    om = omega_partial(u, s, d)
    integrand = om*np.sin(t)
    partial = d/(math.pi*s) * 0.5*math.pi*float(np.dot(w, integrand))
    return full + partial


def geometry_diagnostics(s: float, d: float) -> dict:
    if d == 0.0:
        return {"monotone": True, "omega_min": 2.0*math.pi, "omega_max": 2.0*math.pi}
    # Fixed diagnostic grid includes endpoints for monotonicity of u, but omega is
    # evaluated only at interior nodes to avoid the removable d=s,u=0 endpoint.
    t = np.linspace(0.0, math.pi, DIAG_N)
    u = transformed_u(t, s, d)
    monotone = bool(np.all(np.diff(u) >= -1e-14*max(s,d,1.0)))
    ti = t[1:-1]
    ui = transformed_u(ti, s, d)
    om = omega_partial(ui, s, d)
    finite = bool(np.all(np.isfinite(u)) and np.all(np.isfinite(om)))
    omin = float(np.min(om)); omax = float(np.max(om))
    if not finite or not monotone or omin < -1e-13 or omax > 2.0*math.pi + 1e-13:
        raise ScientificFail("endpoint-regularized geometry invariant")
    return {"monotone": monotone, "omega_min": omin, "omega_max": omax}


def evaluate_pair(s: float, d: float, label: str) -> dict:
    diag = geometry_diagnostics(s,d)
    nl = transformed_normalization(s,d,ORDERS[0])
    nh = transformed_normalization(s,d,ORDERS[1])
    if not (math.isfinite(nl) and math.isfinite(nh)):
        raise ScientificFail("non-finite transformed normalization")
    el = abs(nl-1.0); eh = abs(nh-1.0); lh = abs(nl-nh)
    tol = CENTER_TOL if d == 0.0 else NORM_TOL
    if el > tol or eh > tol:
        raise Blocked(f"endpoint-regularized normalization exceeds frozen threshold: {label}")
    if d != 0.0 and lh > NORM_TOL:
        raise Blocked(f"endpoint-regularized L/H agreement exceeds frozen threshold: {label}")
    return {
        "label": label, "s_cm": s, "d_cm": d,
        "n_l": nl, "n_h": nh,
        "abs_error_l": el, "abs_error_h": eh,
        "lh_abs": lh, "geometry": diag,
    }


def analytic_controls() -> list[tuple[float,float,str]]:
    out=[]
    for s in (1e-6,1.0,1e6): out.append((s,0.0,f"center_s={s:g}"))
    for r in (0.1,0.5,0.9): out.append((1.0,r,f"internal_d_over_s={r:g}"))
    out.append((1.0,1.0,"tangent_d_over_s=1"))
    for r in (1.1,2.0,10.0): out.append((1.0,r,f"external_d_over_s={r:g}"))
    for s in (1e-6,1.0,1e6): out.append((s,2.0*s,f"scale_d_over_s=2_s={s:g}"))
    return out


def run() -> dict:
    try:
        payload = urllib.request.urlopen(MODEL_S_URL, timeout=30).read()
    except Exception as e:
        raise InfrastructureFail(f"Model-S source fetch failed: {e!r}") from e
    if git_blob_sha1(payload) != MODEL_S_BLOB:
        raise InfrastructureFail("Model-S blob mismatch")
    profile = parse_model_s_text(payload.decode())

    focal_rows=[]
    for ci,(x0,z_frozen,_turn) in enumerate(CONTROLS):
        z = continuous_focal_distance_au(profile,x0,R)
        drift = rel(z,z_frozen)
        if drift > FOCAL_TOL:
            raise ScientificFail("observer focal drift")
        focal_rows.append({"control_index":ci,"x0":x0,"z_au":z,"z_frozen_au":z_frozen,"relative_drift":drift})

    controls=[]
    for s,d,label in analytic_controls():
        controls.append(evaluate_pair(s,d,label))

    # H3 fixed dimensionless scale-invariance replicas.
    scale=[r for r in controls if r["label"].startswith("scale_d_over_s=2")]
    for key in ("n_l","n_h"):
        vals=[r[key] for r in scale]
        if max(vals)-min(vals) > SCALE_TOL:
            raise Blocked("dimensionless scale invariance exceeds frozen threshold")

    physical=[]
    for ci,fr in enumerate(focal_rows):
        z=fr["z_au"]
        for ti in THETA_INDICES:
            theta=float(THETAS[ti])
            s=z*AU_CM*theta
            for dm in DELTAS_M:
                d=float(dm)*100.0
                row=evaluate_pair(s,d,f"control={ci},theta_index={ti},delta_m={dm:g}")
                row.update({"control_index":ci,"theta_index":ti,"theta_rad":theta,"delta_m":float(dm)})
                physical.append(row)

    all_rows=controls+physical
    return {
        "status":"PASS_G9_ENDPOINT_REGULARIZED_RADIAL_MEASURE_AUTHORITY",
        "contract":CONTRACT,
        "head_sha":os.getenv("GITHUB_SHA"),
        "model_s_blob":MODEL_S_BLOB,
        "orders":list(ORDERS),
        "focal_rows":focal_rows,
        "analytic_control_count":len(controls),
        "physical_geometry_count":len(physical),
        "max_abs_error_l":max(r["abs_error_l"] for r in all_rows),
        "max_abs_error_h":max(r["abs_error_h"] for r in all_rows),
        "max_lh_abs":max(r["lh_abs"] for r in all_rows),
        "controls":controls,
        "physical":physical,
    }


def main() -> None:
    ap=argparse.ArgumentParser(); ap.add_argument("--output",required=True); args=ap.parse_args()
    try:
        result=run()
        exit_code=0
    except Blocked as e:
        result={"status":"BLOCKED_G9_ENDPOINT_REGULARIZED_RADIAL_MEASURE","reason":str(e),"contract":CONTRACT,"head_sha":os.getenv("GITHUB_SHA")}
        exit_code=0
    except ScientificFail as e:
        result={"status":"SCIENTIFIC_FAIL_G9_RADIAL_MEASURE_GEOMETRY","reason":str(e),"contract":CONTRACT,"head_sha":os.getenv("GITHUB_SHA")}
        exit_code=1
    except Exception as e:
        result={"status":"INFRASTRUCTURE_FAIL_G9_0090B","reason":repr(e),"contract":CONTRACT,"head_sha":os.getenv("GITHUB_SHA")}
        exit_code=1
    Path(args.output).write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k not in ("controls","physical")},indent=2,sort_keys=True))
    raise SystemExit(exit_code)


if __name__ == "__main__":
    main()
