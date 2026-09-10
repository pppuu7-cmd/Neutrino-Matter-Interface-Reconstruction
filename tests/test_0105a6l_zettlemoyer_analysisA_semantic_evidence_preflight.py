from scripts.audit_0105a6l_zettlemoyer_analysisA_semantic_evidence_preflight import (
    FIRST_PAGE,
    LAST_PAGE,
    classify_page,
    exact_decimal_token,
    normalize,
)


def test_scope_is_exactly_frozen_30_pages():
    assert FIRST_PAGE == 129
    assert LAST_PAGE == 158
    assert LAST_PAGE - FIRST_PAGE + 1 == 30


def test_roofit_alone_cannot_close_f1():
    e = classify_page(normalize("Analysis A uses RooFit for the fit."))
    assert e["L0"]["candidate"] is True
    assert e["F1"]["candidate"] is False


def test_explicit_extended_likelihood_is_f1_candidate_only():
    e = classify_page(normalize("Analysis A likelihood used an extended maximum likelihood construction."))
    assert e["F1"]["candidate"] is True


def test_f3_requires_nuisance_marker_and_two_components():
    e = classify_page(normalize("The CEvNS yield was floated while the steady state background had a Gaussian constraint."))
    assert e["F3"]["candidate"] is True
    e2 = classify_page(normalize("The CEvNS yield was floated."))
    assert e2["F3"]["candidate"] is False


def test_f4_requires_coupling_not_just_systematic_templates():
    e = classify_page(normalize("Systematic templates were provided at plus and minus one sigma."))
    assert e["F4"]["candidate"] is False
    e2 = classify_page(normalize("A systematic template variation was interpolated between shapes."))
    assert e2["F4"]["candidate"] is True


def test_f7_number_presence_is_not_precedence():
    e = classify_page(normalize("The steady state normalization is 3154 in the fit table."))
    assert e["F7"]["has_3154"] is True
    assert e["F7"]["candidate_discrepancy_resolution"] is False
    e2 = classify_page(normalize("The table value 3152 is corrected and should be used instead of 3154."))
    assert e2["F7"]["candidate_discrepancy_resolution"] is True


def test_decimal_token_does_not_match_longer_number():
    n = normalize("values 13152 and 31540 are unrelated")
    assert exact_decimal_token(n, "3152") is False
    assert exact_decimal_token(n, "3154") is False
