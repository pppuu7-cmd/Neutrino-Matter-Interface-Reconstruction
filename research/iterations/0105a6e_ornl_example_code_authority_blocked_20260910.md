# 0105a6e — official ORNL example-code authority classified BLOCKED

Date: 2026-09-10
Gate: `NMIR-V2-0105A6E`
Classification: `BLOCKED_0105A6E_OFFICIAL_ORNL_IMPLEMENTATION_AUTHORITY_INCOMPLETE`
Scope: authority acquisition/semantic classification only; NONDISCOVERY.

## Prospective parent

Preregistration: `research/prereg/0105a6e_coherent_ornl_example_code_authority.md`.

0105a6d remains historically and methodologically intact. This new gate tested the distinct official ORNL Git repository explicitly identified by the COHERENT April-2018 data release as its accompanying example-code repository.

## Hosted evidence

NMIR execution head: `c1a8abfaae9e0fed3e816309860968ceee4d0720`
Workflow run/job: `34487115261 / 102904115790`
Workflow conclusion: `success`
Dedicated guards: `5 passed`
Artifact: `10156093860`, `nmir-v2-0105a6e-coherent-ornl-authority`
Artifact ZIP SHA256: `fda2b85402146c48b5db2f54925e7ef470cbc8f1e97fb2e59a36123f502d7d82`
Inventory JSON SHA256: `bb36f3eb3d6e6b0b81475c32effaddd7b85a4f2d4ffde22dc6f25130cd06ba5c`

## Exact provider identity

Official remote:
`https://code.ornl.gov/COHERENT/codeExamples_dataRelease_april2018.git`

Resolved default branch: `refs/heads/master`
Resolved commit: `6d7c821d66aabe0f2784fce67b504faa0bc6498f`
Commit subject: `Initial commit of code examples for data release`
Commit timestamp: `2018-04-25T02:31:09-05:00`
Tree SHA: `9fa70c98f562214be0a819b89ec8a454cadc4c69`
Tracked files: 5

Tracked-byte identities:

- `README`: SHA256 `59e0c19c8edcf1e1909c9509ec083c4b8fd4a7277233f83b39f9aab8773ca694`
- `coherent_readDataExample.py`: SHA256 `bd57ea90a4491921508c94eb986fc3bb4c54bfaa11650e0cc57a8aa6c0cf2cc7`
- `coherent_readParameters.py`: SHA256 `ee22fe482fd5b29a8db1b9ff0eca66483e337e00cf86e45311f56a56eb71f9dd`
- `coherent_readPromptPDF.py`: SHA256 `81e04de0ef5c3b4247cb97e69d3166e16b02ab4dbfe74ffde740c56a9323179a`
- `coherent_readTiming.py`: SHA256 `331bcfd7c02e60621f52a31417fbb6ff5c00de9f5543d2946496c8989b381758`

## Frozen semantic inventory result

The official repository provides deterministic data-handling/response examples:

- `coherent_readPromptPDF.py` contains acceptance/efficiency logic and prompt-neutron handling;
- `coherent_readTiming.py` contains prompt-neutron timing handling;
- README locates efficiency and prompt-neutron examples;
- data and parameter readers are present.

However, across all five tracked text files the frozen inventory found no implementation-level hits for the terms required to recover a unique statistical contract: no `likelihood`, `loglikelihood`, `nll`, `chi2`, `chi-square`, `poisson`, `gaussian`, `constraint`, `profile`, `nuisance`, `covariance`, `correlation`, or `minuit` implementation.

Therefore the exact official repository does not uniquely specify:

- the elementary CsI data objective;
- the full nuisance penalty/constraint model;
- profiling/floating/fixed prescriptions;
- correlation/covariance semantics;
- a complete executable standalone collaboration likelihood.

The data-release documentation itself describes the final comparison generically as calculating a `likelihood or chi2`, which confirms that the public release is an analysis-enabling package rather than a unique published likelihood implementation contract.

## Classification logic

Transport and byte identity succeeded. The blocker is semantic incompleteness, not provider failure:

`BLOCKED_0105A6E_OFFICIAL_ORNL_IMPLEMENTATION_AUTHORITY_INCOMPLETE`

A green workflow is not scientific PASS.

This is not evidence that the Standard Model fails, nor evidence of a BSM residual. It says only that the frozen public official CsI assets tested so far do not determine a unique reproduction of the collaboration statistical fit without analyst choices.

## Authorization state

`SM_NULL_REPRODUCTION_PERMISSION = 0%`

`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`

No downstream fit or residual scan is authorized by this gate.

## Methodological consequence / next front

The next admissible step should not keep searching arbitrary third-party CsI reanalyses for a convenient likelihood. Instead either:

1. prospectively search additional **official collaboration/provider** materials for a uniquely specified CsI statistical implementation; or
2. pivot the standalone-null closure effort to the Ar target, for which 0105a6d already recovered a source tar containing `main.tex` and `supplemental.tex` with explicit likelihood/NLL/profile/RooFit terminology, and test field-by-field whether those official bytes satisfy the frozen implementation contract.

The Ar route is currently the stronger authority-preserving next gate because its source bytes are already available and visibly contain the relevant statistical semantics.
