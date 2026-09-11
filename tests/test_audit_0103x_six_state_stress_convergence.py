import importlib.util
from pathlib import Path

P=Path(__file__).resolve().parents[1]/"scripts"/"audit_0103x_six_state_stress_convergence.py"
spec=importlib.util.spec_from_file_location("audit0103x",P)
mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)


def test_0103x_stress_convergence():
    r,_=mod.run_audit()
    assert r["status"]=="PASS_0103X_SIX_STATE_STRESS_CONVERGENCE_NONTERMINAL"
    assert all(r["gates"].values())
    assert r["metrics"]["scope"]=="NONTERMINAL_SYNTHETIC_NUMERICAL_STRESS_ONLY"
    assert r["metrics"]["max_1024_probability_error_vs_reference"]<=1e-6
    assert r["metrics"]["zero_g_max_antineutrino_leakage"]<=1e-12
