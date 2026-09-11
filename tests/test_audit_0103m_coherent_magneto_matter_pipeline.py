import importlib.util
from pathlib import Path

P=Path(__file__).resolve().parents[1]/"scripts"/"audit_0103m_coherent_magneto_matter_pipeline.py"
spec=importlib.util.spec_from_file_location("audit0103m",P)
mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)


def test_0103m_coherent_synthetic_pipeline():
    r,_=mod.run_audit()
    assert r["status"]=="PASS_0103M_COHERENT_SYNTHETIC_MAGNETO_MATTER_PIPELINE_NONTERMINAL"
    assert all(r["gates"].values())
    assert r["metrics"]["scope"]=="NONTERMINAL_SYNTHETIC_ENGINEERING_ONLY"
    assert r["metrics"]["max_trilinear_interpolation_residual"]<=1e-12
    assert r["metrics"]["zero_g_antineutrino_leakage"]<=1e-12
    assert r["metrics"]["positive_control_antineutrino_probability"]>1e-8
