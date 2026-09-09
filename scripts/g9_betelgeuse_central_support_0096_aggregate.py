#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

CONTRACT = "5e8048a3d77b504bba6a79a077a1c9e153f8cb19"
PRIMARY_STATUS = "SHARD_PASS_V2_G9_BETELGEUSE_CENTRAL_SUPPORT_SCAN"
SENS_STATUS = "SENSITIVITY_CHUNK_PASS_V2_G9_BETELGEUSE_CENTRAL_SUPPORT_SCAN"
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


def fam_summary(obj: dict, path: Path) -> dict:
    fam = obj["family"]
    return {
        "path": path.name,
        "sha256": sha256(path),
        "control_index": int(obj["control_index"]),
        "receiver_index": int(obj["receiver_index"]),
        "z_au": obj["z_au"],
        "receiver_m": obj["receiver_m"],
        "source_distance_pc": fam["source_distance_pc"],
        "source_radius_km": fam["source_radius_km"],
        "theta_rad": fam["theta_rad"],
        "d_target_m": fam["d_target_m"],
        "grid_count": fam["grid_count"],
        "evaluated_count": fam["evaluated_count"],
        "mu_min": fam["mu_min"],
        "mu_min_index": fam["mu_min_index"],
        "mu_min_d_m": fam["mu_min_d_m"],
        "mu_axis_exact": fam["mu_axis_exact"],
        "mu_endpoint_exact": fam["mu_endpoint_exact"],
        "all_ge2": bool(fam["all_ge2"]),
        "focal_drift": obj["focal_drift"],
        "batch_scalar_max_rel": obj["batch_scalar_max_rel"],
        "point_control_relative_error": obj["point_control_relative_error"],
    }


def aggregate_primary(input_dir: Path) -> dict:
    paths = sorted(input_dir.glob("g9_0096_primary_*.json"))
    if len(paths) != 36:
        return {"status": INFRA, "reason": f"expected 36 primary family shards, got {len(paths)}", "contract": CONTRACT}
    families, seen = [], set()
    heads, parent_blobs, model_blobs = set(), set(), set()
    for path in paths:
        obj = read_json(path)
        if obj.get("status") != PRIMARY_STATUS:
            return {"status": obj.get("status", INFRA), "reason": f"invalid primary shard {path.name}", "contract": CONTRACT}
        if obj.get("contract") != CONTRACT:
            return {"status": INFRA, "reason": "primary contract mismatch", "contract": CONTRACT}
        fam = obj.get("family")
        if not isinstance(fam, dict):
            return {"status": INFRA, "reason": f"missing family in {path.name}", "contract": CONTRACT}
        key = (int(obj["control_index"]), int(obj["receiver_index"]), float(fam["source_distance_pc"]), float(fam["source_radius_km"]))
        if key in seen:
            return {"status": INFRA, "reason": f"duplicate family {key}", "contract": CONTRACT}
        seen.add(key)
        heads.add(obj.get("head_sha")); parent_blobs.add(obj.get("parent_evaluator_blob")); model_blobs.add(obj.get("model_s_blob"))
        s = fam_summary(obj, path)
        if int(s["grid_count"]) != 4097 or int(s["evaluated_count"]) != 4097:
            return {"status": INFRA, "reason": f"primary grid-count mismatch in {path.name}", "contract": CONTRACT}
        families.append(s)
    if len(seen) != 36:
        return {"status": INFRA, "reason": "incomplete frozen Cartesian family", "contract": CONTRACT}
    if len(heads) != 1 or len(parent_blobs) != 1 or len(model_blobs) != 1:
        return {"status": INFRA, "reason": "provenance disagreement across primary shards", "contract": CONTRACT}
    worst = min(families, key=lambda f: float(f["mu_min"]))
    primary_all = all(f["all_ge2"] and float(f["mu_min"]) >= 2.0 and float(f["mu_axis_exact"]) >= 2.0 and float(f["mu_endpoint_exact"]) >= 2.0 for f in families)
    return {
        "status": "PRIMARY_PASS_V2_G9_BETELGEUSE_CENTRAL_SUPPORT_SCAN" if primary_all else FAIL,
        "contract": CONTRACT, "head_sha": next(iter(heads)),
        "parent_evaluator_blob": next(iter(parent_blobs)), "model_s_blob": next(iter(model_blobs)),
        "shard_count": 36, "family_count": 36, "primary_grid_count_per_family": 4097,
        "primary_all_ge2": primary_all, "global_primary_mu_min": worst["mu_min"],
        "worst_family": worst, "families": families,
    }


def aggregate_final(primary_path: Path, sensitivity_dir: Path) -> dict:
    primary = read_json(primary_path)
    if primary.get("contract") != CONTRACT:
        return {"status": INFRA, "reason": "primary contract mismatch", "contract": CONTRACT}
    paths = sorted(sensitivity_dir.glob("g9_0096_sensitivity_*.json"))
    if len(paths) != 4:
        return {"status": INFRA, "reason": f"expected 4 sensitivity chunks, got {len(paths)}", "contract": CONTRACT}
    w = primary["worst_family"]
    chunks, seen_chunks, heads, parent_blobs, model_blobs = [], set(), set(), set(), set()
    total_count, sens_all = 0, True
    for path in paths:
        obj = read_json(path)
        if obj.get("status") != SENS_STATUS:
            if str(obj.get("status", "")).startswith("SCIENTIFIC_FAIL_"):
                return {"status": FAIL, "reason": obj.get("reason", "sensitivity scientific failure"), "contract": CONTRACT}
            return {"status": INFRA, "reason": f"invalid sensitivity chunk {path.name}", "contract": CONTRACT}
        if obj.get("contract") != CONTRACT:
            return {"status": INFRA, "reason": "sensitivity contract mismatch", "contract": CONTRACT}
        c = int(obj["chunk_index"])
        if c in seen_chunks or c not in range(4) or int(obj["chunk_count"]) != 4:
            return {"status": INFRA, "reason": "invalid sensitivity chunk partition", "contract": CONTRACT}
        seen_chunks.add(c)
        fam = obj["family"]
        identity = (
            int(obj["control_index"]) == int(w["control_index"]) and
            int(obj["receiver_index"]) == int(w["receiver_index"]) and
            float(fam["source_distance_pc"]) == float(w["source_distance_pc"]) and
            float(fam["source_radius_km"]) == float(w["source_radius_km"])
        )
        if not identity or int(fam["grid_count"]) != 8193:
            return {"status": INFRA, "reason": "sensitivity family/grid identity mismatch", "contract": CONTRACT}
        heads.add(obj.get("head_sha")); parent_blobs.add(obj.get("parent_evaluator_blob")); model_blobs.add(obj.get("model_s_blob"))
        total_count += int(fam["evaluated_count"])
        sens_all = sens_all and bool(fam["all_ge2"]) and float(fam["mu_min"]) >= 2.0
        chunks.append({
            "chunk_index": c, "path": path.name, "sha256": sha256(path),
            "evaluated_count": fam["evaluated_count"], "mu_min": fam["mu_min"],
            "mu_min_index": fam["mu_min_index"], "mu_min_d_m": fam["mu_min_d_m"],
            "all_ge2": fam["all_ge2"],
        })
    if seen_chunks != {0,1,2,3} or total_count != 8193:
        return {"status": INFRA, "reason": f"sensitivity union does not contain exactly 8193 nodes: {total_count}", "contract": CONTRACT}
    if len(heads) != 1 or len(parent_blobs) != 1 or len(model_blobs) != 1:
        return {"status": INFRA, "reason": "sensitivity provenance disagreement", "contract": CONTRACT}
    worst_chunk = min(chunks, key=lambda q: float(q["mu_min"]))
    mu4097 = float(primary["global_primary_mu_min"])
    mu8193 = float(worst_chunk["mu_min"])
    primary_all = bool(primary.get("primary_all_ge2")) and mu4097 >= 2.0
    status = PASS if primary_all and sens_all else FAIL
    rel_diff = abs(mu4097 - mu8193) / max(abs(mu4097), abs(mu8193), 1e-300)
    return {
        "status": status, "contract": CONTRACT,
        "primary_head_sha": primary.get("head_sha"), "sensitivity_head_sha": next(iter(heads)),
        "parent_evaluator_blob": primary.get("parent_evaluator_blob"), "model_s_blob": primary.get("model_s_blob"),
        "primary_summary_sha256": sha256(primary_path),
        "sensitivity_chunk_sha256": {str(c["chunk_index"]): c["sha256"] for c in sorted(chunks, key=lambda x: x["chunk_index"])},
        "family_count": 36, "primary_shard_count": 36, "sensitivity_chunk_count": 4,
        "beta_target_arcsec": 0.050, "primary_grid_count_per_family": 4097,
        "sensitivity_grid_count": 8193, "sensitivity_evaluated_union_count": total_count,
        "global_primary_mu_min": mu4097, "global_sensitivity_mu_min": mu8193,
        "primary_sensitivity_min_relative_difference": rel_diff,
        "worst_family": w, "worst_sensitivity_chunk": worst_chunk,
        "sensitivity_chunks": sorted(chunks, key=lambda x: x["chunk_index"]),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=("primary", "final"), required=True)
    ap.add_argument("--input"); ap.add_argument("--primary"); ap.add_argument("--sensitivity-dir"); ap.add_argument("--output", required=True)
    args = ap.parse_args()
    if args.mode == "primary":
        if not args.input: raise SystemExit("primary mode requires --input")
        out = aggregate_primary(Path(args.input))
    else:
        if not args.primary or not args.sensitivity_dir: raise SystemExit("final mode requires --primary and --sensitivity-dir")
        out = aggregate_final(Path(args.primary), Path(args.sensitivity_dir))
    Path(args.output).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k:v for k,v in out.items() if k not in ("families", "sensitivity_chunks")}, indent=2, sort_keys=True))
    if out["status"] == INFRA: raise SystemExit(1)


if __name__ == "__main__":
    main()
