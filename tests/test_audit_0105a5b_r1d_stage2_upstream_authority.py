from scripts.audit_0105a5b_r1d_stage2_upstream_authority import SOURCES, TOKENS, contexts


def test_sources_are_exact_versioned_upstream_arxiv_ids():
    assert SOURCES == {
        "barr_2006": "https://export.arxiv.org/e-print/astro-ph/0611266v1",
        "sibyll_mceq_2019": "https://export.arxiv.org/e-print/1806.04140v2",
        "csms_2011": "https://export.arxiv.org/e-print/1106.3723v1",
    }


def test_release_internal_labels_are_explicitly_searched():
    for token in ("BarrWP", "BarrWM", "BarrYP", "BarrYM", "BarrZP", "BarrZM"):
        assert token in TOKENS


def test_context_extraction_is_literal_and_bounded():
    text = "alpha BarrWP omega"
    hits = contexts(text, "BarrWP", radius=5)
    assert len(hits) == 1
    assert "BarrWP" in hits[0]
