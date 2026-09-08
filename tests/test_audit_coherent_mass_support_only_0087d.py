import math,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
import audit_coherent_mass_support_only_0087d as m

def test_direct_power_source_native_only():
    assert m.direct_power("10^-2")==-2
    assert m.direct_power("10^3")==3
    assert m.direct_power("10⁻²")==-2
    assert m.direct_power("10³")==3
    assert m.direct_power("103") is None
    assert m.direct_power("10 3") is None

def test_number_value():
    assert math.isclose(m.number_value("10^{-3}"),1e-3)
    assert math.isclose(m.number_value("2.5"),2.5)

def test_threat_high_mass_disjoint():
    r=m.threat([1e6,1e9])
    assert r["classification"]=="PROVABLY_MASS_DISJOINT"
    assert r["side"]=="above_target"

def test_threat_overlap():
    r=m.threat([1.0,1e6])
    assert r["classification"]=="MASS_OVERLAP_THREAT"
    assert r["overlap_interval_eV"][0]==1.0
