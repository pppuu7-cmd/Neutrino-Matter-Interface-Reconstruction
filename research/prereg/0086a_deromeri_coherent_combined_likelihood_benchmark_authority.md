# NMIR preregistration 0086a — De Romeri updated COHERENT combined-likelihood benchmark authority

Date frozen: 2026-09-08
Parent: 0086 `PASS_DEROMERI_COHERENT_UPDATED_SOURCE_ASSET_AUTHORITY`.

## Frozen exact source
- Primary analysis: De Romeri et al., arXiv `2211.11905v2` / JHEP 04 (2023) 035.
- Exact source archive SHA256: `783019f9bb927b69fcdf4fcb3f239729fa9c029e0e3b16ad69d6a777965a355a`.
- Exact source TeX: `COHERENT-Combined-v2.tex`, SHA256 `33e92629a34c16411f1541b2fd2793228953baac48edf099fcbb72efcf44f6a4`.
- Permitted scientific evidence: source-native TeX text only.
- Figures/PDFs, OCR, raster reading, manual digitization, and inferred curve coordinates are forbidden.

## Scientific question
Does the exact source text provide at least one non-circular numerical reference point sufficient to validate an independently implemented updated CsI+LAr combined likelihood before any B-L scan?

## Accepted benchmark forms
A candidate is sufficient only if the source text explicitly binds a numerical value to the same updated CsI+LAr statistical construction and identifies enough semantics to reproduce the reference point. Accepted forms are:
1. an explicit combined `chi2_min` / `-2 log L` (or equivalent statistic) at the SM or another fully specified parameter point; or
2. explicit combined best-fit physics parameter value(s) together with the corresponding numerical minimum statistic and hypothesis; or
3. explicit profiled nuisance best-fit values plus a numerical combined statistic/reference expectation sufficient to test the profile machinery; or
4. an exact source-native table/text reference point that unambiguously evaluates the combined CsI+LAr statistic at a specified parameter point.

A numerical total event count, standalone CsI or standalone LAr fit, a confidence interval without the evaluated statistic, a plot/contour, a Delta-chi2 statement without an absolute/reference value and specified point, or a qualitative statement such as `good agreement` is insufficient.

## PASS criterion
`PASS_DEROMERI_COHERENT_COMBINED_LIKELIHOOD_BENCHMARK_AUTHORITY` requires all of:
- exact archive and TeX hashes match the frozen values;
- the source text defines or explicitly references the updated CsI and LAr likelihood/statistic components and their combination;
- at least one accepted benchmark form above is found in source text;
- benchmark hypothesis/parameter point and statistic semantics are deterministic from local source context;
- no conflicting numerical reference for the same benchmark remains unresolved;
- no figure/manual interpretation is needed.

A PASS authorizes only a later prospectively registered numerical likelihood-reproduction gate. It does not itself authorize a B-L scan or contour.

## BLOCKED criterion
`BLOCKED_DEROMERI_COHERENT_COMBINED_LIKELIHOOD_BENCHMARK_AUTHORITY` if the exact source text contains the likelihood construction but no accepted non-circular numerical combined reference point, or if candidate numbers are semantically insufficient/ambiguous without figure reading.

## Failure taxonomy
- download/hash/extraction/parser/serialization/test failure -> `INFRASTRUCTURE_FAIL`;
- parser false negative demonstrated by raw source context -> parser-conformance defect, not scientific BLOCKED;
- scientific BLOCKED is used only after valid source-text evidence extraction.

## Frozen extraction protocol
The hosted audit must verify both frozen hashes and extract source-native contexts around all case-insensitive occurrences/patterns relevant to: `chi`, `likelihood`, `minimum`, `best fit`, `SM`, `CsI`, `LAr`, `combined`, `B-L`, `vector mediator`, and numerical relations. It may normalize LaTeX whitespace for search but must preserve raw source context in the artifact. Candidate extraction must be generic and must not hard-code any result value discovered after this preregistration.

## Guards
- No PDF/figure reading or digitization.
- No post-result invention of a tolerance.
- No conversion of standalone detector benchmarks into combined-likelihood validation.
- No use of a confidence contour as a benchmark point.
- No B-L mass/coupling scan in 0086a.
- Existing 0074c remains authoritative unless 0086a independently passes for the newer De Romeri likelihood architecture.
- BSM response/enhancement remains locked.

## Next action
PASS -> preregister 0086b numerical reproduction with a tolerance frozen from an external uncertainty/precision statement or an exact equality criterion where appropriate. BLOCKED -> preserve 0074c and retire this updated combined-likelihood route as well; continue to the next actionable F8 constraint-family gap without weakening reproducibility standards.
