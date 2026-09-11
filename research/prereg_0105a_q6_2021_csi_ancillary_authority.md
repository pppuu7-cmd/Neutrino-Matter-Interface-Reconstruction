# NMIR 0105a q6 — prospective authority freeze for COHERENT CsI 2021 ancillary material

Date frozen: 2026-09-11
Branch: `research/0105-bsm-residual-reconstruction`
Scope: NONDISCOVERY authority audit only. No observed BSM residual, systematic Monte Carlo, or post-hoc numerical selection is authorized by this preregistration.

## Motivation and independence

The current NMIR v2 front leaves COHERENT 0105a fields F1 and F7 unresolved and records q5g2/q4fs/q4fs2 as exhausted authority-BLOCKED routes. This q6 route is prospectively frozen as a distinct provenance route before inspecting target scientific content.

Metadata-only discovery identified the official COHERENT Released Data index as explicitly directing the full 2021 CsI CEvNS dataset to ancillary material attached to COHERENT arXiv:2110.07730 / PRL 129, 081801. The arXiv record independently exposes a collaboration-authored supplementary PDF and machine-readable ancillary files. At freeze time, only bibliographic metadata, provenance, filenames, and the existence of those ancillary files have been inspected for route selection; their target F1/F7 scientific content has not been used to choose or modify the criteria below.

Frozen authority chain:
1. Official COHERENT Released Data index (`sites.duke.edu/coherent/data/`) stating that the full 2021 CsI CEvNS dataset is available as ancillary material for arXiv:2110.07730.
2. COHERENT Collaboration, arXiv:2110.07730, `Measurement of the Coherent Elastic Neutrino-Nucleus Scattering Cross Section on CsI by COHERENT`, including its arXiv-hosted ancillary files and collaboration supplementary PDF.

## Frozen target fields

### F1 — elementary count law
PASS only if a primary/collaboration-authored q6 authority explicitly defines enough of the elementary observed-count construction to determine what is counted and the relevant selection/region/bin aggregation without inventing a convention. A merely reproducible total obtained by reverse engineering files is insufficient unless the collaboration source supplies the semantic rule.

### F7 — role/precedence of `3152` versus `3154`
PASS only if a primary/collaboration-authored q6 authority explicitly identifies the semantic role of both values, or gives an unambiguous version/selection/region relationship that determines which value governs the frozen NMIR reproduction target. Numerical proximity, arithmetic reconstruction, chronology alone, or choosing the value that improves agreement is forbidden.

## Fail-closed classification

- `PASS_0105A_Q6_F1_PRIMARY_COUNT_LAW_LOCATED_NONDISCOVERY` only if the F1 criterion above is met verbatim in substance by primary q6 authority.
- `PASS_0105A_Q6_F7_PRIMARY_3152_3154_PRECEDENCE_LOCATED_NONDISCOVERY` only if the F7 criterion above is met verbatim in substance by primary q6 authority.
- Otherwise the relevant field is `BLOCKED_0105A_Q6_*_PRIMARY_SEMANTICS_INCOMPLETE`.
- Partial semantic evidence must be recorded as evidence, not promoted to PASS.
- q6 may close F1, F7, both, or neither; each field is adjudicated independently.

## No-post-hoc guard

After this commit, q6 target content may be inspected. Criteria, target values, and the required authority level must not be widened in response to what the ancillary files contain. Any newly discovered source not contained in the frozen authority chain requires a new prospective route before its target content can count scientifically.
