from pathlib import Path
SRC=Path('scripts/audit_0105a6q5b_argon_official_release_semantic_file_locator.py').read_text()
def test_prereg(): assert '8fb5121c97918b726a95f3440a1f15b5457c751d' in SRC
def test_exact_record(): assert "URL='https://zenodo.org/api/records/3903810'" in SRC and "len(files)==24" in SRC
def test_frozen_rule():
    assert "SUFFIXES=('.py','.c','.cc','.cpp','.h','.yaml','.yml','.json')" in SRC
    assert "TOKENS=('parameter','efficien','likelihood','fit','roo','plot','extract','systematic')" in SRC
def test_no_file_fetch(): assert 'urlopen(req' in SRC and 'urlopen(links' not in SRC and "release_file_bytes_downloaded':False" in SRC
def test_zero_permissions():
    for x in ["systematic_monte_carlo_preregistration_permission_percent':0","systematic_monte_carlo_execution_permission_percent':0","observed_bsm_residual_permission_percent':0"]: assert x in SRC
def test_classes():
    assert 'PASS_0105A6Q5B_ARGON_OFFICIAL_SEMANTIC_FILE_CANDIDATES_LOCATED_NONDISCOVERY' in SRC
    assert 'BLOCKED_0105A6Q5B_NO_SEMANTIC_FILE_CANDIDATES' in SRC
