# NMIR v2 0105a6q4fs2 — exact IUScholarWorks target metadata locator preregistration

Date frozen: 2026-09-11
Branch: `research/0105-bsm-residual-reconstruction`
Parent authority: q4fs1 validated PASS, immutable record commit `394de950d8ef0bc8c33c9869d4b8a70ec354a885`.

## Purpose

Use the prospectively validated official IUScholarWorks metadata discovery endpoint to locate, metadata-only, the institutional repository item corresponding to the already frozen dissertation identity. No bitstream/file acquisition and no scientific-content inspection are authorized in this gate.

## Frozen endpoint and request contract

Endpoint: `https://scholarworks.iu.edu/iuswrrest/api/discover/search/objects`.

Only the q4fs1-authorized standard keys may be sent:

- `query`
- `size`

Freeze the exact query string before execution as:

`"Towards an improved measurement of the CEVNS process with the CENNS-10 LAr Detector" "Benjamin Suh" "2025"`

Freeze `size=20`.

Request header: `Accept: application/json`.

No other query/filter/scope/sort key may be introduced after execution.

## Frozen target identity

- author token: `Benjamin Suh`; acceptable exact metadata author variants are only `Benjamin Suh` or `Benjamin D. Suh` (case-insensitive, whitespace-normalized)
- year: `2025`
- exact title: `Towards an improved measurement of the CEVNS process with the CENNS-10 LAr Detector` (case-insensitive, whitespace-normalized; no fuzzy title matching)

## Frozen inspection boundary

Inspect only the JSON returned by this single discovery request. Do not follow `_links`, item URLs, handles, UUID endpoints, bundles, bitstreams, or files.

For each returned search result, retain only metadata fields already embedded in that discovery-response object that are necessary to test exact title, frozen author variants, and year. A returned UUID may be recorded only if attached to a uniquely matching returned object; it must never be guessed or constructed.

If author or year are not present in the discovery response itself, do not follow links to obtain them: classify BLOCKED.

## Frozen acceptance

PASS: `PASS_0105A6Q4FS2_IUSCHOLARWORKS_TARGET_METADATA_UNIQUE_MATCH_NONDISCOVERY` iff:

1. HTTP status is 200 and response parses as JSON;
2. exactly one returned discovery object matches the exact frozen title;
3. that same returned object contains an allowed exact author variant and year `2025` in metadata embedded directly in the discovery response;
4. a repository item identifier/UUID is present on that same object; and
5. no links or external endpoints are followed.

BLOCKED: `BLOCKED_0105A6Q4FS2_IUSCHOLARWORKS_TARGET_METADATA_NOT_UNIQUELY_RESOLVED` for zero or multiple exact-title matches, missing embedded author/year authority, missing item identifier, non-200 transport, non-JSON response, or any schema insufficiency that prevents exact frozen identity verification without following links.

FAIL: `FAIL_0105A6Q4FS2_PROSPECTIVE_BOUNDARY_VIOLATION` if the implementation follows an item/link/bitstream endpoint, constructs or guesses a target identifier, downloads a file, or inspects dissertation scientific text.

## Hard prohibitions

No fuzzy/semantic search expansion after result inspection. No alternate title tokens. No post-result author spelling expansion. No UUID guessing. No handle/bitstream URL construction. No item-link following. No PDF/file download. No dissertation scientific text. No count-law inference. No pseudo-data, likelihood, nuisance profiling, systematic Monte Carlo, observed residual, BSM fit, significance, or Wilks threshold.

A PASS permits only a later separately preregistered item-metadata/byte-acquisition gate. It does not itself resolve F1/F7.

`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION: 0%`
`OBSERVED_BSM_RESIDUAL_PERMISSION: 0%`
