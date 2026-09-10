# 0105a6l — Zettlemoyer Analysis-A semantic-evidence preflight preregistration

Status: **PREREGISTERED / NONDISCOVERY / MACHINE-TEXT-EVIDENCE PREFLIGHT**

## Purpose

Search only the 0105a6k1-authorized 30-page contiguous interval of the exact 0105a6j institutional dissertation for machine-readable evidence relevant to the unresolved 0105a6i implementation fields F1/F3/F4/F6/F7.

This is deliberately **not a terminal semantic-authority gate**. Machine text extraction/pattern matches may establish that candidate evidence exists and identify its physical PDF pages, but cannot by themselves upgrade the thesis to collaboration-release authority or authorize a numerical fit.

## Frozen source and scope

Only:

- exact thesis SHA256 `6dd2fde86601dea28d323fc38e289935723ad1bf0f8c5f2dcfd845fe2e6badf9`;
- exact byte length `34641327`;
- physical PDF pages **129–158 inclusive**, frozen by 0105a6k1.

No page outside 129–158 may be extracted or searched.

## Frozen evidence families

All matching is case-insensitive after whitespace/punctuation normalization. The audit records page numbers and boolean feature families, not long thesis excerpts.

### L0 — Analysis-A implementation linkage
Candidate linkage requires at least one scoped page containing `analysis a` together with at least one of `likelihood`, `roofit`, `fit`, `systematic`, or `background`.

### F1 — elementary likelihood/statistical law
Candidate explicit evidence requires at least one scoped page containing `likelihood` plus at least one elementary-construction marker:

- `poisson`
- `unbinned`
- `binned likelihood`
- `extended likelihood`
- `extended maximum likelihood`
- `product of probabilities`
- `probability density function`

`RooFit` alone is insufficient.

### F3 — nuisance inventory/constraints
Candidate explicit evidence requires at least one scoped page containing a nuisance/constraint marker (`nuisance`, `gaussian constraint`, `constraint`, `prior`, `float`, `profile`) and at least two distinct Analysis-A component markers among:

- `cevns`
- `steady state`
- `beam related neutron`
- `prompt`
- `delayed`
- `quenching factor`
- `energy resolution`
- `acceptance efficiency`

### F4 — nuisance-to-template coupling/morphing
Candidate explicit evidence requires a scoped page containing a template/PDF/systematic marker and at least one coupling marker:

- `interpolat`
- `morph`
- `vertical morph`
- `horizontal morph`
- `template variation`
- `shape variation`
- `vary the shape`
- `varied shape`

The mere presence of nominal and ±1σ templates is insufficient.

### F6 — systematic combination/correlation
Candidate explicit evidence requires a scoped page containing `systematic` plus at least one combination marker:

- `simultaneous`
- `correlat`
- `covariance`
- `combined`
- `quadrature`
- `independent nuisance`
- `one at a time`
- `alternative fit`

The machine preflight records which marker occurs but does not decide whether that rule is scientifically sufficient.

### F7 — numerical discrepancy/precedence
Record all scoped page hits for exact decimal tokens `3152` and `3154`, plus whether the same page contains `steady state`, `background`, `prediction`, `normalization`, `table`, `analysis a`, or `fit`.

Candidate discrepancy-resolution evidence requires a scoped page containing either 3152 or 3154 and at least one precedence marker:

- `typo`
- `erratum`
- `corrected`
- `should be`
- `instead of`
- `supersede`
- `use 3152`
- `use 3154`

No precedence may be inferred from whichever number happens to appear.

## Output and classifications

The preflight emits:

- exact source identity verification;
- scoped page count and per-page SHA256 of extracted text;
- page numbers for L0/F1/F3/F4/F6/F7 candidate evidence;
- no full-page text and no long excerpts;
- no likelihood numerical evaluation.

If exact source/scope extraction succeeds:

- `PASS_0105A6L_MACHINE_TEXT_EVIDENCE_PREFLIGHT_NONDISCOVERY` if L0 exists and at least one of F1/F3/F4/F6/F7 has candidate explicit evidence;
- `BLOCKED_0105A6L_NO_SCOPED_IMPLEMENTATION_EVIDENCE` if no such evidence is found.

Transport/hash/extraction failure:

`BLOCKED_0105A6L_SOURCE_TRANSPORT_OR_SCOPE_EXTRACTION`.

A PASS only authorizes a later evidence-verification/semantic-authority gate on the **same pages and already-identified evidence families**. It does not mean the implementation contract is complete.

## Hard authority ceiling

- `collaboration_release_authority = false`
- `secondary_collaboration_author_source = true`
- `terminal_semantic_authority_pass = false`
- `sm_null_reproduction_permission_percent = 0`
- `observed_bsm_residual_permission_percent = 0`

## Hard prohibitions

- No pages outside 129–158.
- No observed residual, event-level residual reconstruction, BSM scan, or model fit.
- No terminal F1/F3/F4/F6/F7 COMPLETE classification from regex matches.
- No long thesis excerpt stored in the artifact or repository.
- No post-execution expansion of pattern families; any expansion requires a new prospective gate.
