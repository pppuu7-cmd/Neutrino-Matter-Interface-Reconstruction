from scripts.audit_0105a5b_r1d_external_authority_evidence import TERMS, contexts


def test_exact_dependency_inventory_is_frozen():
    assert TERMS == ["BarrWP", "BarrWM", "BarrYP", "BarrYM", "BarrZP", "BarrZM", "MCEq", "CSMS", "DIS"]


def test_context_extraction_is_literal_case_insensitive_only():
    text = "alpha\nBarrWP authority line\nomega"
    blocks = contexts(text, "barrwp", radius=0)
    assert blocks == ["BarrWP authority line"]


def test_context_extraction_does_not_infer_absent_term():
    assert contexts("no relevant token here", "CSMS", radius=1) == []
