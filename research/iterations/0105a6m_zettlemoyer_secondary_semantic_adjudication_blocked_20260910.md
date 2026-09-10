# 0105a6m — Zettlemoyer candidate-evidence semantic adjudication

Date: 2026-09-10
Classification: **BLOCKED_0105A6M_SECONDARY_AUTHOR_SEMANTIC_EVIDENCE_INCOMPLETE**

## Frozen provenance

- preregistration commit: `b73e32d19f4286174ea247a259413626ec0f570c`
- 0105a6l parent run/job/artifact: `34496447259/102936000719/10159983173`
- parent artifact ZIP SHA256: `0eb725afbc38026708b2fdf01c6a7ae77ac69e3c3dcaf7270499d159feff464e`
- parent `result.json` SHA256: `914d65886e5885dc017f8d118e1400f583450d2f5a64301007702bd439940317`
- bounded-evidence execution head: `05a8cfb4275d59604b7a6d18ebc44cbe8967bf3f`
- run/job: `34496819902/102937268315`
- artifact: `10160137826`, `nmir-v2-0105a6m-zettlemoyer-bounded-semantic-evidence`
- artifact ZIP SHA256: `df11b8726e52b3b1662509d3130bfab39c45bd298e5d21995a0613a375fa7d6b`
- inner `evidence.json` SHA256: `672b8e5ec68e01395250e97fbafcbda956f8ffc51b52773d6379588b1fb87364`
- bounded-evidence tests: `5 passed`

## Exact scope

The extractor revalidated the exact institutional dissertation identity (`34641327` bytes; SHA256 `6dd2fde86601dea28d323fc38e289935723ad1bf0f8c5f2dcfd845fe2e6badf9`) and read only the mechanically inherited candidate pages:

`132, 133, 134, 144, 145, 146, 148, 149, 150, 151, 152, 153, 154, 157, 158`.

No outside page was accessed. No full page was retained. Each stored evidence window was capped at 900 normalized characters per family/page. No numerical fit was performed.

## Frozen field adjudication

### F1 — `COMPLETE_SECONDARY_EVIDENCE`

The bounded evidence identifies Analysis A as a three-dimensional **extended binned maximum-likelihood** fit in energy, F90 and time, using predicted component PDFs and data. The bounded equation evidence further identifies the event/data contribution through the log-density term and the Gaussian-penalty extension for constrained normalizations. This is sufficient at the secondary-author level to determine the elementary statistical family without choosing a new family from RooFit defaults.

This does **not** upgrade the dissertation to collaboration-release authority.

### F3 — `PARTIAL_SECONDARY_EVIDENCE`

The evidence explicitly identifies Gaussian normalization constraints, including prompt BRN, delayed BRN and steady-state/background normalization information, and it distinguishes the CEvNS profile/null role. However the candidate windows do not provide an exhaustive single Analysis-A inventory that unambiguously labels every normalization and every shape/systematic degree of freedom by constrained/floated/profiled status under the frozen F3 criterion.

Therefore no completeness inference is made from common practice or from software defaults.

### F4 — `NO_SECONDARY_EVIDENCE`

0105a6l found no candidate page satisfying the prospectively frozen nuisance-to-template morphing/interpolation vocabulary. The dissertation evidence instead points toward a distinct procedure in which systematic excursion PDFs are generated and studied separately. Under the frozen 0105a6m F4 criterion, separate ±1σ excursion/alternative-fit studies are not enough to define a unique simultaneous interpolation/morphing implementation.

### F6 — `COMPLETE_SECONDARY_EVIDENCE`

The bounded evidence explicitly states that shape-systematic errors are obtained by generating separate ±1σ excursion PDFs, generating pseudo-data under each excursion, fitting with the central-value PDFs, and taking the mean shift relative to the central-value study. It explicitly characterizes the resulting systematic errors as **uncorrelated**. For the reported null-rejection significance, the statistical and systematic errors are then added in quadrature.

Thus the secondary source provides a concrete combination rule for the published Analysis-A systematic treatment. Importantly, this evidence favors a two-layer architecture (central-value likelihood plus external systematic-excursion error evaluation) rather than a simultaneous shape-nuisance morphing likelihood.

### F7 — `UNRESOLVED_SECONDARY_EVIDENCE`

The exact token `3154` appears on the inherited pages as the steady-state/background normalization in the dissertation. The exact token `3152` does not appear in the allowed scope. No `typo`, `erratum`, `corrected`, `should be`, `instead of`, `supersede`, or equivalent explicit precedence statement was found. Repetition of `3154` is not authority to overrule the official release value `3152 ± 25`.

## Overall conclusion

0105a6m is BLOCKED because the frozen overall PASS requires F1/F3/F4/F6 all COMPLETE and F7 RESOLVED. The observed field vector is:

- F1: `COMPLETE_SECONDARY_EVIDENCE`
- F3: `PARTIAL_SECONDARY_EVIDENCE`
- F4: `NO_SECONDARY_EVIDENCE`
- F6: `COMPLETE_SECONDARY_EVIDENCE`
- F7: `UNRESOLVED_SECONDARY_EVIDENCE`

This is not a Standard-Model scientific FAIL and not BSM evidence.

## New methodological consequence

The F6 evidence materially changes the *next question* without changing any frozen earlier result: the published Analysis-A workflow may be a two-layer procedure in which the central-value likelihood handles statistical/normalization fitting while shape-systematic effects are evaluated through separate excursion studies and combined afterward. Therefore a new prospective gate should test whether a **release-consistent reproduction contract** can be defined from that two-layer architecture without inventing continuous shape morphing.

0105a6i remains historically and methodologically valid as a BLOCKED exact analyst-choice-free public-authority gate. It is not retroactively weakened or rewritten.

## Authorization ceiling

- `collaboration_release_authority = false`
- `SM_NULL_REPRODUCTION_PERMISSION = 0%`
- `OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`
