import importlib.util
from pathlib import Path
P=Path(__file__).resolve().parents[1]/"scripts"/"audit_0103q_coherent_state_ingest_rejection.py"
spec=importlib.util.spec_from_file_location("audit0103q",P); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)

def test_0103q_fail_closed_ingest():
    r=mod.run_audit()
    assert r["status"]=="PASS_0103Q_COHERENT_STATE_INGEST_REJECTION_NONTERMINAL"
    assert all(r["gates"].values())
    assert r["corrupted_cases_reaching_propagation"]==0
    assert len(r["negative_cases"])==12
