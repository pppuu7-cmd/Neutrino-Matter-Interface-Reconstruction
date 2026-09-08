#!/usr/bin/env python3
"""NMIR 0087e: fifth-force finite-mass support authority audit.

This gate deliberately consumes the already validated 0079 primary-source
classification ledger for the exact Fayet/MICROSCOPE source bytes.  It does
not infer a finite cutoff from Earth/satellite dimensions or a chosen Yukawa
suppression threshold.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "data" / "fayet_fifth_force_authority_classification_0079.json"
OUT = ROOT / "fifth_force_finite_mass_support_0087e.json"

EXPECTED = {
    "1809.04991v2": "ed233fa73a149ba9801d442339a2c5fd3b5051c1dc2caa1584a000760fcff29b",
    "1712.00856v2": "e058c6338db1151bf631a2c2c5eb09102cb521327227ff5288570e51744cc03d",
}
TARGET = [6.845530367110015e-6, 1.4057345497828417]  # eV


def main() -> int:
    ledger = json.loads(LEDGER.read_text())
    sources = {s["id"].replace("arXiv:", ""): s for s in ledger["primary_sources"]}

    exact_hashes_match = all(
        sid in sources and sources[sid].get("sha256") == sha
        for sid, sha in EXPECTED.items()
    )

    later = sources["1809.04991v2"]["facts"]
    earlier = sources["1712.00856v2"]["facts"]

    # Frozen Route A: neither primary ledger records both finite positive
    # mediator-mass endpoints for the MICROSCOPE B-L constraint.
    route_a = False

    # Frozen Route B: the accepted range semantics explicitly state that no
    # exact numerical finite-range contour/table sufficient for materializing
    # both endpoints was identified.
    route_b = False

    # Frozen Route C: a Yukawa potential is present in the companion source,
    # but the source-defined finite experimental domain required to establish
    # both endpoints is absent.  Qualitative Earth-diameter / altitude wording
    # is not promoted to an endpoint.
    yukawa_formula_present = "exp(-r/lambda_U)" in earlier.get("yukawa_potential", "")
    finite_curve_available = bool(ledger["resolution"].get("finite_range_curve_available"))
    finite_range_text_blocks_materialization = (
        "No exact numerical finite-range contour/table" in earlier.get("finite_range_authority", "")
    )
    route_c = bool(yukawa_formula_present and finite_curve_available and not finite_range_text_blocks_materialization)

    passing = [name for name, ok in (("A", route_a), ("B", route_b), ("C", route_c)) if ok]
    classification = (
        "PASS_FIFTH_FORCE_FINITE_MASS_SUPPORT_AUTHORITY"
        if passing
        else "BLOCKED_FIFTH_FORCE_FINITE_MASS_SUPPORT_AUTHORITY"
    )

    result = {
        "iteration": "0087e",
        "classification": classification,
        "scope": "Fayet/MICROSCOPE primary finite-mass support authority only; no coupling-side geometry",
        "source_provenance": {
            "authority_ledger": str(LEDGER.relative_to(ROOT)),
            "authority_ledger_sha256": hashlib.sha256(LEDGER.read_bytes()).hexdigest(),
            "exact_primary_source_sha256": EXPECTED,
            "exact_hashes_match_validated_0079_ledger": exact_hashes_match,
        },
        "frozen_target_eV": TARGET,
        "routes": {
            "A_explicit_finite_mass_interval": {"pass": route_a, "reason": "no source-explicit pair of finite positive mediator-mass endpoints"},
            "B_explicit_finite_force_range_interval": {"pass": route_b, "reason": "no source-explicit pair of finite positive force-range endpoints"},
            "C_source_explicit_yukawa_response_and_domain": {
                "pass": route_c,
                "yukawa_formula_present": yukawa_formula_present,
                "finite_range_curve_available": finite_curve_available,
                "reason": "Yukawa form exists, but no experiment-defined finite domain with both endpoints; qualitative Earth/altitude scales are forbidden cutoffs",
            },
        },
        "passing_routes": passing,
        "threat_comparison": "UNRESOLVED_MASS_SUPPORT_THREAT" if not passing else "REQUIRES_INTERVAL_COMPARISON",
        "guards": {
            "earth_radius_or_diameter_not_used_as_endpoint": True,
            "orbital_altitude_not_used_as_endpoint": True,
            "arbitrary_yukawa_suppression_threshold_not_used": True,
            "asymptotic_bound_unchanged": True,
            "bsm_response_scan_authorized": False,
        },
        "next_action": "move to localized BBN-tail actionability gate" if not passing else "preregister separate coupling-side geometry gate only if target overlap is certified",
    }

    if not exact_hashes_match:
        result["classification"] = "INFRASTRUCTURE_FAIL_PRIMARY_HASH_MISMATCH"
        result["next_action"] = "stop; restore exact validated Fayet source provenance"

    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    print("output_sha256", hashlib.sha256(OUT.read_bytes()).hexdigest())
    return 0 if result["classification"].startswith(("PASS_", "BLOCKED_")) else 2


if __name__ == "__main__":
    raise SystemExit(main())
