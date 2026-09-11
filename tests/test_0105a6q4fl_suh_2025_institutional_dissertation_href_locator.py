import importlib.util
from pathlib import Path

P = Path(__file__).resolve().parents[1] / "scripts" / "audit_0105a6q4fl_suh_2025_institutional_dissertation_href_locator.py"
spec = importlib.util.spec_from_file_location("q4fl", P)
q = importlib.util.module_from_spec(spec)
spec.loader.exec_module(q)


def test_prereg_and_frozen_sources():
    assert q.PREREG_COMMIT == "deadbcefe38ef9fa4618a57fd65ce82cf7178f3b"
    assert q.SOURCES[0]["sha256"] == "f1c245e9675c1a533bc9ad03ca928820499381d576c5f6fefee59c33b91d7488"
    assert q.SOURCES[1]["sha256"] == "3de3e09e5ebdb4006c0d8b969c3f73a25b041b31534476b6bf6987bbf5591fe6"


def test_frozen_tokens_and_classes():
    assert q.IDENTITY_TOKENS == ("suh", "benjamin", "cenns-10", "cenns10")
    assert q.REPOSITORY_TOKENS == ("scholarworks", "dspace", "/handle/", "/etd", "dissertation")
    assert q.CLASS_SOURCE_DRIFT == "BLOCKED_0105A6Q4FL_FROZEN_SOURCE_IDENTITY_DRIFT"
    assert q.CLASS_NO_CANDIDATES == "BLOCKED_0105A6Q4FL_INSTITUTIONAL_DISSERTATION_LOCATOR_NO_CANDIDATES"
    assert q.CLASS_CANDIDATES == "PASS_0105A6Q4FL_INSTITUTIONAL_DISSERTATION_LOCATOR_CANDIDATES_FOUND_NONDISCOVERY"


def test_anchor_parser_and_relative_resolution():
    payload = b'<html><a href="../docs/suh-dissertation.pdf"> Benjamin   Suh </a><a href="#x">skip</a></html>'
    anchors = q.parse_anchors(payload, "text/html; charset=utf-8")
    assert anchors[0][0] == "../docs/suh-dissertation.pdf"
    c = q.candidate_for("https://ceem.indiana.edu/education/index.html", *anchors[0])
    assert c["resolved_url"] == "https://ceem.indiana.edu/docs/suh-dissertation.pdf"
    assert "suh" in c["identity_tokens"]
    assert ".pdf" in c["repository_payload_tokens"]


def test_repository_candidate_without_identity_and_non_candidate_filters():
    c = q.candidate_for(
        "https://ceem.indiana.edu/education/index.html",
        "https://scholarworks.iu.edu/dspace/handle/123/456",
        "repository",
    )
    assert c is not None
    assert "scholarworks" in c["repository_payload_tokens"]
    assert "/handle/" in c["repository_payload_tokens"]

    assert q.candidate_for("https://ceem.indiana.edu/education/index.html", "#section", "Suh") is None
    assert q.candidate_for("https://ceem.indiana.edu/education/index.html", "mailto:x@example.com", "Benjamin") is None
    assert q.candidate_for("https://ceem.indiana.edu/education/index.html", "/about/index.html", "About") is None
