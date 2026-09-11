from pathlib import Path

SCRIPT=Path('scripts/audit_0105a5b_r1l1_barr2006_archive_structure.py').read_text()
PREREG=Path('research/prereg/0105a5b_r1l1_barr2006_archive_structure_preregistration.md').read_text()


def test_frozen_input_and_hash():
    assert "URL='https://export.arxiv.org/e-print/astro-ph/0611266v1'" in SCRIPT
    assert "EXPECTED_SHA256='f128800ae1eb18fb58c27ce91941b726f1bbf42a7f7ac17a273664f3a81da0f7'" in SCRIPT


def test_complete_extension_rule_is_frozen():
    assert "EXTS=('.tex','.ltx','.txt','.bib','.sty','.cls')" in SCRIPT
    assert "m.isfile() and m.name.lower().endswith(EXTS)" in SCRIPT


def test_member_payload_is_never_read():
    assert '.extractfile(' not in SCRIPT
    assert '.extract(' not in SCRIPT
    assert "'member_payload_read':False" in SCRIPT
    assert "'source_text_inspected':False" in SCRIPT


def test_scientific_permissions_remain_closed():
    for token in ["'barr_nuisance_semantics_inferred':False","'standard_3nu_executed':False","'systematic_monte_carlo_executed':False","'observed_bsm_residual_inspected':False","'observed_bsm_residual_permission_percent':0","'systematic_monte_carlo_execution_permission_percent':0"]:
        assert token in SCRIPT
    assert 'PASS_0105A5B_R1L1_BARR2006_ARCHIVE_STRUCTURE_LOCATED_NONDISCOVERY' in SCRIPT
    assert 'INFRASTRUCTURE_FAIL_0105A5B_R1L1' in SCRIPT


def test_prereg_requires_byte_verification_before_archive_parse():
    assert 'Before any archive parsing' in PREREG
    assert 'f128800ae1eb18fb58c27ce91941b726f1bbf42a7f7ac17a273664f3a81da0f7' in PREREG
