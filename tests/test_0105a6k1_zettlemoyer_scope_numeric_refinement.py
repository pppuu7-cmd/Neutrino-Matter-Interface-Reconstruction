from scripts.audit_0105a6k1_zettlemoyer_scope_numeric_refinement import refine, PARENT_CLASS, THESIS_SHA256


def parent_fixture():
    scores = []
    core_pages = {132,133,134,137,144,145,146,147,148,149,150,156,158,161,165}
    support_pages = {137,150,159}
    for p in range(1, 187):
        scores.append({
            "page": p,
            "A": 2 if p in core_pages else 0,
            "S": 1 if p in core_pages else 0,
            "Y": 1 if p in support_pages else 0,
            "core_hit": p in core_pages,
            "support_hit": p in support_pages,
        })
    return {
        "classification": PARENT_CLASS,
        "source_sha256_observed": THESIS_SHA256,
        "pdf_pages": 186,
        "page_scores": scores,
        "scope_map": {"selected": {"first_core": 132, "last_core": 165}},
    }


def test_refinement_uses_24_page_window_and_30_page_padded_interval():
    r = refine(parent_fixture())
    w = r["winning_core_window"]
    assert w["end"] - w["start"] + 1 == 24
    assert r["future_semantic_interval_width"] == 30


def test_representativeness_threshold_is_two_thirds_ceiling():
    r = refine(parent_fixture())
    assert r["parent_core_hit_count"] == 15
    assert r["required_core_hits"] == 10
    assert r["parent_support_hit_count"] == 3
    assert r["required_support_hits"] == 2


def test_dense_early_window_wins_fixture_deterministically():
    r = refine(parent_fixture())
    assert r["winning_core_window"]["start"] == 132
    assert r["winning_core_window"]["end"] == 155
    assert len(r["winning_core_window"]["core_pages"]) == 11
    assert len(r["winning_core_window"]["support_pages"]) == 2
    assert r["pass_gate"] is True


def test_wrong_parent_class_fails():
    p = parent_fixture()
    p["classification"] = "PASS_WRONG"
    try:
        refine(p)
    except ValueError as exc:
        assert "classification" in str(exc)
    else:
        raise AssertionError("expected fail-closed ValueError")


def test_wrong_thesis_identity_fails():
    p = parent_fixture()
    p["source_sha256_observed"] = "0" * 64
    try:
        refine(p)
    except ValueError as exc:
        assert "thesis identity" in str(exc)
    else:
        raise AssertionError("expected fail-closed ValueError")
