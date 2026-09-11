# NMIR v2 0105a5b-R1j2 — PISA methodology semantic authority locator

Date frozen: 2026-09-11
Parent: validated R1j1 archive-structure PASS.

## Frozen input
Acquire only `https://export.arxiv.org/e-print/1803.05390`; require whole-source SHA256 `e8d26d85195764037765661fb2e5236ec4284a712adbfd9738b7c3908593c6be` before parsing.

Read exactly the complete 21-member R1j1 candidate set, no ranking/pruning: `bits.sty`, `elsarticle.cls`, `main.tex`, `numcompress.sty`, `sample.bib`, `text/ack.tex`, `text/aeff.tex`, `text/bench.tex`, `text/flux.tex`, `text/intro.tex`, `text/motiv.tex`, `text/nmo.tex`, `text/osc.tex`, `text/reco.tex`, `text/res.tex`, `text/significance.tex`, `text/stages.tex`, `text/stages_techniques_intro.tex`, `text/summary.tex`, `text/toy.tex`, `text/valid.tex`.

## Frozen semantic locator
For every candidate, record every case-insensitive literal `PISA` occurrence with at most ±320 characters of context. Additionally record, without interpretation:
1. any `github.com/icecube/pisa` or `icecube/pisa` literal;
2. any 40-hex token occurring within ±320 characters of `PISA`;
3. any of the complete R1i 18 frozen tags when occurring within ±320 characters of `PISA`;
4. the phrases `PISA <tag>`, `PISA v<tag>`, `PISA version <tag>`, `PISA release <tag>` for those 18 tags;
5. any occurrence of the word `version` within ±160 characters of `PISA`, preserving context only and not mapping free-form version text to a tag post-hoc.

Frozen 18 tags: `contours_working_0.1`, `4.3a1`, `4.2.1`, `4.2`, `4.1.4`, `4.1.3`, `4.1.2`, `4.1.1`, `4.1`, `4.0`, `3.2.1`, `3.2`, `3.1`, `3.0`, `2.0.1`, `2.0`, `1.0.1`, `1.0`.

## Classification
`PASS_0105A5B_R1J2_PISA_METHODOLOGY_EXPLICIT_IMPLEMENTATION_AUTHORITY_FOUND_NONDISCOVERY` iff the source contains at least one PISA occurrence and at least one explicit immutable implementation identifier: either a 40-hex token within the PISA context or exactly one of the 18 frozen tags in a qualifying explicit PISA/tag form.

Otherwise, if PISA occurs but no such immutable identifier is found: `BLOCKED_0105A5B_R1J2_PISA_METHODOLOGY_IMPLEMENTATION_STATE_NOT_IMMUTABLY_IDENTIFIED`.

If no PISA occurrence exists in the complete set: `BLOCKED_0105A5B_R1J2_NO_PISA_SEMANTIC_EVIDENCE`. Byte/archive/member failure: `INFRASTRUCTURE_FAIL_0105A5B_R1J2`.

Even PASS would only permit a separately preregistered byte-locked inspection of the explicitly identified implementation state. It does not close Barr/CSMS authority, authorize standard-3nu, systematics MC, observed residuals, or BSM scans.

No PISA repository content may be fetched in R1j2.

`OBSERVED_BSM_RESIDUAL_PERMISSION: 0%`
`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION: 0%`
