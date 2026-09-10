from scripts.audit_0105a6q4b_argon_2018_magnificent_cevns_count_law_locator import flags, PREREG_COMMIT, PARENT_CLASS, EXPECTED_HOST, EXPECTED_PATH

def test_frozen_identity():
    assert PREREG_COMMIT=='f0c8b72e55f37776c41bc6aca2f02d5b6c6b91a1'
    assert PARENT_CLASS=='BLOCKED_0105A6Q4A_POSTER_HAS_NO_COUNT_LAW_CANDIDATE_PAGES'
    assert EXPECTED_HOST=='kicp-workshops.uchicago.edu'
    assert EXPECTED_PATH=='/2018-CEvNS/depot/talk-zettlemoyer-jacob.pdf'

def test_poisson_candidate_requires_pseudodata():
    assert 'DIRECT_COUNT_LAW_CANDIDATE' in flags('pseudo-data counts are Poisson')['categories']
    assert 'DIRECT_COUNT_LAW_CANDIDATE' not in flags('counts are Poisson')['categories']

def test_generation_contract_candidate():
    assert 'IMPLEMENTATION_CONTRACT_CANDIDATE' in flags('pseudo data are generated with RooMCStudy NumEvents')['categories']

def test_count_generation_candidate():
    assert 'COUNT_GENERATION_CANDIDATE' in flags('pseudo-data generated with number of events from model')['categories']

def test_extended_alone_without_pseudodata_is_not_candidate():
    assert flags('extended maximum likelihood')['categories']==[]
