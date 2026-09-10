import inspect

import scripts.audit_0105a6q_argon_systematic_excursion_semantics_preflight_v2 as m


def test_scope_and_parent_ids_are_frozen():
    assert m.PREREG_COMMIT == "5fe9c78d674d8eacf42d834d69ebb3ed19866e31"
    assert (m.PAGE_FIRST, m.PAGE_LAST) == (154, 158)
    assert m.MAX_WINDOW == 700
    assert m.A6M_EXTRACTION_CLASSIFICATION == "EVIDENCE_EXTRACTED_FOR_0105A6M_MANUAL_SEMANTIC_ADJUDICATION"


def test_known_method_closes_q1_q2_q7_q8_but_not_unspecified_laws():
    pages = {
        154: (
            "likelihood fit systematic errors are computed by first generating alternative 1 excursion pdfs "
            "for each systematic then pseudo data sets are generated using the excursion pdf and fit with the "
            "central value pdfs a set of 10000 pseudo data sets are fit for each systematic excursion study "
            "the average difference between the mean best fit value from the excursion pdf and the central value "
            "for a 1 pair of excursion pdfs computes the systematic error from that source the excursion method "
            "computes uncorrelated systematic errors"
        ),
        155: "brn timing mean brn timing width brn energy cevns f90 cevns timing mean",
        156: "systematic source discussion",
        157: "best fit cevns rate 159 43 stat 14 syst statistical and systematic errors are added in quadrature",
        158: "final significance 3.5 stat syst",
    }
    status, details, _ = m.field_evidence(pages)
    assert status["Q1"] == "COMPLETE"
    assert status["Q2"] == "COMPLETE"
    assert status["Q7"] == "COMPLETE"
    assert status["Q8"] == "COMPLETE"
    assert status["Q3"] == "MISSING_OR_PARTIAL"
    assert status["Q4"] == "MISSING_OR_PARTIAL"
    assert status["Q5"] == "MISSING_OR_PARTIAL"
    assert status["Q6"] == "MISSING_OR_PARTIAL"
    assert details["Q3_generation_law_markers"] == {"poisson": False, "fixed": False, "other": False}


def test_q3_requires_explicit_pseudo_count_law_not_extended_likelihood_word():
    pages = {154: "an extended likelihood is used and pseudo data sets are generated", 155: "", 156: "", 157: "", 158: ""}
    status, _, _ = m.field_evidence(pages)
    assert status["Q3"] == "MISSING_OR_PARTIAL"
    pages[154] += " pseudo data event counts are poisson fluctuated"
    status, _, _ = m.field_evidence(pages)
    assert status["Q3"] == "COMPLETE"


def test_q4_requires_explicit_sign_or_absolute_operation():
    base = {154: "average difference for a pair of excursion pdfs", 155: "", 156: "", 157: "", 158: ""}
    status, _, _ = m.field_evidence(base)
    assert status["Q4"] == "MISSING_OR_PARTIAL"
    base[154] += " average absolute excursion difference"
    status, _, _ = m.field_evidence(base)
    assert status["Q4"] == "COMPLETE"


def test_q5_requires_explicit_one_sided_treatment():
    pages = {154: "brn timing width systematic and cevns timing mean systematic", 155: "", 156: "", 157: "", 158: ""}
    status, _, _ = m.field_evidence(pages)
    assert status["Q5"] == "MISSING_OR_PARTIAL"
    pages[154] += " the single excursion systematic is compared with the central value"
    status, _, _ = m.field_evidence(pages)
    assert status["Q5"] == "COMPLETE"


def test_no_pseudodata_likelihood_or_residual_execution_in_auditor():
    source = inspect.getsource(m.run)
    assert '"pseudo_data_generated": False' in source
    assert '"likelihood_evaluated": False' in source
    assert '"observed_bsm_residual_permission_percent": 0' in source
    assert '"observed_bsm_residual_inspected": False' in source
