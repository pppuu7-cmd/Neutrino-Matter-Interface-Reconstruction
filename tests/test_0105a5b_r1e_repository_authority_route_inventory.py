from pathlib import Path

SCRIPT = Path('scripts/audit_0105a5b_r1e_repository_authority_route_inventory.py').read_text()
PREREG = Path('research/prereg/0105a5b_r1e_repository_authority_route_inventory_preregistration.md').read_text()


def test_frozen_markers_and_terms_present():
    for s in ['0105a5b', 'r1d', 'external computational authority', 'upstream authority']:
        assert repr(s) in SCRIPT or f"'{s}'" in SCRIPT
    for s in ['response matrix','derivative table','nuisance response','systematic response','systematic derivative','likelihood code']:
        assert s in SCRIPT


def test_self_and_recovery_files_excluded():
    assert 'research/NMIR_V2_CURRENT_FRONT.md' in SCRIPT
    assert 'research/NMIR_V2_RECOVERY.md' in SCRIPT
    assert '0105a5b_r1e_repository_authority_route_inventory' in SCRIPT


def test_no_network_import_or_calls():
    assert 'urllib' not in SCRIPT
    assert 'requests' not in SCRIPT
    assert 'httpx' not in SCRIPT


def test_zero_permissions_and_no_execution():
    for literal in [
        "'network_requests_executed': False",
        "'external_files_acquired': False",
        "'links_followed': False",
        "'standard_3nu_executed': False",
        "'systematic_monte_carlo_executed': False",
        "'observed_bsm_residual_inspected': False",
        "'observed_bsm_residual_permission_percent': 0",
        "'systematic_monte_carlo_execution_permission_percent': 0",
    ]:
        assert literal in SCRIPT


def test_gate_is_inventory_only():
    assert 'PASS_0105A5B_R1E_REPOSITORY_AUTHORITY_ROUTE_INVENTORY_EMITTED_NONDISCOVERY' in SCRIPT
    assert 'does **not** decide whether any hit is scientifically sufficient or unconsumed' in PREREG
