# 0105a1-a1 — transient HTTP retry amendment

Date: 2026-09-10
Parent: `research/prereg/0105a1_cross_regime_authority_metadata_lock.md`
Trigger: hosted authority-metadata run `34413239570`, job `102672233438`.

## Observed failure

The deterministic 0105a1 metadata tests completed successfully (`4 passed`). The live metadata step then failed while querying the prospectively frozen Zenodo authority route with

`BLOCKED_0105A1_METADATA_HTTP_504 host=zenodo.org`.

This is a transport failure. No observed neutrino residual, likelihood, BSM parameter, authority content, file inventory or experimental result was opened through the failed step.

## Amendment

The frozen authority identities, endpoints, record IDs, DOIs, metadata fields and scientific gates remain unchanged.

The metadata HTTP helper may retry only transient transport failures:

- HTTP 429;
- HTTP 500, 502, 503, 504;
- URL/network transport errors and timeouts.

Use at most 4 total attempts per URL with deterministic backoff delays of 2, 4 and 8 seconds before attempts 2, 3 and 4 respectively.

Non-transient HTTP failures remain immediate fail-closed errors. After the final transient failure, the script must still raise a fail-closed `BLOCKED_0105A1_METADATA_TRANSPORT` error identifying the host and attempt count.

No mirror, alternate record, cached third-party metadata or manually reconstructed inventory is authorized by this amendment.

## Scope guard

This amendment changes transport robustness only. It does not change:

- IceCube DOI `10.7910/DVN/B4RITM`;
- COHERENT CsI DOI `10.5281/zenodo.1228631` / record `1228631`;
- COHERENT Ar DOI `10.5281/zenodo.3903810` / record `3903810`;
- any checksum/version/content gate;
- `observed_residual_execution_allowed = false`;
- `joint_likelihood_claim_allowed = false`;
- the requirement for a later consumed-byte SHA256 lock and null-model reproduction.

This amendment cannot be reused to weaken a later physics-fit convergence or statistical tolerance.