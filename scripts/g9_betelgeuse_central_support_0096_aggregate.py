#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

CONTRACT = "5e8048a3d77b504bba6a79a077a1c9e153f8cb19"
PRIMARY_STATUS = "SHARD_PASS_V2_G9_BETELGEUSE_CENTRAL_SUPPORT_SCAN"
SENS_STATUS = "SENSITIVITY_PASS_V2_G9_BETELGEUSE_CENTRAL_SUPPORT_SCAN"
PASS = "PASS_V2_G9_BETELGEUSE_CENTRAL_SUPPORT_50MAS"
FAIL = "SCIENTIFIC_FAIL_V2_G9_BETELGEUSE_CENTRAL_SUPPORT_50MAS"
INFRA = "INFRASTRUCTURE_FAIL_V2_G9_0096"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def read_json(path: Path) -> dict:
    return json.loads(path.read_text())


def aggregate_primary(input_dir: Path) -> dict:
    paths = sorted(input_dir.glob("g9_0096_primary_*.json"))
    if len(paths) != 9:
        return {"status": INFRA, "reason": f"expected 9 primary shards, got {len(paths)}", "contract": CONTRACT}

    shards = []
    families = []
    heads = set()
    parent_blobs = set()
    model_blobs = set()
    seen = set()
    for path in paths:
        obj = read_json(path)
        if obj.get("status") != PRIMARY_STATUS:
            return {"status": obj.get("status", INFRA), "reason": f"invalid primary shard {path.name}", "contract": CONTRACT}
        if obj.get("contract") != CONTRACT:
            return {"status": INFRA, "reason": "primary contract mismatch", "contract": CONTRACT}
        key = (int(obj["control_index"]), int(obj["receiver_index"]))
        if key in seen:
            return {"status": INFRA, "reason": f"duplicate shard {key}", "contract": CONTRACT}
        seen.add(key)
        heads.add(obj.get("head_sha"))
        parent_blobs.add(obj.get("parent_evaluator_blob"))
        model_blobs.add(obj.get("model_s_blob"))
        shard_summary = {
            "path": path.name,
            "sha256": sha256(path),
            "control_index": key[0],
            "receiver_index": key[1],
            "z_au": obj["z_au"],
            "receiver_m": obj["receiver_m"],
            "focal_drift": obj["focal_drift"],
            "batch_scalar_max_rel": obj["batch_scalar_max_rel"],
            "point_control_relative_error": obj["point_control_relative_error"],
        }
        shards.append(shard_summary)
        fs = obj.get("families", [])
        if len(fs) != 4:
            return {"status": INFRA, "reason": f"expected 4 families in {path.name}", "contract": CONTRACT}
        for fam in fs:
            families.append({
                "control_index": key[0],
                "receiver_index": key[1],
                "z_au": obj["z_au"],
                "receiver_m": obj["receiver_m"],
                "source_distance_pc": fam["source_distance_pc"],
                "source_radius_km": fam["source_radius_km"],
                "theta_rad": fam["theta_rad"],
                "d_target_m": fam["d_target_m"],
                "grid_count": fam["grid_count"],
                "mu_min": fam["mu_min"],
                "mu_min_index": fam["mu_min_index"],
                "mu_min_d_m": fam["mu_min_d_m"],
                "mu_axis_exact": fam["mu_axis_exact"],
                "mu_endpoint_exact": fam["mu_endpoint_exact"],
                "all_ge2": bool(fam["all_ge2"]),
            })

    if len(seen) != 9 or len(families) != 36:
        return {"status": INFRA, "reason": "incomplete frozen Cartesian family", "contract": CONTRACT}
    if len(heads) != 1 or len(parent_blobs) != 1 or len(model_blobs) != 1:
        return {"status": INFRA, "reason": "provenance disagreement across shards", "contract": CONTRACT}

    worst = min(families, key=lambda f: float(f["mu_min"]))
    primary_all_ge2 = all(f["all_ge2"] and float(f["mu_min"]) >= 2.0 for f in families)
    return {
        "status": "PRIMARY_PASS_V2_G9_BETELGEUSE_CENTRAL_SUPPORT_SCAN" if primary_all_ge2 else FAIL,
        "contract": CONTRACT,
        "head_sha": next(iter(heads)),
        "parent_evaluator_blob": next(iter(parent_blobs)),
        "model_s_blob": next(iter(model_blobs)),
        "shard_count": len(shards),
        "family_count": len(families),
        "primary_grid_count_per_family": 4097,
        "primary_all_ge2": primary_all_ge2,
        "global_primary_mu_min": worst["mu_min"],
        "worst_family": worst,
        "shards": shards,
        "families": families,
    }


def aggregate_final(primary_path: Path, sensitivity_path: Path) -> dict:
    primary = read_json(primary_path)
    sens = read_json(sensitivity_path)
    if primary.get("contract") != CONTRACT or sens.get("contract") != CONTRACT:
        return {"status": INFRA, "reason": "contract mismatch", "contract": CONTRACT}
    if primary.get("status") == INFRA or sens.get("status") == INFRA:
        return {"status": INFRA, "reason": "upstream infrastructure failure", "contract": CONTRACT}
    if sens.get("status") != SENS_STATUS:
        if str(sens.get("status", "")).startswith("SCIENTIFIC_FAIL_"):
            return {"status": FAIL, "reason": sens.get("reason", "sensitivity scientific failure"), "contract": CONTRACT}
        return {"status": INFRA, "reason": "invalid sensitivity status", "contract": CONTRACT}

    fam = sens["family"]
    w = primary["worst_family"]
    identity = (
        int(sens["control_index"]) == int(w["control_index"]) and
        int(sens["receiver_index"]) == int(w["receiver_index"]) and
        float(fam["source_distance_pc"]) == float(w["source_distance_pc"]) and
        float(fam["source_radius_km"]) == float(w["source_radius_km"])
    )
    if not identity:
        return {"status": INFRA, "reason": "sensitivity family is not frozen global primary minimum", "contract": CONTRACT}

    mu4097 = float(primary["global_primary_mu_min"])
    mu8193 = float(fam["mu_min"])
    sens_all = bool(fam["all_ge2"]) and mu8193 >= 2.0
    primary_all = bool(primary.get("primary_all_ge2")) and mu4097 >= 2.0
    status = PASS if primary_all and sens_all else FAIL
    rel_diff = abs(mu4097 - mu8193) / max(abs(mu4097), abs(mu8193), 1e-300)
    return {
        "status": status,
        "contract": CONTRACT,
        "head_sha": primary.get("head_sha"),
        "parent_evaluator_blob": primary.get("parent_evaluator_blob"),
        "model_s_blob": primary.get("model_s_blob"),
        "primary_summary_sha256": sha256(primary_path),
        "sensitivity_sha256": sha256(sensitivity_path),
        "family_count": int(primary["family_count"]),
        "shard_count": int(primary["shard_count"]),
        "beta_target_arcsec": 0.050,
        "primary_grid_count_per_family": 4097,
        "sensitivity_grid_count": 8193,
        "global_primary_mu_min": mu4097,
        "global_sensitivity_mu_min": mu8193,
        "minimum_relative_difference": rel_diff,
        "worst_family": w,
        "sensitivity_family": {
            "control_index": sens["control_index"],
            "receiver_index": sens["receiver_index"],
            "z_au": sens["z_au"],
            "receiver_m": sens["receiver_m"],
            "source_distance_pc": fam["source_distance_pc"],
            "source_radius_km": fam["source_radius_km"],
            "theta_rad": fam["theta_rad"],
            "d_target_m": fam["d_target_m"],
            "mu_min": fam["mu_min"],
            "mu_min_index": fam["mu_min_index"],
            "mu_min_d_m": fam["mu_min_d_m"],
            "mu_axis_exact": fam["mu_axis_exact"],
            "mu_endpoint_exact": fam["mu_endpoint_exact"],
            "all_ge2": fam["all_ge2"],
        },
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=("primary", "final"), required=True)
    ap.add_argument("--input")
    ap.add_argument("--primary")
    ap.add_argument("--sensitivity")
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    if args.mode == "primary":
        if not args.input:
            raise SystemExit("primary mode requires --input")
        out = aggregate_primary(Path(args.input))
    else:
        if not args.primary or not args.sensitivity:
            raise SystemExit("final mode requires --primary and --sensitivity")
        out = aggregate_final(Path(args.primary), Path(args.sensitivity))
    Path(args.output).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in out.items() if k not in ("families", "shards")}, indent=2, sort_keys=True))
    if out["status"] == INFRA:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
