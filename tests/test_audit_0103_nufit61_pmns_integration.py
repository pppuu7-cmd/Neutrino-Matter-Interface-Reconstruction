from scripts.audit_0103_nufit61_pmns_integration import run_audit


def test_0103_nufit61_pmns_integration_passes_nonterminal():
    result = run_audit()
    assert result["status"] == "PASS_0103_NUFIT61_PMNS_INTEGRATION_NONTERMINAL"
    assert result["both_orderings_carried"] is True
    assert set(result["branches_emitted"]) == {"normal_ordering", "inverted_ordering"}
    assert all(all(branch["gates"].values()) for branch in result["branches"].values())
    assert result["interpretation"]["ordering_postselection_used"] is False
    assert result["interpretation"]["nufit_pdf_byte_pin_closed"] is False
    assert result["interpretation"]["betelgeuse_pathwise_Bperp_authority_closed"] is False
