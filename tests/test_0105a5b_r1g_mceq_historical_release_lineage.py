from pathlib import Path
S=Path('scripts/audit_0105a5b_r1g_mceq_historical_release_lineage.py').read_text()
P=Path('research/prereg/0105a5b_r1g_mceq_historical_release_lineage_preregistration.md').read_text()

def test_frozen_candidate_count_and_ids():
    assert S.count('release_1_2_') >= 7
    for x in ['mceq108','mceq_1_1_1','release_1_2_6']:
        assert x in S and x in P

def test_metadata_only_endpoint():
    assert 'https://api.github.com/repos/mceq-project/MCEq/commits/' in S
    low=S.lower()
    for x in ['/contents/','/git/trees/','raw.githubusercontent.com','tarball','zipball','readme']:
        assert x not in low

def test_science_prohibitions():
    for x in ['"source_code_inspected":False','"trees_or_blobs_inspected":False','"standard_3nu_executed":False','"systematic_monte_carlo_executed":False','"observed_bsm_residual_inspected":False']:
        assert x in S

def test_nondiscovery_pass_label():
    assert 'PASS_0105A5B_R1G_MCEQ_HISTORICAL_RELEASE_LINEAGE_PINNED_NONDISCOVERY' in S
