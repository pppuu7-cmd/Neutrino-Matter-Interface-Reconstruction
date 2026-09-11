from pathlib import Path
SCRIPT=Path('scripts/audit_0105a5b_r1m1_csms2011_archive_structure.py').read_text()
PREREG=Path('research/prereg/0105a5b_r1m1_csms2011_archive_structure_preregistration.md').read_text()
def test_frozen_input_and_hash():
    assert "URL='https://export.arxiv.org/e-print/1106.3723v1'" in SCRIPT
    assert "EXPECTED_SHA256='274b459c38d54c7b874a3353c622f9c807a1e55dcd2fc27214541e2d9f6015ce'" in SCRIPT
def test_complete_extension_rule_is_frozen():
    assert "EXTS=('.tex','.ltx','.txt','.bib','.sty','.cls')" in SCRIPT
    assert "m.isfile() and m.name.lower().endswith(EXTS)" in SCRIPT
def test_member_payload_is_never_read():
    assert '.extractfile(' not in SCRIPT and '.extract(' not in SCRIPT
    assert "'member_payload_read':False" in SCRIPT and "'source_text_inspected':False" in SCRIPT
def test_permissions_closed():
    for token in ["'csms_nuisance_semantics_inferred':False","'standard_3nu_executed':False","'systematic_monte_carlo_executed':False","'observed_bsm_residual_inspected':False","'observed_bsm_residual_permission_percent':0","'systematic_monte_carlo_execution_permission_percent':0"]: assert token in SCRIPT
    assert 'PASS_0105A5B_R1M1_CSMS2011_ARCHIVE_STRUCTURE_LOCATED_NONDISCOVERY' in SCRIPT
    assert 'INFRASTRUCTURE_FAIL_0105A5B_R1M1' in SCRIPT
def test_prereg_byte_lock():
    assert '274b459c38d54c7b874a3353c622f9c807a1e55dcd2fc27214541e2d9f6015ce' in PREREG
