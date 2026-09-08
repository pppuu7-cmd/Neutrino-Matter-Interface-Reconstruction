import importlib.util, math, pathlib

P = pathlib.Path(__file__).resolve().parents[1] / "scripts" / "audit_shin_yun_sn1987a_analytical_geometry_0084b.py"
spec = importlib.util.spec_from_file_location("m0084b", P)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_source_authority_patterns_on_source_style_tex():
    s = r"""
    \mathcal{L}=e^{\prime}A^{\prime}_{\mu}J^{\prime\mu}
    J^{\prime\mu}=\sum_{f=q,l}q_{f}^{\prime}\bar{f}\gamma^{\mu}f
    anomaly-free $\rm B-L$ current.
    e^{\prime}<10^{-11},\quad m_{\gamma^\prime}<20 {\rm MeV}.
    e^{\prime}>1.5\times10^{-8},\quad m_{\gamma^\prime}<2m_e.
    e^{\prime}m_{\gamma^\prime}<7.4\times10^{-10} {\rm MeV}.
    e^{\prime}m_{\gamma^\prime}>1.2\times10^{-5} {\rm MeV}.
    m_{\gamma^\prime}<1 {\rm MeV}.
    """
    a = m.source_authority(s)
    assert all(a.values()), a


def test_codata_two_me_is_not_rounded_one_mev():
    two = 2.0 * m.M_E_MEV
    assert math.isclose(two, 1.02199790138, rel_tol=0, abs_tol=1e-14)
    assert two != 1.0


def test_transverse_areas_both_variants():
    body = m.region("BODY_NATIVE", "T", 2.0 * m.M_E_MEV)
    concl = m.region("CONCLUSION_SUMMARY", "T", 1.0)
    assert body["polygon_valid_positive"] and body["agreement_within_1e-8"]
    assert concl["polygon_valid_positive"] and concl["agreement_within_1e-8"]
    assert body["analytic_area_decade2"] > concl["analytic_area_decade2"]
    assert math.isclose(concl["mass_width_decades"], 12.0, rel_tol=0, abs_tol=1e-12)


def test_longitudinal_ordering_and_area():
    r = m.region("BODY_NATIVE", "L", 2.0 * m.M_E_MEV)
    assert r["ordering_ok_at_both_endpoints"]
    assert r["polygon_valid_positive"]
    assert r["agreement_within_1e-8"]
    expected_width = math.log10(m.L_HIGH_PRODUCT_MEV / m.L_LOW_PRODUCT_MEV)
    assert math.isclose(r["analytic_area_decade2"], r["mass_width_decades"] * expected_width, rel_tol=1e-14)


def test_t_and_l_are_not_unionized():
    body_t = m.region("BODY_NATIVE", "T", 2.0 * m.M_E_MEV)
    body_l = m.region("BODY_NATIVE", "L", 2.0 * m.M_E_MEV)
    assert body_t["polarization"] == "T"
    assert body_l["polarization"] == "L"
    assert body_t["analytic_area_decade2"] != body_l["analytic_area_decade2"]
