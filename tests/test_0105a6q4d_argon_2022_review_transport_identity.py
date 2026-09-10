from scripts.audit_0105a6q4d_argon_2022_review_transport_identity import (
    URL,
    classify,
    verify_initial_url,
)


def test_frozen_url_is_exactly_valid():
    verify_initial_url(URL)


def test_exact_url_no_redirect_passes():
    assert classify(URL, [], True) == "PASS_0105A6Q4D_EXACT_URL_IDENTITY_CONFIRMED"


def test_same_provider_redirect_is_nondiscovery_pass():
    chain = [{
        "source_url": URL,
        "status": 302,
        "location": "/event/978288/files/review.pdf",
        "resolved_destination_url": "https://indico.cern.ch/event/978288/files/review.pdf",
    }]
    assert classify(
        "https://indico.cern.ch/event/978288/files/review.pdf", chain, True
    ) == "PASS_0105A6Q4D_INDICO_REDIRECT_CHAIN_RECORDED_NONDISCOVERY"


def test_cross_provider_redirect_remains_blocked():
    chain = [{
        "source_url": URL,
        "status": 302,
        "location": "https://example.org/review.pdf",
        "resolved_destination_url": "https://example.org/review.pdf",
    }]
    assert classify(
        "https://example.org/review.pdf", chain, True
    ) == "BLOCKED_0105A6Q4D_CROSS_PROVIDER_REDIRECT_REQUIRES_SEPARATE_AUTHORITY_BINDING"


def test_non_pdf_payload_is_blocked():
    assert classify(URL, [], False) == "BLOCKED_0105A6Q4D_TRANSPORT_DIAGNOSTIC_FAILURE"
