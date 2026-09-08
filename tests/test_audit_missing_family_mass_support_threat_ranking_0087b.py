import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import audit_missing_family_mass_support_threat_ranking_0087b as m


def test_disjoint_above_target():
    r=m.classify_interval([1e7,1e9],[1e-5,2.0])
    assert r["classification"]=="PROVABLY_MASS_DISJOINT"
    assert r["side"]=="above_target"
    assert r["separation_decades"] > 6.0


def test_overlap_endpoint_contact_is_threat():
    r=m.classify_interval([1.0,1e8],[1e-5,1.0])
    assert r["classification"]=="MASS_OVERLAP_THREAT"
    assert r["endpoint_contact_only"] is True


def test_unresolved_stays_threat():
    r=m.classify_interval(None,[1e-5,1.0])
    assert r=={"classification":"UNRESOLVED_MASS_SUPPORT_THREAT"}


def test_positive_interval_validation():
    try:
        m.classify_interval([0.0,1.0],[1e-5,1.0])
    except ValueError:
        pass
    else:
        raise AssertionError("nonpositive support must fail")
