# NMIR v2 Current Front

Last reconciled: 2026-09-10
Repository: `pppuu7-cmd/Neutrino-Matter-Interface-Reconstruction`
Authoritative v2 branch: `research/0105-bsm-residual-reconstruction`

This file tracks NMIR v2 only. Frozen NMIR v1 remains closed at `NMIR_READINESS: 100%` under `research/RECOVERY.md` and must not be reopened or rewritten.

## v2 objective

Prospectively test whether independent neutrino propagation and finite-momentum-transfer scattering authorities contain a nuisance-orthogonal, low-complexity residual that can be mapped to one common microscopic neutrino-matter operator and then make a successful held-out prediction.

Required order:

`authority/provenance lock -> standalone SM/3nu/null reproduction -> nuisance-cleaned residual -> model-agnostic reconstruction -> frozen model-family mapping -> common microscopic operator consistency -> held-out prediction`.

Observed BSM residual execution remains forbidden until a dedicated prospective unlock gate says otherwise.

## Closed pre-data/non-discovery gates

- 0105b: common finite-range propagation/scattering bridge — PASS, NONDISCOVERY.
- 0105c: nuisance-orthogonal residual geometry and cross-regime rank complementarity — PASS in synthetic pre-data scope, NONDISCOVERY.
- 0105d: multi-target composition/range identifiability — PASS, NONDISCOVERY. Ar+Cs and Ar+I have nonzero composition determinants; absolute normalization is required for unique mediator-range recovery.
- 0105e: local fixed-absolute-covariance range-information kernel — PASS, NONDISCOVERY. The pre-data kernel peaks at `m_X = q`; this is not a universal experimental sensitivity law.

## Authority front

### COHERENT

- 0105a2: official collaboration/ORNL semantic route to CsI Zenodo `1228631` and Ar Zenodo `3903810` — PASS.
- 0105a3: prospectively frozen complete 37-file direct byte lock (13 CsI + 24 Ar) — currently `BLOCKED` by Zenodo transport in the recorded hosted execution. This is an authority/transport block, not a scientific null or FAIL. Do not substitute calibration dataset `10.13139/OLCF/1969085` or a secondary mirror without a new prospective authority rule.

### IceCube DeepCore

Frozen Stage-A propagation authority: Dataverse `10.7910/DVN/B4RITM`, release `1.0`. `10.7910/DVN/QKL28Z` is a separate sterile-control authority and is forbidden as a substitute.

- 0105a4 metadata inventory: PASS; run/job/artifact `34418458353/102688456198/10129986472`.
- 0105a4b: invalid parent-inventory/transcription path preserved as historical block.
- 0105a4c: archival-vs-original checksum block preserved as historical diagnostic; default Dataverse tabular access cannot be treated as provider-original bytes.
- 0105a4d Saved Original byte lock: **PASS**.
  - prereg `f8265c78e6caed6615eb6a1f620e7a711b629c9c`
  - execution head `7fa83c288181c20c9e9417fc231bee00767404b9`
  - run/job `34428678301/102719279680`
  - artifact `10133622404`
  - artifact digest `sha256:ec78634fd8c07ec1f36d5ce5922008dbfb1457fdcf0204f4df924e3724223436`
  - inner manifest SHA256 `e0c1d4d88234160b7ee443cea3d38979c84d4f9c3ac50dc12f815c60f7fdda1c`
  - exact 11 files; 9 `?format=original`, 2 direct; 11/11 provider MD5, size and SHA256 gates passed.
  - immutable result: `research/iterations/0105a4d_deepcore_b4ritm_original_representation_byte_lock_result.md`, commit `5c7f788097e3371c4414db9cca39e02fc2ec41d4`.

Baseline repository integrity on execution trigger head also passed: run/job `34428678229/102719279393`. It is CI evidence only, not a scientific PASS.

## Current authorization

DeepCore exact-byte authority is now sufficient to begin a separately prospectively preregistered standard-3nu/null reproduction gate.

COHERENT complete byte authority remains transport-blocked at 0105a3, so no combined propagation+CEvNS observed residual is authorized.

`OBSERVED_BSM_RESIDUAL_PERMISSION: 0%`

## Exact next gates

1. Prospectively freeze DeepCore 0105a5b standard-3nu/null reproduction using collaboration/publication-authorized binning, oscillation convention, likelihood/objective, detector/flux/cross-section/background nuisance semantics and numerical benchmark(s). Only after the prereg is frozen may scientific payload content be consumed for this reproduction.
2. In parallel, continue only authority-preserving COHERENT 0105a3 transport recovery; do not replace the frozen event releases or file set.
3. Do not inspect or fit a BSM/model-agnostic residual yet.

## Stable interpretation guards

Green CI is not a scientific PASS. A reproduction gate must match prospectively frozen collaboration/publication benchmarks within its frozen criterion. Missing covariance/nuisance authority is `BLOCKED`, not permission to invent a covariance. Do not use post-result bin selection, nuisance deletion, re-normalization, operator selection or generic Wilks thresholds to manufacture a residual. 0105b-e are mathematical/pre-data results and are not evidence that BSM physics exists.

## Readiness accounting

- DeepCore authority lock: 100% for the scoped B4RITM byte-authority task.
- COHERENT authority byte lock: not closed; transport BLOCKED.
- 0105 pre-data mathematical layer: strongly developed, but NONDISCOVERY.
- NMIR v2 discovery-readiness: approximately 46% on the current stable scale; do not increase for documentation or CI alone.
- Current DeepCore null-reproduction task: 0% scientific execution at creation of this ledger; preregistration is next.
