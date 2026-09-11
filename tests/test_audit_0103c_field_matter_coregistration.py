import importlib.util
from pathlib import Path

P=Path(__file__).resolve().parents[1]/"scripts"/"audit_0103c_field_matter_coregistration.py"
spec=importlib.util.spec_from_file_location("audit0103c",P)
mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)


def test_0103c_expected_scientific_block():
    r=mod.run_audit()
    assert r["status"]=="PASS_0103C_CLASSIFICATION_EXPECTED_BLOCK"
    assert r["terminal_status"]=="BLOCKED_0103_BETELGEUSE_COHERENT_MAGNETO_MATTER_STATE_AUTHORITY"
    assert r["terminal_admissible"] is False
    assert r["current_combination_class"]=="MIXED_MODEL_ROBUSTNESS_ONLY"
    assert all(r["gates"].values())
