# 0105a6q4c — Ar collaboration-author 2022 review-talk count-law authority locator

Status: **PREREGISTERED BEFORE TARGET PDF BYTE/TEXT INSPECTION / NONDISCOVERY**

Parent: `BLOCKED_0105A6Q4B_2018_PRESENTATION_HAS_NO_COUNT_LAW_CANDIDATE_PAGES`.
Parent immutable record commit: `07e302565164ab0832d5aed6ca82c80501ee2306`.
Parent run/job/artifact: `34528295791 / 103042509396 / 10172447344`.
Parent artifact ZIP SHA256: `0b2b857f7bd5be70103bd8c8c711081fe0bacef1dae2e308fa037cff81f7a890`.
Parent inner result SHA256: `6fde625abdd97db2576004183cc3dae4a029b1a8da6ecf02bb89b65e58185059`.

## Purpose

Seek one genuinely new provenance-qualified collaboration-author artifact for the unresolved CENNS-10 Analysis-A pseudo-data event-count generation law. This gate is only source identity/byte lock plus the unchanged mechanical lexical locator. It may not semantically adjudicate text, generate pseudo-data, evaluate a likelihood, inspect an observed residual, or fit a BSM model.

## Prospectively frozen source identity

Provider: CERN Indico.
Frozen presentation:
- speaker/author: Jacob Zettlemoyer;
- title: `Experimental efforts and physics capabilities of Coherent Elastic Neutrino-Nucleus Scattering (CEvNS)`;
- meeting: 2022 International Workshop on Baryon and Lepton Number Violation;
- date shown on presentation metadata: September 8, 2022;
- exact PDF URL frozen before PDF inspection: `https://indico.cern.ch/event/978288/contributions/5014436/attachments/2504944/4303826/JCZBLV2022_CEvNSReviewTalk.pdf`.

Hosted execution must require HTTPS host `indico.cern.ch`, exact frozen path, no query or fragment, PDF magic, exact byte size recording, and computed SHA256. Redirect to a different host/path is BLOCKED. No mirror, cached copy, transcription, video, or alternate talk may substitute.

This is secondary collaboration-author authority, not Tier-A collaboration-release authority and not permission to override the official COHERENT release.

## Frozen locator procedure

After source identity and byte locking, convert the complete PDF page-by-page with `pdftotext -layout`; lower-case and collapse whitespace. Do not retain or upload page text.

Reuse exactly the q2/q4/q4a/q4b lexical groups and candidate rules, with no additions:
- L1: `pseudo-data` or `pseudo data`;
- L2: `poisson`/`poissonian`, `fixed total`, `fixed number`, `fixed event count`, `number of events is fixed`, `multinomial`, `bootstrap`, `resample`/`resampled`/`resampling`;
- L3: `number of events`, `event count(s)`, `generate*`, `RooMCStudy`, `generateBinned`, `NumEvents`, `Extended`;
- L4: `RooFit`, `RooAbsPdf`, `RooMCStudy`, same-page `TTree`+pseudo-data, `likelihood code`, `fit machinery`.

Candidate rules:
- `DIRECT_COUNT_LAW_CANDIDATE = L1 && L2`;
- `IMPLEMENTATION_CONTRACT_CANDIDATE = L1 && L3 && L4`;
- `COUNT_GENERATION_CANDIDATE = L1 && generation_token && count_token`.

Candidate set is the sorted union. No page may be added or removed after locator output.

## Decision

Non-empty candidate set -> `PASS_0105A6Q4C_2022_REVIEW_CANDIDATE_PAGES_LOCATED_NONDISCOVERY`.

Empty candidate set -> `BLOCKED_0105A6Q4C_2022_REVIEW_HAS_NO_COUNT_LAW_CANDIDATE_PAGES`.

Transport/source-identity/PDF/page-extraction failure -> `BLOCKED_0105A6Q4C_2022_REVIEW_TRANSPORT_OR_IDENTITY_FAILURE`.

A locator PASS is not evidence for a count law. It authorizes only a separate prospective bounded semantic audit of the entire returned candidate set before candidate text inspection, reusing q1/q3 Q3-P/Q3-F/Q3-O without weakening.

If q4c is BLOCKED, do not infer the law and do not rescan previous artifacts with post-result keywords.

Always:
- Tier-A exact collaboration-internal likelihood = `BLOCKED`;
- Tier-B central/null reproduction = PASS at 0105a6o3;
- full Ar systematic pseudo-data reproduction = `BLOCKED`;
- `SYSTEMATIC_MONTE_CARLO_PREREGISTRATION_PERMISSION = 0%`;
- `SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION = 0%`;
- `OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`.