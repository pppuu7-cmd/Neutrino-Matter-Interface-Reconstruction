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

CONTRACT = "5e8048a3d77b504bba6a79a077a1c9e153f8cb19"
PARENT_EVALUATOR_BLOB = "4bedc9431b428292f1b09613f603bea82597f9b5"
PARENT_0090F_CONTRACT = "fc277e3695ebeb2628d133b9385e7d7d2e12a5d5"
SOURCE_DISTANCES_PC = (190.0, 222.0)
SOURCE_RADII_KM = (21.0, 100.0)
BETA_TARGET_ARCSEC = 0.050
BETA_TARGET_RAD = BETA_TARGET_ARCSEC * math.pi / (180.0 * 3600.0)
THETA_MIN_0090F = 1.0e-18
THETA_MAX_0090F = 1.0e-6
ANGULAR_ORDER = 32
RADIAL_ORDER = 64
MAP_TOL = 2e-11
POINT_TOL = 0.005
N_PRIMARY = 4097
N_SENSITIVITY = 8193
SENSITIVITY_CHUNKS = 4


class ScientificFail(RuntimeError):
    pass


class InfrastructureFail(RuntimeError):
    pass


def rel(a: float, b: float) -> float:
    return abs(a - b) / max(abs(a), abs(b), 1e-300)


def blob_sha1_bytes(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def parent_evaluator_blob() -> str:
    p = Path(dual.__file__)
    if p.suffix == ".pyc":
        p = p.with_suffix(".py")
    return blob_sha1_bytes(p.read_bytes())


def pc_cm() -> float:
    return (648000.0 / math.pi) * AU_CM


def source_theta(radius_km: float, distance_pc: float) -> float:
    return radius_km * 1.0e5 / (distance_pc * pc_cm())


def frozen_node(stop_cm: float, n: int, j: int) -> float:
    if not (math.isfinite(stop_cm) and stop_cm > 0.0 and n >= 2 and 0 <= j < n):
        raise ScientificFail("invalid frozen grid node")
    if j == 0:
        return 0.0
    if j == n - 1:
        return stop_cm
    return stop_cm * j / (n - 1)


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


def prepare_control(ci: int, ri: int):
    if ci not in (0, 1, 2) or ri not in (0, 1, 2):
        raise InfrastructureFail("invalid control/receiver index")
    if dual.CONTRACT != "c9d9e46860ef55bec2a5aaaafdac19f6e9de551b":
        raise InfrastructureFail("0090e parent contract mismatch")
    if dual.AMENDMENT != "c95fd80e7b2a54d04f83103e7678acbe8c51f6c6":
        raise InfrastructureFail("0090e parent amendment mismatch")
    pblob = parent_evaluator_blob()
    if pblob != PARENT_EVALUATOR_BLOB:
        raise InfrastructureFail(f"0090e evaluator blob mismatch: {pblob}")

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
    return focal, x0, z, turn, a, pblob, focal_drift, map_conf, point_rel


def family_setup(z: float, a: float, distance_pc: float, radius_km: float) -> dict:
    if distance_pc not in SOURCE_DISTANCES_PC or radius_km not in SOURCE_RADII_KM:
        raise InfrastructureFail("family outside frozen 0096 Cartesian set")
    theta = source_theta(radius_km, distance_pc)
    if not (THETA_MIN_0090F <= theta <= THETA_MAX_0090F):
        raise ScientificFail(f"source theta outside 0090f support: {theta:.17g}")
    s = z * AU_CM * theta
    d_target = z * AU_CM * math.tan(BETA_TARGET_RAD)
    return {
        "theta": theta,
        "s": s,
        "d_target": d_target,
        "ceiling": perfect_whole_sun_mu_upper(a, R),
        "lsb": large_source_ring_excess_upper(s, R),
    }


def run_indices(focal, x0: float, z: float, turn: float, a: float,
                distance_pc: float, radius_km: float, n: int, indices: list[int]) -> dict:
    fs = family_setup(z, a, distance_pc, radius_km)
    rows = []
    for j in indices:
        d = frozen_node(fs["d_target"], n, j)
        mu, area = evaluate_mu(focal, z, turn, x0, a, fs["s"], d, fs["ceiling"], fs["lsb"])
        rows.append({
            "index": j, "d_cm": d, "d_m": d / 100.0,
            "beta_rad_exact": math.atan2(d, z * AU_CM),
            "mu": mu, "area_h_cm2": area, "ge2": mu >= 2.0,
        })
    if not rows:
        raise InfrastructureFail("empty grid chunk")
    min_row = min(rows, key=lambda r: r["mu"])
    return {
        "source_distance_pc": distance_pc,
        "source_radius_km": radius_km,
        "theta_rad": fs["theta"],
        "projected_source_radius_cm": fs["s"],
        "beta_target_arcsec": BETA_TARGET_ARCSEC,
        "beta_target_rad": BETA_TARGET_RAD,
        "d_target_cm": fs["d_target"],
        "d_target_m": fs["d_target"] / 100.0,
        "grid_count": n,
        "evaluated_count": len(rows),
        "mu_min": min_row["mu"],
        "mu_min_index": min_row["index"],
        "mu_min_d_m": min_row["d_m"],
        "all_ge2": all(r["ge2"] for r in rows),
        "rows": rows,
    }


def run_primary(ci: int, ri: int, distance_pc: float, radius_km: float) -> dict:
    focal, x0, z, turn, a, pblob, drift, conf, point_rel = prepare_control(ci, ri)
    fam = run_indices(
        focal, x0, z, turn, a, distance_pc, radius_km,
        N_PRIMARY, list(range(N_PRIMARY))
    )
    # Prospectively required independent exact axis/endpoint evaluations.
    fs = family_setup(z, a, distance_pc, radius_km)
    mu_axis, area_axis = evaluate_mu(focal, z, turn, x0, a, fs["s"], 0.0, fs["ceiling"], fs["lsb"])
    mu_end, area_end = evaluate_mu(focal, z, turn, x0, a, fs["s"], fs["d_target"], fs["ceiling"], fs["lsb"])
    fam.update({
        "mu_axis_exact": mu_axis, "area_axis_exact_cm2": area_axis,
        "mu_endpoint_exact": mu_end, "area_endpoint_exact_cm2": area_end,
        "all_ge2": fam["all_ge2"] and mu_axis >= 2.0 and mu_end >= 2.0,
    })
    return {
        "status": "SHARD_PASS_V2_G9_BETELGEUSE_CENTRAL_SUPPORT_SCAN",
        "contract": CONTRACT, "head_sha": os.getenv("GITHUB_SHA"),
        "parent_0090f_contract": PARENT_0090F_CONTRACT,
        "parent_evaluator_blob": pblob, "model_s_blob": MODEL_S_BLOB,
        "control_index": ci, "receiver_index": ri, "observer_x0": x0,
        "z_au": z, "receiver_m": float(RECEIVERS_M[ri]),
        "focal_drift": drift, "batch_scalar_max_rel": conf,
        "point_control_relative_error": point_rel, "family": fam,
    }


def run_sensitivity_chunk(spec_path: Path, chunk: int) -> dict:
    if chunk not in range(SENSITIVITY_CHUNKS):
        raise InfrastructureFail("invalid sensitivity chunk")
    spec = json.loads(spec_path.read_text())
    w = spec["worst_family"]
    ci, ri = int(w["control_index"]), int(w["receiver_index"])
    distance_pc, radius_km = float(w["source_distance_pc"]), float(w["source_radius_km"])
    focal, x0, z, turn, a, pblob, drift, conf, point_rel = prepare_control(ci, ri)
    indices = list(range(chunk, N_SENSITIVITY, SENSITIVITY_CHUNKS))
    fam = run_indices(focal, x0, z, turn, a, distance_pc, radius_km, N_SENSITIVITY, indices)
    return {
        "status": "SENSITIVITY_CHUNK_PASS_V2_G9_BETELGEUSE_CENTRAL_SUPPORT_SCAN",
        "contract": CONTRACT, "head_sha": os.getenv("GITHUB_SHA"),
        "parent_evaluator_blob": pblob, "model_s_blob": MODEL_S_BLOB,
        "control_index": ci, "receiver_index": ri, "observer_x0": x0,
        "z_au": z, "receiver_m": float(RECEIVERS_M[ri]),
        "focal_drift": drift, "batch_scalar_max_rel": conf,
        "point_control_relative_error": point_rel,
        "chunk_index": chunk, "chunk_count": SENSITIVITY_CHUNKS,
        "family": fam,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=("primary", "sensitivity-chunk"), required=True)
    ap.add_argument("--control", type=int)
    ap.add_argument("--receiver", type=int)
    ap.add_argument("--distance-pc", type=float)
    ap.add_argument("--radius-km", type=float)
    ap.add_argument("--spec")
    ap.add_argument("--chunk", type=int)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    try:
        if args.mode == "primary":
            if None in (args.control, args.receiver, args.distance_pc, args.radius_km):
                raise InfrastructureFail("primary requires control, receiver, distance and radius")
            result = run_primary(args.control, args.receiver, args.distance_pc, args.radius_km)
        else:
            if not args.spec or args.chunk is None:
                raise InfrastructureFail("sensitivity-chunk requires --spec and --chunk")
            result = run_sensitivity_chunk(Path(args.spec), args.chunk)
        code = 0
    except ScientificFail as exc:
        result = {"status": "SCIENTIFIC_FAIL_V2_G9_BETELGEUSE_CENTRAL_SUPPORT_50MAS", "reason": str(exc), "contract": CONTRACT, "head_sha": os.getenv("GITHUB_SHA")}
        code = 1
    except Exception as exc:
        result = {"status": "INFRASTRUCTURE_FAIL_V2_G9_0096", "reason": repr(exc), "contract": CONTRACT, "head_sha": os.getenv("GITHUB_SHA")}
        code = 1
    Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "family"}, indent=2, sort_keys=True))
    raise SystemExit(code)


if __name__ == "__main__":
    main()
