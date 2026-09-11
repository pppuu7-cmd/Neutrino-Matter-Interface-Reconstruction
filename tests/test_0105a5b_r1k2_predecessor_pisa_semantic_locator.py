from pathlib import Path
S=Path('scripts/audit_0105a5b_r1k2_predecessor_pisa_semantic_locator.py').read_text()
P=Path('research/prereg/0105a5b_r1k2_predecessor_pisa_semantic_locator_preregistration.md').read_text()

def test_source_lock_and_full_candidate_set():
    assert "EXPECTED_SHA256='d095d23daf4dc08848b7f3ff5977daaf554db966034ca9d3460e4b88d7c3790a'" in S
    for name in ['history.txt','main.bib','main.tex','readme-epjc.txt','svjour3.cls','text/SampleAndReco.tex','text/abstract.tex','text/acknowledgement.tex','text/analysis.tex','text/conclusion.tex','text/icecube.tex','text/introduction.tex','text/results.tex','text/sensitivity.tex']:
        assert name in S and name in P

def test_bounded_frozen_patterns():
    assert "radius=300" in S
    assert 'HEX40_RE' in S and 'VERSION_RE' in S and 'REPO_RE' in S
    assert 'PASS_0105A5B_R1K2_PREDECESSOR_PISA_IMMUTABLE_STATE_EXPLICIT_NONDISCOVERY' in S
    assert 'BLOCKED_0105A5B_R1K2_PREDECESSOR_PISA_STATE_NOT_IMMUTABLY_IDENTIFIED' in S

def test_hard_prohibitions():
    for x in ["'pisa_repository_content_fetched':False","'standard_3nu_executed':False","'systematic_monte_carlo_executed':False","'observed_bsm_residual_inspected':False"]:
        assert x in S
    assert "'observed_bsm_residual_permission_percent':0" in S
    assert "'systematic_monte_carlo_execution_permission_percent':0" in S
