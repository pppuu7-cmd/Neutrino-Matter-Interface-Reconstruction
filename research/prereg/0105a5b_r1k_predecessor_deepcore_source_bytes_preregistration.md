# 0105a5b R1k — predecessor DeepCore source-byte acquisition preregistration

Date: 2026-09-11
Branch: `research/0105-bsm-residual-reconstruction`
Scope: NMIR v2 authority work only. NMIR v1 remains frozen.

## Motivation and frozen provenance

Validated R1j2 exhausted the cited PISA-methodology source as a version discriminator: PISA is described but no immutable `icecube/pisa` tag/commit is named. A new route must therefore be independent and frozen before target-content inspection.

The exact predecessor IceCube DeepCore analysis authority is prospectively fixed as arXiv identifier `1902.07771`, the earlier IceCube DeepCore oscillation-analysis publication already externally linked to the same analysis lineage. This gate does not infer that its implementation state equals the 2023 analysis state. It asks only whether its exact source bytes can be acquired and immutably locked for a later separately preregistered authority audit.

## Frozen acquisition target

Exact URL: `https://export.arxiv.org/e-print/1902.07771`

No fallback mirror, version substitution, query mutation, DOI/PDF substitution, or alternate source is permitted inside R1k.

## Allowed operations

R1k may only:

1. issue one HTTP GET to the exact frozen URL with a fixed user-agent;
2. record HTTP status, final URL, content type and byte count;
3. compute MD5 and SHA256 over the opaque response bytes;
4. emit an immutable JSON result plus artifact hashes.

## Hard prohibitions

R1k must not:

- open the returned archive/container;
- list members;
- decode/search/read source text;
- inspect PISA repository content;
- compare candidate PISA tags/commits;
- run standard 3nu;
- run systematic Monte Carlo;
- inspect any observed BSM residual.

## Frozen classification

`PASS_0105A5B_R1K_PREDECESSOR_DEEPCORE_SOURCE_BYTES_ACQUIRED_NONDISCOVERY` iff HTTP status is 200 and the opaque payload is nonempty.

Transport/network/non-200/empty-payload problems classify only as `INFRASTRUCTURE_FAIL_0105A5B_R1K`; they do not alter scientific criteria.

A PASS authorizes only a separately preregistered archive-structure/member-name locator. It does not authorize source-text semantic inspection or selection of a PISA implementation state.

`NMIR_V2_DISCOVERY_READINESS: 48%`
`OBSERVED_BSM_RESIDUAL_PERMISSION: 0%`
`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION: 0%`
