import importlib.util
from pathlib import Path

P = Path(__file__).resolve().parents[1] / "scripts" / "audit_restricted_below_1eV_completeness_0087g.py"
spec = importlib.util.spec_from_file_location("g", P)
g = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)

def test_authoritative_blockers_force_blocked():
    r = g.classify()
    assert r["classification"] == "BLOCKED_RESTRICTED_BELOW_1EV_COMPLETENESS"
    assert set(r["unresolved_completeness_blockers"]) == {"cerdeno", "coherent", "fifth_force"}
    assert r["complete_allowed_region_certified"] is False
    assert r["global_external_envelope_certified"] is False
    assert r["bsm_response_unlock"] is False

def test_domain_is_restricted_below_one_ev():
    r = g.classify()
    assert r["domain_eV"]["min_inclusive"] == 6.845530367110015e-6
    assert r["domain_eV"]["max_exclusive"] == 1.0

def test_hypothetical_cleared_blockers_still_only_partial_pass():
    r = g.classify({})
    assert r["classification"] == "PASS_RESTRICTED_BELOW_1EV_PARTIAL_AUTHORITY_CERTIFICATION"
    assert r["complete_allowed_region_certified"] is False
    assert r["bsm_response_unlock"] is False

def test_no_blocker_is_treated_as_null():
    r = g.classify()
    assert r["blocked_family_as_null_assumption"] is False
    assert all(v.startswith("BLOCKED_") for v in r["unresolved_completeness_blockers"].values())
