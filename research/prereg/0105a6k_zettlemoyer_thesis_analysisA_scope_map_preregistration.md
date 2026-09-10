# 0105a6k — Zettlemoyer thesis Analysis-A scope-map preregistration

Status: **PREREGISTERED / NONDISCOVERY / SCOPE-MAP ONLY**

## Purpose

Mechanically identify a single contiguous physical-PDF page interval in the exact 0105a6j byte-locked Zettlemoyer dissertation that is most likely to contain the CENNS-10 / COHERENT Ar Analysis-A statistical implementation. This gate freezes the scope for a later semantic audit and prevents page cherry-picking after seeing implementation details.

This gate does **not** classify likelihood completeness, does not resolve F1/F3/F4/F6/F7, does not execute a fit, and does not inspect any observed BSM/model-agnostic residual.

## Frozen source identity

Only this exact institutional PDF is allowed:

- dissertation: Jacob C. Zettlemoyer, 2020, Indiana University
- DOI: `10.5967/3wza-6w73`
- institutional bitstream identity established by 0105a6j
- exact SHA256: `6dd2fde86601dea28d323fc38e289935723ad1bf0f8c5f2dcfd845fe2e6badf9`
- expected byte length: `34641327`

Any byte mismatch => `BLOCKED_0105A6K_THESIS_BYTE_IDENTITY_MISMATCH` and no text may contribute to the scope map.

## Frozen anchor vocabulary

Case-insensitive, punctuation-normalized anchors:

**Analysis/experiment anchors**
- `analysis a`
- `cenns-10`
- `cenns10`
- `f90`
- `beam-related neutron`
- `beam related neutron`

**Statistical anchors**
- `extended maximum likelihood`
- `maximum likelihood`
- `likelihood`
- `roofit`
- `profile likelihood`
- `gaussian constraint`

**Systematics anchors**
- `systematic uncertainty`
- `systematic uncertainties`
- `quenching factor`
- `energy resolution`
- `acceptance efficiency`

No new anchor may be added after execution.

## Frozen page scoring

For each physical PDF page `p`, after `pdftotext -layout` extraction and lowercase/whitespace normalization:

- `A(p)` = number of distinct analysis/experiment anchors present;
- `S(p)` = number of distinct statistical anchors present;
- `Y(p)` = number of distinct systematics anchors present.

A **core hit** is a page satisfying:

- `A(p) >= 2`, and
- `S(p) >= 1`.

A **support hit** is a page satisfying either:

- `A(p) >= 2` and `Y(p) >= 1`, or
- `S(p) >= 2` and `Y(p) >= 1`.

## Frozen cluster rule

1. Enumerate all core-hit pages in ascending physical-PDF page number.
2. Partition core hits into clusters where consecutive core-hit pages differ by at most `8` physical pages.
3. Score each cluster by the tuple, in this exact lexicographic order:
   - number of core-hit pages (larger wins),
   - number of support-hit pages from first core hit through last core hit inclusive (larger wins),
   - sum of `A+S+Y` over that inclusive core span (larger wins),
   - negative span width (narrower wins),
   - negative first-page number (earlier wins only as final deterministic tie-break).
4. Select exactly one winning cluster.
5. Frozen future semantic interval = `[max(1, first_core-3), min(N_pages, last_core+3)]`.

The ±3-page padding is frozen prospectively to include immediately adjacent definitions/equations without manually selecting favorable pages after seeing content.

## PASS/BLOCKED rule

PASS requires all of:

- exact source SHA256 and byte length match 0105a6j;
- PDF page count is machine-readable and >= 50;
- at least two core-hit pages exist;
- the winning cluster contains at least two core-hit pages;
- the selected future interval is at most 30 physical PDF pages wide;
- the output records every core/support page and score so selection is reproducible.

PASS class:

`PASS_0105A6K_ZETTLEMOYER_ANALYSISA_SCOPE_MAP_NONDISCOVERY`

Otherwise classify fail-closed as:

`BLOCKED_0105A6K_ANALYSISA_SCOPE_NOT_UNIQUELY_MAPPED`

Transport/runtime failures are separately `BLOCKED_0105A6K_SOURCE_TRANSPORT_OR_PDF_EXTRACTION`.

## Authority ceiling

Even PASS means only that a contiguous thesis page interval is frozen for a later semantic audit:

- `collaboration_release_authority = false`
- `secondary_collaboration_author_source = true`
- `thesis_semantic_audit_permission = 100%` only for the selected contiguous interval
- `sm_null_reproduction_permission_percent = 0`
- `observed_bsm_residual_permission_percent = 0`

## Hard prohibitions

- No manual page selection after execution.
- No F1/F3/F4/F6/F7 semantic classification in this gate.
- No likelihood reconstruction or numerical fit.
- No residual calculation or BSM scan.
- No use of thesis text outside the machine-selected interval in the later semantic gate unless a new prospective scope amendment is created first.
