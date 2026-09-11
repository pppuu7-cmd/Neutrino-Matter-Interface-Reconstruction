# 0105a5b R1m — CSMS 2011 source-byte acquisition preregistration

Date: 2026-09-11
Branch: `research/0105-bsm-residual-reconstruction`
Scope: NMIR v2 authority work only. NMIR v1 remains frozen at `NMIR_READINESS: 100%`.

## Motivation and frozen provenance

Validated R1e repository inventory recorded the already-cited upstream DIS cross-section authority as `arXiv:1106.3723v1` (CSMS 2011). The current DeepCore R1d seven-direction computational-authority contract remains BLOCKED. R1m is an independent provenance-qualified authority route and is frozen before target-content inspection.

This gate does not infer any DIS/CSMS nuisance implementation, energy interpolation, cross-section reweighting, derivative, normalization, or mapping to the frozen B4RITM directions. It asks only whether the exact cited source bytes can be acquired and immutably locked for a later separately preregistered authority audit.

## Frozen acquisition target

Exact URL: `https://export.arxiv.org/e-print/1106.3723v1`

No fallback mirror, identifier mutation, version substitution, query mutation, DOI/PDF substitution, alternate source, or target-content inspection is permitted inside R1m.

## Allowed operations

R1m may only:

1. issue one HTTP GET to the exact frozen URL with a fixed user-agent;
2. record HTTP status, final URL, content type and byte count;
3. compute MD5 and SHA256 over the opaque response bytes;
4. emit an immutable JSON result plus artifact hashes.

## Hard prohibitions

R1m must not:

- open the returned archive/container;
- list members;
- decode/search/read source text;
- infer CSMS nuisance semantics or transformations;
- inspect DeepCore residuals;
- run standard 3nu;
- run systematic Monte Carlo;
- inspect any observed BSM residual.

## Frozen classification

`PASS_0105A5B_R1M_CSMS2011_SOURCE_BYTES_ACQUIRED_NONDISCOVERY` iff HTTP status is 200 and the opaque payload is nonempty.

Transport/network/non-200/empty-payload problems classify only as `INFRASTRUCTURE_FAIL_0105A5B_R1M`; they do not alter scientific criteria.

A PASS authorizes only a separately preregistered archive-structure/member-name locator. It does not authorize source-text semantic inspection or any CSMS-to-B4RITM nuisance mapping.

`NMIR_V2_DISCOVERY_READINESS: 48%`
`OBSERVED_BSM_RESIDUAL_PERMISSION: 0%`
`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION: 0%`
