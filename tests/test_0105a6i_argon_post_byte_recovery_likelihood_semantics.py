from scripts.audit_0105a6i_argon_post_byte_recovery_likelihood_semantics import audit


def fixture():
    measurement = r"""
    Analysis A uses an extended maximum likelihood implemented with RooFit.
    The fit uses reconstructed energy, F90, and t_{\rm trig}.
    Background nuisance parameters are profiled. The test statistic is -2 delta ln L.
    """
    release = r"""
    Signal and background probability distribution functions are provided as 3D binned arrays.
    Files include cevnspdf.txt, brnpdf.txt, delbrnpdf.txt, and bkgpdf.txt.
    An uncertainty value represents the width of a Gaussian constraint.
    Use provided binned data with appropriate likelihood procedure.
    Use systematics to run a set of alternative fits. Table 2 reports 3152 +/- 25.
    """
    return audit(measurement, release)


def test_guard_never_unlocks_observed_residual():
    r = fixture()
    assert r["observed_bsm_residual_permission_percent"] == 0


def test_release_choice_blocks_elementary_objective():
    r = fixture()
    assert r["evidence"]["release_appropriate_likelihood_procedure"] is True
    assert r["fields"]["F1_elementary_objective"]["status"] == "PARTIAL_OR_MISSING"


def test_binning_and_template_identity_can_close_independently():
    r = fixture()
    assert r["fields"]["F2_observables_support_binning_templates"]["status"] == "COMPLETE"


def test_missing_morphing_and_correlation_fail_closed():
    r = fixture()
    assert r["fields"]["F4_nuisance_template_coupling"]["status"] == "PARTIAL_OR_MISSING"
    assert r["fields"]["F6_systematic_combination_correlation"]["status"] == "PARTIAL_OR_MISSING"


def test_known_3152_vs_exact_yaml_3154_discrepancy_blocks_f7_and_fit_permission():
    r = fixture()
    assert r["fields"]["F7_numerical_anchors_reproduction_target"]["status"] == "PARTIAL_OR_MISSING"
    assert r["all_fields_complete"] is False
    assert r["classification"] == "BLOCKED_0105A6I_ARGON_LIKELIHOOD_IMPLEMENTATION_AUTHORITY_INCOMPLETE"
    assert r["sm_null_reproduction_permission_percent"] == 0
