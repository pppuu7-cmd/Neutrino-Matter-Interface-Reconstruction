# 0105a4 — DeepCore B4RITM authority-inventory preflight

Date frozen: 2026-09-10
Gate ID: NMIR-V2-0105A4
State: ACTIVE_PREREGISTRATION_ONLY
Parent: `research/authority/0105a_v2_cross_experiment_authority_audit.md`

## Purpose

Pin the exact Harvard Dataverse metadata authority for the **Stage-A propagation candidate** selected prospectively by 0105a:

`Replication Data for: Measurement of atmospheric neutrino mixing with improved IceCube DeepCore calibration and data processing`

Persistent DOI:

`10.7910/DVN/B4RITM`

This gate is metadata/provenance only. It must not evaluate an observed residual or reinterpret the separate 7.5-year sterile-neutrino release.

## Authority separation guard

Two public DeepCore authorities have different roles in NMIR v2:

- `10.7910/DVN/B4RITM` — standard atmospheric-oscillation replication release; selected Stage-A propagation candidate;
- `10.7910/DVN/QKL28Z` — 7.5-year sterile-neutrino data release; sterile-control/constraint authority under 0101 semantics.

0105a4 must fail if the returned persistent identity resolves to `QKL28Z` or otherwise fails to identify `B4RITM`.

## Frozen endpoint

Use Harvard Dataverse Native API persistent-ID resolution:

`https://dataverse.harvard.edu/api/datasets/:persistentId/?persistentId=doi:10.7910/DVN/B4RITM`

URL encoding of the query parameter is transport-only.

## Frozen output inventory

The normalized result must preserve at least:

- Dataverse API status;
- dataset id and persistent URL/identifier;
- exact released version number and minor version;
- version state and release time;
- for every listed file: Dataverse file id, filename, content type, byte size, persistent id if present, checksum type/value, description and categories if present;
- SHA256 of the raw Dataverse JSON response;
- deterministic SHA256 of the normalized inventory.

## Frozen gates

PASS requires:

1. API status `OK`;
2. returned persistent identity contains `B4RITM` / expected DOI;
3. returned identity does not contain `QKL28Z`;
4. version is released;
5. file inventory is nonempty;
6. every listed file has a nonempty filename;
7. every listed file has positive integer byte size;
8. every listed file has a provider checksum type and checksum value;
9. no observed residual execution is authorized.

No particular filename is selected as the future consumed likelihood object in this gate. Selection of consumed files must occur only after this full inventory is pinned and the release documentation is audited for reproduction semantics.

## Allowed result

PASS:

`PASS_0105A4_DEEPCORE_B4RITM_AUTHORITY_INVENTORY_NONTERMINAL`

Otherwise:

`BLOCKED_0105A4_DEEPCORE_B4RITM_AUTHORITY_INVENTORY_INCOMPLETE`.

Always set:

- `deepcore_consumed_byte_lock_complete=false`;
- `observed_residual_execution_allowed=false`.
