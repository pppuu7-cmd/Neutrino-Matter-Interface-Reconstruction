from pathlib import Path
SRC=Path('scripts/adjudicate_0105a6q5e_argon_semantic_contract.py').read_text()

def test_prereg_and_parent_hashes_frozen():
    for x in ['7e414409b9f79da0a24090ef5ce3583d67a30e09','269ff3984ff40b7010f35b755b4f1ef5207ba82ae285d08ef035b29b1d30a178','0c45f7cbba28c5a3a21222d45ff3bd6260ad9849629e71c3be9c82ddc875a324','36fd99270bf11aec076849c6560a4315c3a4a72f']:
        assert x in SRC

def test_only_q5d_evidence_categories_used():
    for x in ["cat_windows(d,'E1')","cat_windows(d,'E3')","cat_windows(d,'E4')","cat_windows(d,'E5')"]: assert x in SRC

def test_frozen_questions_and_no_defaults():
    for x in ['F1','F4','F6','F7','poisson','multinomial','morph','interpol','simultaneous','covariance','3152','3154']:
        assert x in SRC

def test_parent_invalid_fail_closed():
    assert 'BLOCKED_0105A6Q5E_PARENT_EVIDENCE_INVALID' in SRC
    assert "q5d zip digest mismatch" in SRC
    assert "q5d inner digest mismatch" in SRC

def test_required_items_conjunctive():
    assert "f1=='PASS_EXPLICIT' and f4=='PASS_EXPLICIT' and f6=='PASS_EXPLICIT'" in SRC

def test_hard_science_guards():
    for x in ["pseudo_data_generated':False","likelihood_evaluated':False","fit_executed':False","nuisance_profiled':False","systematic_monte_carlo_executed':False","observed_bsm_residual_inspected':False"]: assert x in SRC

def test_permissions_zero():
    assert "systematic_monte_carlo_execution_permission_percent':0" in SRC
    assert "observed_bsm_residual_permission_percent':0" in SRC

def test_terminal_classes():
    for x in ['PASS_0105A6Q5E_ARGON_RELEASE_SEMANTIC_CONTRACT_SUFFICIENT_NONDISCOVERY','BLOCKED_0105A6Q5E_ARGON_RELEASE_SEMANTIC_CONTRACT_INCOMPLETE','BLOCKED_0105A6Q5E_PARENT_EVIDENCE_INVALID']:
        assert x in SRC
