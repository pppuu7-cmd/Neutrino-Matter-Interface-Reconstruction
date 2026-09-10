from scripts.audit_0105a6q2_argon_pseudodata_count_law_locator import flags, BENCHMARK, PREREG_COMMIT


def test_identity_constants_are_frozen():
    assert BENCHMARK == 'NMIR-V2-0105A6Q2'
    assert PREREG_COMMIT == 'f1607e221b775feb0fbdb081986fca160d4cd155'


def test_direct_poisson_candidate_requires_pseudodata():
    assert 'DIRECT_COUNT_LAW_CANDIDATE' in flags('pseudo-data event counts are poisson distributed')['categories']
    assert 'DIRECT_COUNT_LAW_CANDIDATE' not in flags('ordinary counts are poisson distributed')['categories']


def test_implementation_candidate_requires_l1_l3_l4():
    cats = flags('pseudo data are generated with RooMCStudy using NumEvents')['categories']
    assert 'IMPLEMENTATION_CONTRACT_CANDIDATE' in cats


def test_count_generation_candidate_requires_generate_and_count():
    cats = flags('pseudo-data are generated with a number of events drawn somehow')['categories']
    assert 'COUNT_GENERATION_CANDIDATE' in cats
    assert 'COUNT_GENERATION_CANDIDATE' not in flags('pseudo-data are generated from pdfs')['categories']


def test_no_semantic_candidate_from_extended_alone_without_pseudodata():
    assert flags('an extended maximum likelihood is used')['categories'] == []


def test_resampling_is_direct_candidate_only_with_pseudodata():
    assert 'DIRECT_COUNT_LAW_CANDIDATE' in flags('pseudo data use bootstrap resampling')['categories']
