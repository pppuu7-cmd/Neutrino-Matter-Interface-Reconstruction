import importlib.util
from pathlib import Path

P = Path(__file__).resolve().parents[1] / "scripts" / "audit_0105a6e_coherent_ornl_example_code_authority.py"
spec = importlib.util.spec_from_file_location("a6e", P)
a6e = importlib.util.module_from_spec(spec)
spec.loader.exec_module(a6e)


def test_provider_is_exact_official_ornl_repo():
    assert a6e.REMOTE == "https://code.ornl.gov/COHERENT/codeExamples_dataRelease_april2018.git"


def test_forbidden_permissions_remain_zero_in_script():
    text = P.read_text()
    assert '"sm_null_reproduction_permission_percent": 0' in text
    assert '"observed_bsm_residual_permission_percent": 0' in text
    assert '"scientific_pass_classified": False' in text


def test_inventory_terms_cover_likelihood_and_nuisance_semantics():
    required = {"likelihood", "poisson", "chi2", "constraint", "profile", "nuisance", "covariance", "background", "efficiency", "quenching"}
    assert required.issubset(set(a6e.TERMS))


def test_binary_decoder_fails_closed():
    assert a6e.decode_text(b"\x00\x01\x02\x03" * 100) is None


def test_term_hits_are_case_insensitive():
    hits = a6e.term_hits("Likelihood POISSON nuisance nuisance")
    assert hits["likelihood"]["count"] == 1
    assert hits["poisson"]["count"] == 1
    assert hits["nuisance"]["count"] == 2
