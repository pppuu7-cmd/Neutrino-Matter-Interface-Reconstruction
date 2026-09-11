# NMIR 0105a q7 hosted artifact validation — immutable result

Date classified: 2026-09-11
Scope: NONDISCOVERY authority/reproducibility validation only.

## Frozen authority chain

- q7 scientific preregistration: `ca909d318365dfb05b7b52c8abeacfbdd1f8bb7d`
- q7 prose scientific result: `4516909ca2d58f7e7cb541dd2e40f844f8f18f4f`
- hosted-validation amendment: `e97d5157dd586160b0e9feb476eb4975d88fe513`
- hosted execution head: `f52c282f472736c3b5fffccd25e07c543699d4d4`
- run/job/artifact: `34629320828 / 103362008779 / 10274904595`

## Artifact integrity

GitHub provider artifact digest:

`sha256:ab5ce95e807fad976364077cb1f72f5f924ef784cc0e37fce992c0584a00c1d0`

Independently downloaded artifact ZIP SHA256:

`ab5ce95e807fad976364077cb1f72f5f924ef784cc0e37fce992c0584a00c1d0`

The provider digest and independently downloaded ZIP digest are identical.

Inner `result.json` SHA256:

`fdebc7e7c565e1f39e1bd5c1a0bea61c77bd8f451cca42e27b49d66176bf6cc7`

Primary-input byte locks emitted by the hosted validator:

- arXiv:2003.10630v3 PDF: `51b8b9787971ce521291482555d3d4a31cbd009c60e448a6cd2efa2d76a2f513`
- arXiv:2003.10630v4 PDF: `e5fab16204b367710af681104388b6e991281b3d7ebda3716c04afb6a1f3ace8`
- arXiv:2003.10630v7 PDF: `2f875bda728739a85a2568db44761d7f164e113e77613d8f884e6c4b071acef2`
- arXiv:2003.10630 current history HTML: `c2207556235a45fd816b13c7779b4e911736d1716144ab095e730a849dbc8efd`
- arXiv:2006.12659 release PDF: `13d39e641abd3be07b26b5a952ae944698012adf7290431f11b8da15b44d74b2`

## Frozen-condition adjudication

All four preregistered q7 conditions were located in the primary authority corpus:

1. v3 Analysis-A Table-I SS/NSS field contains `3154 +/- 25` — PASS.
2. v4 changes the same field to `3152 +/- 25` — PASS.
3. primary arXiv version history identifies v4 as `fix typo in table 1` — PASS.
4. corrected `3152 +/- 25` persists in the final/current primary authority and/or official release paper — PASS.

Hosted machine-readable status:

`PASS_0105A_Q7_F7_PRIMARY_VERSIONED_PRECEDENCE_LOCATED_NONDISCOVERY`

Scientific classification after raw artifact review:

`PASS_0105A_Q7_F7_PRIMARY_VERSIONED_PRECEDENCE_LOCATED_NONDISCOVERY`

The hosted result therefore validates, rather than merely repeats, the earlier prose q7 PASS. `3154` is the obsolete pre-correction Table-I value and `3152` is the corrected authoritative Analysis-A SS input for the frozen reproduction target.

## Authorization boundary

This closes F7 only. It does not close F1, authorize Tier-A exact likelihood reconstruction, systematic Monte Carlo, observed residual scans, or any BSM scan. q6 remains LAr scope-mismatched and does not transfer CsI counting conventions to the LAr target.
