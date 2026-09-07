import importlib.util
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "materialize_fayet_bl_asymptotic_0079a.py"
spec = importlib.util.spec_from_file_location("m0079a", SCRIPT)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_classification_passes():
    r = m.calculate()
    assert r["classification"] == "PASS_FIFTH_FORCE_B_L_ASYMPTOTIC_MATERIALIZATION"


def test_frozen_mapping_roundtrip():
    r = m.calculate()
    assert r["replication"]["relative_epsilon_roundtrip"] <= 1e-12
    assert 2.4e-25 <= r["result"]["g_BL_upper_2sigma"] <= 2.7e-25


def test_independent_decimal_replica():
    r = m.calculate()
    assert r["replication"]["relative_e_double_vs_decimal"] <= 1e-12
    assert r["replication"]["relative_g_double_vs_decimal"] <= 1e-12


def test_no_finite_mass_extrapolation():
    r = m.calculate()
    assert r["scope"].startswith("strict long-range/asymptotic")
    assert r["checks"]["finite_mass_contour_emitted"] is False
    assert "NOT a hard validity edge" in r["diagnostic_only"]["guard"]
