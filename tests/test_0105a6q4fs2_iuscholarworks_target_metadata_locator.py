from pathlib import Path

SCRIPT=Path('scripts/audit_0105a6q4fs2_iuscholarworks_target_metadata_locator.py').read_text()
PREREG=Path('research/prereg/0105a6q4fs2_iuscholarworks_target_metadata_locator_preregistration.md').read_text()


def test_exact_endpoint_query_and_size_are_frozen():
    assert "https://scholarworks.iu.edu/iuswrrest/api/discover/search/objects" in SCRIPT
    assert '"Towards an improved measurement of the CEVNS process with the CENNS-10 LAr Detector" "Benjamin Suh" "2025"' in SCRIPT
    assert "SIZE='20'" in SCRIPT
    assert "urllib.parse.urlencode({'query':QUERY,'size':SIZE})" in SCRIPT


def test_exact_identity_only_no_fuzzy_expansion():
    assert "AUTHORS={'benjamin suh','benjamin d. suh'}" in SCRIPT
    assert "norm(v)==norm(TITLE)" in SCRIPT
    assert 'No fuzzy/semantic search expansion' in PREREG


def test_no_link_or_file_following_and_zero_science_permissions():
    for literal in [
        "'item_links_followed':False", "'identifier_guessed_or_constructed':False",
        "'file_or_bitstream_downloaded':False", "'dissertation_scientific_text_inspected':False",
        "'likelihood_evaluated':False", "'pseudo_data_generated':False",
        "'systematic_monte_carlo_executed':False", "'observed_bsm_residual_inspected':False",
        "'systematic_monte_carlo_execution_permission_percent':0",
        "'observed_bsm_residual_permission_percent':0",
    ]:
        assert literal in SCRIPT


def test_only_one_network_request_site_in_implementation():
    assert SCRIPT.count('urllib.request.urlopen(')==1


def test_frozen_classifications_present():
    assert 'PASS_0105A6Q4FS2_IUSCHOLARWORKS_TARGET_METADATA_UNIQUE_MATCH_NONDISCOVERY' in SCRIPT
    assert 'BLOCKED_0105A6Q4FS2_IUSCHOLARWORKS_TARGET_METADATA_NOT_UNIQUELY_RESOLVED' in SCRIPT
