import importlib.util
from pathlib import Path

P = Path(__file__).resolve().parents[1] / "scripts" / "audit_0105a6q4fr_suh_2025_institutional_manifest_transport_repair.py"
spec = importlib.util.spec_from_file_location("q4fr", P)
q = importlib.util.module_from_spec(spec)
spec.loader.exec_module(q)


def test_frozen_prereg_and_endpoints():
    assert q.PREREG_COMMIT == "f47dda9bd5fda788c4497d58e4a2f58f2e042cb3"
    assert q.CEEM_PLAQUE_URL == "https://ceem.indiana.edu/events/phd-plaques/suh-benjamin.html"
    assert q.CEEM_EDUCATION_URL == "https://ceem.indiana.edu/education/index.html"


def test_frozen_identity_contract():
    assert q.AUTHORS == ("Benjamin D. Suh", "Benjamin Suh")
    assert q.YEAR == "2025"
    assert q.TITLE == "TOWARDS AN IMPROVED MEASUREMENT OF THE CEVNS PROCESS WITH THE CENNS-10 LAR DETECTOR"


def test_identity_is_case_insensitive_and_whitespace_tolerant_only():
    body = b"""<html><body><h1>Benjamin Suh</h1><p>2025</p>
    <div>Towards an improved measurement of the CEVNS process with the
    CENNS-10 LAr detector</div></body></html>"""
    flags = q.identity_flags(body, "text/html; charset=utf-8")
    assert flags == {"author": True, "year": True, "title": True, "complete": True}


def test_identity_fails_if_any_frozen_component_is_missing_or_changed():
    base = """<html><body>Benjamin D. Suh 2025
    TOWARDS AN IMPROVED MEASUREMENT OF THE CEVNS PROCESS WITH THE CENNS-10 LAR DETECTOR
    </body></html>"""
    assert q.identity_flags(base.encode(), "text/html")["complete"]

    no_year = base.replace("2025", "2024").encode()
    assert not q.identity_flags(no_year, "text/html")["complete"]

    changed_title = base.replace("IMPROVED MEASUREMENT", "BETTER MEASUREMENT").encode()
    assert not q.identity_flags(changed_title, "text/html")["complete"]

    wrong_author = base.replace("Benjamin D. Suh", "Another Researcher").encode()
    assert not q.identity_flags(wrong_author, "text/html")["complete"]


def test_terminal_classes_are_exactly_frozen():
    assert q.PASS_CLASS == "PASS_0105A6Q4FR_INSTITUTIONAL_MANIFEST_TRANSPORT_REPAIRED_NONDISCOVERY"
    assert q.BLOCKED_CLASS == "BLOCKED_0105A6Q4FR_INSTITUTIONAL_MANIFEST_TRANSPORT_OR_IDENTITY_INCOMPLETE"
