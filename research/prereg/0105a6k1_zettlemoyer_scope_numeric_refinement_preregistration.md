# 0105a6k1 — Zettlemoyer Analysis-A scope numeric-refinement preregistration

Status: **PREREGISTERED / NONDISCOVERY / NUMERIC-SCOPE-REFINEMENT ONLY**

## Purpose

Refine the 0105a6k 40-page blocked scope using **only the already-emitted numeric page scores and cluster metadata** from the immutable 0105a6k artifact. This gate must not re-download, extract, search, read, render, or otherwise inspect the thesis PDF or any thesis text.

The goal is to obtain a deterministic <=30-page future semantic-audit interval without manual page trimming or post-hoc anchor changes.

## Frozen parent evidence

Only this exact parent artifact is allowed:

- parent gate: `0105a6k`
- run/job: `34494682427/102929983821`
- artifact ID: `10159251542`
- artifact name: `nmir-v2-0105a6k-zettlemoyer-analysisA-scope-map`
- artifact ZIP SHA256: `dba1006dd49dc863f8e1cef95c2fbefa424f41c7bc66f93d438f81ad46b49eb4`
- parent `result.json` SHA256: `5d12e129e0fcdcea63ae7329e86310e7339162713d62ace7bffab01e5c37ad30`
- parent exact thesis SHA256: `6dd2fde86601dea28d323fc38e289935723ad1bf0f8c5f2dcfd845fe2e6badf9`

Any artifact/result hash mismatch => transport/evidence BLOCKED.

## Frozen parent region

The algorithm may operate only inside the parent-selected winning cluster's inclusive core span. No secondary cluster may be substituted.

From the parent result, the expected winning core span is mechanically read, not hard-coded as a scientific choice. Parent metadata currently records a 34-page core span with 15 core hits and 3 support hits inside that span; those values must be re-derived from the verified parent JSON.

## Frozen 24-page window rule

The parent semantic ceiling was 30 pages and its prospectively frozen context padding was ±3 pages. Therefore the refinement core-window width is fixed to:

`30 - 3 - 3 = 24 physical PDF pages`.

For every possible inclusive 24-page window fully contained in the verified parent winning core span, compute this lexicographic ranking tuple:

1. number of parent `core_hit=true` pages inside the window — larger wins;
2. number of parent `support_hit=true` pages inside the window — larger wins;
3. sum of parent `A+S+Y` scores over all 24 pages — larger wins;
4. negative window start page — earlier wins only as final deterministic tie-break.

Select exactly one winning 24-page core window.

The frozen future semantic interval is then:

`[window_start - 3, window_end + 3]`

with PDF boundaries applied only if necessary. For the present non-boundary parent region, this should be exactly 30 pages wide.

## Representativeness guard

A refined interval may PASS only if the selected 24-page core window contains at least:

- `ceil(2/3 * N_parent_core_hits)` of the parent winning cluster's core-hit pages; and
- `ceil(2/3 * N_parent_support_hits_in_core_span)` of its support-hit pages.

This guard prevents a narrow but unrepresentative local peak from replacing the broader mechanically identified Analysis/statistics region.

## PASS/BLOCKED rule

PASS requires all of:

- exact parent artifact ZIP and inner JSON hashes verified;
- parent classification exactly `BLOCKED_0105A6K_ANALYSISA_SCOPE_NOT_UNIQUELY_MAPPED`;
- parent source SHA256 still equals the 0105a6j thesis identity;
- a verified parent winning cluster exists and has span width >30 but >=24;
- a unique deterministic winning 24-page window is produced under the frozen rank rule;
- the representativeness guard passes;
- padded future interval width <=30 pages;
- no thesis PDF/text is accessed by this gate.

PASS class:

`PASS_0105A6K1_ZETTLEMOYER_SCOPE_NUMERIC_REFINEMENT_NONDISCOVERY`

Otherwise:

`BLOCKED_0105A6K1_SCOPE_REFINEMENT_NOT_REPRESENTATIVE_OR_NONUNIQUE`

Evidence transport/hash/runtime failure:

`BLOCKED_0105A6K1_PARENT_EVIDENCE_TRANSPORT_OR_IDENTITY`

## Authority ceiling

Even PASS authorizes only a later, separately preregistered semantic audit of the exact selected contiguous interval:

- `collaboration_release_authority = false`
- `secondary_collaboration_author_source = true`
- `sm_null_reproduction_permission_percent = 0`
- `observed_bsm_residual_permission_percent = 0`

No likelihood completeness field is evaluated here.
