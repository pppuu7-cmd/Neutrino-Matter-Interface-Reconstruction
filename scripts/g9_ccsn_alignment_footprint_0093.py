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
    MODEL_S_BLOB, MODEL_S_URL, R, CONTROLS, RECEIVERS_M,
    git_blob_sha1, bulk_focal_factory, conformance,
)
from nmir.g9_continuous_projection import continuous_focal_distance_au
from nmir.g9_persistent_lens import large_source_ring_excess_upper, perfect_whole_sun_mu_upper
from nmir.gravity_extended import AU_CM, parse_model_s_text

CONTRACT = "ffaa7706bf335b301833fe49754297b804cf713a"
PARENT_0090F_CONTRACT = "fc277e3695ebeb2628d133b9385e7d7d2e12a5d5"
PARENT_EVALUATOR_BLOB = "4bedc9431b428292f1b09613f603bea82597f9b5"
SOURCE_AUTHORITY_PATH = Path("data/g9_ccsn_source_authority_0061.json")
SOURCE_AUTHORITY_BLOB = "ed2e5ab50375abb1049b86348a2e570b5e7b99f5"
SOURCE_RADII_KM = (21.0, 100.0)
DISTANCE_KPC = 10.0
ANGULAR_ORDER = 32
RADIAL_ORDER = 64
MAP_TOL = 2e-11
POINT_TOL = 0.005
ZERO_MU_ABS_TOL = 1e-12
N_LOG = 257
N_REFINE = 32
D_START_M = 100.0


class ScientificFail(RuntimeError):
    pass


class InfrastructureFail(RuntimeError):
    pass


def rel(a: float, b: float) -> float:
    return abs(a-b) / max(abs(a), abs(b), 1e-300)


def blob_sha1_bytes(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def parent_evaluator_blob() -> str:
    p = Path(dual.__file__)
    if p.suffix == ".pyc":
        p = p.with_suffix(".py")
    return blob_sha1_bytes(p.read_bytes())


def load_source_authority() -> dict:
    raw = SOURCE_AUTHORITY_PATH.read_bytes()
    blob = blob_sha1_bytes(raw)
    if blob != SOURCE_AUTHORITY_BLOB:
        raise ScientificFail(f"0061 source-authority blob mismatch: {blob}")
    obj = json.loads(raw)
    if float(obj["benchmark_distance_kpc"]) != DISTANCE_KPC:
        raise ScientificFail("0061 distance authority mismatch")
    ss = obj["source_size"]
    if float(ss["fiducial_radius_km"]) != SOURCE_RADII_KM[0]:
        raise ScientificFail("0061 fiducial radius mismatch")
    if float(ss["sensitivity_radius_km"]) != SOURCE_RADII_KM[1]:
        raise ScientificFail("0061 sensitivity radius mismatch")
    return obj


def source_theta(radius_km: float) -> float:
    # IAU exact AU is inherited through AU_CM.  1 pc = 648000/pi AU.
    pc_cm = (648000.0 / math.pi) * AU_CM
    distance_cm = DISTANCE_KPC * 1000.0 * pc_cm
    return radius_km * 1.0e5 / distance_cm


def map_ymax(focal, z: float, turn: float, x0: float) -> tuple[float, list[dict]]:
    endpoints = sorted({
        float(v)
        for seg in radial.monotone_abs_segments(turn, x0)
        for v in seg
    })
    vals = [float(radial.abs_y(focal, z, [x])[0]) for x in endpoints]
    if not vals or not all(math.isfinite(v) and v >= 0.0 for v in vals):
        raise ScientificFail("invalid map endpoint values")
    rows = [{"x": x, "abs_y_cm": y} for x, y in zip(endpoints, vals)]
    return max(vals), rows


def evaluate_mu(focal, z: float, turn: float, x0: float, a: float,
                s: float, d_cm: float, ceiling: float, lsb: float) -> tuple[float, float]:
    try:
        area = dual.ray_averaged_area(
            focal, z, turn, x0, a, s, d_cm, ANGULAR_ORDER, RADIAL_ORDER
        )
    except dual.ScientificFail as exc:
        raise ScientificFail(str(exc)) from exc
    except Exception as exc:
        raise InfrastructureFail(f"ray evaluation failed at d={d_cm}: {exc!r}") from exc
    mu = 1.0 + area / (math.pi * a * a)
    if not math.isfinite(mu) or mu < 1.0:
        raise ScientificFail("magnification invariant")
    if mu > ceiling * (1.0 + 1e-12):
        raise ScientificFail("whole-aperture ceiling")
    if (mu - 1.0) > lsb * (1.0 + 1e-9):
        raise ScientificFail("large-source aperture bound")
    return mu, area


def log_nodes(start_cm: float, stop_cm: float) -> list[float]:
    if not (stop_cm > start_cm > 0.0):
        raise ScientificFail("invalid offset interval")
    ls, le = math.log(start_cm), math.log(stop_cm)
    vals = [math.exp(ls + j / (N_LOG - 1) * (le - ls)) for j in range(N_LOG)]
    vals[0] = start_cm
    vals[-1] = stop_cm
    return vals


def refine_straddle(focal, z, turn, x0, a, s, ceiling, lsb,
                    d0: float, mu0: float, d1: float, mu1: float) -> dict:
    f0, f1 = mu0 - 2.0, mu1 - 2.0
    if f0 == 0.0:
        return {"lo_cm": d0, "hi_cm": d0, "mu_lo": mu0, "mu_hi": mu0,
                "lo_state": True, "hi_state": True, "iterations": 0}
    if f1 == 0.0:
        return {"lo_cm": d1, "hi_cm": d1, "mu_lo": mu1, "mu_hi": mu1,
                "lo_state": True, "hi_state": True, "iterations": 0}
    if f0 * f1 > 0.0:
        raise ScientificFail("refinement called without threshold straddle")

    lo, hi, mlo, mhi = d0, d1, mu0, mu1
    sign_lo = f0 > 0.0
    for _ in range(N_REFINE):
        mid = math.sqrt(lo * hi)
        mmid, _ = evaluate_mu(focal, z, turn, x0, a, s, mid, ceiling, lsb)
        sign_mid = (mmid - 2.0) >= 0.0
        if sign_mid == sign_lo:
            lo, mlo = mid, mmid
        else:
            hi, mhi = mid, mmid
    return {
        "lo_cm": lo, "hi_cm": hi, "mu_lo": mlo, "mu_hi": mhi,
        "lo_state": mlo >= 2.0, "hi_state": mhi >= 2.0,
        "iterations": N_REFINE,
        "relative_width": (hi - lo) / max(lo, hi, 1e-300),
    }


def run_shard(ci: int, ri: int) -> dict:
    if ci not in (0, 1, 2) or ri not in (0, 1, 2):
        raise InfrastructureFail("invalid shard index")
    if dual.CONTRACT != "c9d9e46860ef55bec2a5aaaafdac19f6e9de551b":
        raise InfrastructureFail("0090e parent contract mismatch")
    if dual.AMENDMENT != "c95fd80e7b2a54d04f83103e7678acbe8c51f6c6":
        raise InfrastructureFail("0090e parent amendment mismatch")
    pblob = parent_evaluator_blob()
    if pblob != PARENT_EVALUATOR_BLOB:
        raise InfrastructureFail(f"0090e evaluator blob mismatch: {pblob}")
    load_source_authority()

    try:
        payload = urllib.request.urlopen(MODEL_S_URL, timeout=30).read()
    except Exception as exc:
        raise InfrastructureFail(f"Model-S fetch failed: {exc!r}") from exc
    if git_blob_sha1(payload) != MODEL_S_BLOB:
        raise InfrastructureFail("Model-S blob mismatch")
    profile = parse_model_s_text(payload.decode())
    focal = bulk_focal_factory(profile)
    x0, z_frozen, turn = CONTROLS[ci]
    z = continuous_focal_distance_au(profile, x0, R)
    focal_drift = rel(z, z_frozen)
    if focal_drift > MAP_TOL:
        raise ScientificFail("observer focal-distance drift")
    map_conf = conformance(profile, focal, z)
    if map_conf > MAP_TOL:
        raise ScientificFail("batch/scalar signed-map conformance")

    a = float(RECEIVERS_M[ri]) * 100.0
    point_area = radial.point_area_exact(focal, z, turn, x0, a)
    ref_area = radial.REFERENCE_AREAS_CM2[ci][a]
    point_rel = rel(point_area, ref_area)
    if point_rel > POINT_TOL:
        raise ScientificFail(f"0089e point-control mismatch rel={point_rel:.17g}")

    ymax, map_endpoints = map_ymax(focal, z, turn, x0)
    ceiling = perfect_whole_sun_mu_upper(a, R)
    families = []

    for radius_km in SOURCE_RADII_KM:
        theta = source_theta(radius_km)
        s = z * AU_CM * theta
        if not (math.isfinite(theta) and theta > 0.0 and math.isfinite(s) and s > 0.0):
            raise ScientificFail("invalid CCSN source size")
        lsb = large_source_ring_excess_upper(s, R)
        d_start_cm = D_START_M * 100.0
        d_zero_cm = math.nextafter(ymax + s + a, math.inf)
        nodes = log_nodes(d_start_cm, d_zero_cm)
        rows = []
        for j, d in enumerate(nodes):
            mu, area = evaluate_mu(focal, z, turn, x0, a, s, d, ceiling, lsb)
            rows.append({
                "index": j,
                "d_cm": d,
                "d_m": d / 100.0,
                "beta_rad": d / (z * AU_CM),
                "mu": mu,
                "area_h_cm2": area,
                "ge2": mu >= 2.0,
            })

        if rows[0]["mu"] < 2.0:
            raise ScientificFail("CCSN 100-m continuity sentinel no longer survives")
        if abs(rows[-1]["mu"] - 1.0) > ZERO_MU_ABS_TOL:
            raise ScientificFail(
                f"no-overlap ceiling check failed mu={rows[-1]['mu']:.17g}"
            )

        straddles = []
        reentries = 0
        for left, right in zip(rows[:-1], rows[1:]):
            if left["ge2"] != right["ge2"]:
                if (not left["ge2"]) and right["ge2"]:
                    reentries += 1
                rr = refine_straddle(
                    focal, z, turn, x0, a, s, ceiling, lsb,
                    left["d_cm"], left["mu"], right["d_cm"], right["mu"]
                )
                rr.update({
                    "coarse_left_index": left["index"],
                    "coarse_right_index": right["index"],
                    "direction": "pass_to_fail" if left["ge2"] else "fail_to_pass",
                })
                straddles.append(rr)

        first_fail_index = next((r["index"] for r in rows if not r["ge2"]), None)
        if first_fail_index is None:
            raise ScientificFail("no non-survivor before certified no-overlap ceiling")
        prefix_last = rows[first_fail_index - 1] if first_fail_index > 0 else None
        first_cross = next((r for r in straddles if r["direction"] == "pass_to_fail"), None)
        if prefix_last is None or first_cross is None:
            raise ScientificFail("missing initial survivor-prefix threshold bracket")

        max_survivor = max((r for r in rows if r["ge2"]), key=lambda q: q["d_cm"])
        families.append({
            "source_radius_km": radius_km,
            "theta_rad": theta,
            "projected_source_radius_cm": s,
            "y_max_cm": ymax,
            "d_zero_cm": d_zero_cm,
            "d_zero_m": d_zero_cm / 100.0,
            "row_count": len(rows),
            "survivor_count": sum(int(r["ge2"]) for r in rows),
            "first_fail_index": first_fail_index,
            "contiguous_prefix_last_survivor_m": prefix_last["d_m"],
            "max_sampled_survivor_m": max_survivor["d_m"],
            "sampled_reentry_count": reentries,
            "threshold_straddles": straddles,
            "rows": rows,
        })

    return {
        "status": "SHARD_PASS_G9_CCSN_ALIGNMENT_FOOTPRINT_SCAN",
        "contract": CONTRACT,
        "head_sha": os.getenv("GITHUB_SHA"),
        "parent_0090f_contract": PARENT_0090F_CONTRACT,
        "parent_evaluator_blob": pblob,
        "source_authority_blob": SOURCE_AUTHORITY_BLOB,
        "model_s_blob": MODEL_S_BLOB,
        "control_index": ci,
        "receiver_index": ri,
        "observer_x0": x0,
        "z_au": z,
        "turn_x": turn,
        "receiver_m": float(RECEIVERS_M[ri]),
        "focal_drift": focal_drift,
        "batch_scalar_max_rel": map_conf,
        "point_control_relative_error": point_rel,
        "map_endpoints": map_endpoints,
        "y_max_cm": ymax,
        "families": families,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--control", type=int, required=True)
    ap.add_argument("--receiver", type=int, required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    try:
        result = run_shard(args.control, args.receiver)
        code = 0
    except ScientificFail as exc:
        result = {
            "status": "SCIENTIFIC_FAIL_G9_CCSN_ALIGNMENT_FOOTPRINT",
            "reason": str(exc), "contract": CONTRACT,
            "control_index": args.control, "receiver_index": args.receiver,
            "head_sha": os.getenv("GITHUB_SHA"),
        }
        code = 1
    except Exception as exc:
        result = {
            "status": "INFRASTRUCTURE_FAIL_G9_0093",
            "reason": repr(exc), "contract": CONTRACT,
            "control_index": args.control, "receiver_index": args.receiver,
            "head_sha": os.getenv("GITHUB_SHA"),
        }
        code = 1
    Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "families"}, indent=2, sort_keys=True))
    raise SystemExit(code)


if __name__ == "__main__":
    main()
