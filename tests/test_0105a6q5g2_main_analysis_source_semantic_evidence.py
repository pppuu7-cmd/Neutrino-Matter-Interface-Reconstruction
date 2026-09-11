from pathlib import Path

P=Path('scripts/audit_0105a6q5g2_main_analysis_source_semantic_evidence.py')
S=P.read_text()

def test_frozen_prereg_and_source_identity():
    assert "PREREG='6da043ddbfc8dd3ef40fbe02892d9315e1a944ca'" in S
    assert "SHA='2edeb3dcc3df99de575c8b2091f48099a7538eedf9f382996d943c7fbe7e2114'" in S
    assert 'SIZE=446096' in S

def test_complete_six_member_set_is_frozen():
    for name,size in {
        'authors.tex':6826,'commands.tex':3979,'main.bbl':37145,
        'main.bib':45756,'main.tex':30063,'supplemental.tex':9705,
    }.items():
        assert repr(name) in S and str(size) in S

def test_scope_is_only_f1_f7_and_inherits_f4_f6():
    assert "'F1':[" in S and "'F7':[" in S
    assert "'F4':[" not in S and "'F6':[" not in S
    assert 'RESOLVED_EXPLICIT_SEPARATE_ALTERNATIVE_FITS' in S
    assert 'RESOLVED_EXPLICIT_SEPARATE_SYSTEMATIC_FITS' in S

def test_fail_closed_permissions():
    assert "'likelihood_evaluated':False" in S
    assert "'pseudo_data_generated':False" in S
    assert "'systematic_monte_carlo_executed':False" in S
    assert "'observed_bsm_residual_inspected':False" in S
    assert "'systematic_monte_carlo_execution_permission_percent':0" in S
    assert "'observed_bsm_residual_permission_percent':0" in S

def test_lexical_union_contains_frozen_required_terms():
    for token in ['poisson','multinomial','fixed[- ]?total','number of events','event count','pseudo[- ]?data','pseudodata','extended likelihood','roofit','3152','3154','steady[- ]?state','normalization','central value']:
        assert token in S.lower()

def test_no_automatic_semantic_pass():
    assert "out['classification']='BLOCKED_0105A6Q5G2_MAIN_ANALYSIS_SOURCE_F1_F7_CONTRACT_INCOMPLETE'" in S
    assert 'lexical coincidence alone never promotes a semantic PASS' in S
