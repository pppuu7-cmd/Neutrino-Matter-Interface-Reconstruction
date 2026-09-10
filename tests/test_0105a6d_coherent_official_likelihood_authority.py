from pathlib import Path

P = Path('scripts/audit_0105a6d_coherent_official_likelihood_authority.py').read_text()
R = Path('research/prereg/0105a6d_coherent_official_likelihood_implementation_authority.md').read_text()
A = Path('research/amendments/0105a6d_a_hosted_inventory_split.md').read_text()


def test_frozen_provider_scope():
    for token in ('1228631', '3903810', '1708.01294v1', '2003.10630v7'):
        assert token in P and token in R


def test_no_scientific_unlock_in_inventory():
    assert 'observed_bsm_residual_permission_percent": 0' in P
    assert 'sm_null_reproduction_permission_percent": 0' in P
    assert 'semantic_completeness_classified": False' in P
    assert 'OBSERVED_BSM_RESIDUAL_PERMISSION = 0%' in R
    assert 'SM_NULL_REPRODUCTION_PERMISSION = 0%' in R


def test_inventory_split_and_terms_are_frozen():
    assert 'PASS_0105A6D_STAGE_A_OFFICIAL_AUTHORITY_INVENTORY_NONDISCOVERY' in P
    assert 'PASS_0105A6D_STAGE_A_OFFICIAL_AUTHORITY_INVENTORY_NONDISCOVERY' in A
    for token in ('RooNLLVar', 'RooAddPdf', 'RooDataHist', 'Poisson', 'Gaussian constraint', 'fitTo'):
        assert token.lower() in P.lower()
