from pathlib import Path
S=Path('scripts/audit_0105a5b_r1j1_pisa_methodology_archive_structure.py').read_text()
P=Path('research/prereg/0105a5b_r1j1_pisa_methodology_archive_structure_preregistration.md').read_text()
def test_frozen_source():
 assert '1803.05390' in S and 'e8d26d85195764037765661fb2e5236ec4284a712adbfd9738b7c3908593c6be' in S
 assert 'e8d26d85195764037765661fb2e5236ec4284a712adbfd9738b7c3908593c6be' in P
def test_classes():
 for c in ['PASS_0105A5B_R1J1_PISA_METHODOLOGY_ARCHIVE_STRUCTURE_LOCATED_NONDISCOVERY','BLOCKED_0105A5B_R1J1_NO_SOURCE_TEXT_CANDIDATES','INFRASTRUCTURE_FAIL_0105A5B_R1J1']: assert c in S
def test_no_member_payload_read():
 assert 'extractfile' not in S and '.read()' in S  # only HTTP response body is read
def test_permissions_zero():
 for x in ["'source_text_inspected':False","'pisa_repository_content_inspected':False","'standard_3nu_executed':False","'systematic_monte_carlo_executed':False","'observed_bsm_residual_inspected':False"]: assert x in S
