from scripts.extract_0105a6m_zettlemoyer_candidate_evidence_windows import (
    MAX_WINDOW_CHARS,
    bounded_window,
    derive_allowed_pages,
)


def parent_fixture():
    return {
        "classification": "PASS_0105A6L_MACHINE_TEXT_EVIDENCE_PREFLIGHT_NONDISCOVERY",
        "git_sha": "32e7845e07c2255b90bc8e4f283d30891a84b450",
        "candidate_evidence_pages": {
            "L0": [132, 150],
            "F1": [145, 150],
            "F3": [132, 151],
            "F4": [],
            "F6": [154],
            "F7": [],
        },
        "f7_exact_number_pages": {"3152": [], "3154": [151, 152]},
    }


def test_dynamic_scope_is_exact_union_only():
    assert derive_allowed_pages(parent_fixture()) == [132, 145, 150, 151, 152, 154]


def test_wrong_parent_classification_fails_closed():
    p = parent_fixture()
    p["classification"] = "BLOCKED"
    try:
        derive_allowed_pages(p)
    except ValueError:
        pass
    else:
        raise AssertionError("non-PASS parent was accepted")


def test_scope_expansion_fails_closed():
    p = parent_fixture()
    p["candidate_evidence_pages"]["F1"].append(159)
    try:
        derive_allowed_pages(p)
    except ValueError:
        pass
    else:
        raise AssertionError("out-of-scope page was accepted")


def test_evidence_window_never_exceeds_cap_or_equals_full_page():
    text = "a" * 500 + " likelihood " + "b" * 1200
    w = bounded_window(text, ["likelihood"])
    assert len(w["window"]) <= MAX_WINDOW_CHARS
    assert w["window"] != text


def test_missing_marker_emits_no_context():
    w = bounded_window("abc def ghi", ["likelihood"])
    assert w["window"] == ""
    assert w["present_markers"] == []
