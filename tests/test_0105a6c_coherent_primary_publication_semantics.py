from scripts.audit_0105a6c_coherent_primary_publication_semantics import (
    PHRASE_FAMILIES,
    TARGETS,
    normalized,
    pages_for_phrases,
    pages_with_near_terms,
)


def test_frozen_publication_hashes_are_exact():
    assert TARGETS["csi"]["sha256"] == "a47539271203e0d0ea71a45ede2535011bcd2b0cdb2a846beecb1f54302fe9fc"
    assert TARGETS["ar"]["sha256"] == "2f875bda728739a85a2568db44761d7f164e113e77613d8f884e6c4b071acef2"


def test_semantic_inventory_families_do_not_encode_completeness():
    required = {
        "maximum_likelihood",
        "extended_maximum_likelihood",
        "binned_fit",
        "cevns_component",
        "prompt_or_beam_neutron",
        "steady_state_background",
        "gaussian_constraint",
        "profile_likelihood",
        "null_or_significance_benchmark",
        "pseudo_validation",
    }
    assert set(PHRASE_FAMILIES) == required
    assert "complete" not in " ".join(PHRASE_FAMILIES)


def test_page_locators_are_deterministic_and_one_based():
    pages = ["No match here", "Extended maximum likelihood fit", "prompt neutron background"]
    assert pages_for_phrases(pages, ["extended maximum likelihood"]) == [2]
    assert pages_for_phrases(pages, ["prompt neutron"]) == [3]


def test_near_term_locator_does_not_conflate_distant_terms():
    assert pages_with_near_terms(["Poisson fit likelihood"], "poisson", "likelihood", 30) == [1]
    far = "Poisson " + ("x" * 100) + " likelihood"
    assert pages_with_near_terms([far], "poisson", "likelihood", 20) == []


def test_normalization_is_format_only():
    assert normalized("Profile\n Likelihood") == "profile likelihood"
