# 0105a6q5f — exact arXiv:2006.12659 source byte acquisition preregistration

Date: 2026-09-11
Gate: `NMIR-V2-0105A6Q5F`
Scope: additional provenance-qualified methodology authority acquisition only; NONDISCOVERY.

## Authorization and rationale

q5e is validated `BLOCKED_0105A6Q5E_ARGON_RELEASE_SEMANTIC_CONTRACT_INCOMPLETE`; its exact four-file official-release semantic route is exhausted for F1/F4/F6/F7. q5a2 independently bound exact arXiv publication `2006.12659` into the validated public provenance chain. No equivalent active q5f source route was found in the current repository state.

The next genuinely additional authority is therefore the **exact source bundle of the already-bound collaboration publication arXiv:2006.12659**, selected by pre-existing provenance rather than by its unseen contents.

## Frozen acquisition endpoint and transport

Request only `https://arxiv.org/e-print/2006.12659`. Redirects are allowed only within the `arxiv.org` domain family. Do not request alternate versions after observing the payload. Record requested/final URL, HTTP status, response byte count, content type, ETag/Last-Modified if supplied, MD5 and SHA256 of the exact returned bytes.

This gate must not inspect source text, extract archive members, search keywords, compile TeX, evaluate likelihoods or inspect event residuals. It may only check that a non-empty payload was returned by the exact frozen arXiv source endpoint and record its immutable byte identity.

## Frozen terminal classes

- `PASS_0105A6Q5F_ARXIV_2006_12659_SOURCE_BYTES_ACQUIRED_NONDISCOVERY` iff the exact endpoint returns HTTP 200 with a non-empty payload and the final host remains in the arXiv.org family.
- `BLOCKED_0105A6Q5F_ARXIV_SOURCE_TRANSPORT_FAILURE` otherwise.

A PASS permits only a separately prospectively frozen source-archive structural/semantic locator that binds to the q5f SHA256 before reading any source member contents. It does not itself change q5e, close F1/F4/F6/F7, authorize systematic MC, or authorize observed residual analysis.

`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION = 0%`
`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`