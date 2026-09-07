from scripts.audit_esseili_kribs_bbn_semantics_0081 import classify_text, extract_bound, extract_cl


ABS_FIXTURE = r'''
\includegraphics{Presentation/CnstrntPlotMajoranaYp.pdf}
\caption{$\Delta Y_p$ contours for ``Majorana'' neutrino case. A conservative upper bound is $\Delta Y_p \lesssim 0.008$ at 95\% C.L.}
\includegraphics{Presentation/CnstrntPlotDiracYp.pdf}
\caption{Same as Fig. 7, but for the ``Dirac'' neutrino case.}
We define the BSM deviation of helium abundance as $\Delta Y_p \equiv \left|Y_p^{\rm BSM}-Y_p^{\rm SM}\right|$.
'''

SIGNED_FIXTURE = ABS_FIXTURE.replace(
    r"\left|Y_p^{\rm BSM}-Y_p^{\rm SM}\right|",
    r"Y_p^{\rm BSM}-Y_p^{\rm SM}",
)

EXACT_SOURCE_STYLE_FIXTURE = r'''
\includegraphics[width=1.0\textwidth]{Presentation/CnstrntPlotMajoranaYp.pdf}
\caption{$\Delta Y_p$ contours for ``Majorana'' neutrino case. A conservative upper bound is $\Delta Y_p = 0.008$ at $95\%$ C.L.}
\includegraphics[width=1.0\textwidth]{Presentation/CnstrntPlotDiracYp.pdf}
\caption{Same as figure 7, but for the ``Dirac'' neutrino case.}
We define the BSM deviation of helium
abundance as
\begin{equation}
\label{DeltaYpEqn}
\Delta Y_p = Y_p\vert^{\text{equation } \ref{YpEqn}}_{\text{BSM}}-Y_p\vert^{\text{equation } \ref{YpEqn}}_{\text{SM}}.
\end{equation}
In accordance with the discussion, a conservative upper bound is $\Delta Y_p= 0.008$ at $95\%$ C.L\@.
'''


def test_absolute_fixture_passes_and_recovers_semantics():
    r = classify_text(ABS_FIXTURE)
    assert r["classification"] == "PASS_COSMOLOGY_B_L_BBN_OBSERVATIONAL_SEMANTICS"
    assert r["frozen_source_result"]["delta_Yp_upper_bound"] == 0.008
    assert r["frozen_source_result"]["confidence_level_percent"] == 95
    assert r["frozen_source_result"]["delta_Yp_definition_kind"] == "absolute_difference"
    assert r["frozen_source_result"]["delta_Yp_uses_absolute_deviation"] is True
    assert all(r["checks"].values())


def test_signed_bsm_minus_sm_fixture_also_passes_frozen_contract():
    r = classify_text(SIGNED_FIXTURE)
    assert r["classification"] == "PASS_COSMOLOGY_B_L_BBN_OBSERVATIONAL_SEMANTICS"
    assert r["frozen_source_result"]["delta_Yp_definition_kind"] == "signed_BSM_minus_SM"
    assert r["frozen_source_result"]["delta_Yp_uses_absolute_deviation"] is False
    assert r["checks"]["delta_yp_sign_or_absolute_convention_recovered"] is True


def test_exact_source_style_tex_passes_without_contract_change():
    r = classify_text(EXACT_SOURCE_STYLE_FIXTURE)
    assert r["classification"] == "PASS_COSMOLOGY_B_L_BBN_OBSERVATIONAL_SEMANTICS"
    assert r["frozen_source_result"]["delta_Yp_upper_bound"] == 0.008
    assert r["frozen_source_result"]["confidence_level_percent"] == 95
    assert r["frozen_source_result"]["delta_Yp_definition_kind"] == "signed_BSM_minus_SM"
    assert r["frozen_source_result"]["delta_Yp_uses_absolute_deviation"] is False
    assert all(r["checks"].values())


def test_tex_bound_and_cl_parser():
    ctx = r"a conservative upper bound is $\dYp \lesssim 0.008$ at 95\% C.L."
    assert extract_bound(ctx) == 0.008
    assert extract_cl(ctx) == 95
    exact = r"a conservative upper bound is $\Delta Y_p=0.008$ at $95\%$ C.L\@."
    assert extract_bound(exact) == 0.008
    assert extract_cl(exact) == 95


def test_missing_sign_or_absolute_definition_cannot_be_full_pass():
    text = ABS_FIXTURE.replace(
        r"\Delta Y_p \equiv \left|Y_p^{\rm BSM}-Y_p^{\rm SM}\right|",
        r"\Delta Y_p \equiv f(Y_p^{\rm BSM},Y_p^{\rm SM})",
    )
    r = classify_text(text)
    assert r["classification"] == "PARTIAL_PASS_BBN_THRESHOLD_ONLY"
    assert r["checks"]["delta_yp_sign_or_absolute_convention_recovered"] is False


def test_cmb_only_threshold_does_not_pass_bbn_semantics():
    text = ABS_FIXTURE.replace(
        r"A conservative upper bound is $\Delta Y_p \lesssim 0.008$ at 95\% C.L.",
        r"Current CMB constraints give $\Delta N_{\rm eff}\lesssim0.4$ at 95\% C.L."
    )
    r = classify_text(text)
    assert r["classification"].startswith("BLOCKED")
