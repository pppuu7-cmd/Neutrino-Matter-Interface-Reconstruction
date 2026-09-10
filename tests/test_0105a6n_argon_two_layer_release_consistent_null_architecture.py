from scripts.audit_0105a6n_argon_two_layer_release_consistent_null_architecture import audit


def parent_fixture():
    return {
        "pages": [
            {"evidence_windows": {"F1": {"window": "analysis a extended binned maximum likelihood ln f xi cevns signal is profiled"}}},
            {"evidence_windows": {"F3": {"window": "gaussian constraint prompt brn delayed brn steady state profile likelihood cevns signal is profiled"}}},
            {"evidence_windows": {"F6": {"window": "systematic excursion pdf uncorrelated systematic errors added in quadrature stat only 3 9 stat syst 3 5"}}},
        ]
    }


def primary_measurement():
    return "extended maximum likelihood profile -2 Delta ln L"


def primary_release():
    return "3 dimensional binned arrays Gaussian constraint cevnspdf.txt brnpdf.txt delbrnpdf.txt bkgpdf.txt systematics are used in alternative fits 3152"


def test_full_frozen_architecture_can_pass_without_fit():
    r = audit(primary_measurement(), primary_release(), parent_fixture())
    assert r["all_architecture_fields_pass"] is True
    assert r["tierB_argon_null_preregistration_permission_percent"] == 100
    assert r["tierA_exact_sm_null_reproduction_permission_percent"] == 0
    assert r["observed_bsm_residual_permission_percent"] == 0
    assert r["numerical_fit_performed"] is False


def test_missing_alternative_fit_semantics_blocks_a3():
    r = audit(primary_measurement(), primary_release().replace("alternative fits", "shape files"), parent_fixture())
    assert r["architecture_fields"]["A3_shape_systematic_architecture"]["pass"] is False
    assert r["all_architecture_fields_pass"] is False


def test_missing_uncorrelated_excursion_semantics_blocks_a3():
    p = parent_fixture()
    p["pages"][2]["evidence_windows"]["F6"]["window"] = "systematic excursion pdf added in quadrature stat only 3 9 stat syst 3 5"
    r = audit(primary_measurement(), primary_release(), p)
    assert r["architecture_fields"]["A3_shape_systematic_architecture"]["pass"] is False


def test_single_steady_state_anchor_cannot_pass_conflict_containment():
    p = parent_fixture()
    for x in p["pages"]:
        for payload in x["evidence_windows"].values():
            payload["window"] = payload["window"].replace("3154", "")
    r = audit(primary_measurement(), primary_release(), p)
    assert r["architecture_fields"]["A5_dual_anchor_conflict_containment"]["pass"] is False


def test_authority_ceiling_never_promotes_secondary_to_release_authority():
    r = audit(primary_measurement(), primary_release(), parent_fixture())
    assert r["authority_separation"]["collaboration_release_authority_from_secondary_source"] is False
