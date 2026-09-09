# 0105a2 — COHERENT official release-route provenance preflight

Date frozen: 2026-09-10
Gate ID: NMIR-V2-0105A2
State: ACTIVE_PREREGISTRATION_ONLY
Parent: `research/prereg/0105_v2_model_agnostic_bsm_residual_reconstruction.md`
Sibling: 0105a1 cross-regime file-inventory lock.

## Purpose

Pin the **collaboration-authoritative route** from the official COHERENT/ORNL data-release page to the two legacy CEvNS event releases required by NMIR v2, without consuming event bytes or residual-dependent information.

This gate exists because a repository DOI can be technically accessible yet semantically wrong for the analysis. It must distinguish event releases from calibration/response datasets before any file-level authority is promoted.

## Frozen official anchor

Official collaboration page:

`https://coherent.ornl.gov/data-releases/`

The page must identify both of the following CEvNS release records:

1. first CEvNS detection on argon -> Zenodo record `3903810`, expected DOI identity `10.5281/zenodo.3903810`;
2. first CEvNS detection -> Zenodo record `1228631`, expected DOI identity `10.5281/zenodo.1228631`.

The route may contain the historical `/record/` or current `/records/` Zenodo path form and may include a URL fragment. Record identity is the frozen semantic key.

## Explicit non-substitution guard

ORNL/OLCF dataset DOI `10.13139/OLCF/1969085` is a distinct COHERENT CsI[Na] **nuclear-recoil response/calibration** release. It is scientifically useful for detector-response reproduction but is not the CsI CEvNS event release `1228631` and must never silently replace it.

0105a2 must therefore preserve two roles:

- `1228631` / `3903810`: event-release authority route;
- `10.13139/OLCF/1969085`: separate calibration/response auxiliary authority only.

## Frozen checks

The implementation must:

1. fetch only the official ORNL data-release landing page;
2. preserve raw response bytes and SHA256;
3. verify that both expected Zenodo record IDs are linked from that page;
4. reject a fixture/page that contains only one of the two records;
5. reject unrelated Zenodo record IDs as substitutes;
6. preserve the calibration DOI distinction in the normalized result;
7. set `event_byte_lock_complete=false`;
8. set `observed_residual_execution_allowed=false`;
9. make no claim that ORNL HTML bytes are equivalent to Zenodo event bytes;
10. make no likelihood, fit or BSM significance calculation.

## Relation to 0105a1

A PASS here establishes **semantic provenance from collaboration to repository**, not file-level immutability. 0105a1 remains responsible for exact repository version/file inventory/checksums. If Zenodo transport remains unavailable, 0105a2 may PASS while 0105a as a whole remains BLOCKED.

No fallback source is authorized to fabricate Zenodo file checksums.

## Allowed result

If all checks pass:

`PASS_0105A2_COHERENT_OFFICIAL_RELEASE_ROUTE_PINNED_NONTERMINAL`

Otherwise:

`BLOCKED_0105A2_COHERENT_OFFICIAL_RELEASE_ROUTE_UNRESOLVED`.
