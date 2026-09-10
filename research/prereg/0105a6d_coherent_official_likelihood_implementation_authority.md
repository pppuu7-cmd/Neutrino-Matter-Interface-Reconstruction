# 0105a6d — COHERENT official likelihood-implementation authority acquisition

Date: 2026-09-10
Gate: `NMIR-V2-0105A6D`
Parent: `BLOCKED_0105A6C_EXACT_LIKELIHOOD_SEMANTICS_INCOMPLETE`
Stage: authority acquisition/inventory only

## Purpose

Prospectively test whether the already-authorized official COHERENT provider chain contains an implementation-level likelihood/nuisance contract that resolves the exact blocker identified by 0105a6c. This gate does not reproduce the SM/null likelihood and cannot inspect an observed BSM residual.

## Frozen authority scope

Only the following provider families are admissible:

1. official COHERENT CsI[Na] Zenodo data release record `1228631`, preserving the already validated collaboration -> Zenodo provenance and all provider-listed files for that exact record;
2. official COHERENT CENNS-10 Ar data release record `3903810`, preserving the already validated collaboration -> Zenodo provenance and all provider-listed files for that exact record;
3. exact arXiv source archives for the byte-pinned primary publications `1708.01294v1` and `2003.10630v7`, used only to inspect source/supplement implementation statements corresponding to the already frozen PDFs.

No calibration-only release may replace a CEvNS event release. No secondary phenomenology/reanalysis repository, generic RooFit tutorial, or common-practice likelihood convention is admissible authority.

## Frozen required implementation contract

For either target to resolve its 0105a6c blocker, official authority must uniquely specify enough to implement the collaboration standalone SM/null fit without analyst invention:

- elementary data likelihood family/objective, including whether the released binned data enter through a Poisson-product, unbinned/extended construction, chi-square, or another exact form;
- exact expected components and their bin/domain normalization in that objective;
- every nuisance parameter needed by the released analysis, its constraint/penalty distribution, sign/units and coupling to rate or shape;
- profiling/floating/fixed prescription;
- any required correlations/covariance or explicit statement of independence;
- an executable or mathematically complete rule connecting release templates/response assets to the objective;
- at least one collaboration-published numerical benchmark already frozen by 0105a6c for a later reproduction tolerance.

A filename/phrase hit is a locator only. `likelihood`, `RooFit`, `chi2`, `Poisson`, or `Gaussian` text alone is not a PASS.

## Deterministic inventory

Before execution, freeze the following searches over every text-decodable provider asset and arXiv source member:

`likelihood`, `loglikelihood`, `log likelihood`, `nll`, `RooFit`, `RooNLLVar`, `RooAddPdf`, `RooDataHist`, `Poisson`, `chi2`, `chi-square`, `Gaussian constraint`, `constraint`, `profile`, `nuisance`, `covariance`, `correlation`, `Minuit`, `fitTo`.

The result must emit provider identity, filename/source-member path, provider checksum where available, computed SHA256, byte size, deterministic term hits, and exact source-archive SHA256 for both arXiv archives.

## Classification

- `PASS_0105A6D_OFFICIAL_IMPLEMENTATION_AUTHORITY_NONDISCOVERY`: official frozen assets contain a uniquely executable implementation contract satisfying all required fields for at least one target; PASS must identify the exact bytes/member paths and field-by-field authority.
- `BLOCKED_0105A6D_OFFICIAL_IMPLEMENTATION_AUTHORITY_ABSENT_OR_INCOMPLETE`: transport and bytes are valid but the frozen official scope does not uniquely specify the required implementation contract.
- `BLOCKED_0105A6D_AUTHORITY_BYTE_MISMATCH_OR_TRANSPORT`: an exact frozen provider/source asset cannot be retrieved or identity cannot be established.
- `INFRASTRUCTURE_FAIL_0105A6D`: runtime/tool failure before the authority inventory is complete.

No criterion may be weakened after output inspection.

`SM_NULL_REPRODUCTION_PERMISSION = 0%`

`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`

## Forbidden operations

No construction/minimization of a likelihood; no nuisance fit; no new significance; no observed-minus-null residual; no BSM scan; no choice of bins, priors, correlations, thresholds or operator families from observed data.

## Next gate rule

Only an independently validated 0105a6d PASS can authorize a separate prospectively frozen numerical standalone COHERENT SM/null reproduction gate for the target(s) whose implementation contract is complete. A BLOCKED result does not authorize filling missing semantics from common practice.
