import importlib.util
from pathlib import Path
P=Path(__file__).resolve().parents[1]/"scripts"/"audit_0105a6g_argon_direct_file_semantic_recovery.py"
s=importlib.util.spec_from_file_location("a6g",P); a6g=importlib.util.module_from_spec(s); s.loader.exec_module(a6g)

def test_parent_manifest_identity_is_frozen():
    assert a6g.PARENT_MANIFEST_SHA256=="5ccaea9ae1b59cb60d0db0a28b98a334d8fb32fb39a436301126a32fcd523091"

def test_exact_ar_authority_identity():
    assert a6g.AR_RECORD=="3903810"
    assert a6g.AR_DOI=="10.5281/zenodo.3903810"
    assert a6g.EXPECTED_AR_FILES==24

def test_direct_provider_prefix_only():
    text=P.read_text()
    assert 'https://zenodo.org/records/{AR_RECORD}/files/' in text
    assert "mirror" not in text.lower()

def test_no_analysis_permission_or_fit_execution():
    text=P.read_text().lower()
    assert '"sm_null_reproduction_permission_percent":0' in text
    assert '"observed_bsm_residual_permission_percent":0' in text
    assert 'scientific_semantic_pass_classified":false' in text
    assert "minimize(" not in text and "fitto(" not in text

def test_semantic_terms_cover_frozen_fields():
    required={"likelihood","profile","constraint","correlation","covariance","systematic","background","efficiency","parameter"}
    assert required.issubset(set(a6g.TERMS))
