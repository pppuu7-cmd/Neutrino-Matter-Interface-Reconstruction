from scripts.audit_esseili_kribs_bbn_semantics_0081 import classify_text, extract_bound, extract_cl


FIXTURE = r'''
\includegraphics{Presentation/CnstrntPlotMajoranaYp.pdf}
\caption{$\Delta Y_p$ contours for ``Majorana'' neutrino case. A conservative upper bound is $\Delta Y_p \lesssim 0.008$ at 95\% C.L.}
\includegraphics{Presentation/CnstrntPlotDiracYp.pdf}
\caption{Same as Fig. 7, but for the ``Dirac'' neutrino case.}
We define the BSM deviation of helium abundance as $\Delta Y_p \equiv \left|Y_p-Y_p^{\rm SM}\right|$.
'''


def test_frozen_fixture_passes_and_recovers_exact_semantics():
    r = classify_text(FIXTURE)
    assert r["classification"] == "PASS_COSMOLOGY_B_L_BBN_OBSERVATIONAL_SEMANTICS"
    assert r["frozen_source_result"]["delta_Yp_upper_bound"] == 0.008
    assert r["frozen_source_result"]["confidence_level_percent"] == 95
    assert r["frozen_source_result"]["delta_Yp_uses_absolute_deviation"] is True
    assert all(r["checks"].values())


def test_tex_bound_and_cl_parser():
    ctx = r"a conservative upper bound is $\dYp \lesssim 0.008$ at 95\% C.L."
    assert extract_bound(ctx) == 0.008
    assert extract_cl(ctx) == 95


def test_missing_absolute_value_cannot_be_full_pass():
    text = FIXTURE.replace(r"\left|Y_p-Y_p^{\rm SM}\right|", r"Y_p-Y_p^{\rm SM}")
    r = classify_text(text)
    assert r["classification"] == "PARTIAL_PASS_BBN_THRESHOLD_ONLY"
    assert r["checks"]["absolute_value_convention_recovered"] is False


def test_cmb_only_threshold_does_not_pass_bbn_semantics():
    text = FIXTURE.replace(
        r"A conservative upper bound is $\Delta Y_p \lesssim 0.008$ at 95\% C.L.",
        r"Current CMB constraints give $\Delta N_{\rm eff}\lesssim0.4$ at 95\% C.L."
    )
    r = classify_text(text)
    assert r["classification"].startswith("BLOCKED")
