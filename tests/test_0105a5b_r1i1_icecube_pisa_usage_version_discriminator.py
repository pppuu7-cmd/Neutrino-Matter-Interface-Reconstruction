from pathlib import Path
S=Path('scripts/audit_0105a5b_r1i1_icecube_pisa_usage_version_discriminator.py').read_text()
P=Path('research/prereg/0105a5b_r1i1_icecube_pisa_usage_version_discriminator_preregistration.md').read_text()

def test_exact_source_and_member_locks():
    assert 'https://export.arxiv.org/e-print/2304.12236' in S
    assert '111c41e49dd50880bc6b00aca95a2479216622b47235fcb68e2a02e22456a149' in S
    assert '2c25f03bfadc482a81a8f490efd15df3481988485630f92a255bb3f3c4c3708e' in S
    assert '0055d6eb0585c44f2074b8f29712c38e1c645154d88830074fb7bff37b00e20c' in S

def test_complete_frozen_tag_set():
    tags=['contours_working_0.1','4.3a1','4.2.1','4.2','4.1.4','4.1.3','4.1.2','4.1.1','4.1','4.0','3.2.1','3.2','3.1','3.0','2.0.1','2.0','1.0.1','1.0']
    for t in tags: assert t in S and t in P

def test_fail_closed_classes():
    for c in ['PASS_0105A5B_R1I1_PISA_USAGE_AND_VERSION_UNIQUELY_DISCRIMINATED_NONDISCOVERY','BLOCKED_0105A5B_R1I1_PISA_REFERENCED_VERSION_NOT_UNIQUELY_DISCRIMINATED','BLOCKED_0105A5B_R1I1_PISA_NOT_REFERENCED_BY_ICECUBE_SOURCE','INFRASTRUCTURE_FAIL_0105A5B_R1I1']:
        assert c in S

def test_no_pisa_repository_content_endpoint():
    for bad in ['api.github.com/repos/icecube/pisa/contents','raw.githubusercontent.com/icecube/pisa','github.com/icecube/pisa/blob','github.com/icecube/pisa/tree']:
        assert bad not in S.lower()

def test_science_prohibitions():
    for m in ["'pisa_repository_content_inspected':False","'standard_3nu_executed':False","'systematic_monte_carlo_executed':False","'observed_bsm_residual_inspected':False","'observed_bsm_residual_permission_percent':0","'systematic_monte_carlo_execution_permission_percent':0"]:
        assert m in S
