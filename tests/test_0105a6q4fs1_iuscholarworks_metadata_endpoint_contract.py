from pathlib import Path

SCRIPT=Path('scripts/audit_0105a6q4fs1_iuscholarworks_metadata_endpoint_contract.py').read_text()
PREREG=Path('research/prereg/0105a6q4fs1_iuscholarworks_metadata_endpoint_contract_preregistration.md').read_text()


def test_endpoint_and_sentinel_frozen():
    assert "https://scholarworks.iu.edu/iuswrrest/api/discover/search/objects" in SCRIPT
    assert "NMIR_ENDPOINT_CONTRACT_SENTINEL_0105A6Q4FS1" in SCRIPT
    assert "query" in PREREG and "size" in PREREG


def test_target_literals_are_failure_guards_not_query():
    assert "target_specific_search_executed':False" in SCRIPT
    assert "FAIL_0105A6Q4FS1_UNEXPECTED_TARGET_CONTENT_EXPOSURE" in SCRIPT
    assert "urllib.parse.urlencode({'query':SENTINEL,'size':'1'})" in SCRIPT


def test_scientific_prohibitions_zero():
    for literal in [
        "'pdf_downloaded':False", "'pdf_content_inspected':False",
        "'likelihood_evaluated':False", "'pseudo_data_generated':False",
        "'systematic_monte_carlo_executed':False", "'observed_bsm_residual_inspected':False",
        "'systematic_monte_carlo_execution_permission_percent':0",
        "'observed_bsm_residual_permission_percent':0",
    ]:
        assert literal in SCRIPT


def test_frozen_classifications_present():
    assert 'PASS_0105A6Q4FS1_IUSCHOLARWORKS_METADATA_ENDPOINT_CONTRACT_VALIDATED_NONDISCOVERY' in SCRIPT
    assert 'BLOCKED_0105A6Q4FS1_IUSCHOLARWORKS_METADATA_ENDPOINT_TRANSPORT_OR_SCHEMA_UNAVAILABLE' in SCRIPT
