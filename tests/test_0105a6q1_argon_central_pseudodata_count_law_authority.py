import inspect

import scripts.audit_0105a6q1_argon_central_pseudodata_count_law_authority as m


def scoped(p152, p153=""):
    return {152: p152, 153: p153}


def test_scope_and_parent_are_frozen():
    assert m.PREREG_COMMIT == "268d7acb9d42e70fc6fe1fbf5d299df3ce1d8f64"
    assert m.PARENT_Q_RESULT_SHA256 == "a996df0b6f9d12f03d1fc57cc3d69f13d1b941e3771eb99be9877510d34e6884"
    assert (m.PAGE_FIRST, m.PAGE_LAST) == (152, 153)
    assert m.MAX_WINDOW == 900


def test_generated_from_pdf_and_extended_alone_do_not_close_q3():
    detected, classification, _ = m.classify_count_law(scoped(
        "pseudo data sets are generated from the central value pdfs and an extended binned maximum likelihood is used"
    ))
    assert detected == "NONE"
    assert classification == "BLOCKED_0105A6Q1_PSEUDODATA_COUNT_LAW_NOT_EXPLICIT"


def test_explicit_poisson_count_law_closes_q3p():
    detected, classification, details = m.classify_count_law(scoped(
        "for each pseudo data set the number of events is poisson fluctuated around the expected event count"
    ))
    assert detected == "Q3-P"
    assert classification == "PASS_0105A6Q1_EXPLICIT_PSEUDODATA_COUNT_LAW_SECONDARY_AUTHORITY_NONDISCOVERY"
    assert any(details["poisson_markers"].values())


def test_explicit_fixed_total_closes_q3f():
    detected, classification, _ = m.classify_count_law(scoped(
        "the pseudo data sample uses a fixed total number of events and event coordinates are drawn from the pdf"
    ))
    assert detected == "Q3-F"
    assert classification.startswith("PASS_")


def test_conflicting_laws_fail_closed():
    detected, classification, _ = m.classify_count_law(scoped(
        "pseudo data event counts are poisson fluctuated; another instruction says the pseudo data use a fixed total number of events"
    ))
    assert detected == "CONFLICT"
    assert classification == "BLOCKED_0105A6Q1_CONFLICTING_PSEUDODATA_COUNT_LAW_AUTHORITY"


def test_run_has_no_mc_likelihood_or_residual_path():
    source = inspect.getsource(m.run)
    assert '"systematic_monte_carlo_execution_permission_percent": 0' in source
    assert '"pseudo_data_generated": False' in source
    assert '"likelihood_evaluated": False' in source
    assert '"observed_bsm_residual_permission_percent": 0' in source
    assert '"observed_bsm_residual_inspected": False' in source
