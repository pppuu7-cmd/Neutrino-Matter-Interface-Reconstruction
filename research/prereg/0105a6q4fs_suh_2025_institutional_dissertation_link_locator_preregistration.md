# NMIR v2 0105a6q4fs — Suh 2025 institutional dissertation link locator preregistration

Date frozen: 2026-09-11
Branch: `research/0105-bsm-residual-reconstruction`
Parent validated manifest PASS: q4fr record `5cdf1c32b249bbc155813c331774213b58c9d378`.

## Purpose

Mechanically inventory and classify hyperlink metadata from the two exact official-IU pages validated by q4fr, without following any hyperlink and without downloading or inspecting dissertation bytes. This is a locator only.

## Frozen input pages and byte identities

A. `https://ceem.indiana.edu/events/phd-plaques/suh-benjamin.html`
- bytes: `23370`
- SHA256: `f1c245e9675c1a533bc9ad03ca928820499381d576c5f6fefee59c33b91d7488`

B. `https://ceem.indiana.edu/education/index.html`
- bytes: `67845`
- SHA256: `3de3e09e5ebdb4006c0d8b969c3f73a25b041b31534476b6bf6987bbf5591fe6`

Both exact page identities must be revalidated before parsing links. Byte mismatch is FAIL; transport failure is BLOCKED.

## Frozen locator procedure

Parse HTML locally after exact-byte validation. Record every `<a href>` link from each page as requested-page, raw href, resolved absolute URL, and normalized visible anchor text. Do not request/follow any returned link.

Define a deterministic `dissertation_link_candidate` flag before inspection. A link is a candidate iff its absolute URL or visible anchor text contains at least one case-insensitive literal from this frozen union:

- `dissertation`
- `thesis`
- `scholarworks`
- `irem` / `ir` only when present as a complete URL path/domain token, not arbitrary substring
- `.pdf`
- `download`
- `Benjamin Suh`
- `Benjamin D. Suh`
- `Towards an improved measurement of the CEVNS process with the CENNS-10 LAr detector`

Retain **all** candidate links; no ranking, pruning, or choosing among candidates is permitted in q4fs. Also retain the total count and SHA256 of a canonical JSON serialization of the complete all-link inventory so later steps cannot silently change the candidate universe.

## Frozen classifications

PASS: `PASS_0105A6Q4FS_INSTITUTIONAL_DISSERTATION_LINK_CANDIDATES_LOCATED_NONDISCOVERY` iff both exact page identities validate and at least one frozen-rule candidate link is returned.

BLOCKED: `BLOCKED_0105A6Q4FS_NO_INSTITUTIONAL_DISSERTATION_LINK_CANDIDATES` iff both exact pages validate but the frozen candidate set is empty.

BLOCKED: `BLOCKED_0105A6Q4FS_SOURCE_TRANSPORT_FAILURE` for transport failure.

FAIL: `FAIL_0105A6Q4FS_SOURCE_BYTE_IDENTITY_MISMATCH` for page-byte mismatch.

## Hard prohibitions

No returned hyperlink may be requested or followed in this gate. No PDF/file download, `pdftotext`, OCR, source-text semantic adjudication, pseudo-data generation, likelihood evaluation, systematic Monte Carlo, nuisance profiling, observed residual construction, BSM fit, significance calculation, or Wilks threshold is permitted.

A PASS permits only a separately prospectively preregistered acquisition/byte-lock gate over the complete returned candidate set or over a candidate selected by a criterion frozen before following it. It does not authorize dissertation semantic reading.

`SYSTEMATIC_MONTE_CARLO_PREREGISTRATION_PERMISSION: 0%`
`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION: 0%`
`OBSERVED_BSM_RESIDUAL_PERMISSION: 0%`
