# NMIR v2 0105a5b-R1h — IceCube-source MCEq version discriminator

Date frozen: 2026-09-11
Parent: validated R1g `PASS_0105A5B_R1G_MCEQ_HISTORICAL_RELEASE_LINEAGE_BYTE_LOCKED_NONDISCOVERY`.

## Purpose
Determine whether the already-authorized IceCube analysis publication source itself explicitly distinguishes exactly one member of the complete frozen 11-candidate historical MCEq lineage, before any MCEq implementation/source inspection.

## Frozen authority corpus
Only the exact public source bundle for IceCube analysis `arXiv:2304.12236` may be acquired from `https://export.arxiv.org/e-print/2304.12236`. No other publication, web search result, MCEq README, documentation, source/blob/tree/archive, or DeepCore output may be inspected by this gate.

The R1g candidate set is frozen unchanged:
`mceq108`, `mceq_1_1_1`, `release_1_1_2`, `release_1_1_3`, `release_1_2_0`, `release_1_2_1`, `release_1_2_2`, `release_1_2_3`, `release_1_2_4`, `release_1_2_5`, `release_1_2_6`.

## Frozen locator rule
After transport succeeds, inspect only text-like source members (`.tex`, `.txt`, `.bib`, `.sty`, `.cls`). For each candidate, search case-insensitively for either its literal tag or the mechanically derived semantic version forms `MCEq X.Y.Z`, `MCEq vX.Y.Z`, `MCEq version X.Y.Z`, and `version X.Y.Z` only when `MCEq` occurs within 160 characters of that version occurrence. For `mceq108`, X.Y.Z=`1.0.8`; for later tags derive X.Y.Z directly from the numeric suffix.

Record candidate/member/matched-form and a maximum 320-character context window only. Do not search for additional version forms after viewing results.

## Classification
`PASS_0105A5B_R1H_ICECUBE_MCEQ_VERSION_UNIQUELY_DISCRIMINATED_NONDISCOVERY` iff exactly one frozen candidate has at least one qualifying match and all matches resolve to that same candidate.

`BLOCKED_0105A5B_R1H_ICECUBE_MCEQ_VERSION_NOT_UNIQUELY_DISCRIMINATED` iff zero or more than one frozen candidates match.

Transport/archive parsing failures are `INFRASTRUCTURE_FAIL_0105A5B_R1H`.

A PASS is authority/provenance only: it may identify which already-frozen MCEq state is explicitly named by IceCube, but does not authorize MCEq implementation inspection by itself, does not define Barr nuisance transformations, and does not close DIS/CSMS authority. A subsequent implementation-inspection gate must be separately preregistered.

Hard prohibitions: no MCEq source/README/tree/blob/archive inspection; no version choice by numerical agreement; no standard-3nu; no systematic MC; no observed residual; no BSM scan.

`OBSERVED_BSM_RESIDUAL_PERMISSION: 0%`
`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION: 0%`
