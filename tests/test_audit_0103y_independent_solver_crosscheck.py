import importlib.util
from pathlib import Path
P=Path(__file__).resolve().parents[1]/"scripts"/"audit_0103y_independent_solver_crosscheck.py"
spec=importlib.util.spec_from_file_location("audit0103y",P); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
def test_0103y_independent_solver_crosscheck():
    r=mod.run_audit()
    assert r["status"]=="PASS_0103Y_INDEPENDENT_SOLVER_CROSSCHECK_NONTERMINAL"
    assert all(r["gates"].values())
    assert r["metrics"]["max_probability_linf"]<=5e-6
