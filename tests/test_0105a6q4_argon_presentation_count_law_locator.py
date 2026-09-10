from scripts.audit_0105a6q4_argon_presentation_count_law_locator import flags, PREREG_COMMIT, MD5

def test_frozen_identity():
    assert PREREG_COMMIT=='7c497f6c20df351aa2d9ee033663c2da330186d2'
    assert MD5=='090a0273868c98d26ed1f4a31effb4a8'

def test_poisson_candidate_requires_pseudodata():
    assert 'DIRECT_COUNT_LAW_CANDIDATE' in flags('pseudo-data counts are Poisson')['categories']
    assert 'DIRECT_COUNT_LAW_CANDIDATE' not in flags('counts are Poisson')['categories']

def test_generation_contract_candidate():
    c=flags('pseudo data are generated with RooMCStudy NumEvents')['categories']
    assert 'IMPLEMENTATION_CONTRACT_CANDIDATE' in c

def test_count_generation_candidate():
    c=flags('pseudo-data generated with number of events from model')['categories']
    assert 'COUNT_GENERATION_CANDIDATE' in c

def test_extended_alone_without_pseudodata_is_not_candidate():
    assert flags('extended maximum likelihood')['categories']==[]
