from scripts.audit_0105a6j_zettlemoyer_thesis_provenance_byte_lock import classify

TITLE = "First Detection of Coherent Elastic Neutrino-Nucleus Scattering on an Argon Target"


def good():
    coherent = f"2020 Jacob C. Zettlemoyer (Indiana University): {TITLE} doi 10.5967/3wza-6w73"
    iu = f"Zettlemoyer, Jacob C. {TITLE} Thesis Ph.D. Indiana University Department of Physics 2020 DOI 10.5967/3wza-6w73"
    measurement = "COHERENT Collaboration authors include J. Zettlemoyer"
    pdf = b"%PDF-1.7\n" + b"x" * 30_000_001
    return classify(coherent, iu, measurement, pdf, "https://scholarworks.iu.edu/dspace/bitstreams/id/download", "application/pdf")


def test_complete_provenance_can_pass_only_secondary_ceiling():
    r = good()
    assert r["all_provenance_gates_pass"] is True
    assert r["classification"] == "PASS_0105A6J_ZETTLEMOYER_THESIS_PROVENANCE_BYTE_LOCK_NONDISCOVERY"
    assert r["authority_ceiling"]["collaboration_release_authority"] is False
    assert r["authority_ceiling"]["secondary_collaboration_author_source"] is True


def test_never_unlocks_fit_or_residual():
    r = good()
    assert r["authority_ceiling"]["sm_null_reproduction_permission_percent"] == 0
    assert r["authority_ceiling"]["observed_bsm_residual_permission_percent"] == 0


def test_missing_coherent_index_fails_closed():
    r = classify("unrelated", f"Zettlemoyer, Jacob C. {TITLE} 2020 Indiana University 10.5967/3wza-6w73", "J. Zettlemoyer", b"%PDF" + b"x"*30_000_001, "https://scholarworks.iu.edu/x", "application/pdf")
    assert r["gates"]["P1_coherent_index_identity"] is False
    assert r["all_provenance_gates_pass"] is False


def test_noninstitutional_pdf_fails_custody():
    r = good()
    r2 = classify(f"Jacob C. Zettlemoyer {TITLE} 10.5967/3wza-6w73", f"Zettlemoyer, Jacob C. {TITLE} 2020 Indiana University 10.5967/3wza-6w73", "J. Zettlemoyer", b"%PDF" + b"x"*30_000_001, "https://example.org/copy.pdf", "application/pdf")
    assert r["gates"]["P5_custody_consistency"] is True
    assert r2["gates"]["P5_custody_consistency"] is False


def test_too_small_or_nonpdf_payload_fails_byte_gate():
    r = classify(f"Jacob C. Zettlemoyer {TITLE} 10.5967/3wza-6w73", f"Zettlemoyer, Jacob C. {TITLE} 2020 Indiana University 10.5967/3wza-6w73", "J. Zettlemoyer", b"not a pdf", "https://scholarworks.iu.edu/x", "text/html")
    assert r["gates"]["P4_pdf_byte_acquisition"] is False
    assert r["classification"] == "BLOCKED_0105A6J_ZETTLEMOYER_THESIS_PROVENANCE_OR_BYTE_AUTHORITY_INCOMPLETE"
