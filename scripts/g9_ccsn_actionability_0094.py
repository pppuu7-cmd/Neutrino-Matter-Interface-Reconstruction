#!/usr/bin/env python3
import argparse, hashlib, json, math
from pathlib import Path

AU_M = 149_597_870_700.0
EXPECTED_0093_JSON_SHA256 = "9a5aea9e1d3fd00a16781870e93ee95956a3886ed47edb3a244155ce0dd23a5b"
BENCHMARK_DISTANCE_PC = 10_000.0
PROMPT_POINTING_DEG = 3.0
PRESN_OPERATIONAL_REACH_PC = 510.0
PRESN_DIRECTIONAL_SCOPE_PC = 1_000.0
BURST_HORIZON_S = 20.0


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def evaluate(parent: dict) -> dict:
    if parent.get("status") != "BLOCKED_G9_CCSN_ALIGNMENT_TOPOLOGY":
        raise ValueError("unexpected 0093 status")
    fams = parent.get("families", [])
    if len(fams) != 18:
        raise ValueError("0093 family count mismatch")
    rows = []
    for f in fams:
        beta = float(f["d_zero_m"]) / (float(f["z_au"]) * AU_M)
        rows.append({
            "control_index": f["control_index"],
            "receiver_m": f["receiver_m"],
            "source_radius_km": f["source_radius_km"],
            "d_zero_m": f["d_zero_m"],
            "z_au": f["z_au"],
            "beta_zero_rad": beta,
            "beta_zero_arcsec": beta * 180.0 / math.pi * 3600.0,
        })
    widest = max(rows, key=lambda r: r["beta_zero_rad"])
    beta_max = widest["beta_zero_rad"]
    prompt = math.radians(PROMPT_POINTING_DEG)
    ratio = prompt / beta_max
    p_iso = (1.0 - math.cos(beta_max)) / 2.0

    prompt_too_broad = prompt > beta_max
    presn_reach_not_10kpc = PRESN_OPERATIONAL_REACH_PC < BENCHMARK_DISTANCE_PC
    presn_direction_scope_not_10kpc = PRESN_DIRECTIONAL_SCOPE_PC < BENCHMARK_DISTANCE_PC
    prompt_not_prepositioning = True  # frozen causal role of burst-triggered SNEWS information

    status = (
        "SCIENTIFIC_FAIL_G9_CCSN_PROSPECTIVE_ACTIONABILITY_V1"
        if prompt_too_broad and presn_reach_not_10kpc and presn_direction_scope_not_10kpc and prompt_not_prepositioning
        else "BLOCKED_G9_CCSN_PROSPECTIVE_ACTIONABILITY_AUTHORITY"
    )
    return {
        "status": status,
        "contract": "0094_g9_ccsn_prospective_actionability_closure",
        "parent_0093_status": parent["status"],
        "parent_0093_reentry_count": parent["sampled_reentry_count_total"],
        "benchmark": {
            "distance_pc": BENCHMARK_DISTANCE_PC,
            "burst_horizon_s": BURST_HORIZON_S,
            "single_observer": True,
        },
        "widest_strict_no_overlap_support": widest,
        "beta_zero_max_rad": beta_max,
        "beta_zero_max_arcsec": widest["beta_zero_arcsec"],
        "prompt_pointing_deg": PROMPT_POINTING_DEG,
        "prompt_to_beta_zero_ratio": ratio,
        "presn_operational_reach_pc": PRESN_OPERATIONAL_REACH_PC,
        "presn_directional_scope_pc": PRESN_DIRECTIONAL_SCOPE_PC,
        "isotropic_cap_control_only": p_iso,
        "necessary_condition_flags": {
            "prompt_pointing_broader_than_strict_support": prompt_too_broad,
            "operational_presn_reach_does_not_cover_10kpc": presn_reach_not_10kpc,
            "published_presn_directional_scope_does_not_cover_10kpc": presn_direction_scope_not_10kpc,
            "burst_trigger_is_not_prepositioning_information_for_same_leading_wavefront": prompt_not_prepositioning,
        },
        "authorities": {
            "snews2": "arXiv:2406.17743",
            "prompt_10kpc_pointing": "arXiv:1901.01599",
            "presn_directionality": "arXiv:2004.02045",
            "presn_operational_alert": "arXiv:2404.09920",
            "ccsn_source": "data/g9_ccsn_source_authority_0061.json",
        },
        "guards": [
            "0093 topology remains BLOCKED",
            "isotropic cap is not a Galactic CCSN probability",
            "no swarm or known-nearby-progenitor assumption",
            "0092b-a2 transmission remains independently external-authority BLOCKED",
            "no detector/material/BSM/power multiplication",
        ],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--parent", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    parent_path = Path(args.parent)
    got = sha256(parent_path)
    if got != EXPECTED_0093_JSON_SHA256:
        raise SystemExit(f"INFRASTRUCTURE_FAIL_G9_0094 parent hash {got}")
    parent = json.loads(parent_path.read_text())
    result = evaluate(parent)
    result["parent_0093_json_sha256"] = got
    Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
