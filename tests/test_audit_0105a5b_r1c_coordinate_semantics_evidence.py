from scripts.audit_0105a5b_r1c_coordinate_semantics_evidence import documentation_candidate, evidence_lines


def test_documentation_candidate_is_authority_inventory_only():
    assert documentation_candidate("README.txt", "text/plain")
    assert documentation_candidate("notes.md", "application/octet-stream")
    assert documentation_candidate("data.csv", "text/comma-separated-values")
    assert not documentation_candidate("plot.png", "image/png")


def test_evidence_lines_are_literal_not_mapping_inference():
    text = "unrelated\nreco_energy bin edges are documented here\nPID category description\n"
    lines = evidence_lines(text)
    assert lines == ["reco_energy bin edges are documented here", "PID category description"]
    # The collector must not manufacture mapping conclusions.
    assert all("bijection" not in line.lower() for line in lines)
