from scripts.audit_0105a6q4a_argon_neutrino2020_poster_count_law_locator import flags, PREREG_COMMIT, MD5, PARENT_CLASS

def test_frozen_identity():
    assert PREREG_COMMIT=='578f211209a8074df33d783ac6f204f71f2e99ad'
    assert MD5=='c00fe90b1e16f3069ff6970308ee8345'
    assert PARENT_CLASS=='BLOCKED_0105A6Q4_PRESENTATION_HAS_NO_COUNT_LAW_CANDIDATE_PAGES'

def test_poisson_candidate_requires_pseudodata():
    assert 'DIRECT_COUNT_LAW_CANDIDATE' in flags('pseudo-data counts are Poisson')['categories']
    assert 'DIRECT_COUNT_LAW_CANDIDATE' not in flags('counts are Poisson')['categories']

def test_generation_contract_candidate():
    assert 'IMPLEMENTATION_CONTRACT_CANDIDATE' in flags('pseudo data are generated with RooMCStudy NumEvents')['categories']

def test_count_generation_candidate():
    assert 'COUNT_GENERATION_CANDIDATE' in flags('pseudo-data generated with number of events from model')['categories']

def test_extended_alone_without_pseudodata_is_not_candidate():
    assert flags('extended maximum likelihood')['categories']==[]
