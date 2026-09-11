from pathlib import Path
S=Path('scripts/audit_0105a5b_r1j_pisa_methodology_source_bytes.py').read_text()
P=Path('research/prereg/0105a5b_r1j_pisa_methodology_source_bytes_preregistration.md').read_text()

def test_exact_source_only():
    assert 'https://export.arxiv.org/e-print/1803.05390' in S and 'https://export.arxiv.org/e-print/1803.05390' in P
    assert '2304.12236' not in S

def test_classes():
    assert 'PASS_0105A5B_R1J_PISA_METHODOLOGY_SOURCE_BYTES_ACQUIRED_NONDISCOVERY' in S
    assert 'INFRASTRUCTURE_FAIL_0105A5B_R1J' in S

def test_no_archive_or_content_processing():
    for bad in ['tarfile','zipfile','extract','getmembers','namelist','readme','api.github.com/repos/icecube/pisa']:
        assert bad not in S.lower()

def test_prohibitions():
    for m in ["'archive_opened':False","'member_listed':False","'source_text_inspected':False","'pisa_repository_content_inspected':False","'standard_3nu_executed':False","'systematic_monte_carlo_executed':False","'observed_bsm_residual_inspected':False","'observed_bsm_residual_permission_percent':0","'systematic_monte_carlo_execution_permission_percent':0"]:
        assert m in S
