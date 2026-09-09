# 0105a2 result — official COHERENT release-route provenance

Date: 2026-09-10
Gate ID: NMIR-V2-0105A2
Final state: `PASS_0105A2_COHERENT_OFFICIAL_RELEASE_ROUTE_PINNED_NONTERMINAL`

## Scope

This gate establishes only the collaboration-authoritative semantic route from the official COHERENT/ORNL data-release landing page to the two preregistered legacy CEvNS event-release records. It does not establish file-level Zenodo byte immutability and does not authorize an observed residual analysis.

## Hosted authority

Workflow run:

- run: `34417860871`
- job: `102686630178`
- head: `7a9602d5183203256229946c23388f1fa8680094`
- conclusion: SUCCESS
- deterministic route tests: SUCCESS
- live official-page pin: SUCCESS
- nonterminal provenance guard: SUCCESS
- artifact upload: SUCCESS

Workflow artifact:

- name: `nmir-v2-0105a2-coherent-official-route`
- artifact id: `10129768114`
- artifact digest: `sha256:7575c61ceaa5d19972a7168dec5b5ed3cf1e3451539949b42f9198630a46f77e`

## Pinned official-page result

Official anchor:

`https://coherent.ornl.gov/data-releases/`

Raw hosted-response HTML SHA256:

`b945fde4e3d5bfdc56d2e7e9a4710410360eb9970680bc3d05c2742af317fe37`

The pinned page linked exactly the expected release identities used by this gate:

- CsI CEvNS event release: Zenodo record `1228631`, expected DOI `10.5281/zenodo.1228631`;
- Ar CEvNS event release: Zenodo record `3903810`, expected DOI `10.5281/zenodo.3903810`.

Observed links in the pinned page were:

- `https://zenodo.org/record/1228631...`
- `https://zenodo.org/record/3903810...`

The normalized result has all six frozen gates true, including the explicit non-substitution guard.

## Calibration non-substitution

`10.13139/OLCF/1969085` remains separately classified as CsI[Na] nuclear-recoil response/calibration authority. It is not the CsI CEvNS event release and may not replace Zenodo record `1228631` in an event-level analysis.

## Remaining authority block

This PASS does **not** close parent gate 0105a. The normalized result intentionally states:

- `event_byte_lock_complete = false`;
- `observed_residual_execution_allowed = false`.

0105a1 still requires exact current Zenodo version/file inventory and provider checksums (and later exact consumed-byte SHA256) for records `1228631` and `3903810`. The persistent Zenodo API 504 observed by 0105a1 therefore remains an active transport/provenance blocker.

No alternate source is authorized to fabricate or infer the missing file checksums.

## Scientific interpretation

The semantic dataset identity is no longer ambiguous: the official collaboration route itself points to the same two event records preregistered by NMIR v2. This removes a provenance-substitution risk, but it is not a BSM result and not a data-fit result.
