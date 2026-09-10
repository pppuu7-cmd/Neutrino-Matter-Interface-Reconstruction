# 0105a6q4e — Ar 2022 review authority-bound count-law locator

Status: **PREREGISTERED BEFORE ANY TARGET PDF PAGE-TEXT INSPECTION / PROSPECTIVE**

## Parents and immutable provenance

Scientific predecessor q4c:
- classification: `BLOCKED_0105A6Q4C_2022_REVIEW_TRANSPORT_OR_IDENTITY_FAILURE`;
- result SHA256: `988fbbc0b5c2f0a74562fb33a829eaae8ff3ebedd1ded7e25376d967a43ef612`;
- q4c lexical implementation Git blob SHA1: `cd24f33be2b17f643d13d2399719e9bf26fecc7b`;
- q4c must remain historically BLOCKED and is not reclassified by q4e.

Transport predecessor q4d:
- run/job/artifact: `34534299833 / 103062198583 / 10174763404`;
- artifact ZIP SHA256: `e62f20e5d2d770599dc203419848300d2f433ef7715162603d812ea39039660d`;
- result SHA256: `fd36f42625747fd849a1aa44acca61804dac84844f172f1eb4c5d91bb131e848`;
- classification: `BLOCKED_0105A6Q4D_CROSS_PROVIDER_REDIRECT_REQUIRES_SEPARATE_AUTHORITY_BINDING`;
- q4d must remain historically BLOCKED and is not reclassified by q4e.

q4d observed exactly one HTTP 302 from the frozen legacy CERN Indico URL to the exact `indico.global` URL below, followed by HTTP 200 and a valid PDF. q4d did not inspect page text.

## Authority binding fixed before content inspection

The cross-host transition is accepted for **this new prospective locator only** because all of the following were available before q4e content inspection:

1. q4d mechanically recorded the exact legacy-to-new URL redirect and exact response bytes.
2. CERN's 2025 Indico Workshop has an official CERN-hosted contribution titled `indico.global`, presented by Adrian Mönnich (CERN):
   `https://indico.cern.ch/event/1503347/contributions/6472568/`
3. The associated CERN-hosted `indico.global` presentation documents the migration problem, changing database IDs, the requirement not to break links, and the need for redirects from old URLs to new URLs:
   `https://indico.cern.ch/event/1503347/contributions/6472568/attachments/3062290/5415486/presentation-global.pdf`
4. The CERN Site Report (31 March 2025) reports completion of migration of approximately 12,000 Indico events to `indico.global`:
   `https://indico.cern.ch/event/1477299/contributions/6367009/attachments/3041294/5372471/CERN%20Site%20Report%20Lugano%202025.pdf`

This authority binding does not authorize arbitrary `indico.global` documents. It authorizes only the exact target identity below.

## Frozen target identity

Legacy URL recorded by q4d:
`https://indico.cern.ch/event/978288/contributions/5014436/attachments/2504944/4303826/JCZBLV2022_CEvNSReviewTalk.pdf`

Exact authority-bound target URL:
`https://indico.global/event/13069/contributions/114762/attachments/53315/102415/JCZBLV2022_CEvNSReviewTalk.pdf`

Required response identity before any text extraction:
- final URL must equal the exact authority-bound target URL;
- HTTP status must be 200;
- payload must begin `%PDF-`;
- payload size must equal `18484736` bytes;
- payload SHA256 must equal `af0fb243be7d8433fbc003de1d963bee3b3510467cfbbd6b1990f1e6626de817`.

Any failure of these identity conditions terminates before `pdftotext` with:
`BLOCKED_0105A6Q4E_TARGET_IDENTITY_FAILURE`.

## Frozen lexical contract — exactly q4c

q4e may not invent, remove, broaden, narrow, reorder semantically, or tune search terms after seeing the PDF. It must reuse the q4c `norm()` and `flags()` implementation from Git blob `cd24f33be2b17f643d13d2399719e9bf26fecc7b` exactly.

The q4c contract is:
- L1: `pseudo-data` / `pseudo data`;
- L2: `poisson`, `poissonian`, `fixed total`, `fixed number`, `fixed event count`, `number of events is fixed`, `multinomial`, `bootstrap`, or resample variants;
- L3: generation token OR event-count token OR API token (`RooMCStudy`, `generateBinned`, `numEvents`, `extended`);
- L4: RooFit/implementation token (`RooFit`, `RooAbsPdf`, `RooMCStudy`, `likelihood code`, `fit machinery`) OR L1 together with `TTree`.

Candidate categories remain exactly:
- `DIRECT_COUNT_LAW_CANDIDATE` iff L1 AND L2;
- `IMPLEMENTATION_CONTRACT_CANDIDATE` iff L1 AND L3 AND L4;
- `COUNT_GENERATION_CANDIDATE` iff L1 AND generation token AND count token.

## Frozen execution and retained output

1. Recover and verify the exact q4d result artifact by frozen ZIP and result SHA256.
2. Verify q4d classification, final URL, payload size, and payload SHA256 against this preregistration.
3. Verify the q4c lexical implementation Git blob identity before execution.
4. Download the exact target URL without accepting a changed final URL.
5. Verify all target byte-identity gates before any `pdftotext` execution.
6. Only after all gates pass, run `pdftotext -layout` and apply the exact q4c lexical contract page-by-page.
7. Retain/upload only page number, normalized-page-text SHA256, boolean lexical flags, category labels, source identity, page count, and audit booleans. Do not retain/upload page text.
8. Do not generate pseudo-data, evaluate a likelihood, inspect observed BSM residuals, tune a model, or execute/preregister systematic Monte Carlo.

## Frozen decision classes

- Exact target identity fails before text extraction: `BLOCKED_0105A6Q4E_TARGET_IDENTITY_FAILURE`.
- q4c lexical implementation identity fails: `BLOCKED_0105A6Q4E_LEXICAL_CONTRACT_IDENTITY_FAILURE`.
- Exact PDF is inspected under the frozen q4c lexical contract and no candidate page exists: `BLOCKED_0105A6Q4E_2022_REVIEW_HAS_NO_COUNT_LAW_CANDIDATE_PAGES`.
- One or more candidate pages exist: `PASS_0105A6Q4E_2022_REVIEW_CANDIDATE_PAGES_LOCATED_NONDISCOVERY`.

A PASS is only a locator result. Candidate pages require a separately preregistered q4f semantic/authority audit before any count-law claim can be used downstream.

Always:
- Tier-A exact collaboration-internal likelihood = `BLOCKED`;
- Tier-B central/null reproduction = PASS at 0105a6o3;
- full Ar systematic pseudo-data reproduction = `BLOCKED`;
- `SYSTEMATIC_MONTE_CARLO_PREREGISTRATION_PERMISSION = 0%`;
- `SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION = 0%`;
- `OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`;
- NMIR v1 remains frozen and untouched.
