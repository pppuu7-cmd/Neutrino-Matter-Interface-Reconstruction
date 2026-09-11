from pathlib import Path
SRC=Path('scripts/audit_0105a6q5c1_argon_zenodo_content_negotiation_transport_repair.py').read_text()

def test_prereg_bound(): assert 'cf3d7bebc1aae654ec09a78284c6f3162df4f9df' in SRC
def test_all_four_frozen_endpoints_and_hashes():
    for n in ['CENNS10AnlAEfficiency.txt','readYAMLParameters.py','PlotExtractedData.C','LArParametersAnlA.yaml']:
        assert f'https://zenodo.org/api/records/3903810/files/{n}/content' in SRC
    for h in ['21ce25451c1ed552752ff4a22496deab3ff5dba178bf360813eaff1d25be89e2','3f1660c54987b9d87f47eda2d19306c2fd061ada72cfb7d3857d996164dd3cd6','c669946d425148fab271d97f99d079b83dbd8f060fea3dd57ac7e00ebecf7d5f','a206a77220436d0173c4783ae8fddeab97adf5e144f3d65005eff0870257693e']:
        assert h in SRC
def test_only_content_negotiation_repair():
    assert "headers={'User-Agent':'NMIR-q5c1-byte-lock/1.0'}" in SRC
    assert 'application/octet-stream' not in SRC
    assert "explicit_accept_header_used':False" in SRC
def test_exact_identity_conjunction():
    assert 'sm=len(b)==size; mm=md5==emd5; hm=sha==esha' in SRC
    assert 'if not (sm and mm and hm): mismatch=True' in SRC
def test_zenodo_only_redirect(): assert "h=='zenodo.org' or h.endswith('.zenodo.org')" in SRC
def test_no_content_persistence_and_zero_science():
    assert 'write_bytes(b)' not in SRC
    for x in ["scientific_content_inspected':False","pseudo_data_generated':False","likelihood_evaluated':False","observed_bsm_residual_inspected':False","systematic_monte_carlo_preregistration_permission_percent':0","systematic_monte_carlo_execution_permission_percent':0","observed_bsm_residual_permission_percent':0"]: assert x in SRC
def test_terminal_classes():
    for x in ['PASS_0105A6Q5C1_ARGON_OFFICIAL_FOUR_SEMANTIC_FILES_BYTE_LOCKED_NONDISCOVERY','BLOCKED_0105A6Q5C1_ZENODO_DIRECT_TRANSPORT_FAILURE','FAIL_0105A6Q5C1_OFFICIAL_BYTE_IDENTITY_MISMATCH']: assert x in SRC
