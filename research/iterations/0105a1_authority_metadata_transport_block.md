# 0105a1 — cross-regime authority metadata transport block

Date recorded: 2026-09-10
Parent preregistration: `research/prereg/0105a1_cross_regime_authority_metadata_lock.md`
Preregistration commit: `c878c583518bcae96c70a8784876a464ace38d68`
Transport amendment: `research/prereg/0105a1_a1_transient_http_retry_amendment.md`, commit `23863b27ebd6b0847476293cf452b4da0f10ee00`

## Frozen authority targets

- IceCube DeepCore replication DOI `10.7910/DVN/B4RITM`;
- COHERENT CsI Zenodo DOI `10.5281/zenodo.1228631`, record `1228631`;
- COHERENT Ar Zenodo DOI `10.5281/zenodo.3903810`, record `3903810`.

No observed neutrino residual or BSM fit is authorized by this gate.

## First hosted attempt

Workflow: `0105a1 pin cross-regime authority metadata`
Run/job: `34413239570/102672233438`
Head: `43810759e06309f468508477d67b2e3816188605`

Deterministic metadata tests:
- `4 passed in 0.05 s`.

Live metadata step failed with:

`BLOCKED_0105A1_METADATA_HTTP_504 host=zenodo.org`.

No normalized inventory or scientific result was promoted from the failed run.

## Transport-only amendment and second hosted attempt

The amendment allowed at most four attempts for prospectively listed transient failures only (HTTP 429/500/502/503/504 or network timeout/URL transport failure), with deterministic 2/4/8-s backoff. Authority IDs, DOI targets, gates and scientific semantics were unchanged.

Implementation commit:
`d7bffea7ed58b87259ef7b5a5857db35871b6a6c`.

Second run/job:
`34413456295/102672909070`

Again the deterministic metadata tests passed:
- `4 passed in 0.05 s`.

The live metadata step exhausted all four prospectively allowed attempts and failed with:

`BLOCKED_0105A1_METADATA_TRANSPORT host=zenodo.org attempts=4`.

Thus retry/backoff did not convert an unavailable authority route into a false PASS.

## Independent semantic cross-check

Public indexed material independently confirms the frozen COHERENT DOI identities and the scientific content expected from those releases: the CsI release is described as containing binned signal/background-region information and systematics for independent analyses; the Ar release describes 3D energy/F90/time arrays, signal/background PDFs, YAML systematic quantities and guidance for alternative fits.

Those semantic cross-checks are useful for source identity but are **not** substituted for the frozen Zenodo file/version/checksum inventory.

## Classification

`BLOCKED_0105A1_AUTHORITY_METADATA_INCOMPLETE`

Reason subtype:
`ZENODO_HOSTED_TRANSPORT_BLOCK_AFTER_PROSPECTIVE_RETRY`

This is an external provenance/transport block, not a physics failure and not evidence that the underlying COHERENT releases are unavailable to all clients.

## Scientific guards retained

- `observed_residual_execution_allowed = false`;
- `joint_likelihood_claim_allowed = false`;
- no manually reconstructed Zenodo file inventory;
- no secondary-source checksum promoted as provider authority;
- no switch to a mirror after failure without a separate prospective authority-equivalence gate;
- later consumed-byte SHA256 and null-control reproduction remain mandatory.

## Next authority route

0105a1 may be revisited only through a separately preregistered authority-equivalence or immutable-source route that does not weaken the frozen provenance requirements. Until then, 0105 Stage-A observed residual execution remains locked.
