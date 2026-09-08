import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_fifth_force_finite_mass_support_0087e.py"
OUT = ROOT / "fifth_force_finite_mass_support_0087e.json"


def run_gate():
    cp = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True, capture_output=True, text=True)
    return json.loads(OUT.read_text()), cp


def test_exact_primary_hashes_are_frozen_and_match_0079_authority():
    result, _ = run_gate()
    assert result["source_provenance"]["exact_hashes_match_validated_0079_ledger"] is True
    assert result["source_provenance"]["exact_primary_source_sha256"]["1809.04991v2"] == "ed233fa73a149ba9801d442339a2c5fd3b5051c1dc2caa1584a000760fcff29b"
    assert result["source_provenance"]["exact_primary_source_sha256"]["1712.00856v2"] == "e058c6338db1151bf631a2c2c5eb09102cb521327227ff5288570e51744cc03d"


def test_no_allowed_route_has_two_finite_endpoints():
    result, _ = run_gate()
    assert result["routes"]["A_explicit_finite_mass_interval"]["pass"] is False
    assert result["routes"]["B_explicit_finite_force_range_interval"]["pass"] is False
    assert result["routes"]["C_source_explicit_yukawa_response_and_domain"]["yukawa_formula_present"] is True
    assert result["routes"]["C_source_explicit_yukawa_response_and_domain"]["pass"] is False


def test_classification_is_blocked_and_forbidden_cutoffs_unused():
    result, _ = run_gate()
    assert result["classification"] == "BLOCKED_FIFTH_FORCE_FINITE_MASS_SUPPORT_AUTHORITY"
    assert result["passing_routes"] == []
    assert result["threat_comparison"] == "UNRESOLVED_MASS_SUPPORT_THREAT"
    assert all(result["guards"].values()) is False  # bsm_response_scan_authorized is intentionally False
    assert result["guards"]["earth_radius_or_diameter_not_used_as_endpoint"] is True
    assert result["guards"]["orbital_altitude_not_used_as_endpoint"] is True
    assert result["guards"]["arbitrary_yukawa_suppression_threshold_not_used"] is True
    assert result["guards"]["bsm_response_scan_authorized"] is False
