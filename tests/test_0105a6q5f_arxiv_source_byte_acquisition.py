from pathlib import Path
SRC=Path('scripts/audit_0105a6q5f_arxiv_source_byte_acquisition.py').read_text()
def test_prereg(): assert 'cc4a01a55bb8232325a82df48b0ac220a7a0bef5' in SRC
def test_exact_source_endpoint(): assert "URL='https://arxiv.org/e-print/2006.12659'" in SRC
def test_arxiv_only_redirects(): assert "h=='arxiv.org' or h.endswith('.arxiv.org')" in SRC
def test_byte_identity_recorded(): assert "'md5':hashlib.md5(b).hexdigest()" in SRC and "'sha256':hashlib.sha256(b).hexdigest()" in SRC
def test_no_semantic_inspection():
    for x in ["source_text_inspected':False","archive_members_extracted':False","keywords_searched':False","likelihood_evaluated':False","observed_bsm_residual_inspected':False"]: assert x in SRC
def test_permissions_zero(): assert "systematic_monte_carlo_execution_permission_percent':0" in SRC and "observed_bsm_residual_permission_percent':0" in SRC
def test_classes():
    assert 'PASS_0105A6Q5F_ARXIV_2006_12659_SOURCE_BYTES_ACQUIRED_NONDISCOVERY' in SRC
    assert 'BLOCKED_0105A6Q5F_ARXIV_SOURCE_TRANSPORT_FAILURE' in SRC
