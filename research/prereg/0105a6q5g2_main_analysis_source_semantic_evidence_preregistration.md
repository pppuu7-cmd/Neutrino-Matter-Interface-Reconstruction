# 0105a6q5g2 — main Analysis-A source semantic-evidence preregistration

Date: 2026-09-11
Gate: `NMIR-V2-0105A6Q5G2`
Scope: bounded authority/implementation semantic evidence only; NONDISCOVERY.

Parent q5g1 validated PASS record: `56b4d2a58b5e79b8321d2c12ea09bcd776d648a6`.
Frozen exact arXiv source: endpoint `https://arxiv.org/e-print/2003.10630`, bytes `446096`, SHA256 `2edeb3dcc3df99de575c8b2091f48099a7538eedf9f382996d943c7fbe7e2114`.

## Frozen complete candidate set

No candidate-member payload has been inspected under q5g1. q5g1 returned exactly six source-text candidates and q5g2 must include all of them without ranking or pruning:

- `authors.tex` — 6826 bytes
- `commands.tex` — 3979 bytes
- `main.bbl` — 37145 bytes
- `main.bib` — 45756 bytes
- `main.tex` — 30063 bytes
- `supplemental.tex` — 9705 bytes

Before reading any candidate payload, reacquire the exact source bundle and require exact byte count and SHA256. Extract/read only these six exact members. All other member payloads remain unread.

## Frozen questions inherited unchanged from q5f2

q5f2 resolved F4 and F6 but left only the following authority blockers. q5g2 may adjudicate only these two items:

- **F1 elementary observation/count law**: explicit statement identifying Poisson, fixed-total/multinomial, or another explicitly specified elementary event/count-generation law relevant to the Argon analysis/pseudo-data construction. Generic `extended likelihood`, `maximum likelihood`, RooFit usage, fit normalizations, or common HEP practice are insufficient.
- **F7 central-count anchor/precedence**: explicit statement resolving which central event-count/normalization anchor governs when `3152` and `3154` conflict, or an explicit rule showing that they serve distinct non-conflicting roles. Mere occurrence of either number is insufficient.

F4 remains `RESOLVED_EXPLICIT_SEPARATE_ALTERNATIVE_FITS` and F6 remains `RESOLVED_EXPLICIT_SEPARATE_SYSTEMATIC_FITS` from validated q5f2; q5g2 must not reopen or modify those findings.

## Frozen evidence procedure

For F1 and F7, search the full text of all six candidates using lexical unions fixed in code before hosted execution. Retain every lexical hit with exact member name and line number plus deterministic ±4-line context. The lexical unions must be broad enough to cover the already-frozen semantics, but once committed they must not be changed after any candidate payload is inspected.

F1 lexical union must include literal variants covering at least: `Poisson`, `multinomial`, `fixed total`, `fixed-total`, `number of events`, `event count`, `events are generated`, `generated events`, `pseudo-data`, `pseudodata`, `toy`, `extended likelihood`, and `RooFit`.

F7 lexical union must include literal variants covering at least: `3152`, `3154`, `steady-state`, `steady state`, `background`, `normalization`, `central value`, `events`, and `counts`.

Classification may rely only on literal text retained from the complete six-member set. No inference from software defaults, standard HEP practice, q5f2 external source text, figure appearance, or uninspected archive members is permitted. If evidence is absent, incomplete, ambiguous, or contradictory, the corresponding item is `BLOCKED_INCOMPLETE_OR_AMBIGUOUS`. A positive item requires an explicit statement that uniquely supplies the frozen contract.

## Frozen outcomes

- `PASS_0105A6Q5G2_MAIN_ANALYSIS_SOURCE_F1_F7_CONTRACT_COMPLETE_NONDISCOVERY` iff exact source identity matches and both F1 and F7 are explicitly and uniquely resolved by retained literal source evidence.
- `BLOCKED_0105A6Q5G2_MAIN_ANALYSIS_SOURCE_F1_F7_CONTRACT_INCOMPLETE` iff exact source identity matches but either F1 or F7 is absent, incomplete, ambiguous, or contradictory.
- `BLOCKED_0105A6Q5G2_SOURCE_TRANSPORT_OR_EXTRACTION_FAILURE` if exact source acquisition or extraction cannot complete.
- `FAIL_0105A6Q5G2_SOURCE_BYTE_IDENTITY_MISMATCH` if acquired bytes disagree with the frozen q5g/q5g1 identity.

A PASS is authority/implementation NONDISCOVERY only. It does not itself authorize pseudo-data generation, systematic Monte Carlo, likelihood execution, nuisance profiling, observed residual inspection, BSM fitting, significance calculation, or Wilks thresholds. Any subsequent numerical gate must be separately prospectively preregistered after all relevant authority requirements are shown complete.

A BLOCKED result exhausts this exact six-member main-source route under these criteria and must not trigger post-hoc lexical expansion, candidate pruning, or semantic relaxation.

`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION = 0%`
`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`