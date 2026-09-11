# 0105a-q8 preregistration — Zettlemoyer CENNS-10 LAr Analysis-A elementary count-law authority

Date frozen: 2026-09-11
Branch: `research/0105-bsm-residual-reconstruction`
Parent scientific front: 0105a COHERENT observed-vs-null reconstruction, F1 elementary count law
Mode: NONDISCOVERY external-authority audit

## Frozen context

NMIR v1 remains closed and immutable. In NMIR v2, q7 has prospectively resolved F7 (`3152 +/- 25` is the corrected authoritative Analysis-A steady-state input). The remaining COHERENT semantic micro-front is F1: an exact elementary observed/auxiliary count-law construction sufficient to reproduce the CENNS-10 LAr Analysis-A statistical model without inventing an unpublished on/off convention.

The q5g2, q4fs and q4fs2 authority routes are exhausted/BLOCKED. q6 is scope-BLOCKED because CsI counting semantics cannot be transferred into the LAr target. This q8 route may not broaden, reinterpret or repair those earlier routes post hoc.

No observed BSM residual may be inspected and no systematic Monte Carlo may be executed from this preregistration alone.

## Prospectively fixed source identity

Target source, fixed before scientific-content inspection:

- Jacob C. Zettlemoyer, *First Detection of Coherent Elastic Neutrino-Nucleus Scattering on an Argon Target*, PhD dissertation, Indiana University, Department of Physics, May 2020.
- Indiana University persistent item: `https://hdl.handle.net/2022/25448`
- DOI: `https://doi.org/10.5967/3wza-6w73`
- The dissertation is independently listed on the official COHERENT/ORNL thesis index as the 2020 Indiana University PhD thesis on the first argon detection.

Only metadata, title, abstract, repository identity and official COHERENT thesis-list provenance were inspected before this freeze. The target dissertation body/PDF scientific content was not inspected before this preregistration.

## Frozen authority tier and scope

This source is an analysis-member dissertation/institutional primary-adjacent authority tied directly to the CENNS-10 LAr first-detection analysis. It is below the collaboration paper/released-data authority for conflicts, but it is admissible as an independent provenance-qualified route for analysis-construction semantics that may have been omitted from the compressed collaboration publication.

A q8 PASS cannot override any explicit conflicting statement in the final collaboration paper or official released-data documentation. Any conflict is a FAIL/BLOCKED outcome requiring separate adjudication.

## Frozen F1 target

F1 is satisfied by this route only if the dissertation explicitly supplies, for the same CENNS-10 LAr production-run / Analysis-A statistical construction, enough elementary counting semantics to determine the observed-data and steady-state/off-beam auxiliary contribution without an invented convention.

The minimum semantic payload is prospectively fixed as all of the following:

1. an explicit Poisson or mathematically equivalent elementary count/generative likelihood statement for the relevant on-beam and/or auxiliary/off-beam counts;
2. an explicit role for the steady-state/off-beam sample as an auxiliary measurement or count-bearing constraint, not merely as a qualitative background template;
3. an explicit normalization/exposure relation, scale factor, oversampling factor, or equivalent mapping that tells how the auxiliary/off-beam count information enters the Analysis-A steady-state expectation/constraint;
4. unambiguous scope linkage to the first-detection CENNS-10 LAr production data / Analysis A (or an explicitly stated statistically identical construction used for it).

An algebraically equivalent formulation is admissible; exact notation such as `n_on`, `n_off`, `alpha` is not required.

## Frozen classifications

### PASS

`PASS_0105A_Q8_F1_ZETTLEMOYER_LAR_ELEMENTARY_COUNTLAW_LOCATED_NONDISCOVERY`

Only if all four minimum semantic elements above are explicitly present and mutually compatible with the authoritative final collaboration paper/release.

### BLOCKED

`BLOCKED_0105A_Q8_F1_ZETTLEMOYER_LAR_ELEMENTARY_COUNTLAW_INCOMPLETE`

If the dissertation provides only one or more of: profile-likelihood summaries, a Gaussian `N_SS` constraint, a quoted statistical uncertainty, qualitative off-beam/background language, a background PDF/template description, oversampling prose without a count-law mapping, or other partial semantics insufficient to reconstruct the elementary auxiliary count law.

### FAIL

`FAIL_0105A_Q8_F1_ZETTLEMOYER_LAR_ELEMENTARY_COUNTLAW_CONTRADICTED_OR_INAPPLICABLE`

If the dissertation explicitly states a construction incompatible with the frozen F1 target, is tied to a different data-taking/analysis configuration without an explicit crosswalk, or contradicts the final collaboration/release authority in a way that prevents promotion.

## Inspection protocol frozen before target-content read

After this commit only:

1. inspect the dissertation PDF/body for exact terms and equations related to Analysis A, likelihood, steady-state background, off-beam/background windows, Poisson/count likelihood, nuisance constraints, exposure/oversampling/scaling and event totals;
2. preserve page/equation/table references and short quotations or faithful paraphrases;
3. compare any candidate elementary law against the final collaboration paper and official LAr released-data semantics already frozen in the ledger;
4. classify PASS/BLOCKED/FAIL exactly under the above contract;
5. commit an immutable q8 result record before any dependent scientific promotion.

No criterion may be relaxed after inspecting the target content. Absence of the required payload is a scientific BLOCKED result, not permission to infer the missing law from standard statistical practice.

## Authorization consequences

A q8 PASS may close only the F1 authority field and permit the next prospectively frozen COHERENT null-reproduction gate. It does not itself authorize observed BSM residual inspection, systematic Monte Carlo, a Tier-A exact collaboration likelihood claim, or a new BSM model.

A q8 BLOCKED/FAIL leaves F1 unresolved. Any subsequent route must be genuinely independent and prospectively frozen; q5g2/q4fs/q4fs2/q6 may not be recycled under a new label.
