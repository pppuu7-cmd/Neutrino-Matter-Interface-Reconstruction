import math
import sys
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
import audit_cerdeno_mass_support_only_0087c_r1 as m


def test_direct_signed_power_only():
    assert m.direct_power_r1("10⁻³")==-3
    assert m.direct_power_r1("10^-2")==-2
    assert m.direct_power_r1("10^2")==2
    assert m.direct_power_r1("10²")==2
    assert m.direct_power_r1("10 2") is None
    assert m.direct_power_r1("102") is None


def test_threat_disjoint_high_mass():
    r=m.base.threat([1e7,1e9])
    assert r["classification"]=="PROVABLY_MASS_DISJOINT"
    assert r["side"]=="above_target"
    assert r["separation_decades"]>6


def test_threat_overlap_endpoint_or_band():
    r=m.base.threat([1.0,1e8])
    assert r["classification"]=="MASS_OVERLAP_THREAT"
    assert r["overlap_interval_eV"][0]==1.0
    assert r["overlap_interval_eV"][1]>1.0


def test_linfit_exact_log_axis():
    a,b=m.base.linfit([10.0,20.0,30.0],[-2.0,-1.0,0.0])
    assert math.isclose(a,0.1,rel_tol=0,abs_tol=1e-12)
    assert math.isclose(b,-3.0,rel_tol=0,abs_tol=1e-12)
