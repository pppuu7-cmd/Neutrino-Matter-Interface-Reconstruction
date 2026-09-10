# 0105a6f — COHERENT Ar implementation-contract semantic closure

Date: 2026-09-10
Gate: `NMIR-V2-0105A6F`
Parent evidence: 0105a6d Ar source-byte PASS within an overall CsI-transport BLOCKED gate
Stage: official authority semantic classification only; NONDISCOVERY

## Purpose

Determine prospectively whether the already byte-validated official COHERENT CENNS-10 Ar assets uniquely specify the standalone Standard-Model/null statistical implementation well enough to authorize a separate numerical reproduction gate. This gate itself performs no likelihood minimization and no observed residual calculation.

## Frozen authority scope

Only these exact official/provider assets are admissible:

1. COHERENT Ar Zenodo data release record `3903810`, DOI `10.5281/zenodo.3903810`;
2. exact arXiv source archive `2003.10630v7`, already observed at SHA256 `2edeb3dcc3df99de575c8b2091f48099a7538eedf9f382996d943c7fbe7e2114`;
3. within that source archive, `main.tex` SHA256 `9e7785c68173921361722af9b95d99c05ff2cdafbf7565fc6b8a057b626b2c86` and `supplemental.tex` SHA256 `183ec77ea668c91611fef8f8e117f3796e36eed36d27026608d1830b11a60a57`;
4. official record-3903810 text-decodable analysis/configuration assets, especially `LArParametersAnlA.yaml`, `readYAMLParameters.py`, `PlotExtractedData.C`, nominal component PDFs and their released systematic-variation PDFs.

No secondary phenomenology/reanalysis code, generic RooFit conventions, or analyst-chosen priors are admissible.

## Frozen semantic fields

The audit must classify each field independently as `COMPLETE`, `PARTIAL`, or `ABSENT`, with byte/member path and literal context locators:

F1. **Objective family** — exact elementary likelihood/NLL/fit construction used for the released Analysis A result.
F2. **Expected components and domains** — signal/background components and their energy/F90/time or other normalization domains.
F3. **Nuisance parameter contract** — every nuisance required by the released fit, its units/sign, nominal value and constraint/penalty semantics.
F4. **Shape/rate coupling** — executable or mathematically complete mapping of each nuisance to rate/template/shape deformation.
F5. **Profiling/floating/fixed prescription** — which parameters are profiled/floated/fixed and how the optimum is obtained.
F6. **Correlation/covariance prescription** — required correlations/covariance, or an explicit statement that the relevant constraints are independent.
F7. **Published numerical reproduction benchmark** — at least one collaboration-published quantity tied to this exact analysis that can be frozen prospectively for a later reproduction tolerance.

A keyword hit alone is not semantic completion. The source context must uniquely determine the field without importing common practice.

## Deterministic extraction

The hosted audit must:

- re-fetch `2003.10630v7` from official arXiv source/e-print endpoints and require the exact frozen archive SHA256;
- require exact SHA256 for `main.tex` and `supplemental.tex` as above;
- fetch record `3903810` metadata and every provider-listed text-decodable file used as authority;
- record provider checksum, byte size and independent SHA256;
- emit deterministic line-numbered contexts around the frozen locator terms:
  `likelihood`, `NLL`, `RooFit`, `profile`, `fit`, `constraint`, `correlation`, `systematic`, `uncertainty`, `normalization`, `background`, `CEvNS`, `BRN`, `prompt`, `steady`, `F90`, `energy`, `time`;
- emit candidate field mappings but leave scientific PASS/BLOCKED classification to an independent semantic review step.

## PASS/BLOCKED rule

`PASS_0105A6F_ARGON_IMPLEMENTATION_CONTRACT_COMPLETE_NONDISCOVERY` requires **all F1-F7 COMPLETE** from the frozen official scope.

If any field is PARTIAL or ABSENT, classify:
`BLOCKED_0105A6F_ARGON_IMPLEMENTATION_CONTRACT_INCOMPLETE`.

If exact frozen bytes cannot be recovered, classify:
`BLOCKED_0105A6F_ARGON_AUTHORITY_BYTE_OR_TRANSPORT`.

No field may be upgraded by assumption or common statistical practice.

## Authorization

This semantic gate alone cannot run a fit.

`SM_NULL_REPRODUCTION_PERMISSION = 0%`

`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`

Only an independently reviewed all-fields COMPLETE PASS can authorize a new, separately preregistered numerical Ar SM/null reproduction gate. Even then the BSM residual remains locked until the parent 0105 conditions are separately satisfied.
