# NMIR v2 0105a6q4fs1 — IUScholarWorks metadata endpoint/query-contract probe preregistration

Date frozen: 2026-09-11
Branch: `research/0105-bsm-residual-reconstruction`
Parent authority state: q4fr PASS; q4fs BLOCKED with zero candidates. q5g2 remains BLOCKED for F1/F7.

## Purpose

Prospectively validate a stable official IUScholarWorks repository REST metadata-discovery endpoint and its generic query parameter contract **without searching for Benjamin Suh, the dissertation title, 2025, or any target-specific token**. This is transport/API-contract authority only.

## Frozen institutional provenance

Official repository UI: `https://scholarworks.iu.edu/dspace/`.
Observed official-host REST content is served under `https://scholarworks.iu.edu/iuswrrest/api/`.

Freeze the candidate metadata-discovery endpoint before execution as:

`https://scholarworks.iu.edu/iuswrrest/api/discover/search/objects`

The future target locator, if and only if this gate PASSes, may use only the standard metadata-only discovery query key `query` plus pagination key `size`; the exact target query string must be prospectively frozen in a later gate before it is sent.

## Frozen q4fs1 request

Perform exactly one GET to the frozen endpoint with a deliberately non-target generic impossible sentinel query:

- `query=NMIR_ENDPOINT_CONTRACT_SENTINEL_0105A6Q4FS1`
- `size=1`
- `Accept: application/json`

The sentinel contains no author/title/year/dissertation scientific-content token and cannot identify the Suh target.

Record requested URL, final URL, HTTP status, content type, response byte count, SHA256, and whether the response is parseable JSON. If JSON, record only top-level keys and HAL `_links` relation names plus whether a search result container/object list can be located structurally. Do not retain or inspect item metadata payloads beyond what is needed to establish the generic response schema; with the impossible sentinel, returned target items are not expected.

## Frozen classifications

PASS: `PASS_0105A6Q4FS1_IUSCHOLARWORKS_METADATA_ENDPOINT_CONTRACT_VALIDATED_NONDISCOVERY` iff transport is HTTP 200, response is JSON, and the response exposes a machine-readable DSpace discovery/search structure sufficient to prospectively define a later metadata-only exact target query.

BLOCKED: `BLOCKED_0105A6Q4FS1_IUSCHOLARWORKS_METADATA_ENDPOINT_TRANSPORT_OR_SCHEMA_UNAVAILABLE` for non-200 transport, non-JSON response, or absence of a machine-readable discovery/search structure.

FAIL: `FAIL_0105A6Q4FS1_UNEXPECTED_TARGET_CONTENT_EXPOSURE` if the response unexpectedly contains any case-insensitive frozen target literal: `Benjamin Suh`, `Benjamin D. Suh`, or `Towards an improved measurement of the CEVNS process with the CENNS-10 LAr Detector`.

## Hard prohibitions

No target-specific repository search. No item UUID inference. No bitstream/file URL construction or following. No PDF/file download. No dissertation text inspection. No pseudo-data generation, likelihood evaluation, nuisance profiling, systematic Monte Carlo, observed residual construction, BSM fit, significance calculation, or Wilks threshold.

A PASS permits only a separately prospectively preregistered metadata-only target locator with exact author/year/title query semantics frozen before execution.

`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION: 0%`
`OBSERVED_BSM_RESIDUAL_PERMISSION: 0%`
