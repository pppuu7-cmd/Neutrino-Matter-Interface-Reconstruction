# 0105a6q5a1 — ORNL release-page structure diagnostic preregistration

Date: 2026-09-11
Gate: `NMIR-V2-0105A6Q5A1`
Scope: transport/page-structure provenance diagnostic only; NONDISCOVERY.

## Parent

Parent q5a validated record: `research/iterations/0105a6q5a_argon_official_release_provenance_inventory_blocked_20260911.md`, record commit `d7c888741d0c7c807c5cdfa8c6083593ac8a1b47`.
Parent class: `BLOCKED_0105A6Q5A_ORNL_RELEASE_ROUTE_FAILURE` with ORNL HTTP 200 but frozen `matching_anchor_count=0`; local 0105a3, Zenodo and arXiv predicates PASS.

## Question

Without changing q5a, what anchor/link structure is actually exposed by the already-frozen first-party page `https://coherent.ornl.gov/data-releases/`, and is Zenodo record `3903810` present in href metadata despite failure of q5a's visible-text predicate?

## Frozen endpoint

Only `https://coherent.ornl.gov/data-releases/` may be requested. Same-provider redirects are allowed. No discovered href may be followed.

## Frozen extraction

Parse HTML anchors only. Retain for each anchor: ordinal index, whitespace-collapsed visible text, literal href, resolved hostname/path/query/fragment, and booleans for: visible text contains `data release`; visible text contains `argon`; href targets Zenodo record `3903810` using `/record/3903810` or `/records/3903810`; href hostname is `zenodo.org` or `www.zenodo.org`.

Do not retain surrounding paragraphs, scientific prose, abstracts, PDFs, plots or linked payloads.

## Frozen terminal classes

- `PASS_0105A6Q5A1_ORNL_ZENODO_3903810_LINK_STRUCTURALLY_PRESENT_NONDISCOVERY` iff HTTP 200 and at least one anchor href explicitly targets Zenodo record 3903810.
- `BLOCKED_0105A6Q5A1_ORNL_ZENODO_3903810_LINK_NOT_PRESENT` iff HTTP 200 but no anchor href targets record 3903810.
- `BLOCKED_0105A6Q5A1_ORNL_PAGE_TRANSPORT_FAILURE` iff the endpoint cannot be fetched under the frozen transport rule.

No result from q5a1 retroactively changes q5a. A q5a1 PASS authorizes only a separately preregistered repaired provenance predicate based on structural href identity; it does not authorize q5b code/text inspection.

## Artifact contract

Retain requested/final URL, HTTP status, redirect count, response byte count/SHA256/content-type, total anchor count, filtered anchor metadata defined above, classification, git/prereg provenance and hard-guard booleans.

## Prohibitions

No linked-resource fetch; no release-file download/re-hash; no scientific semantic inspection; no pseudo-data; no likelihood; no nuisance profiling; no systematic MC; no observed residual/BSM inspection.

`SYSTEMATIC_MONTE_CARLO_PREREGISTRATION_PERMISSION = 0%`
`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION = 0%`
`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`