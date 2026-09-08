#!/usr/bin/env python3
import json
from pathlib import Path

LOW_E = 6.845530367110015e-6
HIGH_E_EXCLUSIVE = 1.0
UNRESOLVED = {
    "cerdeno": "BLOCKED_CERDENO_MASS_SUPPORT_ONLY_AUTHORITY",
    "coherent": "BLOCKED_COHERENT_MASS_SUPPORT_ONLY_AUTHORITY",
    "fifth_force": "BLOCKED_FIFTH_FORCE_FINITE_MASS_SUPPORT_AUTHORITY",
}
DISJOINT = {
    "na64": "PROVABLY_MASS_DISJOINT_FROM_0087B_LOWMASS_TARGET",
    "bbn_below_1eV": "NO_ACCEPTED_0087B_SUPPORT_OVERLAP_BELOW_1EV",
}

def classify(unresolved=None):
    unresolved = dict(UNRESOLVED if unresolved is None else unresolved)
    if unresolved:
        classification = "BLOCKED_RESTRICTED_BELOW_1EV_COMPLETENESS"
        complete_allowed_region = False
        bsm_unlock = False
        statement = (
            "Accepted authority supports only a restricted below-1-eV partial-authority topology statement; "
            "it does not certify a complete allowed component because unresolved Cerdeño, COHERENT, and "
            "finite-mass fifth-force support could overlap the domain and have no accepted disjointness authority."
        )
    else:
        classification = "PASS_RESTRICTED_BELOW_1EV_PARTIAL_AUTHORITY_CERTIFICATION"
        complete_allowed_region = False
        bsm_unlock = False
        statement = (
            "A precisely scoped below-1-eV partial-authority certification is defensible, but it is not a global "
            "or complete external envelope and does not unlock BSM response."
        )
    return {
        "gate": "0087g",
        "classification": classification,
        "domain_eV": {"min_inclusive": LOW_E, "max_exclusive": HIGH_E_EXCLUSIVE},
        "accepted_disjoint_or_nonoverlap": DISJOINT,
        "unresolved_completeness_blockers": unresolved,
        "blocked_family_as_null_assumption": False,
        "complete_allowed_region_certified": complete_allowed_region,
        "global_external_envelope_certified": False,
        "bsm_response_unlock": bsm_unlock,
        "statement": statement,
    }

def main():
    result = classify()
    out = Path("restricted_below_1eV_completeness_0087g.json")
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
