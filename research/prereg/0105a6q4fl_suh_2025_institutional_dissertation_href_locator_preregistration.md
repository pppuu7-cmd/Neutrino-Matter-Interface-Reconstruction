# NMIR v2 0105a6q4fl — Suh 2025 institutional dissertation href locator preregistration

Date frozen: 2026-09-11
Branch: `research/0105-bsm-residual-reconstruction`
Parent result record: `cc496c75273ee3c904c714c001c37e3d8cdf96bf`

## Purpose

Determine prospectively whether either of the two authority-bound Indiana University metadata pages frozen by q4fr exposes an institutional link that can serve as a candidate route toward the Benjamin Suh 2025 dissertation. This is an HTML-link locator only. No located link may be followed in this gate.

## Frozen parent authority

q4fr hosted run: `34545436341`; job: `103096914611`; artifact: `10178825152`.

q4fr artifact ZIP SHA256: `700e03367aa2f7760c3bfe8272ed2efe29236790d6fcc78746c905e3de5eef89`.
q4fr inner `result.json` SHA256: `af1af99fec76f8e3a1c20056af7be3cf6e688314b7703e58eaf871c5c985681a`.

Frozen source A:
`https://ceem.indiana.edu/events/phd-plaques/suh-benjamin.html`
- exact byte count: `23370`
- exact SHA256: `f1c245e9675c1a533bc9ad03ca928820499381d576c5f6fefee59c33b91d7488`

Frozen source B:
`https://ceem.indiana.edu/education/index.html`
- exact byte count: `67845`
- exact SHA256: `3de3e09e5ebdb4006c0d8b969c3f73a25b041b31534476b6bf6987bbf5591fe6`

Both pages must still return HTTP 200 and match the exact frozen byte count and SHA256 before href parsing. Any mismatch is fail-closed source drift.

## Frozen locator algorithm

Parse only HTML `<a href>` attributes and their anchor text from the two exact payloads. Relative href values are mechanically resolved with `urljoin` against the frozen source URL. Fragment-only links, `mailto:`, `tel:`, and `javascript:` links are excluded.

Normalize candidate-testing text by HTML-unescaping, collapsing whitespace, and case-folding. No fuzzy matching is permitted.

Frozen identity tokens:
- `suh`
- `benjamin`
- `cenns-10`
- `cenns10`

Frozen repository/payload tokens, evaluated only in the resolved href string:
- `scholarworks`
- `dspace`
- `/handle/`
- `/etd`
- `dissertation`
- href path ending in `.pdf`

A link is a locator candidate iff either:
1. at least one frozen identity token occurs in the resolved href or anchor text; or
2. at least one frozen repository/payload token occurs in the resolved href.

Duplicate candidates are deduplicated by resolved URL. Candidate output may retain only source URL, resolved URL, normalized anchor text, and matched frozen token/category. No surrounding page text is retained.

## Frozen classifications

Source drift:
`BLOCKED_0105A6Q4FL_FROZEN_SOURCE_IDENTITY_DRIFT`

Zero locator candidates:
`BLOCKED_0105A6Q4FL_INSTITUTIONAL_DISSERTATION_LOCATOR_NO_CANDIDATES`

One or more locator candidates:
`PASS_0105A6Q4FL_INSTITUTIONAL_DISSERTATION_LOCATOR_CANDIDATES_FOUND_NONDISCOVERY`

A candidate PASS is not authority binding to a dissertation payload and is not a scientific result. Any candidate URL may be followed only by a later separately preregistered acquisition/identity gate.

## Prohibitions and permissions

No located href may be requested in q4fl. No PDF may be downloaded. No dissertation body text, `pdftotext`, OCR, count-law semantics, likelihood, pseudo-data generation, systematic Monte Carlo, observed-data residual, or BSM fit is permitted.

`SYSTEMATIC_MONTE_CARLO_PREREGISTRATION_PERMISSION: 0%`
`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION: 0%`
`OBSERVED_BSM_RESIDUAL_PERMISSION: 0%`