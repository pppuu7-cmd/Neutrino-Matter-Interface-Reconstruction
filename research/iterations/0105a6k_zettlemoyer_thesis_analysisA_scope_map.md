# 0105a6k — Zettlemoyer thesis Analysis-A scope-map result

Date: 2026-09-10
Scope: **NONDICOVERY / SCOPE-MAP ONLY**

## Frozen gate

Preregistration: `research/prereg/0105a6k_zettlemoyer_thesis_analysisA_scope_map_preregistration.md`

Preregistration commit: `b0dfb320210ec10654de600819bcf9a6e1c3d4d6`

The gate used only the exact 0105a6j institutional dissertation bytes and a prospectively frozen anchor/scoring/cluster rule to identify a future contiguous semantic-audit interval. It did not classify likelihood semantics, execute a fit, or inspect any observed BSM/model-agnostic residual.

## Hosted execution provenance

- execution head: `d714a0d7fe6490567bcb007ba3b1c66bde663229`
- workflow run: `34494682427`
- job: `102929983821`
- artifact: `10159251542`, `nmir-v2-0105a6k-zettlemoyer-analysisA-scope-map`
- artifact size: `3489` bytes
- artifact ZIP digest: `sha256:dba1006dd49dc863f8e1cef95c2fbefa424f41c7bc66f93d438f81ad46b49eb4`
- inner `result.json` SHA256: `5d12e129e0fcdcea63ae7329e86310e7339162713d62ace7bffab01e5c37ad30`
- deterministic guards: `5 passed`

## Exact source identity

- expected bytes: `34641327`
- observed bytes: `34641327`
- expected SHA256: `6dd2fde86601dea28d323fc38e289935723ad1bf0f8c5f2dcfd845fe2e6badf9`
- observed SHA256: `6dd2fde86601dea28d323fc38e289935723ad1bf0f8c5f2dcfd845fe2e6badf9`
- physical PDF pages: `186`

The source-identity gate therefore passed exactly. No transport or byte mismatch occurred.

## Frozen mechanical page-map outcome

Core-hit pages were:

`14, 15, 132, 133, 134, 137, 144, 145, 146, 147, 148, 149, 150, 156, 158, 161, 165`.

The prospectively frozen ranking selected the dominant cluster:

`132, 133, 134, 137, 144, 145, 146, 147, 148, 149, 150, 156, 158, 161, 165`.

For that cluster:

- first core page: `132`
- last core page: `165`
- core-span width: `34`
- core-hit count: `15`
- support hits inside the core span: `3`
- summed anchor score in the core span: `92`
- frozen padded future interval: physical PDF pages `129–168`
- padded interval width: `40`

The preregistration required the selected future interval to be at most `30` physical PDF pages. Because `40 > 30`, the terminal class is:

`BLOCKED_0105A6K_ANALYSISA_SCOPE_NOT_UNIQUELY_MAPPED`

## Interpretation

This is a **scope-selection BLOCKED**, not a provenance failure and not a scientific/physics FAIL. The exact thesis bytes remain provenance-qualified by 0105a6j, and the mechanical map clearly localizes a dominant high-density Analysis/statistics region. However, the frozen first-pass cluster rule chains hits across too broad a physical-page span to authorize a semantic audit under the preregistered 30-page ceiling.

The interval must not be shortened manually after seeing this result. Any narrower scope must be selected by a new prospectively frozen deterministic refinement gate operating only on the already-emitted page scores/cluster metadata, without reading thesis text or changing likelihood semantics.

## Authority ceiling

- `collaboration_release_authority = false`
- `secondary_collaboration_author_source = true`
- `thesis_semantic_audit_permission = 0%` under 0105a6k
- `SM_NULL_REPRODUCTION_PERMISSION = 0%`
- `OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`
