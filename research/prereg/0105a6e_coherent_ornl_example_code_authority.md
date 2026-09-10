# 0105a6e — COHERENT official ORNL example-code authority acquisition

Date: 2026-09-10
Gate: `NMIR-V2-0105A6E`
Parent: `BLOCKED_0105A6D_AUTHORITY_BYTE_MISMATCH_OR_TRANSPORT`
Stage: official authority acquisition/inventory only; NONDISCOVERY

## Motivation

0105a6d is terminally BLOCKED under its frozen source set because all official arXiv source/e-print endpoints for `1708.01294v1` resolve to the same PDF bytes rather than a source archive. The 0105a6d contract is not amended.

The official COHERENT April-2018 data-release documentation identifies the ORNL GitLab repository `https://code.ornl.gov/COHERENT/codeExamples_dataRelease_april2018` as the accompanying Git repository for the CsI data release. This gate prospectively tests that distinct official-provider asset as a new authority route.

## Frozen provider scope

Only this repository is admissible:

`https://code.ornl.gov/COHERENT/codeExamples_dataRelease_april2018.git`

The hosted execution must:

1. resolve and record the exact remote default-branch commit SHA before inspecting file contents;
2. clone only that exact resolved commit from the official ORNL GitLab host;
3. record Git remote URL, commit SHA, commit timestamp, tree SHA and a deterministic inventory of all tracked files;
4. record SHA256 and byte size of every tracked file;
5. inventory deterministic text hits for the frozen implementation terms below;
6. preserve a transport BLOCK if the exact repository/commit cannot be acquired.

The resolved commit becomes the immutable byte identity of this gate's execution evidence. A later provider update requires a new gate/version, not silent movement of authority.

## Frozen implementation terms

Search all text-decodable tracked files for:

`likelihood`, `loglikelihood`, `log likelihood`, `nll`, `chi2`, `chi-square`, `poisson`, `gaussian`, `constraint`, `profile`, `nuisance`, `covariance`, `correlation`, `minuit`, `fit`, `background`, `efficiency`, `acceptance`, `quenching`, `prompt neutron`, `steady state`.

Term hits are locators, never sufficient for PASS by themselves.

## Required contract for scientific PASS

`PASS_0105A6E_OFFICIAL_ORNL_IMPLEMENTATION_AUTHORITY_NONDISCOVERY` requires the exact official repository bytes to uniquely specify enough of the standalone CsI SM/null analysis to implement it without analyst invention:

- elementary data objective/likelihood family;
- expected signal and background components and their normalization domains;
- nuisance parameters, constraints/penalties, sign/units and rate/shape coupling;
- profiling/floating/fixed prescription;
- required correlations/covariance or an explicit independence prescription;
- executable or mathematically complete mapping from released data/response assets to the objective;
- a collaboration-published numerical benchmark suitable for a later frozen reproduction tolerance.

If the repository is only data-reading/plotting example code and does not uniquely close those fields, classification is `BLOCKED_0105A6E_OFFICIAL_ORNL_IMPLEMENTATION_AUTHORITY_INCOMPLETE`.

If repository identity/bytes cannot be acquired, classification is `BLOCKED_0105A6E_ORNL_TRANSPORT_OR_IDENTITY`.

A green CI job is not scientific PASS.

## Forbidden operations

No likelihood minimization, nuisance fit, significance recomputation, observed-minus-null residual, BSM scan, operator-family choice or tuning from observed data.

`SM_NULL_REPRODUCTION_PERMISSION = 0%`

`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`

## Next gate rule

Only an independently reviewed 0105a6e scientific PASS can authorize a separate prospectively frozen CsI Standard-Model/null reproduction gate. A BLOCKED result cannot be repaired by importing a secondary phenomenology repository or by filling missing conventions from common practice.
