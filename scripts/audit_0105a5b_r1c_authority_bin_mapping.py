#!/usr/bin/env python3
"""NMIR v2 0105a5b R1c authority-derived coordinate mapping.

Authority-only NONDISCOVERY gate.  This code deliberately computes no oscillated
expectation, likelihood, nuisance fit, residual, BSM parameter, or significance.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import urllib.request
from pathlib import Path

API = "https://dataverse.harvard.edu/api/access/datafile"
DOI = "10.7910/DVN/B4RITM"
VERSION = "1.0"
FORBIDDEN_DOI = "10.7910/DVN/QKL28Z"

ENERGY_EDGES = [6.31, 8.45862141, 11.33887101, 15.19987592, 20.37559363,
                27.3136977, 36.61429921, 49.08185342, 65.79474104,
                88.19854278, 158.49]
COSZEN_EDGES = [-1.0, -0.89, -0.78, -0.67, -0.56, -0.45, -0.34, -0.23,
                -0.12, -0.01, 0.1]
PID_EDGES = [0.55, 0.75, 1.0]

# Exact Saved Original bytes already recovered in the hosted R1c authority bundle.
# These SHA256 locks prevent a mutable-provider fetch from silently changing the gate.
FILES = {
    "data.csv": (11646859, "68bdc3db7404d497a0c439fb2d95ab0b7ed9942ac4ed6dde236e761413360cfd"),
    "mc_nu_nc.csv": (11646850, "aab94b5e0e285135471d5eb7b27db3f818f40c423ed95f27af6d3ba06becf355"),
    "mc_nue_cc.csv": (11646852, "a968f274726dc4b316c6eb9d93901dacda13dc92528d1081887fd473a958cf8b"),
    "mc_numu_cc.csv": (11646856, "a3bc53223d8e6f9b9e43e36d277550976631315f5a00771dff2c588120410724"),
    "mc_nutau_cc.csv": (11646855, "7e8596016ae4a9fca8e2d805c132f3b89ac9a6eacfb1ea828a7347f6c0184f07"),
    "readme.md": (11674676, "0f8e7bbc6059d18376843370e36e98a0cfa69fbc4bd767df694c6d65f861149f"),
}


def fetch_original(file_id: int) -> bytes:
    req = urllib.request.Request(
        f"{API}/{file_id}?format=original",
        headers={"User-Agent": "NMIR-v2-0105a5b-r1c-mapping"},
    )
    with urllib.request.urlopen(req, timeout=300) as r:
        return r.read()


def strict_bin(x: float, edges: list[float]) -> int:
    hits = [j for j in range(len(edges) - 1) if edges[j] < x < edges[j + 1]]
    if len(hits) != 1:
        raise ValueError(f"coordinate {x!r} does not lie strictly inside exactly one bin")
    return hits[0]


def cell_key(row: dict[str, str]) -> tuple[int, int, int]:
    return (
        strict_bin(float(row["pid"]), PID_EDGES),
        strict_bin(float(row["reco_coszen"]), COSZEN_EDGES),
        strict_bin(float(row["reco_energy"]), ENERGY_EDGES),
    )


def rows_from_bytes(payload: bytes):
    text = io.TextIOWrapper(io.BytesIO(payload), encoding="utf-8-sig", newline="")
    yield from csv.DictReader(text)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    ap.add_argument("--raw-dir", required=True)
    args = ap.parse_args()
    out = Path(args.output)
    raw_dir = Path(args.raw_dir)
    raw_dir.mkdir(parents=True, exist_ok=True)

    payloads: dict[str, bytes] = {}
    manifest = {}
    try:
        for name, (file_id, expected_sha) in FILES.items():
            payload = fetch_original(file_id)
            got = hashlib.sha256(payload).hexdigest()
            if got != expected_sha:
                raise RuntimeError(f"SHA256 mismatch for {name}: {got} != {expected_sha}")
            payloads[name] = payload
            (raw_dir / name).write_bytes(payload)
            manifest[name] = {"file_id": file_id, "sha256": got, "byte_count": len(payload)}
    except Exception as exc:
        result = {
            "benchmark": "NMIR-V2-0105A5B-R1C-MAPPING",
            "status": "INFRASTRUCTURE_FAIL_0105A5B_R1C",
            "reason": str(exc),
            "dataset_doi": DOI,
            "frozen_version": VERSION,
            "observed_bsm_residual_permission_percent": 0,
        }
        out.write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
        print(result["status"])
        return 2

    readme = payloads["readme.md"].decode("utf-8-sig")
    authority_phrases = [
        "The reconstructed variables are provided in the analysis binning, such that events fall into the mid-point of their bin.",
        "The reconstructed variables follow the same convention as `data.csv`",
    ]
    missing_phrases = [p for p in authority_phrases if p not in readme]
    if missing_phrases:
        result = {
            "benchmark": "NMIR-V2-0105A5B-R1C-MAPPING",
            "status": "BLOCKED_0105A5B_R1C_COORDINATE_SEMANTICS_AUTHORITY_INCOMPLETE",
            "reason": "FROZEN_README_AUTHORITY_PHRASE_MISSING",
            "missing_phrases": missing_phrases,
            "file_manifest": manifest,
            "observed_bsm_residual_permission_percent": 0,
        }
        out.write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
        print(result["status"])
        return 3

    try:
        observed_rows = list(rows_from_bytes(payloads["data.csv"]))
        observed_coord_tuples = {
            (float(r["pid"]), float(r["reco_coszen"]), float(r["reco_energy"]))
            for r in observed_rows
        }
        observed_keys = [cell_key(r) for r in observed_rows]

        mc_coord_tuples: set[tuple[float, float, float]] = set()
        for name in ("mc_nu_nc.csv", "mc_nue_cc.csv", "mc_numu_cc.csv", "mc_nutau_cc.csv"):
            for r in rows_from_bytes(payloads[name]):
                mc_coord_tuples.add((float(r["pid"]), float(r["reco_coszen"]), float(r["reco_energy"])))
        mc_keys = {
            (
                strict_bin(pid, PID_EDGES),
                strict_bin(cosz, COSZEN_EDGES),
                strict_bin(energy, ENERGY_EDGES),
            )
            for pid, cosz, energy in mc_coord_tuples
        }
    except Exception as exc:
        result = {
            "benchmark": "NMIR-V2-0105A5B-R1C-MAPPING",
            "status": "SCIENTIFIC_FAIL_0105A5B_R1C_COORDINATE_MAPPING_NONBIJECTIVE",
            "reason": f"STRICT_BIN_MAPPING_FAILED: {exc}",
            "file_manifest": manifest,
            "observed_bsm_residual_permission_percent": 0,
        }
        out.write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
        print(result["status"])
        return 4

    observed_key_set = set(observed_keys)
    criteria = {
        "observed_row_count_200": len(observed_rows) == 200,
        "observed_coordinate_tuple_count_200": len(observed_coord_tuples) == 200,
        "observed_unique_cell_keys_200": len(observed_key_set) == 200,
        "mc_coordinate_tuple_count_200": len(mc_coord_tuples) == 200,
        "mc_unique_cell_keys_200": len(mc_keys) == 200,
        "cell_key_sets_equal": observed_key_set == mc_keys,
        "observed_full_shape_2x10x10": observed_key_set == {(p, z, e) for p in range(2) for z in range(10) for e in range(10)},
        "mc_full_shape_2x10x10": mc_keys == {(p, z, e) for p in range(2) for z in range(10) for e in range(10)},
        "pid_representation_maps_same_upper_bin": strict_bin(0.88, PID_EDGES) == strict_bin(0.875, PID_EDGES) == 1,
    }

    status = (
        "PASS_0105A5B_R1C_COORDINATE_SEMANTICS_AUTHORITY_NONDISCOVERY"
        if all(criteria.values())
        else "SCIENTIFIC_FAIL_0105A5B_R1C_COORDINATE_MAPPING_NONBIJECTIVE"
    )
    result = {
        "benchmark": "NMIR-V2-0105A5B-R1C-MAPPING",
        "dataset_doi": DOI,
        "forbidden_sterile_doi": FORBIDDEN_DOI,
        "frozen_version": VERSION,
        "authority_mapping_rule": "strict interior boundary index independently on pid,reco_coszen,reco_energy",
        "energy_edges_gev": ENERGY_EDGES,
        "coszen_edges": COSZEN_EDGES,
        "pid_edges": PID_EDGES,
        "file_manifest": manifest,
        "observed_row_count": len(observed_rows),
        "observed_coordinate_tuple_count": len(observed_coord_tuples),
        "mc_coordinate_tuple_count": len(mc_coord_tuples),
        "observed_unique_cell_key_count": len(observed_key_set),
        "mc_unique_cell_key_count": len(mc_keys),
        "observed_pid_labels": sorted({x[0] for x in observed_coord_tuples}),
        "mc_pid_labels": sorted({x[0] for x in mc_coord_tuples}),
        "criteria": criteria,
        "status": status,
        "oscillated_expectation_computed": False,
        "likelihood_computed": False,
        "nuisance_fit_executed": False,
        "observed_minus_null_residual_computed": False,
        "bsm_quantity_computed": False,
        "observed_bsm_residual_permission_percent": 0,
    }
    out.write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print(status)
    print(f"observed_keys={len(observed_key_set)} mc_keys={len(mc_keys)} equal={observed_key_set == mc_keys}")
    return 0 if status.startswith("PASS_") else 4


if __name__ == "__main__":
    raise SystemExit(main())
