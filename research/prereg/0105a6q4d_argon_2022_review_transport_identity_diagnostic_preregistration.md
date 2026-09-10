# 0105a6q4d — Ar 2022 review-talk transport identity diagnostic

Status: **PREREGISTERED BEFORE ANY NEW TARGET PDF TEXT/PAGE INSPECTION / TRANSPORT-ONLY**

Parent scientific locator: `BLOCKED_0105A6Q4C_2022_REVIEW_TRANSPORT_OR_IDENTITY_FAILURE`.
Parent q4c run/job/artifact: `34533749589 / 103060401624 / 10174553754`.
Parent q4c result SHA256: `988fbbc0b5c2f0a74562fb33a829eaae8ff3ebedd1ded7e25376d967a43ef612`.
Parent error: `resolved provider URL identity mismatch`.

## Purpose

Resolve only the transport/identity ambiguity exposed by q4c. The diagnostic must determine the exact HTTP redirect chain and final provider URL reached from the already frozen CERN Indico PDF URL. It is not a count-law search and it may not inspect, extract, normalize, retain, or semantically evaluate PDF page text.

## Frozen source request

Initial URL (identical to q4c):
`https://indico.cern.ch/event/978288/contributions/5014436/attachments/2504944/4303826/JCZBLV2022_CEvNSReviewTalk.pdf`

Expected initial scheme/host/path:
- scheme: `https`;
- host: `indico.cern.ch`;
- path: `/event/978288/contributions/5014436/attachments/2504944/4303826/JCZBLV2022_CEvNSReviewTalk.pdf`;
- no query;
- no fragment.

## Frozen diagnostic procedure

1. Verify the initial URL identity exactly before network access.
2. Execute an HTTPS GET with a dedicated redirect recorder.
3. Record, in order, every HTTP redirect response as only:
   - source URL;
   - HTTP status;
   - raw `Location` header;
   - resolved destination URL.
4. Record the final response URL, final HTTP status, selected transport headers (`Content-Type`, `Content-Length`, `ETag`, `Last-Modified`, `Content-Disposition` when present), byte length, first-five-byte PDF magic boolean, and SHA256 of the complete response bytes.
5. Do **not** run `pdftotext`, OCR, strings extraction, page counting, lexical scanning, semantic inspection, likelihood evaluation, pseudo-data generation, or BSM fitting.
6. Do not retain or upload the PDF bytes; upload only the structured transport result and its SHA256 record.

## Decision classes

- If the request cannot be completed or the final payload is not a PDF: `BLOCKED_0105A6Q4D_TRANSPORT_DIAGNOSTIC_FAILURE`.
- If the final URL is exactly the q4c frozen URL: `PASS_0105A6Q4D_EXACT_URL_IDENTITY_CONFIRMED`.
- If one or more redirects occur but every hop remains on `indico.cern.ch` and the final payload is a PDF: `PASS_0105A6Q4D_INDICO_REDIRECT_CHAIN_RECORDED_NONDISCOVERY`.
- If any redirect leaves `indico.cern.ch`: `BLOCKED_0105A6Q4D_CROSS_PROVIDER_REDIRECT_REQUIRES_SEPARATE_AUTHORITY_BINDING`.

A PASS does **not** retroactively change q4c and does not authorize page-text inspection. After q4d, any new locator must be separately prospectively preregistered with an explicit identity rule justified by the q4d transport record. A cross-provider redirect may not be accepted merely because bytes appear to be a PDF; it requires a separate authoritative binding before any content inspection.

Always:
- Tier-A exact collaboration-internal likelihood = `BLOCKED`;
- Tier-B central/null reproduction = PASS at 0105a6o3;
- full Ar systematic pseudo-data reproduction = `BLOCKED`;
- `SYSTEMATIC_MONTE_CARLO_PREREGISTRATION_PERMISSION = 0%`;
- `SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION = 0%`;
- `OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`;
- NMIR v1 remains frozen and untouched.
