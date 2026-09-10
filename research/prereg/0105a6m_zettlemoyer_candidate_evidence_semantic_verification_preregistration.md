# 0105a6m — Zettlemoyer candidate-evidence semantic verification preregistration

Status: **PREREGISTERED / CONDITIONAL ON 0105a6l PASS / NONDISCOVERY / SECONDARY-AUTHOR EVIDENCE ONLY**

## Purpose

If and only if 0105a6l returns `PASS_0105A6L_MACHINE_TEXT_EVIDENCE_PREFLIGHT_NONDISCOVERY`, verify the actual meaning of the candidate evidence that 0105a6l identified for the unresolved 0105a6i fields F1/F3/F4/F6/F7.

This gate is deliberately narrower than a new search. It may inspect only candidate pages already identified by the immutable 0105a6l result. It cannot search additional thesis pages, cannot promote the dissertation to collaboration-release authority, and cannot authorize a numerical fit.

## Dynamic scope frozen before the parent result

The allowed page set is defined mechanically from the immutable 0105a6l artifact:

`allowed_pages = sorted(unique(L0_pages ∪ F1_pages ∪ F3_pages ∪ F4_pages ∪ F6_pages ∪ F7_pages ∪ raw_F7_3152_pages ∪ raw_F7_3154_pages))`.

No other page may be read. If the parent classification is not PASS, this gate must not execute.

The parent artifact identity (run/job/artifact/result SHA256) must be frozen into the execution workflow before evidence extraction. The exact thesis identity remains:

- SHA256 `6dd2fde86601dea28d323fc38e289935723ad1bf0f8c5f2dcfd845fe2e6badf9`;
- byte length `34641327`;
- institutional custody path frozen by 0105a6j.

## Evidence capture rule

For each allowed page, extraction may retain only bounded evidence windows centered on the already-detected marker families. Maximum retained context is **900 normalized characters per evidence family per page**. Full-page text is forbidden in artifacts/repository.

The semantic adjudication must cite page number, matched family and a SHA256 of the normalized page text. Absence of evidence outside the allowed pages may not be inferred.

## Frozen field sufficiency criteria

### F1 — elementary likelihood law

`COMPLETE_SECONDARY_EVIDENCE` requires enough explicit information to reconstruct the elementary data likelihood without choosing a new statistical family. At minimum the evidence must unambiguously identify whether Analysis A is binned or unbinned and whether it is extended, and must identify how observed data enter the likelihood (event-density/product form or bin-count law). The phrases `likelihood`, `maximum likelihood`, `extended maximum likelihood`, or `RooFit` alone are insufficient.

### F3 — nuisance inventory and constraints

`COMPLETE_SECONDARY_EVIDENCE` requires an explicit Analysis-A nuisance inventory sufficient to distinguish all normalization nuisances and all shape/systematic nuisances relevant to the published fit, together with their constrained/floated/profiled status. A list of systematic-error magnitudes or a partial component list is insufficient.

### F4 — nuisance-to-template coupling/morphing

`COMPLETE_SECONDARY_EVIDENCE` requires an explicit mapping from each relevant shape nuisance to the nominal/varied template or PDF, including how intermediate nuisance values are represented or how the variation is otherwise applied in the likelihood. Merely stating that ±1σ templates were produced, or that alternate fits were performed, is insufficient for a unique simultaneous morphing implementation.

### F6 — simultaneous systematic combination/correlation

`COMPLETE_SECONDARY_EVIDENCE` requires an explicit joint rule sufficient to determine which systematic/nuisance effects are varied simultaneously, independently, one-at-a-time, or with correlations/covariance, and how their contributions enter the final likelihood/profile/statistic. `added in quadrature` may describe a published error budget but does not by itself define a simultaneous likelihood nuisance model.

### F7 — `3152 ± 25` versus `3154 ± 25` precedence

`RESOLVED_SECONDARY_EVIDENCE` requires an explicit correction, erratum, typo statement, supersession statement, or direct instruction selecting one value over the other. Repetition of either number, chronology, or apparent consistency with another table cannot establish precedence.

## Classification

Each field is assigned one of:

- `COMPLETE_SECONDARY_EVIDENCE`
- `PARTIAL_SECONDARY_EVIDENCE`
- `NO_SECONDARY_EVIDENCE`
- for F7 only, `RESOLVED_SECONDARY_EVIDENCE` or `UNRESOLVED_SECONDARY_EVIDENCE`.

Overall:

- `PASS_0105A6M_SECONDARY_AUTHOR_SEMANTIC_EVIDENCE_SUFFICIENT_NONDISCOVERY` only if F1, F3, F4 and F6 are `COMPLETE_SECONDARY_EVIDENCE` and F7 is `RESOLVED_SECONDARY_EVIDENCE`;
- otherwise `BLOCKED_0105A6M_SECONDARY_AUTHOR_SEMANTIC_EVIDENCE_INCOMPLETE`.

A PASS means only that this provenance-qualified secondary collaboration-author source contains a complete candidate implementation description suitable for a later **independent corroboration/authority-upgrade gate**. It does not establish collaboration-release authority and does not itself authorize fitting.

## Hard authority ceiling

Always, regardless of semantic content:

- `collaboration_release_authority = false`
- `secondary_collaboration_author_source = true`
- `sm_null_reproduction_permission_percent = 0`
- `observed_bsm_residual_permission_percent = 0`

## Hard prohibitions

- No thesis page outside mechanically inherited 0105a6l candidate pages.
- No post-result expansion of evidence families.
- No inference of missing formulas from RooFit defaults, common practice, or software conventions.
- No numerical likelihood implementation, minimization, fit, residual construction, BSM scan, or model comparison.
- No claim that a dissertation, even by a collaboration author, is itself the official released likelihood.
