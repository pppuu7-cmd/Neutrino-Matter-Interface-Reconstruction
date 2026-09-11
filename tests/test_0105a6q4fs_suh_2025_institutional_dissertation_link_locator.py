from pathlib import Path
S=Path('scripts/audit_0105a6q4fs_suh_2025_institutional_dissertation_link_locator.py').read_text()

def test_prereg_and_exact_sources():
    assert "PREREG='a55e26040be8fdd059563781d5a3a8c5ba1ed259'" in S
    assert '23370' in S and 'f1c245e9675c1a533bc9ad03ca928820499381d576c5f6fefee59c33b91d7488' in S
    assert '67845' in S and '3de3e09e5ebdb4006c0d8b969c3f73a25b041b31534476b6bf6987bbf5591fe6' in S

def test_full_frozen_title_present():
    assert "towards an improved measurement of the cevns process with the cen..." in S.lower()

def test_locator_never_follows_returned_links():
    assert "'page_links_followed':False" in S
    assert "'pdf_downloaded':False" in S
    assert 'urlopen(req' in S
    assert "urllib.parse.urljoin" in S

def test_permissions_remain_zero():
    assert "'systematic_monte_carlo_execution_permission_percent':0" in S
    assert "'observed_bsm_residual_permission_percent':0" in S
    assert "'likelihood_evaluated':False" in S
    assert "'pseudo_data_generated':False" in S

def test_frozen_terminal_classes():
    for c in ['PASS_0105A6Q4FS_INSTITUTIONAL_DISSERTATION_LINK_CANDIDATES_LOCATED_NONDISCOVERY','BLOCKED_0105A6Q4FS_NO_INSTITUTIONAL_DISSERTATION_LINK_CANDIDATES','BLOCKED_0105A6Q4FS_SOURCE_TRANSPORT_FAILURE','FAIL_0105A6Q4FS_SOURCE_BYTE_IDENTITY_MISMATCH']:
        assert c in S
