from pathlib import Path

SCRIPT = Path('scripts/audit_0105a5b_r1l_barr2006_source_bytes.py').read_text()
PREREG = Path('research/prereg/0105a5b_r1l_barr2006_source_bytes_preregistration.md').read_text()


def test_exact_frozen_url_and_no_fallbacks():
    assert "URL='https://export.arxiv.org/e-print/astro-ph/0611266v1'" in SCRIPT
    assert 'fallback' not in SCRIPT.lower()


def test_prohibitions_are_hardcoded_false():
    for key in [
        'archive_opened','member_listed','source_text_inspected',
        'barr_nuisance_semantics_inferred','standard_3nu_executed',
        'systematic_monte_carlo_executed','observed_bsm_residual_inspected'
    ]:
        assert f"'{key}':False" in SCRIPT


def test_permissions_remain_zero():
    assert "'observed_bsm_residual_permission_percent':0" in SCRIPT
    assert "'systematic_monte_carlo_execution_permission_percent':0" in SCRIPT
    assert 'PASS_0105A5B_R1L_BARR2006_SOURCE_BYTES_ACQUIRED_NONDISCOVERY' in SCRIPT
    assert 'INFRASTRUCTURE_FAIL_0105A5B_R1L' in SCRIPT


def test_prereg_matches_target():
    assert 'astro-ph/0611266v1' in PREREG
    assert 'archive-structure/member-name locator' in PREREG
