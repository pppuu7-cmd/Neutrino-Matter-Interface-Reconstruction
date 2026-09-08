import math,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
import audit_coherent_mass_support_only_0087d_r1 as m


def test_direct_power_source_native_only():
    assert m.base.direct_power("10^-2")==-2
    assert m.base.direct_power("10^3")==3
    assert m.base.direct_power("10⁻²")==-2
    assert m.base.direct_power("10³")==3
    assert m.base.direct_power("103") is None
    assert m.base.direct_power("10 3") is None


def test_number_value():
    assert math.isclose(m.base.number_value("10^{-3}"),1e-3)
    assert math.isclose(m.base.number_value("2.5"),2.5)


def test_threat_high_mass_disjoint():
    r=m.base.threat([1e6,1e9])
    assert r["classification"]=="PROVABLY_MASS_DISJOINT"
    assert r["side"]=="above_target"


def test_threat_overlap():
    r=m.base.threat([1.0,1e6])
    assert r["classification"]=="MASS_OVERLAP_THREAT"
    assert r["overlap_interval_eV"][0]==1.0


def test_starred_includegraphics_is_resolved():
    tex=[("main.tex", r'''\begin{figure*}
\includegraphics*[width=.7\linewidth]{Coherent_Results_B-L.pdf}
\caption{Excluded regions in the $M_{Z'}-g_{Z'}$ plane for the $B-L$ model.}
\end{figure*}''')]
    members={"Coherent_Results_B-L.pdf":b"dummy"}
    r=m.figure_candidates_r1(tex,members)
    assert len(r)==1
    assert r[0]["resolved"]=="Coherent_Results_B-L.pdf"
