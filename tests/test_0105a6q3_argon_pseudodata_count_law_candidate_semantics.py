from scripts.audit_0105a6q3_argon_pseudodata_count_law_candidate_semantics import classify, PAGES, PAGE_HASHES, PREREG_COMMIT


def test_frozen_candidate_set_and_prereg():
    assert PAGES == [145, 152, 153]
    assert PREREG_COMMIT == 'be5e6b6d381b8b2667466768edcf2f175fce8996'
    assert set(PAGE_HASHES) == {145, 152, 153}


def test_explicit_poisson_is_q3p():
    d,c,_=classify({145:'pseudo-data number of events is poisson distributed',152:'',153:''})
    assert d=='Q3-P' and c.startswith('PASS_')


def test_extended_alone_is_not_poisson_evidence():
    d,c,_=classify({145:'pseudo-data use an extended binned maximum likelihood',152:'',153:''})
    assert d=='NONE' and c=='BLOCKED_0105A6Q3_PSEUDODATA_COUNT_LAW_STILL_NOT_EXPLICIT'


def test_fixed_total_is_q3f():
    d,c,_=classify({145:'pseudo-data have a fixed total event count',152:'',153:''})
    assert d=='Q3-F' and c.startswith('PASS_')


def test_bootstrap_is_q3o():
    d,c,_=classify({145:'pseudo-data event counts are obtained by bootstrap resampling',152:'',153:''})
    assert d in ('Q3-O','CONFLICT')


def test_conflicting_explicit_laws_block():
    d,c,_=classify({145:'pseudo-data number of events is poisson distributed',152:'pseudo-data have a fixed total event count',153:''})
    assert d=='CONFLICT' and c=='BLOCKED_0105A6Q3_CONFLICTING_PSEUDODATA_COUNT_LAW_AUTHORITY'
