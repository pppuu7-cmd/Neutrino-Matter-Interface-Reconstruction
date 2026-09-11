from pathlib import Path
SRC=Path('scripts/audit_0105a6q5c_argon_official_semantic_four_file_byte_lock.py').read_text()

def test_prereg_bound():
    assert 'dc855ab6367ecb7ac095ac2e7d36db358cef8b2a' in SRC

def test_complete_four_file_set_and_urls():
    for n in ['CENNS10AnlAEfficiency.txt','readYAMLParameters.py','PlotExtractedData.C','LArParametersAnlA.yaml']:
        assert n in SRC
        assert f'https://zenodo.org/api/records/3903810/files/{n}/content' in SRC

def test_frozen_sha256_identities():
    for h in ['21ce25451c1ed552752ff4a22496deab3ff5dba178bf360813eaff1d25be89e2','3f1660c54987b9d87f47eda2d19306c2fd061ada72cfb7d3857d996164dd3cd6','c669946d425148fab271d97f99d079b83dbd8f060fea3dd57ac7e00ebecf7d5f','a206a77220436d0173c4783ae8fddeab97adf5e144f3d65005eff0870257693e']:
        assert h in SRC

def test_exact_identity_checks_are_conjunctive():
    assert 'sm=len(b)==size; mm=md5==emd5; hm=sha==esha' in SRC
    assert 'if not (sm and mm and hm): mismatch=True' in SRC

def test_redirects_remain_zenodo_only():
    assert "h=='zenodo.org' or h.endswith('.zenodo.org')" in SRC
    assert "raise RuntimeError('cross-provider redirect')" in SRC

def test_file_contents_not_persisted():
    assert "'files':{}" in SRC
    assert "Path(a.output).write_bytes(data)" in SRC
    assert 'write_bytes(b)' not in SRC
    assert "'content':b" not in SRC

def test_hard_science_guards_and_permissions_zero():
    for x in ["scientific_content_inspected':False","pseudo_data_generated':False","likelihood_evaluated':False","observed_bsm_residual_inspected':False","systematic_monte_carlo_preregistration_permission_percent':0","systematic_monte_carlo_execution_permission_percent':0","observed_bsm_residual_permission_percent':0"]:
        assert x in SRC

def test_frozen_terminal_classes():
    for x in ['PASS_0105A6Q5C_ARGON_OFFICIAL_FOUR_SEMANTIC_FILES_BYTE_LOCKED_NONDISCOVERY','BLOCKED_0105A6Q5C_ZENODO_DIRECT_TRANSPORT_FAILURE','FAIL_0105A6Q5C_OFFICIAL_BYTE_IDENTITY_MISMATCH']:
        assert x in SRC
