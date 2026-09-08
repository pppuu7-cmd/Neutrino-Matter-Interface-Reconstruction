#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

CONTRACT = "ffaa7706bf335b301833fe49754297b804cf713a"
EXPECTED_SHARDS = 9
EXPECTED_FAMILIES = 18
AU_CM = 1.495978707e13
RAD_TO_ARCSEC = 648000.0 / math.pi


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    files = sorted(Path(args.input).glob("g9_0093_shard_*.json"))
    if len(files) != EXPECTED_SHARDS:
        out = {
            "status": "INFRASTRUCTURE_FAIL_G9_0093",
            "reason": f"expected {EXPECTED_SHARDS} shards, found {len(files)}",
            "contract": CONTRACT,
        }
        Path(args.output).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
        raise SystemExit(1)

    shards = [json.loads(p.read_text()) for p in files]
    if any(s.get("contract") != CONTRACT for s in shards):
        out = {"status": "INFRASTRUCTURE_FAIL_G9_0093", "reason": "contract mismatch", "contract": CONTRACT}
        Path(args.output).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
        raise SystemExit(1)
    bad = [s for s in shards if s.get("status") != "SHARD_PASS_G9_CCSN_ALIGNMENT_FOOTPRINT_SCAN"]
    if bad:
        statuses = [s.get("status") for s in bad]
        status = (
            "SCIENTIFIC_FAIL_G9_CCSN_ALIGNMENT_FOOTPRINT"
            if any(x == "SCIENTIFIC_FAIL_G9_CCSN_ALIGNMENT_FOOTPRINT" for x in statuses)
            else "INFRASTRUCTURE_FAIL_G9_0093"
        )
        out = {"status": status, "contract": CONTRACT, "bad_statuses": statuses}
        Path(args.output).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
        raise SystemExit(1)

    seen = {(int(s["control_index"]), int(s["receiver_index"])) for s in shards}
    if seen != {(i, j) for i in range(3) for j in range(3)}:
        out = {"status": "INFRASTRUCTURE_FAIL_G9_0093", "reason": "shard identity/cardinality mismatch", "contract": CONTRACT}
        Path(args.output).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
        raise SystemExit(1)

    fam = []
    for s in shards:
        z = float(s["z_au"])
        for f in s["families"]:
            first = next((x for x in f["threshold_straddles"] if x["direction"] == "pass_to_fail"), None)
            if first is None:
                out = {"status": "SCIENTIFIC_FAIL_G9_CCSN_ALIGNMENT_FOOTPRINT", "reason": "missing first pass-to-fail crossing", "contract": CONTRACT}
                Path(args.output).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
                raise SystemExit(1)
            pass_cm = float(first["lo_cm"])
            fail_cm = float(first["hi_cm"])
            # The direction is pass-to-fail, so the refined lo endpoint must remain the survivor side.
            if not bool(first["lo_state"]) or bool(first["hi_state"]):
                out = {"status": "SCIENTIFIC_FAIL_G9_CCSN_ALIGNMENT_FOOTPRINT", "reason": "refined crossing state orientation mismatch", "contract": CONTRACT}
                Path(args.output).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
                raise SystemExit(1)
            beta = pass_cm / (z * AU_CM)
            fam.append({
                "control_index": int(s["control_index"]),
                "receiver_index": int(s["receiver_index"]),
                "receiver_m": float(s["receiver_m"]),
                "z_au": z,
                "source_radius_km": float(f["source_radius_km"]),
                "theta_rad": float(f["theta_rad"]),
                "projected_source_radius_cm": float(f["projected_source_radius_cm"]),
                "y_max_cm": float(f["y_max_cm"]),
                "d_zero_m": float(f["d_zero_m"]),
                "sampled_reentry_count": int(f["sampled_reentry_count"]),
                "contiguous_prefix_last_survivor_m": float(f["contiguous_prefix_last_survivor_m"]),
                "max_sampled_survivor_m": float(f["max_sampled_survivor_m"]),
                "first_crossing_pass_m": pass_cm / 100.0,
                "first_crossing_fail_m": fail_cm / 100.0,
                "first_crossing_mu_pass": float(first["mu_lo"]),
                "first_crossing_mu_fail": float(first["mu_hi"]),
                "first_crossing_relative_width": float(first.get("relative_width", 0.0)),
                "beta_pass_rad": beta,
                "beta_pass_arcsec": beta * RAD_TO_ARCSEC,
                "beta_pass_microarcsec": beta * RAD_TO_ARCSEC * 1e6,
                "straddle_count": len(f["threshold_straddles"]),
            })

    if len(fam) != EXPECTED_FAMILIES:
        out = {"status": "INFRASTRUCTURE_FAIL_G9_0093", "reason": f"expected {EXPECTED_FAMILIES} families, found {len(fam)}", "contract": CONTRACT}
        Path(args.output).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
        raise SystemExit(1)

    reentries = sum(x["sampled_reentry_count"] for x in fam)
    conservative = min(fam, key=lambda x: x["first_crossing_pass_m"])
    widest = max(fam, key=lambda x: x["first_crossing_pass_m"])
    min_prefix = min(x["contiguous_prefix_last_survivor_m"] for x in fam)
    max_prefix = max(x["contiguous_prefix_last_survivor_m"] for x in fam)

    if reentries:
        status = "BLOCKED_G9_CCSN_ALIGNMENT_TOPOLOGY"
    elif conservative["first_crossing_pass_m"] <= 100.0:
        status = "SCIENTIFIC_FAIL_G9_CCSN_ALIGNMENT_FOOTPRINT"
    else:
        status = "PASS_G9_CCSN_ALIGNMENT_FOOTPRINT_EXPANDED"

    out = {
        "status": status,
        "contract": CONTRACT,
        "shard_count": len(shards),
        "family_count": len(fam),
        "sampled_reentry_count_total": reentries,
        "conservative_ccsn_footprint": conservative,
        "widest_ccsn_footprint": widest,
        "minimum_contiguous_prefix_last_survivor_m": min_prefix,
        "maximum_contiguous_prefix_last_survivor_m": max_prefix,
        "families": sorted(fam, key=lambda x: (x["control_index"], x["receiver_index"], x["source_radius_km"])),
        "guards": [
            "numerical geometry only",
            "no claim that generic future CCSN direction is known prospectively",
            "0092b-a2 nuclear-channel authority blocker remains independent",
            "no detector/material/power multiplication",
        ],
    }
    Path(args.output).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in out.items() if k != "families"}, indent=2, sort_keys=True))
    raise SystemExit(0 if status.startswith("PASS_") or status.startswith("BLOCKED_") else 1)


if __name__ == "__main__":
    main()
