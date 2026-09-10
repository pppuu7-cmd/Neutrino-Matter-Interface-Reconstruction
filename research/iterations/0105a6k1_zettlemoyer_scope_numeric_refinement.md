# 0105a6k1 — Zettlemoyer Analysis-A scope numeric-refinement result

Date: 2026-09-10
Scope: **NONDICOVERY / NUMERIC-SCOPE-REFINEMENT ONLY**

## Frozen gate

Preregistration: `research/prereg/0105a6k1_zettlemoyer_scope_numeric_refinement_preregistration.md`

Preregistration commit: `83dd52043e91229fd41c73711cf802eda71fdc2a`

The gate consumed only the verified numeric page-score evidence emitted by 0105a6k. It did not download, extract, render, search, read, or otherwise access the thesis PDF/text.

## Hosted execution provenance

- execution head: `3842a5404a4715ac2d816fb97923d866466a054d`
- workflow run: `34495029313`
- job: `102931170588`
- artifact: `10159389799`, `nmir-v2-0105a6k1-zettlemoyer-scope-numeric-refinement`
- artifact size: `1748` bytes
- artifact ZIP digest: `sha256:ef6deccc8c9bdbc813691dccd5de989ef82a08b3d0257ada6af3a295f339a308`
- inner `result.json` SHA256: `1964bcf3b688cde22ffc52cba956f3b47d232972051decd204a604aff0d9b64c`
- deterministic guards: `5 passed`

## Parent evidence identity

The workflow independently downloaded and verified the exact frozen 0105a6k artifact:

- parent artifact ZIP expected/observed SHA256: `dba1006dd49dc863f8e1cef95c2fbefa424f41c7bc66f93d438f81ad46b49eb4`
- parent `result.json` expected/observed SHA256: `5d12e129e0fcdcea63ae7329e86310e7339162713d62ace7bffab01e5c37ad30`
- `pdf_or_thesis_text_accessed = false`.

## Frozen numeric-refinement outcome

Verified parent winning core span: physical PDF pages `132–165`.

- parent core-hit count: `15`
- parent support-hit count inside that core span: `3`
- representativeness requirement: at least `10/15` core hits and `2/3` support hits
- candidate 24-page windows: `11`
- top-rank tie: `false`

The unique winning 24-page core window is:

`132–155`

It contains:

- `11/15` parent core-hit pages: `132, 133, 134, 137, 144, 145, 146, 147, 148, 149, 150`;
- `2/3` parent support-hit pages: `137, 150`;
- anchor-score sum: `66`;
- frozen rank tuple: `[11, 2, 66, -132]`.

The representativeness guard therefore passed.

Applying the prospectively frozen ±3-page context padding gives the exact future semantic-audit interval:

**physical PDF pages `129–158` inclusive**

with exact width `30` pages.

Terminal classification:

`PASS_0105A6K1_ZETTLEMOYER_SCOPE_NUMERIC_REFINEMENT_NONDISCOVERY`

## Consequence

A later, separately preregistered thesis-semantic audit may inspect **only physical PDF pages 129–158 inclusive** from the exact 0105a6j PDF identity `6dd2fde86601dea28d323fc38e289935723ad1bf0f8c5f2dcfd845fe2e6badf9`.

This PASS does not itself establish any likelihood semantics and does not upgrade the thesis to collaboration-release authority.

## Authority ceiling

- `collaboration_release_authority = false`
- `secondary_collaboration_author_source = true`
- `THESIS_SEMANTIC_AUDIT_PERMISSION = 100%` only for physical PDF pages `129–158`
- `SM_NULL_REPRODUCTION_PERMISSION = 0%`
- `OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`
