# 0105a5b R1m3 — prospective CSMS→B4RITM/IceCube experimental-authority mapping

Date: 2026-09-11
Branch: `research/0105-bsm-residual-reconstruction`
Prerequisite: validated `PASS_0105A5B_R1M2_CSMS2011_PRIMARY_DIS_UNCERTAINTY_SEMANTICS_LOCATED_NONDISCOVERY` only.

## Scientific question
Can the already frozen repository authority corpus establish an experimental DeepCore/IceCube mapping from the primary CSMS DIS uncertainty semantics to a fully computable nuisance contract, without inventing any convention after inspection?

## Prospectively frozen corpus rule
Before any R1m3 target-content inspection, freeze the corpus mechanically as every tracked UTF-8-readable file at the execution commit whose repository path is under `research/`, `data/`, `scripts/`, or `theory/` and whose *path only* contains at least one of the case-insensitive tokens `b4ritm`, `deepcore`, `icecube`, or `0105a5b`. Exclude only R1m3 implementation/test/workflow/output files themselves. No ranking, pruning, or addition based on content is allowed.

The script must emit the complete selected-path inventory and SHA256 for every readable corpus member before semantic classification. Binary/unreadable members are retained in the inventory as unreadable and may not be silently dropped.

## Frozen PASS contract
`PASS_0105A5B_R1M3_CSMS_B4RITM_EXPERIMENTAL_MAPPING_COMPLETE_NONDISCOVERY` requires repository-authorized experimental evidence, in bounded contexts associated with IceCube/DeepCore/B4RITM and CSMS/Cooper-Sarkar/DIS cross-section semantics, for **all** of:

1. exact experimental nuisance identifier or unambiguous named direction;
2. a computable event/reweight transformation (not merely “cross-section uncertainty” prose);
3. sign/orientation convention for the variation;
4. explicit prior/range/amplitude convention;
5. covariance/correlation/normalization convention sufficient to instantiate the nuisance without an analyst-chosen fill-in.

Evidence may span multiple frozen corpus files only when the files provide explicit cross-references making the mapping unambiguous. Mere terminology similarity, generic theory uncertainty, numerical agreement, date proximity, code-output matching, or analyst inference is insufficient.

If any mandatory element is absent or ambiguous, classify exactly:
`BLOCKED_0105A5B_R1M3_CSMS_B4RITM_EXPERIMENTAL_MAPPING_INCOMPLETE`.

Infrastructure/read failures that prevent complete corpus execution classify `INFRASTRUCTURE_FAIL_0105A5B_R1M3`.

## Hard prohibitions
- Do not execute standard 3nu reproduction.
- Do not execute systematic Monte Carlo or pseudo-data generation.
- Do not inspect observed BSM residuals.
- Do not select a nuisance amplitude, sign, covariance, normalization, binning, model family, or threshold.
- Do not inspect network targets or acquire new external content in this gate.
- Do not reinterpret R1l2 Barr BLOCKED as permission for a Barr mapping gate.

## Authorization consequence
A validated R1m3 PASS authorizes only a separately preregistered computational-contract realization/audit using the frozen mapping. It does **not** itself authorize observed residuals or systematic MC. R1m3 BLOCKED leaves DeepCore R1d and standalone 3nu BLOCKED.

`NMIR_V2_DISCOVERY_READINESS: 48%`
`OBSERVED_BSM_RESIDUAL_PERMISSION: 0%`
`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION: 0%`
