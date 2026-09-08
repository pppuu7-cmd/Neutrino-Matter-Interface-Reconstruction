import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from g9_ccsn_actionability_0094 import AU_M, evaluate


def parent():
    fams=[]
    for i in range(18):
        fams.append({
            "control_index": i//6,
            "receiver_m": [1.0,10.0,100.0][(i//2)%3],
            "source_radius_km": [21.0,100.0][i%2],
            "d_zero_m": 665_000_000.0 + i,
            "z_au": 24.0,
        })
    return {"status":"BLOCKED_G9_CCSN_ALIGNMENT_TOPOLOGY","families":fams,"sampled_reentry_count_total":39}


def test_beta_mapping():
    r=evaluate(parent())
    expected=max((665_000_000.0+i)/(24.0*AU_M) for i in range(18))
    assert math.isclose(r["beta_zero_max_rad"], expected, rel_tol=0, abs_tol=1e-18)


def test_scoped_actionability_fail_under_frozen_authorities():
    r=evaluate(parent())
    assert r["status"] == "SCIENTIFIC_FAIL_G9_CCSN_PROSPECTIVE_ACTIONABILITY_V1"
    assert r["prompt_to_beta_zero_ratio"] > 100
    assert 0 < r["isotropic_cap_control_only"] < 1e-6


def test_parent_topology_is_required():
    p=parent(); p["status"]="PASS_G9_CCSN_ALIGNMENT_FOOTPRINT_EXPANDED"
    try:
        evaluate(p)
    except ValueError:
        return
    raise AssertionError("unexpected parent status accepted")
