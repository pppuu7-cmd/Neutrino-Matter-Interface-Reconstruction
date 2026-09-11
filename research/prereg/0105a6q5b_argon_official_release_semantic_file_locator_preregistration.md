# 0105a6q5b — Argon official-release semantic-file locator preregistration

Date: 2026-09-11
Gate: `NMIR-V2-0105A6Q5B`
Scope: official Zenodo metadata-only locator; authority/provenance; NONDISCOVERY.

## Parent authorization

Parent q5a2 validated classification: `PASS_0105A6Q5A2_ARGON_OFFICIAL_RELEASE_STRUCTURAL_PROVENANCE_BOUND_NONDISCOVERY`, immutable record commit `c7290228641ba8a8b6363481e98f49aa2a6081e1`.

This gate may inspect only Zenodo record-3903810 metadata and the immutable q5a2 local record. It may not download or inspect any release-file bytes.

## Frozen candidate rule

For every file entry in exact Zenodo API record `3903810`, normalize only the metadata filename/key with Unicode NFKC + casefold. Mark a file as an implementation/semantic candidate iff either:

1. its filename ends in one of: `.py`, `.c`, `.cc`, `.cpp`, `.h`, `.yaml`, `.yml`, `.json`; OR
2. its filename contains at least one frozen lexical token: `parameter`, `efficien`, `likelihood`, `fit`, `roo`, `plot`, `extract`, `systematic`.

Retain all matches; do not rank, prune, or choose among them after seeing the list. Retain only filename/key, size, provider checksum and metadata link fields. No file download URL may be followed.

## Frozen authority checks

- q5a2 immutable local record contains its exact PASS class and run/job/artifact provenance;
- Zenodo record id exactly `3903810`, DOI exactly `10.5281/zenodo.3903810`, version exactly `1.0`, and title identity exactly as frozen in q5a/q5a2;
- exact metadata file count remains 24;
- every candidate retains its provider metadata checksum and size.

## Frozen terminal classes

- `PASS_0105A6Q5B_ARGON_OFFICIAL_SEMANTIC_FILE_CANDIDATES_LOCATED_NONDISCOVERY` iff parent binding and Zenodo identity pass and >=1 candidate is returned.
- `BLOCKED_0105A6Q5B_PARENT_PROVENANCE_BINDING_FAILURE`.
- `BLOCKED_0105A6Q5B_ZENODO_METADATA_IDENTITY_FAILURE`.
- `BLOCKED_0105A6Q5B_NO_SEMANTIC_FILE_CANDIDATES`.
- `BLOCKED_0105A6Q5B_PROVIDER_TRANSPORT_FAILURE`.

PASS authorizes only a separate prospective byte-identity/semantic-inspection gate over the complete returned candidate set. It does not authorize choosing a subset post hoc, pseudo-data generation, likelihood evaluation, systematic MC, or observed residual analysis.

`SYSTEMATIC_MONTE_CARLO_PREREGISTRATION_PERMISSION = 0%`
`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION = 0%`
`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`