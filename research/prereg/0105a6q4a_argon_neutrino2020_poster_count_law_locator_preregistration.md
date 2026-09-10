# 0105a6q4a — Ar collaboration-author Neutrino-2020 poster count-law authority locator

Status: **PREREGISTERED BEFORE POSTER BYTE/TEXT INSPECTION / NONDISCOVERY**

Parent: `BLOCKED_0105A6Q4_PRESENTATION_HAS_NO_COUNT_LAW_CANDIDATE_PAGES`.
Parent immutable record commit: `a2a88447f75cd6452d09c2af3d1b8ca32045f33f`.
Parent run/job/artifact: `34517232078 / 103005576575 / 10168186403`.
Parent artifact ZIP SHA256: `188f9c852533506c906cf39f591638a6db4812be8500e7dce953eca5c02aa1f3`.
Parent inner result SHA256: `039bb01dc39021ce0c5a48995f9b4acbcac9a2762d9435acc0079ef81b5df396`.

## Purpose

Seek a genuinely new provenance-qualified collaboration-author artifact for the unresolved CENNS-10 Analysis-A pseudo-data event-count generation law after q4 found no candidate pages in the 2019 presentation.

This gate is only a provider byte-lock plus mechanical lexical locator. It must not semantically adjudicate poster text, generate pseudo-data, evaluate a likelihood, inspect observed residuals, or fit any BSM model.

## Prospectively frozen provider/source

Only the following collaboration-author artifact is allowed:

- Zenodo record `4252695`, `First Detection of CEvNS on Argon with the CENNS-10 Liquid Argon Detector`;
- creator: Jacob Zettlemoyer;
- resource type: poster associated with Neutrino 2020;
- exact PDF file: `JCZNeutrino2020CENNS10Landscape.pdf`;
- provider MD5: `c00fe90b1e16f3069ff6970308ee8345`;
- canonical provider file URL: `https://zenodo.org/records/4252695/files/JCZNeutrino2020CENNS10Landscape.pdf?download=1`.

The hosted gate must verify provider MD5 and PDF identity and compute/store exact file size + SHA256 before any text conversion. Provider-byte mismatch is fail-closed.

This is secondary collaboration-author authority, not Tier-A collaboration-release authority. Even a locator/semantic PASS cannot upgrade Tier-A exact likelihood status by itself.

The MP4 on the same record is outside this gate and must not be inspected here.

## Frozen locator procedure

After byte verification, convert the complete PDF page-by-page with `pdftotext -layout`; lower-case and collapse whitespace. Do not retain or upload page text.

For every physical page compute normalized-text SHA256. Reuse exactly the q2/q4 lexical groups and candidate rules without additions:

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

Non-empty candidate set -> `PASS_0105A6Q4A_POSTER_CANDIDATE_PAGES_LOCATED_NONDISCOVERY`.

Empty candidate set -> `BLOCKED_0105A6Q4A_POSTER_HAS_NO_COUNT_LAW_CANDIDATE_PAGES`.

Provider/transport/PDF/page-extraction failure -> `BLOCKED_0105A6Q4A_POSTER_TRANSPORT_OR_IDENTITY_FAILURE`.

A locator PASS means only that candidate pages exist. It is not evidence for any event-count law.

## Authorization consequence

If q4a locator PASS, only a separate prospective semantic audit of the entire returned candidate set may be preregistered before inspecting candidate text, reusing q1/q3 Q3-P/Q3-F/Q3-O without weakening.

If q4a BLOCKED, do not infer the law. Continue only to another genuinely new provenance-qualified collaboration-author/collaboration-owned implementation artifact; do not rescan q4/q4a with post-result keywords.

Always:
- Tier-A exact collaboration-internal likelihood = `BLOCKED`;
- Tier-B central/null reproduction = PASS at 0105a6o3;
- full Ar systematic pseudo-data reproduction = `BLOCKED`;
- `SYSTEMATIC_MONTE_CARLO_PREREGISTRATION_PERMISSION = 0%`;
- `SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION = 0%`;
- `OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`.
