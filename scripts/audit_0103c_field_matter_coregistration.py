#!/usr/bin/env python3
import json

TERMINAL_BLOCK = "BLOCKED_0103_BETELGEUSE_COHERENT_MAGNETO_MATTER_STATE_AUTHORITY"


def run_audit():
    matter = {
        "model_id": "25_79_0p005_ml",
        "family": "Farmer_25Msun_presupernova",
        "role": "0100_matter_source_environment",
    }
    field = {
        "model_id": "DORCH_2004_NONLINEAR_MHD_NOT_RECOVERED",
        "family": "Betelgeuse_like_star_in_a_box",
        "role": "0103_candidate_magnetic_authority",
    }
    same_model_identity = matter["model_id"] == field["model_id"]
    co_located_state_available = False
    independent_mapping_authority_available = False
    mixed_model_terminal_allowed = False
    posthoc_rescaling_allowed = False

    gates = {
        "matter_identity_explicit": bool(matter["model_id"]),
        "field_identity_explicit": bool(field["model_id"]),
        "model_mismatch_recognized": not same_model_identity,
        "co_located_state_not_falsely_claimed": not co_located_state_available,
        "mapping_authority_not_falsely_claimed": not independent_mapping_authority_available,
        "mixed_model_terminal_forbidden": not mixed_model_terminal_allowed,
        "posthoc_rescaling_forbidden": not posthoc_rescaling_allowed,
    }
    terminal_admissible = (
        same_model_identity and co_located_state_available
    ) or independent_mapping_authority_available
    gates["current_sources_not_terminal"] = not terminal_admissible

    result = {
        "audit": "NMIR-0103C-FIELD-MATTER-COREGISTRATION",
        "matter_source": matter,
        "field_source": field,
        "same_model_identity": same_model_identity,
        "co_located_matter_field_state_available": co_located_state_available,
        "independent_mapping_authority_available": independent_mapping_authority_available,
        "mixed_model_terminal_allowed": mixed_model_terminal_allowed,
        "posthoc_rescaling_allowed": posthoc_rescaling_allowed,
        "current_combination_class": "MIXED_MODEL_ROBUSTNESS_ONLY",
        "terminal_admissible": terminal_admissible,
        "terminal_status": TERMINAL_BLOCK,
        "gates": gates,
    }
    result["status"] = (
        "PASS_0103C_CLASSIFICATION_EXPECTED_BLOCK"
        if all(gates.values()) and result["terminal_status"] == TERMINAL_BLOCK
        else "FAIL_0103C_CLASSIFIER"
    )
    return result


if __name__ == "__main__":
    result = run_audit()
    print(json.dumps(result, indent=2, sort_keys=True))
    if result["status"] != "PASS_0103C_CLASSIFICATION_EXPECTED_BLOCK":
        raise SystemExit(1)
