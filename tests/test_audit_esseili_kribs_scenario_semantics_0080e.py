from scripts.audit_esseili_kribs_scenario_semantics_0080e import classify_text, combination_candidate_contexts


BASE = r'''
Our Delta N_eff calculations have been carried out in two scenarios: neutrinos have Dirac masses, or, right-handed neutrinos acquire Majorana masses.
This ``Dirac case'' is one of the two cases we will consider in this paper.
The alternative, ``Majorana case'', is one where the right-handed neutrinos acquire Majorana masses.
\caption{Calculations of $\dneff$ for the ``Majorana'' neutrino case.}
\caption{Same as figure 5, but for the ``Dirac'' neutrino case.}
'''


def test_alternative_scenarios_pass_without_composition_rule():
    r = classify_text(BASE)
    assert r["classification"] == "PASS_COSMOLOGY_B_L_SCENARIO_CONDITIONAL_AUTHORITY"
    assert all(r["checks"].values())
    assert r["explicit_common_combination_rule_detected"] is False
    assert r["common_combination_candidate_contexts"] == []


def test_explicit_result_combination_is_not_silently_treated_as_alternatives():
    text = BASE + " For the final constraint, we combine the Majorana and Dirac case results with equal weight."
    r = classify_text(text)
    assert r["classification"] == "PASS_COSMOLOGY_B_L_COMMON_COMBINATION_AUTHORITY"
    assert r["explicit_common_combination_rule_detected"] is True
    assert len(r["common_combination_candidate_contexts"]) == 1


def test_model_building_combined_dirac_mass_phrase_is_not_a_constraint_combination():
    text = BASE + " When combined with the Dirac mass terms, Majorana masses lead to the usual see-saw formula."
    assert combination_candidate_contexts(text) == []
    assert classify_text(text)["classification"] == "PASS_COSMOLOGY_B_L_SCENARIO_CONDITIONAL_AUTHORITY"


def test_missing_alternative_authority_blocks():
    text = BASE.replace("The alternative, ``Majorana case'', is one where the right-handed neutrinos acquire Majorana masses.\n", "")
    r = classify_text(text)
    assert r["classification"] == "BLOCKED_COSMOLOGY_B_L_SCENARIO_SEMANTICS"
