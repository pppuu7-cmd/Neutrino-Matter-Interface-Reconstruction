#!/usr/bin/env python3
"""Hosted fail-closed benchmark for NMIR iteration 0074a."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import sys

from nmir.coherent_argon_sm_0074a import calculate_events, load_efficiency

EXPECTED_EFF_SHA256 = "21ce25451c1ed552752ff4a22496deab3ff5dba178bf360813eaff1d25be89e2"
TARGET = 128.0
TOLERANCE = 17.0
MAX_REFINEMENT_FRACTION = 0.005


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def math_is_finite_nonnegative(x: float) -> bool:
    import math
    return math.isfinite(x) and x >= 0.0


def main() -> int:
    root = Path(os.environ.get("NMIR_0074_INPUT", "artifacts/coherent_0074"))
    eff_path = root / "argon_analysis_a" / "CENNS10AnlAEfficiency.txt"
    if not eff_path.exists():
        raise FileNotFoundError(eff_path)
    actual_hash = sha256(eff_path)
    if actual_hash != EXPECTED_EFF_SHA256:
        raise RuntimeError(f"efficiency SHA256 mismatch: {actual_hash}")

    eff = load_efficiency(eff_path)
    coarse = calculate_events(eff, n_t=2000)
    fine = calculate_events(eff, n_t=8000)
    no_eff = calculate_events(eff, n_t=4000, apply_efficiency=False)
    no_ff = calculate_events(eff, n_t=4000, form_factor=False)

    refinement = abs(fine["total"] - coarse["total"]) / fine["total"]
    checks = {
        "within_frozen_128_pm_17": abs(fine["total"] - TARGET) <= TOLERANCE,
        "refinement_le_0p5pct": refinement <= MAX_REFINEMENT_FRACTION,
        "all_flavors_finite_nonnegative": all(
            math_is_finite_nonnegative(fine[k]) for k in ("numu_prompt", "nue", "numubar")
        ),
        "disable_efficiency_not_lower": no_eff["total"] >= fine["total"],
        "F_equal_1_not_lower": no_ff["total"] >= fine["total"],
    }
    passed = all(checks.values())
    classification = (
        "PASS_COHERENT_AR_SM_NORMALIZATION_BENCHMARK"
        if passed
        else "SCIENTIFIC_FAIL_COHERENT_AR_SM_NORMALIZATION_BENCHMARK"
    )
    result = {
        "schema": "nmir.coherent_argon_sm_0074a.v1",
        "classification": classification,
        "frozen_target_events": TARGET,
        "frozen_tolerance_events": TOLERANCE,
        "efficiency_sha256": actual_hash,
        "coarse_n_t": 2000,
        "fine_n_t": 8000,
        "coarse_events": coarse,
        "fine_events": fine,
        "refinement_fraction": refinement,
        "no_efficiency_total_events": no_eff["total"],
        "unit_form_factor_total_events": no_ff["total"],
        "checks": checks,
        "guards": {
            "release_cevnspdf_used_as_answer": False,
            "bestfit_159_used_as_target": False,
            "b_minus_l_scan_performed": False,
        },
    }
    out = Path(os.environ.get("NMIR_0074A_RESULT", "artifacts/coherent_0074a/result.json"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(out.read_text(), end="")
    return 0 if passed else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"NMIR_0074A_INFRASTRUCTURE_FAIL: {exc}", file=sys.stderr)
        raise
