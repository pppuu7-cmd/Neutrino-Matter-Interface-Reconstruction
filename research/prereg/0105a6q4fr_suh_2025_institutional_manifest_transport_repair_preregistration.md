# NMIR v2 0105a6q4fr — Suh 2025 institutional manifest transport repair preregistration

Date frozen: 2026-09-11
Branch: `research/0105-bsm-residual-reconstruction`
Parent diagnostic: 0105a6q4ft, record commit `82df8544f41ef34e5557a389335a595b900d2635`

## Purpose

Repair only the transport/endpoint defect localized by 0105a6q4ft. This gate does not inspect dissertation PDF bytes or text and does not alter any scientific/count-law criterion.

## Frozen identity criteria retained from q4f

Target identity remains exactly:
- author: Benjamin D. Suh / Benjamin Suh;
- year: 2025;
- dissertation title: `TOWARDS AN IMPROVED MEASUREMENT OF THE CEVNS PROCESS WITH THE CENNS-10 LAR DETECTOR` (case-insensitive presentation only; wording must match);
- institution: Indiana University Bloomington / official Indiana University institutional provenance.

## Frozen official-IU endpoints

A. CEEM plaque metadata endpoint retained unchanged:
`https://ceem.indiana.edu/events/phd-plaques/suh-benjamin.html`

B. Broken ScholarWorks Discover endpoint is replaced prospectively by the official CEEM graduate-thesis index:
`https://ceem.indiana.edu/education/index.html`

Reason for replacement is transport only: q4ft established the frozen ScholarWorks Discover endpoint returns HTTP 404 while the CEEM endpoint is HTTP 200. The replacement endpoint was selected because it is official Indiana University institutional metadata and independently lists the same author/year/title identity; it is not selected from dissertation scientific content.

## Mechanical gate

For each endpoint record requested URL, final URL, HTTP status, content type, byte count and SHA256. PASS requires both official IU endpoints to return HTTP 200 and both payloads to independently contain the frozen author/year/title identity. Failure of transport or identity is BLOCKED.

No URL discovered inside either page may be followed in this gate. No PDF may be downloaded. No `pdftotext`, OCR, semantic likelihood adjudication, pseudo-data generation, systematic Monte Carlo, observed-data residual construction or BSM fit is permitted.

## Frozen classifications

PASS: `PASS_0105A6Q4FR_INSTITUTIONAL_MANIFEST_TRANSPORT_REPAIRED_NONDISCOVERY`

BLOCKED: `BLOCKED_0105A6Q4FR_INSTITUTIONAL_MANIFEST_TRANSPORT_OR_IDENTITY_INCOMPLETE`

Infrastructure failure remains separately classifiable as infrastructure/transport failure and may only be repaired without changing the above identity/scientific criteria.

## Permissions

A PASS permits only a later prospectively preregistered institutional dissertation locator/acquisition gate. It does not itself authorize dissertation PDF inspection, count-law semantic adjudication, systematic Monte Carlo, standalone residual construction, or BSM analysis.

`SYSTEMATIC_MONTE_CARLO_PREREGISTRATION_PERMISSION: 0%`
`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION: 0%`
`OBSERVED_BSM_RESIDUAL_PERMISSION: 0%`
