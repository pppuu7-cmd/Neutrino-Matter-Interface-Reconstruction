# 0105a6c — COHERENT semantic-completeness classification

Date: 2026-09-10
Gate: `NMIR-V2-0105A6C`
Classification: `BLOCKED_0105A6C_EXACT_LIKELIHOOD_SEMANTICS_INCOMPLETE`

## Frozen authority consumed

This classification consumes only the preregistered 0105a6c primary-publication inventory plus the already frozen 0105a6 Stage-A COHERENT release-side authority. It does not construct or minimize a likelihood, inspect an observed residual, fit nuisance parameters, or scan BSM physics.

### 0105a6c hosted inventory
- execution head: `c9b5831c57527ee49da150029f952e3091af354a`
- run/job: `34473348331 / 102858177647`
- dedicated guards: `5 passed`
- artifact: `10150437065`
- provider/independent ZIP SHA256: `6ecaa6b69a2475d4502f6b9906d76f3f8725323fd1d2603fd19d5aec19814a79`
- inner `primary_publication_semantic_inventory.json` SHA256: `2ba663beb37fb3d1617b8db8fcec79891f2579dd520f071b970786cc7d0f198e`
- CsI PDF SHA256: `a47539271203e0d0ea71a45ede2535011bcd2b0cdb2a846beecb1f54302fe9fc`
- Ar PDF SHA256: `2f875bda728739a85a2568db44761d7f164e113e77613d8f884e6c4b071acef2`
- inventory status: `PASS_0105A6C_PRIMARY_PUBLICATION_SEMANTIC_INVENTORY_NONDISCOVERY`

### newest 0105a6 Stage-A hosted authority inventory
- execution head: `066a45fc69bde739c3403b9755c5b490734f5bc5`
- run/job: `34473603556 / 102858999960`
- dedicated guards: `3 passed`
- artifact: `10150542561`
- provider/independent ZIP SHA256: `419306364bdfaaa6e4ed4bfd14818cb483c836a1b1ef8eb4bf34fbd7191cd4a8`
- inner `authority_inventory.json` SHA256: `eea0d8220bff4261a0dc04d9b1c861bce4434f9c76f3ca4fdaaf921f91ded4f8`
- inventory status: `PASS_0105A6_STAGE_A_AUTHORITY_INVENTORY_NONDISCOVERY`

## Frozen completeness test

Per `research/prereg/0105a6c_coherent_primary_publication_semantic_inventory.md`, standalone SM/null reproduction may be authorized only if collaboration authority specifies, without analyst invention:
1. per-bin/data likelihood family and objective;
2. component expectations entering that objective;
3. nuisance parameters, constraint distributions and couplings;
4. profiling/floating prescription;
5. normalization/exposure and detector-response semantics;
6. at least one collaboration numerical benchmark usable for reproduction.

A phrase such as maximum likelihood, a profile curve, or quoted significance is explicitly insufficient to fill a missing elementary likelihood or nuisance wiring.

## Evidence classification

### CsI[Na]
The frozen primary publication supplies a profile-likelihood fit, signal/background component descriptions, an unconstrained CEvNS amplitude, a constrained prompt-neutron rate, a steady-state constraint from AC data, a best-fit benchmark (`134 ± 22` counts; `77 ± 16%` of SM) and a 6.7-sigma null benchmark with toy-MC coverage checks. The frozen release-side files supply binning, detector-response/acceptance semantics, flux/exposure inputs, prompt-neutron normalization uncertainty and other parameter uncertainties.

However, the frozen authority does not literally provide a mathematically complete elementary per-bin likelihood/objective and complete nuisance-penalty/coupling specification sufficient to reconstruct the collaboration fit uniquely. The release companion itself permits a user to calculate a likelihood or chi-square rather than defining one unique collaboration objective. Therefore the exact standalone collaboration likelihood cannot be reconstructed without analyst convention.

### CENNS-10 Ar Analysis A
The frozen primary publication states an extended maximum-likelihood fit to binned `(F90, t_trig, E)` data with components `CEvNS`, `BRN`, and `SS`; it specifies several Gaussian constraints, free/floating choices, pseudo-data validation, best-fit event counts, and null significance. It also defines the profile statistic `-2 Delta ln L` and reports that it is profiled over SS and BRN event counts.

The frozen release-side authority supplies the three-dimensional PDFs, exact binning, central/best-fit normalizations, Gaussian widths for major components, response inputs, exposure and benchmark normalizations.

Nevertheless, the allowed authority still does not provide the complete elementary binned extended-likelihood expression and a uniquely executable wiring of all nuisance/shape-systematic terms and correlations used in Analysis A. The published `-2 Delta ln L` expression is a profile-ratio statistic, not the missing full event/bin objective. Consequently the full collaboration likelihood is not uniquely reproducible under the frozen no-invention rule.

## Classification

`BLOCKED_0105A6C_EXACT_LIKELIHOOD_SEMANTICS_INCOMPLETE`

This is an **authority BLOCKED**, not a scientific FAIL and not evidence against the Standard Model. Both hosted inventories remain NONDISCOVERY PASSes. The blocker is specifically exact collaboration-likelihood/nuisance implementation authority.

`SM_NULL_REPRODUCTION_PERMISSION = 0%`

`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`

No observed residual, new significance, nuisance fit or BSM quantity was computed.

## Exact next allowed gate

A new gate may prospectively seek **official collaboration/provider implementation authority** that closes the missing elementary likelihood and nuisance wiring. It must remain limited to official COHERENT collaboration/provider release assets, publication-linked supplementary material, and exact implementation artifacts with byte/version provenance. Phenomenology reanalyses and generic RooFit/common-practice conventions are forbidden substitutes. If no such implementation authority exists in the prospectively frozen search scope, retain BLOCKED and move to the next independent actionable v2 authority gap.
