import importlib.util
from pathlib import Path
P=Path(__file__).resolve().parents[1]/"scripts"/"audit_0103z_rephasing_covariance.py"
spec=importlib.util.spec_from_file_location("audit0103z",P); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
def test_0103z_rephasing_covariance():
    r=mod.run_audit()
    assert r["status"]=="PASS_0103Z_SIX_STATE_REPHASING_COVARIANCE_NONTERMINAL"
    assert all(r["gates"].values())
    assert r["metrics"]["max_probability_residual"]<=2e-12
