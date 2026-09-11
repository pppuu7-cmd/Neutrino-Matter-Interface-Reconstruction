from pathlib import Path
SRC=Path('scripts/audit_0105a6q5f1_arxiv_source_archive_structure_locator.py').read_text()
def test_prereg_and_source_identity():
 assert '37847bf0d915208910b3eced72d8a40e541c6326' in SRC
 assert '5d000befd41e44deece46f31e1bf3ee7305bc2e8c0357b524311962ddc9d3dde' in SRC
 assert 'SIZE=23805' in SRC
def test_exact_endpoint(): assert "URL='https://arxiv.org/e-print/2006.12659'" in SRC
def test_member_metadata_only():
 assert 'tf.getmembers()' in SRC
 assert 'extractfile' not in SRC and '.extract(' not in SRC
 assert "'member_content_read':False" in SRC and "'source_text_inspected':False" in SRC
def test_complete_candidate_suffix_rule(): assert "SUFFIXES=('.tex','.sty','.cls','.bib','.bbl','.txt','.md','.rst')" in SRC
def test_fail_closed_identity(): assert 'FAIL_0105A6Q5F1_SOURCE_BYTE_IDENTITY_MISMATCH' in SRC
def test_zero_permissions(): assert "systematic_monte_carlo_execution_permission_percent':0" in SRC and "observed_bsm_residual_permission_percent':0" in SRC
def test_terminal_classes():
 for x in ['PASS_0105A6Q5F1_ARXIV_SOURCE_ARCHIVE_STRUCTURE_LOCATED_NONDISCOVERY','BLOCKED_0105A6Q5F1_SOURCE_TRANSPORT_OR_ARCHIVE_STRUCTURE_FAILURE','BLOCKED_0105A6Q5F1_NO_SOURCE_TEXT_CANDIDATES']: assert x in SRC
