# 0105a6q5a — validated Argon official-release provenance inventory

Date: 2026-09-11
Gate: `NMIR-V2-0105A6Q5A`
Classification: `BLOCKED_0105A6Q5A_ORNL_RELEASE_ROUTE_FAILURE`
Scope: authority/provenance only; NONDISCOVERY.

## Frozen preregistration

Preregistration commit: `1b487a2ea8bad7eecc6d02eff30e7f26be28315d`.
Execution head: `26cdd7354ac14b0482c68bce5f19489dd10c08a5`.

## Hosted execution and independent artifact validation

- run: `34547357396`
- job: `103102765542`
- artifact: `10179501141`, `nmir-v2-0105a6q5a-argon-official-release-provenance-inventory`
- dedicated guards: `7 passed`
- provider artifact ZIP SHA256: `14c2536a47feb3e8fae281dfb7e919c734c30f3c36703f790104894343408b6f`
- independently downloaded ZIP SHA256: `14c2536a47feb3e8fae281dfb7e919c734c30f3c36703f790104894343408b6f`
- independent inner `result.json` SHA256: `b08125a2c0f09075f62afd1c850484b22f410edf7276568fa2613f0aebbce8eb`

Green Actions success is not used as scientific PASS; classification follows the frozen predicates applied to the raw result.

## Frozen predicate outcome

Local 0105a3 binding: PASS. Zenodo record predicate: PASS with exact record `3903810`, DOI `10.5281/zenodo.3903810`, version `1.0`, title match and exactly 24 metadata file entries. arXiv predicate: PASS for exact id `2006.12659` and title identity.

ORNL transport itself succeeded (`HTTP 200`; payload SHA256 `7ed4bcc3f99d494b134418d060a122c8c7531c7c3b738350bcb09ea715b804f9`), but the prospectively frozen ORNL anchor predicate returned `matching_anchor_count=0`. Therefore the frozen terminal class is `BLOCKED_0105A6Q5A_ORNL_RELEASE_ROUTE_FAILURE`.

This is a provenance/authority BLOCKED result, not a Standard-Model scientific FAIL and not BSM evidence. The q5a predicate is not weakened or reinterpreted after observing the result.

## Hard guards retained

`release_file_bytes_downloaded=false`; `release_file_bytes_rehashed=false`; `scientific_release_content_inspected=false`; `pseudo_data_generated=false`; `likelihood_evaluated=false`; `observed_bsm_residual_inspected=false`.

`SYSTEMATIC_MONTE_CARLO_PREREGISTRATION_PERMISSION = 0%`
`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION = 0%`
`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`

## Exact next allowed action

Only a new prospective ORNL page-structure/provenance diagnostic may determine why the frozen anchor predicate failed while transport succeeded. It must inspect only anchor metadata/structure from the already-named ORNL Data Releases page, must not inspect scientific release content, must not follow discovered links, and must not alter q5a retrospectively. Any repaired provenance binding requires its own later prospective gate.