# 0105a6q5c1 — Argon Zenodo content-negotiation transport repair preregistration

Date: 2026-09-11
Gate: `NMIR-V2-0105A6Q5C1`
Scope: transport repair + exact byte identity only; NONDISCOVERY.

## Parent diagnosis

q5c validated record commit `2858c33ebf1d75cfbe82d949d8a838b0815a2cb4` classified `BLOCKED_0105A6Q5C_ZENODO_DIRECT_TRANSPORT_FAILURE`: all four exact Zenodo API content endpoints returned HTTP 406 before payload acquisition while q5c requested `Accept: application/octet-stream`.

## Frozen repair

Repeat exactly the same four q5c URLs, sizes, provider MD5 values and 0105a3 SHA256 values. The only transport change is to omit the explicit `Accept: application/octet-stream` request header and use normal HTTP content negotiation. User-Agent may remain. Redirects remain Zenodo-only.

No endpoint, filename, expected size, MD5, SHA256, provider, candidate set or scientific criterion may change.

## Frozen terminal classes

- `PASS_0105A6Q5C1_ARGON_OFFICIAL_FOUR_SEMANTIC_FILES_BYTE_LOCKED_NONDISCOVERY` iff all four fetches succeed and all exact size+MD5+SHA256 identities match.
- `BLOCKED_0105A6Q5C1_ZENODO_DIRECT_TRANSPORT_FAILURE` if any direct fetch still fails before comparable payload acquisition.
- `FAIL_0105A6Q5C1_OFFICIAL_BYTE_IDENTITY_MISMATCH` if transport succeeds but any exact identity fails.

PASS authorizes only a separately preregistered semantic audit over the complete four-file set. It does not itself authorize systematic MC or observed residual analysis.

`SYSTEMATIC_MONTE_CARLO_PREREGISTRATION_PERMISSION = 0%`
`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION = 0%`
`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`