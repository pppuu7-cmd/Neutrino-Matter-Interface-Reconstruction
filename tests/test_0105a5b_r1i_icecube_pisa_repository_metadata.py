from pathlib import Path
S=Path('scripts/audit_0105a5b_r1i_icecube_pisa_repository_metadata.py').read_text()
P=Path('research/prereg/0105a5b_r1i_icecube_pisa_repository_metadata_preregistration.md').read_text()

def test_exact_provider_endpoints():
    for u in ['https://api.github.com/repos/icecube/pisa','https://api.github.com/repos/icecube/pisa/tags?per_page=100','https://api.github.com/repos/icecube/pisa/releases?per_page=100']:
        assert u in S and u in P

def test_fail_closed_classes():
    for c in ['PASS_0105A5B_R1I_ICECUBE_PISA_METADATA_PINNABLE_NONDISCOVERY','BLOCKED_0105A5B_R1I_ICECUBE_PISA_METADATA_NOT_PINNABLE','INFRASTRUCTURE_FAIL_0105A5B_R1I']:
        assert c in S

def test_no_content_endpoints():
    for bad in ['/readme','/contents/','/git/trees/','/git/blobs/','/zipball','/tarball']:
        assert bad not in S.lower()

def test_science_prohibitions():
    for marker in ["'readme_inspected':False","'implementation_inspected':False","'archive_inspected':False","'standard_3nu_executed':False","'systematic_monte_carlo_executed':False","'observed_bsm_residual_inspected':False","'observed_bsm_residual_permission_percent':0","'systematic_monte_carlo_execution_permission_percent':0"]:
        assert marker in S
