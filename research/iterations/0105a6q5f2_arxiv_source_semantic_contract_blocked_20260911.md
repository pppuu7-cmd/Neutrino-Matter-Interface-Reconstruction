# 0105a6q5f2 — validated arXiv source semantic-contract audit

Date: 2026-09-11
Gate: `NMIR-V2-0105A6Q5F2`
Classification: `BLOCKED_0105A6Q5F2_ARXIV_SOURCE_SEMANTIC_CONTRACT_INCOMPLETE`
Scope: authority/implementation semantics only; NONDISCOVERY.

## Prospective chain

- q5f1 PASS record: `e0e632c06ad026308faf58738262dcb8a2a31bde`
- q5f2 preregistration: `58e32cedffb6c173079f8098513dbc1e81fbb4b6`, committed before any candidate-member payload inspection
- implementation: `d55d97c7350cb4fa1d73e07539fca52d8a3e87cb`
- guards: `5468fa0a62faa952a52a85113b2e311d8bf1e994`
- execution head: `9abb961030db17ada79983cf30d6569cc64766b6`

## Hosted validation

- run/job/artifact: `34551690439/103115756953/10181041069`
- dedicated guards: `5 passed`
- provider artifact ZIP SHA256: `715d71051aa1fb1925150ae1b37e63409e72b73fb5e4c9ebd59f260f3765a51b`
- independently downloaded ZIP SHA256: `715d71051aa1fb1925150ae1b37e63409e72b73fb5e4c9ebd59f260f3765a51b`
- independent inner `result.json` SHA256: `aaa8d3ca46b93ac0673d2189dbd852af70292782138ca0582770f1e8dcc8c8d2`
- source identity revalidated: HTTP 200, 23805 bytes, SHA256 `5d000befd41e44deece46f31e1bf3ee7305bc2e8c0357b524311962ddc9d3dde`

All four prospectively frozen candidates were read, with exact member hashes retained. No other archive member payload was needed for the gate.

## Frozen-item adjudication from retained literal windows

- **F1 elementary observation/count law: `BLOCKED_INCOMPLETE_OR_AMBIGUOUS`.** There are zero F1 lexical hits in the complete four-candidate source set. No explicit Poisson, multinomial, fixed-total, or other elementary count-generation law is supplied. An extended/likelihood convention is therefore not inferred.
- **F4 shape-systematic application: `RESOLVED_EXPLICIT_SEPARATE_ALTERNATIVE_FITS`.** `CENNS10DataReleaseCompanion.tex` explicitly states that the data are fit with alternative PDFs to generate the systematic-error envelope; it provides ±1σ systematic PDFs where applicable and states that the systematic rows identify which PDFs to fit to replicate each systematic effect. It also explicitly refers to separate systematic fits and to running a set of alternative fits. This supplies the application contract without inventing continuous morphing/interpolation.
- **F6 simultaneous/correlation treatment: `RESOLVED_EXPLICIT_SEPARATE_SYSTEMATIC_FITS`.** The same prospectively retained windows explicitly describe separate systematic fits / a set of alternative fits for individual systematic effects. No simultaneous joint nuisance morph is stated or assumed. This resolves the relevant joint-vs-separate question for the released systematic-error procedure; unrelated correlations are not used.
- **F7 central-count anchor/precedence: `BLOCKED_INCOMPLETE_OR_AMBIGUOUS`.** The source explicitly gives steady-state background CV `3152±25`, but the complete source evidence contains no `3154` occurrence and no literal precedence/distinct-role rule reconciling the release-source 3152 with the already frozen YAML 3154 anchor. Therefore the pre-existing conflict remains unresolved.

Because the frozen q5f2 overall PASS required all four F1/F4/F6/F7 to be uniquely resolved, F1 and F7 force overall BLOCKED. This does not undo the useful F4/F6 resolution.

This is authority/implementation BLOCKED, not a Standard-Model scientific FAIL and not BSM evidence. No pseudo-data, likelihood evaluation, optimizer, systematic Monte Carlo, nuisance profile, observed residual, BSM scan, significance or Wilks threshold was executed.

`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION = 0%`
`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`

## Exact continuation rule

The arXiv:2006.12659 companion-source route is exhausted under its frozen candidate set and semantic criteria. F4/F6 are now explicit; only F1 and F7 remain authority blockers from this route. Any next authority step must be separately prospectively registered and genuinely additional provenance-qualified collaboration/publication authority. It must not broaden q5f2 lexical rules post hoc or infer F1/F7 from software defaults or convention.