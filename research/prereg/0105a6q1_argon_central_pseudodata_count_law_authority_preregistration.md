# 0105a6q1 — Ar central-value pseudo-data count-law authority preregistration

Status: **PREREGISTERED / NO NEW THESIS EXTRACTION YET / NONDISCOVERY**

Parent: `BLOCKED_0105A6Q_SYSTEMATIC_EXCURSION_SEMANTICS_INCOMPLETE`.
Parent result SHA256: `a996df0b6f9d12f03d1fc57cc3d69f13d1b941e3771eb99be9877510d34e6884`.

## Scientific purpose

Resolve only the remaining critical 0105a6q field **Q3: the pseudo-data event-count generation law** used by the COHERENT CENNS-10 Analysis-A systematic-excursion study.

The q bounded evidence on physical PDF page 154 explicitly says that the systematic pseudo-data are generated `as in the study using the central-value PDFs`. The present gate therefore targets only the immediately preceding central-value pseudo-data study. It is not a general reread of the dissertation and it may not revisit q acceptance criteria after seeing the result.

No pseudo-data generation, likelihood evaluation, observed residual, BSM fit or model-family inference is permitted in this gate.

## Frozen source identity

Institutional Zettlemoyer dissertation:

- byte length: `34641327`;
- SHA256: `6dd2fde86601dea28d323fc38e289935723ad1bf0f8c5f2dcfd845fe2e6badf9`;
- custody/provenance remains the already-passed 0105a6j institutional secondary-author source; it is not promoted to collaboration-release authority.

Parent q evidence must independently verify:

- artifact/result identity above;
- q classification `BLOCKED_0105A6Q_SYSTEMATIC_EXCURSION_SEMANTICS_INCOMPLETE`;
- q `critical_unresolved_fields == ["Q3"]`.

## Frozen page scope

Read **physical PDF pages 152–153 inclusive and no others**.

Rationale fixed before extraction:

- page 154 refers backward to the central-value pseudo-data study;
- the already-existing 0105a6m bounded evidence places Table 7.9 and the central-value pseudo-data reconstruction-bias discussion on physical page 152 and the continuation/statistical-null discussion on page 153;
- these two contiguous pages are therefore the smallest authority-motivated section scope capable of answering Q3 without page cherry-picking.

The gate must record a SHA256 of normalized machine text for each page. Full page text must not be committed or uploaded. Bounded evidence windows are capped at **900 normalized characters per page**.

## Frozen Q3 decision rule

Q3 is `COMPLETE_EXPLICIT_COUNT_LAW` only if the allowed pages explicitly identify the stochastic law for pseudo-data event counts in a way that uniquely determines one of the following categories.

### Q3-P — Poisson / extended-count generation

Accept only explicit language semantically equivalent to one or more of:

- pseudo-data event/bin counts are Poisson or Poisson-fluctuated;
- the total pseudo-data event count is drawn from a Poisson distribution with stated/expected mean;
- an extended event-generation procedure is explicitly stated to fluctuate the total count according to Poisson statistics.

The standalone word `extended` in a likelihood description is insufficient.

### Q3-F — fixed-total generation

Accept only explicit language that the number of generated events is fixed to a stated/predicted count, with event coordinates/categories drawn conditional on that fixed total. Explicit multinomial conditional sampling qualifies here if stated.

### Q3-O — other explicit law

Accept a different law only if it is named/described sufficiently to implement without choosing an unstated stochastic convention (for example, an explicit bootstrap/resampling law).

## Explicit non-evidence

None of the following closes Q3 by itself:

- `pseudo-data are generated from the central-value PDFs`;
- `binned` or `unbinned` pseudo-data;
- `extended binned maximum likelihood`;
- RooFit/RooMCStudy/RooAbsPdf naming without an explicit generation-count option or law;
- the number `10000` of pseudo-data sets;
- reconstruction-bias results, RMS values or fitted-rate agreement;
- common HEP/RooFit practice or software defaults inferred from memory/documentation not present in the frozen source scope.

## Conflict rule

If the two pages contain mutually inconsistent count-law statements, classify `BLOCKED_0105A6Q1_CONFLICTING_PSEUDODATA_COUNT_LAW_AUTHORITY` rather than selecting one after the fact.

If no explicit law is present, classify `BLOCKED_0105A6Q1_PSEUDODATA_COUNT_LAW_NOT_EXPLICIT`.

Transport/hash/page-extraction failure is `BLOCKED_0105A6Q1_SOURCE_TRANSPORT_OR_SCOPE_EXTRACTION`.

A positive result is `PASS_0105A6Q1_EXPLICIT_PSEUDODATA_COUNT_LAW_SECONDARY_AUTHORITY_NONDISCOVERY`.

## Output ceiling

The machine result may retain only:

- source/page/hash receipts;
- detected category `Q3-P`, `Q3-F`, `Q3-O`, `NONE`, or `CONFLICT`;
- bounded evidence windows up to 900 normalized characters/page;
- boolean markers needed to apply this preregistration;
- terminal classification.

It must not retain full page text or the institutional PDF.

## Authorization consequence

Even a PASS does **not** authorize observed residual work and does not upgrade Tier-A exact collaboration-internal likelihood authority.

If PASS:

- `SYSTEMATIC_MONTE_CARLO_PREREGISTRATION_PERMISSION = 100%`;
- `SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION = 0%` until a separate prospective MC preregistration freezes PRNG, seeds, exact 10,000× ensemble, retained excursion-rate semantics, paired/one-sided estimators, quadrature combination and the published systematic benchmark acceptance test.

If BLOCKED:

- no pseudo-data may be generated;
- seek another provenance-qualified collaboration-author/institutional or exact implementation source rather than infer the law.

Always:

- Tier-A exact collaboration-internal likelihood = `BLOCKED`;
- Tier-B central/null reproduction = PASS at 0105a6o3;
- `OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`.
