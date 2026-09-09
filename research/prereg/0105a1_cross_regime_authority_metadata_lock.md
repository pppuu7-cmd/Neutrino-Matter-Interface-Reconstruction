# 0105a1 — cross-regime authority metadata lock

Date frozen: 2026-09-10
Gate ID: NMIR-V2-0105A1
Parent: `research/authority/0105a_v2_cross_experiment_authority_audit.md`
State: ACTIVE_PREREGISTRATION_ONLY

## Purpose

Before opening any observed 0105 Stage-A residual, immutably enumerate the current public metadata/version/file/checksum inventories for the strongest present cross-regime candidate authorities.

This is provenance discovery only. It does not authorize a residual fit, BSM fit, joint likelihood, parameter scan or significance calculation.

## Frozen authority identities

### Propagation side

IceCube DeepCore atmospheric-oscillation replication dataset:
- persistent DOI: `10.7910/DVN/B4RITM`
- metadata endpoint: Harvard Dataverse Native API persistent-id route for exactly that DOI.

The metadata lock must record at minimum:
- API status;
- dataset persistent URL/identifier;
- latest released version number/minor number/state/release time;
- every returned file id, filename, content type, byte size, persistent id and provider checksum type/value.

No file may be selected as the sole consumed likelihood/response object during metadata discovery. Selection occurs only after the full inventory is frozen.

### Finite-q scattering side

COHERENT public releases:
- CsI first CEvNS observation release: Zenodo record `1228631`, DOI `10.5281/zenodo.1228631`;
- Ar first CEvNS detection release: Zenodo record `3903810`, DOI `10.5281/zenodo.3903810`.

For each Zenodo record, the metadata lock must record at minimum:
- record id;
- DOI and concept DOI if supplied;
- title/publication/update metadata;
- every returned filename/key, byte size, provider checksum and immutable download/self link when supplied.

## Frozen gates

The metadata discovery is a nonterminal PASS only if:

1. Harvard Dataverse API status is `OK`;
2. DeepCore file inventory is nonempty;
3. the returned Dataverse persistent identity is consistent with DOI `10.7910/DVN/B4RITM`;
4. both Zenodo records resolve;
5. both Zenodo inventories are nonempty;
6. returned DOI identity for each Zenodo record is consistent with the frozen DOI/record;
7. every inventoried file has a nonempty filename/key and a positive size;
8. every inventoried file has a provider checksum where the service supplies checksums;
9. raw metadata bytes and normalized inventory JSON are themselves SHA256-hashed;
10. the result explicitly keeps `observed_residual_execution_allowed = false` and `joint_likelihood_claim_allowed = false`.

Any missing/ambiguous version, identity or checksum remains BLOCKED rather than being guessed.

## Byte-level follow-up

A metadata PASS does not prove that downloaded file bytes match the metadata or that the release is sufficient to reproduce the collaboration likelihood.

After this inventory is frozen, a new child gate must prospectively select the exact consumed files for:
- DeepCore Standard-Model/3-flavor control reproduction;
- COHERENT Ar/CsI SM control reproduction;

and independently SHA256 the downloaded bytes. Provider MD5/checksums are provenance aids, not substitutes for the later consumed-byte SHA256 lock.

## Allowed classification

PASS:
`PASS_0105A1_CROSS_REGIME_AUTHORITY_METADATA_INVENTORY_NONTERMINAL`

otherwise:
`BLOCKED_0105A1_AUTHORITY_METADATA_INCOMPLETE`
