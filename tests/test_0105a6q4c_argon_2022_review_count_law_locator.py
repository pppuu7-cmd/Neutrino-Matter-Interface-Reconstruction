from scripts.audit_0105a6q4c_argon_2022_review_count_law_locator import flags, PREREG_COMMIT, PARENT_CLASS, EXPECTED_HOST, EXPECTED_PATH

def test_frozen_identity():
    assert PREREG_COMMIT=='3e11e1fc9343d10d6c97ed2dacff52cee9e228ba'
    assert PARENT_CLASS=='BLOCKED_0105A6Q4B_2018_PRESENTATION_HAS_NO_COUNT_LAW_CANDIDATE_PAGES'
    assert EXPECTED_HOST=='indico.cern.ch'
    assert EXPECTED_PATH=='/event/978288/contributions/5014436/attachments/2504944/4303826/JCZBLV2022_CEvNSReviewTalk.pdf'

def test_poisson_candidate_requires_pseudodata():
    assert 'DIRECT_COUNT_LAW_CANDIDATE' in flags('pseudo-data counts are Poisson')['categories']
    assert 'DIRECT_COUNT_LAW_CANDIDATE' not in flags('counts are Poisson')['categories']

def test_generation_contract_candidate():
    assert 'IMPLEMENTATION_CONTRACT_CANDIDATE' in flags('pseudo data are generated with RooMCStudy NumEvents')['categories']

def test_count_generation_candidate():
    assert 'COUNT_GENERATION_CANDIDATE' in flags('pseudo-data generated with number of events from model')['categories']

def test_extended_alone_without_pseudodata_is_not_candidate():
    assert flags('extended maximum likelihood')['categories']==[]
