# 0105a6i — Ar post-byte-recovery likelihood-semantics audit preregistration

Status: **PREREGISTERED / NONDISCOVERY**

## Purpose

Determine whether the union of already frozen provider-backed COHERENT Ar authority is sufficient to define a unique, analyst-choice-free Standard-Model/null Analysis-A likelihood contract **after** the 0105a6h exact-byte recovery of `LArParametersAnlA.yaml` and `CENNS10AnlAEfficiency.txt`.

This is a semantic authority gate only. It does not execute a fit, inspect or compute a nuisance-cleaned residual, scan BSM parameters, select a residual basis, map model families, or estimate discovery significance.

## Frozen authority set

Only the following evidence classes may contribute scientific authority:

1. COHERENT measurement paper, arXiv:2003.10630v7 / PRL 126, 012002 (Analysis A semantics).
2. COHERENT Ar data-release document, arXiv:2006.12659v2.
3. The already accepted 0105a3 official Zenodo record/byte inventory for record 3903810.
4. The two 0105a6h files accepted solely because they are byte-identical to the frozen 0105a3 official identities:
   - `LArParametersAnlA.yaml`, SHA256 `a206a77220436d0173c4783ae8fddeab97adf5e144f3d65005eff0870257693e`;
   - `CENNS10AnlAEfficiency.txt`, SHA256 `21ce25451c1ed552752ff4a22496deab3ff5dba178bf360813eaff1d25be89e2`.

Third-party implementations, phenomenology papers, package defaults, RooFit conventions not explicitly stated by the provider, and analyst intuition have **zero scientific authority** in this gate.

## Frozen semantic fields

The audit must classify each field as `COMPLETE` or `PARTIAL_OR_MISSING` and must emit provider-backed evidence for every `COMPLETE` field.

- **F1 — elementary objective/statistical law.** Exact mathematical construction of the Analysis-A extended likelihood, including whether released 3D arrays enter as binned Poisson terms, an unbinned extended mixture, or another provider-specified law, plus all auxiliary constraint factors needed for the null fit.
- **F2 — observables/support/binning/template identity.** Exact fit observables, their support and binning, and identities/normalizations of data, CEvNS, prompt-BRN, delayed-BRN and steady-state templates.
- **F3 — nuisance inventory and constraints.** Complete nuisance list needed for the released Analysis-A null reproduction, with central values, prior/constraint widths, and which quantities are unconstrained.
- **F4 — nuisance-to-template coupling.** Exact rule by which every rate and shape nuisance modifies expected counts/templates, including interpolation/morphing between nominal and ±1σ shapes and any parameter correlations.
- **F5 — profiling/minimization and null statistic.** Which parameters are profiled/floated/constrained and the provider-defined null-vs-signal test statistic/objective comparison.
- **F6 — systematic-template combination/correlation rule.** Exact treatment of the released systematic variations when more than one systematic is present, including whether variations are profiled simultaneously, refitted one-at-a-time, combined in quadrature, correlated, or otherwise handled.
- **F7 — numerical anchors and reproduction target.** Provider-backed numerical anchors sufficient to prospectively define a later reproduction target without seeing a new residual. Any discrepancy between provider documents must be explicitly preserved and resolved by a frozen precedence rule or else F7 is not COMPLETE.

## Frozen discrepancy rule

The known steady-state CV discrepancy is not to be silently repaired:

- release-document Table 2: `3152 ± 25`;
- exact official-byte-equivalent YAML: `3154 ± 25`.

For this audit the discrepancy itself is evidence. F7 can be `COMPLETE` only if provider authority supplies an explicit precedence/erratum rule. The audit may not choose one because it is newer, machine-readable, numerically convenient, or closer to a fit result.

## PASS/BLOCKED rule

`PASS_0105A6I_ARGON_POST_BYTE_RECOVERY_LIKELIHOOD_SEMANTICS_NONDISCOVERY` is allowed **only if F1–F7 are all COMPLETE** from the frozen authority set and the resulting Analysis-A SM/null contract contains no analyst-selectable likelihood, nuisance-morphing, correlation, or discrepancy-resolution choices.

If any field is `PARTIAL_OR_MISSING`, classify:

`BLOCKED_0105A6I_ARGON_LIKELIHOOD_IMPLEMENTATION_AUTHORITY_INCOMPLETE`.

A BLOCKED result is an authority result, not a physics failure.

## Hard prohibitions

- No observed BSM/model-agnostic residual inspection or calculation.
- No SM/null numerical fit in this gate.
- No Poisson, Gaussian, χ², interpolation or morphing rule may be supplied because it is conventional or convenient.
- No use of third-party implementation output as provider authority.
- No silent resolution of `3152` versus `3154`.
- No change to F1–F7, the PASS rule, or allowed authority after reading the outcome.
- `OBSERVED_BSM_RESIDUAL_PERMISSION` remains `0%` regardless of this gate's outcome.

## Consequence

A PASS would authorize only a **new, separately preregistered** Ar SM/null numerical-reproduction gate. A BLOCKED result forbids such a provider-faithful reproduction until a new prospective authority-acquisition gate closes the missing semantic fields.
