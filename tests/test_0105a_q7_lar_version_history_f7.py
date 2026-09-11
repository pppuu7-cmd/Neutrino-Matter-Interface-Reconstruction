from scripts.validate_0105a_q7_lar_version_history_f7 import classify

V3='Analysis A predicted SS 3154 ± 25'
V4='Analysis A predicted SS 3152 ± 25'
V7='Analysis A predicted NSS 3152 ± 25'
H='Comments: V3 fixes figures V4: fix typo in table 1 V7 final'
R='Analysis A steady state NSS 3152 ± 25'

def test_all_four_frozen_conditions_pass():
    r=classify(V3,V4,V7,H,R)
    assert all(r['conditions'].values())
    assert r['scientific_claim_machine_validated']

def test_missing_any_condition_blocks():
    r=classify(V3,V4,V7,H.replace('fix typo in table 1','other change'),R)
    assert not r['scientific_claim_machine_validated']
    assert r['status'].startswith('BLOCKED_0105A_Q7_')

def test_wrong_pre_v4_value_blocks():
    r=classify(V3.replace('3154','3152'),V4,V7,H,R)
    assert not r['conditions']['v3_3154']
