# 0105a6q5a2 — Argon official-release structural provenance binding preregistration

Date: 2026-09-11
Gate: `NMIR-V2-0105A6Q5A2`
Scope: authority/provenance only; NONDISCOVERY.

## Parent evidence

q5a remains `BLOCKED_0105A6Q5A_ORNL_RELEASE_ROUTE_FAILURE` under its original visible-text predicate. q5a1 independently passed at record commit `ae59a47532ca0411e315a00a33494a69a5336e70`, showing that the frozen ORNL Data Releases page contains exactly one anchor whose href structurally targets Zenodo record 3903810. q5a1 does not rewrite q5a.

## Frozen authority chain

This gate re-tests the same full public chain as q5a with one prospectively specified ORNL predicate justified by q5a1:

1. local immutable 0105a3 byte-lock identity must match the exact frozen run/job/artifact/digests already used by q5a;
2. `https://coherent.ornl.gov/data-releases/` must return HTTP 200 and contain >=1 HTML anchor whose resolved host is `zenodo.org`/subdomain and whose resolved path is exactly `/record/3903810` or `/records/3903810` (optional trailing slash/fragment/query do not alter record identity); visible anchor text is not a criterion;
3. Zenodo API record 3903810 must satisfy the exact q5a id/DOI/version/title/24-file metadata predicates;
4. arXiv `2006.12659` must satisfy the exact q5a id/title predicate.

Same-provider redirects only. No release file bytes may be downloaded or re-hashed. No scientific release content may be inspected.

## Frozen terminal classes

- `PASS_0105A6Q5A2_ARGON_OFFICIAL_RELEASE_STRUCTURAL_PROVENANCE_BOUND_NONDISCOVERY` iff all four authority predicates pass.
- `BLOCKED_0105A6Q5A2_LOCAL_0105A3_AUTHORITY_BINDING_FAILURE`.
- `BLOCKED_0105A6Q5A2_ORNL_STRUCTURAL_ROUTE_FAILURE`.
- `BLOCKED_0105A6Q5A2_ZENODO_RECORD_METADATA_FAILURE`.
- `BLOCKED_0105A6Q5A2_ARXIV_METADATA_FAILURE`.
- `BLOCKED_0105A6Q5A2_PROVIDER_TRANSPORT_FAILURE`.

PASS authorizes only a new prospectively preregistered q5b release-file locator/semantic-authority step. It does not itself authorize release-file content inspection, null/systematic MC, or observed residual analysis.

`SYSTEMATIC_MONTE_CARLO_PREREGISTRATION_PERMISSION = 0%`
`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION = 0%`
`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`