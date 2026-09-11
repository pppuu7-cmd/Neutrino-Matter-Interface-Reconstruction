# 0105a5b R1k2 — predecessor DeepCore PISA implementation semantic locator preregistration

Date: 2026-09-11
Branch: `research/0105-bsm-residual-reconstruction`
Prerequisite: validated R1k1 archive-structure PASS.

## Frozen source and candidate set

Required source SHA256: `d095d23daf4dc08848b7f3ff5977daaf554db966034ca9d3460e4b88d7c3790a`.

The complete candidate set is frozen exactly as returned by R1k1, with no ranking or pruning:
`history.txt`, `main.bib`, `main.tex`, `readme-epjc.txt`, `svjour3.cls`, `text/SampleAndReco.tex`, `text/abstract.tex`, `text/acknowledgement.tex`, `text/analysis.tex`, `text/conclusion.tex`, `text/icecube.tex`, `text/introduction.tex`, `text/results.tex`, `text/sensitivity.tex`.

## Frozen semantic questions

For every candidate payload R1k2 may record only:
1. case-insensitive occurrences of `PISA` with bounded ±300-character context;
2. literal `icecube/pisa` or GitHub URLs containing `pisa`;
3. 40-hex tokens within ±300 characters of a PISA occurrence;
4. explicit version-like forms within ±300 characters of PISA: `vN`, `vN.M`, `vN.M.P`, `version N[.M[.P]]`, `release N[.M[.P]]`, `tag ...`, `commit ...`.

These patterns are frozen before payload inspection. No result-dependent expansion is allowed.

## Frozen classification

`PASS_0105A5B_R1K2_PREDECESSOR_PISA_IMMUTABLE_STATE_EXPLICIT_NONDISCOVERY` only if an explicit immutable 40-hex commit or an explicit repository tag/version literal is present in a PISA context.

Otherwise classification is `BLOCKED_0105A5B_R1K2_PREDECESSOR_PISA_STATE_NOT_IMMUTABLY_IDENTIFIED`.

A PASS would identify only a predecessor-analysis implementation state. It would not prove that the 2023 analysis used the same state. A separate prospective cross-analysis compatibility/provenance gate would still be required before any implementation use.

## Hard prohibitions

No PISA repository fetch, no implementation-code inspection, no numerical/output matching, no post-hoc tag selection, no standard-3nu execution, no systematic Monte Carlo, and no observed BSM residual inspection.

`NMIR_V2_DISCOVERY_READINESS: 48%`
`OBSERVED_BSM_RESIDUAL_PERMISSION: 0%`
`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION: 0%`
