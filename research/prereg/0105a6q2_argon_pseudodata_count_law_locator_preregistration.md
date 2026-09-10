# 0105a6q2 — Ar pseudo-data count-law implementation-authority locator preregistration

Status: **PREREGISTERED / NO NEW THESIS-WIDE EXTRACTION YET / NONDISCOVERY**

Parent: `BLOCKED_0105A6Q1_PSEUDODATA_COUNT_LAW_NOT_EXPLICIT`.
Parent immutable record commit: `028de631ddd3be826415f79a4680d6a05cfe5db0`.
Parent hosted run/job/artifact: `34512119788/102988544718/10166199306`.
Parent artifact ZIP SHA256: `e3ca7ffe41032b61980c63d6e4e2c7c4be25e21712697dd1fd215284b8dd28bf`.
Parent inner `result.json` SHA256: `f1d0495fd17ed99fef54086da373a666aa33ef49b3dd61e390297f507b63b201`.

## Purpose

Locate, without semantic adjudication, any additional pages in the already-authorized institutional Jacob C. Zettlemoyer dissertation that could contain an explicit pseudo-data event-count generation law or an exact software/API generation contract relevant to COHERENT CENNS-10 Analysis-A.

0105a6q1 prospectively read only physical PDF pages 152–153 and found no explicit Poisson/fixed-total/multinomial/bootstrap count law. The correct next action is therefore a provenance-preserving **mechanical locator**, not an inferred stochastic convention and not a numerical pseudo-data study.

This gate must not generate pseudo-data, evaluate a likelihood, inspect an observed residual, fit BSM parameters, choose a count law, or promote institutional secondary-author material to Tier-A collaboration-release authority.

## Frozen source identity

Institutional dissertation only:

- canonical item: Indiana University ScholarWorks, `FIRST DETECTION OF COHERENT ELASTIC NEUTRINO-NUCLEUS SCATTERING ON AN ARGON TARGET`, Jacob C. Zettlemoyer, 2020;
- exact download URL already used by 0105a6q1: `https://scholarworks.iu.edu/dspace/bitstreams/a56e81c4-990a-4f54-b98d-6276a3c7c80a/download`;
- byte length: `34641327`;
- SHA256: `6dd2fde86601dea28d323fc38e289935723ad1bf0f8c5f2dcfd845fe2e6badf9`.

No mirror, OCR rewrite, presentation, phenomenology paper, or generic RooFit documentation may substitute for these bytes in this gate.

## Frozen locator procedure

Convert the complete PDF to machine text page-by-page using `pdftotext -layout`. Normalize each physical page by lower-casing and collapsing whitespace. The locator may read all physical pages, but it may **not retain or upload page text**.

For every physical page, record only:

- physical page number;
- SHA256 of normalized page text;
- boolean hit flags for the frozen lexical groups below.

No bounded text windows are permitted in this locator artifact. This is intentional: candidate pages must be selected mechanically first, and only a later separately preregistered semantic gate may expose bounded evidence from the complete frozen candidate set.

### L1 — pseudo-data marker

Case/spacing/hyphen-insensitive semantic forms of:

- `pseudo-data`;
- `pseudo data`.

### L2 — explicit stochastic-count terms

Any of:

- `poisson` / `poissonian`;
- `fixed total`;
- `fixed number`;
- `fixed event count`;
- `number of events is fixed`;
- `multinomial`;
- `bootstrap`;
- `resample`, `resampled`, `resampling`.

### L3 — generation/count contract terms

Any of:

- `number of events`;
- `event count` / `event counts`;
- `generate`, `generated`, `generation`, `generating`;
- `RooMCStudy`;
- `generateBinned`;
- `NumEvents`;
- `Extended`.

### L4 — implementation/framework terms

Any of:

- `RooFit`;
- `RooAbsPdf`;
- `RooMCStudy`;
- `TTree` together with `pseudo-data` on the same page;
- `likelihood code`;
- `fit machinery`.

## Frozen candidate rule

A physical page is a `DIRECT_COUNT_LAW_CANDIDATE` if `L1 && L2`.

A physical page is an `IMPLEMENTATION_CONTRACT_CANDIDATE` if `L1 && L3 && L4`.

A physical page is a `COUNT_GENERATION_CANDIDATE` if `L1` and both a generation token (`generate*`) and a count token (`number of events` or `event count*`) occur on the same page.

The frozen candidate set is the union of these three categories, sorted by physical page number. No page may be added or removed after seeing locator output.

If the candidate set is non-empty, the locator classification is `PASS_0105A6Q2_CANDIDATE_PAGES_LOCATED_NONDISCOVERY`. This PASS means only that deterministic candidate pages exist; it is **not** evidence that any candidate states an explicit count law.

If the candidate set is empty, classify `BLOCKED_0105A6Q2_NO_ADDITIONAL_COUNT_LAW_CANDIDATE_PAGES`.

Transport/hash/page-splitting failure is `BLOCKED_0105A6Q2_SOURCE_TRANSPORT_OR_LOCATOR_FAILURE`.

## Output ceiling

The artifact may contain only source identity, page count, per-page normalized-text SHA256, lexical booleans for candidate pages, candidate category labels, sorted candidate page numbers, and terminal locator classification. It must not retain or upload dissertation bytes or page text.

## Authorization consequence

Even locator PASS does not authorize pseudo-data generation or a stochastic-law choice.

If PASS, the only newly authorized action is a separate prospective semantic preregistration that freezes the **entire mechanically returned candidate-page set before any candidate-page text is inspected**. That semantic gate may then test the original q1 categories Q3-P/Q3-F/Q3-O without changing them.

If BLOCKED, the institutional-dissertation route is exhausted for this unresolved field under the present lexical contract; seek a new provenance-qualified collaboration-author code/archive/supplement authority rather than infer the law.

Always:

- Tier-A exact collaboration-internal likelihood = `BLOCKED`;
- Tier-B central/null reproduction = PASS at 0105a6o3;
- Tier-B systematic pseudo-data reproduction remains `BLOCKED`;
- `SYSTEMATIC_MONTE_CARLO_PREREGISTRATION_PERMISSION = 0%`;
- `SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION = 0%`;
- `OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`.