# 0105a6q5f2 — arXiv source semantic-evidence preregistration

Date: 2026-09-11
Gate: `NMIR-V2-0105A6Q5F2`
Scope: bounded authority/implementation semantic evidence only; NONDISCOVERY.

Parent q5f1 validated PASS record: `e0e632c06ad026308faf58738262dcb8a2a31bde`.
Frozen exact arXiv source SHA256: `5d000befd41e44deece46f31e1bf3ee7305bc2e8c0357b524311962ddc9d3dde`, bytes `23805`, endpoint `https://arxiv.org/e-print/2006.12659`.

## Frozen complete candidate set

No source-member payload has been inspected before this preregistration. q5f1 returned exactly four source-text candidates, all of which must be included without ranking or pruning:

- `authors_els.tex` — 4985 bytes
- `CENNS10DataReleaseCompanion.bbl` — 1308 bytes
- `CENNS10DataReleaseCompanion.bib` — 1274 bytes
- `CENNS10DataReleaseCompanion.tex` — 27656 bytes

Before reading any candidate payload, reacquire the exact source bundle and require exact byte count and SHA256. Extract/read only these four exact members. Other member payloads remain unread.

## Frozen unresolved questions inherited from q5e

This gate may adjudicate only whether the publication source explicitly supplies additional authority sufficient to resolve these already-frozen q5e items:

- **F1 elementary observation/count law**: explicit statement identifying Poisson, fixed-total/multinomial, or another explicitly specified elementary event/count-generation law relevant to the Argon analysis/pseudo-data construction. Generic `extended likelihood`, `maximum likelihood`, RooFit usage, or normalizations alone are insufficient.
- **F4 shape-systematic application**: explicit statement specifying how the published ±1σ/shape systematic alternatives enter the analysis (for example, separate excursions/fits, interpolation/morphing with a stated rule, or another explicit application contract). Merely naming systematic PDFs/files is insufficient.
- **F6 simultaneous/correlation treatment**: explicit statement specifying whether the relevant shape/systematic directions are applied/fitted jointly or separately and any correlation/independence rule required for the likelihood/systematic procedure. Unrelated correlation statements are insufficient.
- **F7 central-count anchor/precedence**: explicit statement resolving which central event-count/normalization anchor governs when `3152` and `3154` conflict, or an explicit rule showing that they serve distinct non-conflicting roles. Mere occurrence of either number is insufficient.

## Frozen evidence procedure

For each F1/F4/F6/F7, search the full text of all four candidates using a preregistered broad lexical union tied to that question, then retain every hit with exact member name and line number plus a deterministic ±4-line context window. The lexical union must be fixed in code before hosted execution and must not be amended after seeing source text. Classification must rely only on literal text in retained windows; no inference from software defaults, standard HEP practice, or external documents is permitted.

If an item has no literal evidence, or evidence is incomplete, ambiguous, or contradictory, classify that item `BLOCKED_INCOMPLETE_OR_AMBIGUOUS`. A positive item requires an explicit statement that uniquely supplies the required contract above. Do not resolve contradictions by preference/ranking after seeing the evidence.

## Frozen outcomes

- `PASS_0105A6Q5F2_ARXIV_SOURCE_SEMANTIC_CONTRACT_COMPLETE_NONDISCOVERY` iff source identity matches and **all four** F1/F4/F6/F7 are explicitly and uniquely resolved by retained literal source evidence.
- `BLOCKED_0105A6Q5F2_ARXIV_SOURCE_SEMANTIC_CONTRACT_INCOMPLETE` iff source identity matches but one or more of F1/F4/F6/F7 is absent, incomplete, ambiguous, or contradictory.
- `BLOCKED_0105A6Q5F2_SOURCE_TRANSPORT_OR_EXTRACTION_FAILURE` if exact source acquisition or extraction cannot complete.
- `FAIL_0105A6Q5F2_SOURCE_BYTE_IDENTITY_MISMATCH` if acquired bytes disagree with the frozen q5f/q5f1 identity.

A PASS is authority/implementation NONDISCOVERY only. It may permit a separately prospectively preregistered Ar standalone null/systematics reproduction gate, subject to all other frozen authority requirements. A BLOCKED result exhausts this arXiv-source route under these criteria and must not trigger post-hoc lexical expansion or semantic relaxation.

No pseudo-data generation, likelihood evaluation, optimizer execution, systematic Monte Carlo, nuisance profiling, observed residual inspection, BSM model scan, significance calculation, or generic Wilks threshold is permitted in q5f2.

`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION = 0%`
`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`