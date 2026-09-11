import importlib.util
from pathlib import Path

P=Path(__file__).resolve().parents[1]/"scripts"/"audit_0103e_end_to_end_surrogate_spin_flavor.py"
spec=importlib.util.spec_from_file_location("audit0103e",P)
mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)


def test_0103e_end_to_end_surrogate():
    r=mod.run_audit()
    assert r["status"]=="PASS_0103E_END_TO_END_INTERFACE_NONPHYSICAL"
    assert all(r["gates"].values())
    assert r["metrics"]["scope"]=="NONPHYSICAL_INTERFACE_ONLY"
    assert r["metrics"]["zero_g_antineutrino_leakage"]<=1e-13
    assert r["metrics"]["positive_control_antineutrino_probability"]>1e-6
