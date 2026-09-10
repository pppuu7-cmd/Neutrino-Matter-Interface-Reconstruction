from scripts.audit_0105a6k_zettlemoyer_thesis_analysisA_scope_map import page_scores, select_scope


def make_pages(n=60):
    return ["ordinary thesis text" for _ in range(n)]


def test_core_hit_requires_analysis_and_statistical_anchors():
    pages = make_pages()
    pages[19] = "Analysis A CENNS-10 maximum likelihood"
    s = page_scores(pages)
    assert s[19]["core_hit"] is True
    assert s[0]["core_hit"] is False


def test_support_hit_can_capture_systematic_context():
    pages = make_pages()
    pages[20] = "CENNS-10 F90 quenching factor systematic uncertainty"
    s = page_scores(pages)
    assert s[20]["support_hit"] is True
    assert s[20]["core_hit"] is False


def test_cluster_rule_prefers_more_core_hits_before_other_scores():
    pages = make_pages(80)
    pages[9] = "Analysis A CENNS-10 likelihood"
    pages[10] = "Analysis A F90 likelihood"
    pages[39] = "Analysis A CENNS-10 RooFit maximum likelihood systematic uncertainty quenching factor"
    mapping = select_scope(page_scores(pages))
    assert mapping["selected"]["core_pages"] == [10, 11]


def test_padding_is_exactly_three_pages_when_not_at_boundary():
    pages = make_pages()
    pages[19] = "Analysis A CENNS-10 likelihood"
    pages[21] = "Analysis A F90 maximum likelihood"
    selected = select_scope(page_scores(pages))["selected"]
    assert selected["first_core"] == 20
    assert selected["last_core"] == 22
    assert selected["future_interval_first_page"] == 17
    assert selected["future_interval_last_page"] == 25


def test_no_core_hits_returns_no_selected_scope():
    mapping = select_scope(page_scores(make_pages()))
    assert mapping["core_pages"] == []
    assert mapping["selected"] is None
