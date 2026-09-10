# 0105a6q3 — Ar pseudo-data count-law frozen candidate-page semantic audit

Status: **PREREGISTERED BEFORE NEW CANDIDATE-PAGE TEXT INSPECTION / NONDISCOVERY**

Parent locator: `PASS_0105A6Q2_CANDIDATE_PAGES_LOCATED_NONDISCOVERY`.
Parent immutable record commit: `a5b246d1ca44c84653191a2db32fafdab8418386`.
Parent execution/run/job/artifact: `6e1250777d68d10f1f4bafb388f694a92cdaf7a2 / 34516620445 / 103003504742 / 10167939898`.
Parent artifact ZIP SHA256: `0db4fd55a3a3a09110f7f60c2dd388b1d65089b04e549961806fbdd360a286a3`.
Parent inner `result.json` SHA256: `c0d913c442130817b7b59e2a785784b40b85e3c501ce9309699a55b0e66e88f3`.

## Scientific purpose

Adjudicate the same unresolved q1 field Q3 — the stochastic event-count generation law used for the CENNS-10 Analysis-A pseudo-data studies — using **all and only** pages mechanically selected prospectively by 0105a6q2.

The complete frozen physical-PDF candidate set is exactly:

`[145, 152, 153]`

No page may be added, removed, expanded to a neighboring page, or selected after candidate text is inspected. Physical pages 152–153 were already boundedly inspected under q1; page 145 is the only newly located candidate. q3 nevertheless evaluates the complete frozen set jointly to avoid selective evidence handling.

No pseudo-data generation, likelihood evaluation, observed residual, BSM fit, or model-family inference is permitted.

## Frozen source identity

Institutional Jacob C. Zettlemoyer dissertation only:

- byte length `34641327`;
- SHA256 `6dd2fde86601dea28d323fc38e289935723ad1bf0f8c5f2dcfd845fe2e6badf9`;
- exact ScholarWorks download already frozen upstream.

The q2 parent artifact must independently verify the exact candidate set and normalized text hashes:

- p145 `5a96deead926de7effdc82a6f9d8f842c57ad848ddbfd315b25f9726d1677c42`;
- p152 `922b45c4a92f1dc0085b506dcd59e627c394d05d7b70951c6d2bd19bdbb73cea`;
- p153 `96622db01938d38707e3a9945cd34c581ae08debada402ffc434bd5de5adbd52`.

## Frozen extraction/output ceiling

Extract only physical pages 145, 152 and 153 from the exact PDF. Normalize identically to q2. Before semantic classification, each normalized page SHA256 must equal the q2 frozen hash.

The artifact may retain one bounded evidence window per frozen page, capped at 1200 normalized characters and centered on the earliest pseudo-data/generation/count/Poisson/fixed/multinomial/bootstrap/RooFit marker. Full page text is forbidden in repository/artifact output.

## Frozen Q3 decision rule — unchanged from q1

### Q3-P — Poisson / extended-count generation

PASS as Q3-P only if the frozen pages explicitly state that pseudo-data event/bin counts are Poisson/Poisson-fluctuated, that the total pseudo-data event count is drawn from a Poisson distribution with a stated/expected mean, or that an extended generation procedure explicitly fluctuates total count according to Poisson statistics.

The word `extended` by itself remains insufficient.

### Q3-F — fixed-total generation

PASS as Q3-F only if the frozen pages explicitly state that the generated event count is fixed to a stated/predicted number and coordinates/categories are sampled conditional on that total. Explicit multinomial conditional sampling qualifies.

### Q3-O — other explicit law

PASS as Q3-O only if a different stochastic generation law is explicitly described well enough to implement without choosing an unstated convention, e.g. explicit bootstrap/resampling.

## Frozen non-evidence

Still insufficient by itself:

- pseudo-data generated from central-value PDFs;
- binned/unbinned labels;
- extended binned maximum likelihood;
- RooFit/RooMCStudy/RooAbsPdf naming without explicit generation-count option/law;
- the number of pseudo-data sets;
- reconstruction-bias/RMS agreement;
- software defaults or common HEP practice not explicitly stated in the frozen pages.

## Decision

Exactly one explicit category -> `PASS_0105A6Q3_EXPLICIT_PSEUDODATA_COUNT_LAW_SECONDARY_AUTHORITY_NONDISCOVERY`.

No explicit category -> `BLOCKED_0105A6Q3_PSEUDODATA_COUNT_LAW_STILL_NOT_EXPLICIT`.

Conflicting explicit categories -> `BLOCKED_0105A6Q3_CONFLICTING_PSEUDODATA_COUNT_LAW_AUTHORITY`.

Source/hash/candidate-set/extraction mismatch -> `BLOCKED_0105A6Q3_SOURCE_OR_CANDIDATE_INTEGRITY_FAILURE`.

## Authorization consequence

A q3 PASS would authorize only a separate prospective systematic-MC preregistration. That future prereg must freeze the exact count law/category now found, PRNG algorithm/version, all seeds, exact 10,000× ensemble size if reproducing the published procedure, central and excursion PDF identities, nuisance/excursion handling, estimator definitions, combination rule, optimizer and convergence requirements, and benchmark tolerances **before any systematic pseudo-data are generated**.

q3 itself never authorizes execution.

If q3 BLOCKED, do not infer a count law. The dissertation route is exhausted under the q1/q2/q3 contract and the next route must be genuinely new provenance-qualified implementation authority.

Always:

- Tier-A exact collaboration-internal likelihood = `BLOCKED`;
- Tier-B central/null reproduction = PASS at 0105a6o3;
- `SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION = 0%`;
- `OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`.