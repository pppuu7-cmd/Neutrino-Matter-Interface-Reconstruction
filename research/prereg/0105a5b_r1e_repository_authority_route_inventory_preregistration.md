# NMIR v2 0105a5b-R1e — repository authority-route inventory preregistration

Date frozen: 2026-09-11
Branch: `research/0105-bsm-residual-reconstruction`

## Purpose

Machine-check the already committed NMIR v2 repository record for any still-unconsumed DeepCore R1d external computational-authority route. This gate does not contact external sources, does not inspect new scientific content, and cannot authorize standard-3nu reproduction by itself.

## Frozen corpus

Scan tracked UTF-8 repository files under `research/`, `scripts/`, `tests/`, and `.github/workflows/` at the execution commit, excluding this R1e preregistration, implementation, tests, workflow, generated artifacts, `research/NMIR_V2_CURRENT_FRONT.md`, and `research/NMIR_V2_RECOVERY.md`.

Only files containing at least one case-insensitive marker from the frozen set below enter the inventory:

- `0105a5b`
- `r1d`
- `external computational authority`
- `upstream authority`

Within those files record, without following anything:

1. literal `http://` or `https://` URLs;
2. literal strings matching `zenodo`, `github`, `repository`, `artifact`, `response matrix`, `derivative table`, `nuisance response`, `systematic response`, `systematic derivative`, `likelihood code`;
3. the source file path and line number for every hit.

## Frozen classification

PASS/NONDISCOVERY `PASS_0105A5B_R1E_REPOSITORY_AUTHORITY_ROUTE_INVENTORY_EMITTED_NONDISCOVERY` iff the deterministic repository scan completes and emits a canonical inventory plus SHA256.

BLOCKED `BLOCKED_0105A5B_R1E_REPOSITORY_AUTHORITY_ROUTE_INVENTORY_EMPTY_OR_UNREADABLE` iff the scan cannot read the frozen corpus or finds no R1d-related source files.

This gate deliberately does **not** decide whether any hit is scientifically sufficient or unconsumed. That interpretation requires a later immutable consume/classify step. A PASS does not authorize external fetching, link following, standard-3nu reproduction, nuisance construction, systematic Monte Carlo, observed residuals, or BSM inference.

## Hard prohibitions

No network requests. No external file acquisition. No link following. No modification of R1d scientific criteria. No use of QKL28Z as a replacement for B4RITM. No standard-3nu execution. No observed residual inspection.

`OBSERVED_BSM_RESIDUAL_PERMISSION: 0%`
`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION: 0%`
