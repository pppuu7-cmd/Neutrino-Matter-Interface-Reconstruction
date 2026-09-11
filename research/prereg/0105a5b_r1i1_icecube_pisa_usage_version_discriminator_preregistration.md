# NMIR v2 0105a5b-R1i1 — IceCube-source PISA usage/version discriminator

Date frozen: 2026-09-11
Parent: validated `PASS_0105A5B_R1I_ICECUBE_PISA_METADATA_PINNABLE_NONDISCOVERY`.

## Purpose
Determine whether the exact, already-byte-locked IceCube analysis source `arXiv:2304.12236` explicitly references PISA and, if so, whether it explicitly identifies exactly one member of the complete frozen 18-tag `icecube/pisa` lineage. This must happen before any PISA implementation/source inspection.

## Frozen authority bytes
Acquire only `https://export.arxiv.org/e-print/2304.12236` and require whole-source SHA256 exactly:
`111c41e49dd50880bc6b00aca95a2479216622b47235fcb68e2a02e22456a149`.

After archive opening, inspect exactly these two already-R1h-byte-locked members and reject any byte mismatch:
- `main.tex`: SHA256 `2c25f03bfadc482a81a8f490efd15df3481988485630f92a255bb3f3c4c3708e`
- `MyBibFile.bib`: SHA256 `0055d6eb0585c44f2074b8f29712c38e1c645154d88830074fb7bff37b00e20c`

No other archive member payload may be read.

## Frozen complete PISA candidate lineage
`contours_working_0.1`, `4.3a1`, `4.2.1`, `4.2`, `4.1.4`, `4.1.3`, `4.1.2`, `4.1.1`, `4.1`, `4.0`, `3.2.1`, `3.2`, `3.1`, `3.0`, `2.0.1`, `2.0`, `1.0.1`, `1.0` with exact commit SHAs as frozen in the R1i immutable note.

## Frozen locator
Search both exact members case-insensitively for literal `PISA`. Record every occurrence with at most 480 characters total context (240 each side).

A tag/version match is qualifying only if one of these explicit forms occurs case-insensitively within the same source member:
- `PISA <tag>`
- `PISA v<tag>`
- `PISA version <tag>`
- `PISA release <tag>`
where whitespace between terms may vary but no alternative version spelling may be added after viewing results. For `contours_working_0.1`, apply the same four literal forms.

Do not infer a version from publication date, release date, numeric proximity, dependency compatibility, output agreement, or latest-version logic.

## Classification
- `PASS_0105A5B_R1I1_PISA_USAGE_AND_VERSION_UNIQUELY_DISCRIMINATED_NONDISCOVERY` iff at least one `PISA` occurrence exists and exactly one frozen tag has one or more qualifying explicit-form matches.
- `BLOCKED_0105A5B_R1I1_PISA_REFERENCED_VERSION_NOT_UNIQUELY_DISCRIMINATED` iff at least one `PISA` occurrence exists but zero or more than one frozen tags qualify.
- `BLOCKED_0105A5B_R1I1_PISA_NOT_REFERENCED_BY_ICECUBE_SOURCE` iff no `PISA` occurrence exists.
- source/hash/archive/member failure is `INFRASTRUCTURE_FAIL_0105A5B_R1I1`.

A PASS is authority/provenance only. It permits only a separately preregistered byte-locked inspection of the uniquely identified PISA state. It does not authorize standard-3nu reproduction, Barr/CSMS transformations, systematics MC, observed residuals, or BSM scans.

Hard prohibitions: no PISA README/source/tree/blob/archive inspection; no GitHub content endpoint for `icecube/pisa`; no version inference; no 3nu; no systematic MC; no observed residual.

`OBSERVED_BSM_RESIDUAL_PERMISSION: 0%`
`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION: 0%`
