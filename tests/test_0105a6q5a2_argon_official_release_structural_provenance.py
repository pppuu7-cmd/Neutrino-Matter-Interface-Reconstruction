from pathlib import Path
SRC=Path('scripts/audit_0105a6q5a2_argon_official_release_structural_provenance.py').read_text()

def test_prereg_bound(): assert '2897bd6c6d55f312dd4ab07cd528d4f3a3fa33fa' in SRC
def test_structural_record_identity():
    assert "re.fullmatch(r'/(?:record|records)/3903810',path)" in SRC
    assert "host=='zenodo.org' or host.endswith('.zenodo.org')" in SRC
def test_reuses_frozen_q5a_non_ornl_predicates():
    assert 'base.check_local' in SRC and 'base.inspect_zenodo' in SRC and 'base.inspect_arxiv' in SRC
def test_hard_no_science_guards():
    for x in ["release_file_bytes_downloaded':False","release_file_bytes_rehashed':False","scientific_release_content_inspected':False","pseudo_data_generated':False","likelihood_evaluated':False","observed_bsm_residual_inspected':False"]: assert x in SRC
def test_permissions_zero():
    assert "systematic_monte_carlo_preregistration_permission_percent':0" in SRC
    assert "systematic_monte_carlo_execution_permission_percent':0" in SRC
    assert "observed_bsm_residual_permission_percent':0" in SRC
def test_terminal_classes_frozen():
    for x in ['PASS_0105A6Q5A2_ARGON_OFFICIAL_RELEASE_STRUCTURAL_PROVENANCE_BOUND_NONDISCOVERY','BLOCKED_0105A6Q5A2_ORNL_STRUCTURAL_ROUTE_FAILURE','BLOCKED_0105A6Q5A2_PROVIDER_TRANSPORT_FAILURE']: assert x in SRC
