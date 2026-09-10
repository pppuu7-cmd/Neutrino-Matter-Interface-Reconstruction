# 0105a6i — Ar post-byte-recovery likelihood-semantics audit

Date: 2026-09-10
Scope: **NONDICOVERY / authority semantics only**

## Frozen gate

Preregistration: `research/prereg/0105a6i_argon_post_byte_recovery_likelihood_semantics_audit_preregistration.md`

Preregistration commit: `12521b8ae88aea7889c200ee913920ab645448a6`

The gate asked whether the union of the frozen COHERENT Ar measurement/release authority plus the 0105a6h exact-byte-equivalent `LArParametersAnlA.yaml` and `CENNS10AnlAEfficiency.txt` defines a unique, analyst-choice-free Analysis-A Standard-Model/null likelihood contract. No numerical fit and no observed residual were permitted.

## Hosted execution provenance

- execution head: `73fd5c61e436cd21146b5e5eb7d2ebe50c9bf24b`
- workflow run: `34493442843`
- job: `102925744627`
- artifact: `10158722909`, `nmir-v2-0105a6i-argon-post-byte-recovery-semantics`
- artifact ZIP digest: `sha256:b6d1ab0961d6790f75743542fdec2087f792edf9f7292bb87335337445dfa180`
- inner `result.json` SHA256: `f2f5354126daa98acc2bfea3d1b1f70916285f3b4e697d8da426b5c7d57c7d42`
- deterministic guards: `5 passed`

Exact provider source payloads were successfully acquired in this run:

- measurement e-print `2003.10630v7`: 446096 bytes, SHA256 `2edeb3dcc3df99de575c8b2091f48099a7538eedf9f382996d943c7fbe7e2114`;
- Ar data-release e-print `2006.12659v2`: 23805 bytes, SHA256 `5d000befd41e44deece46f31e1bf3ee7305bc2e8c0357b524311962ddc9d3dde`.

Previously frozen exact-byte semantic anchors carried into the preregistration:

- `LArParametersAnlA.yaml`: SHA256 `a206a77220436d0173c4783ae8fddeab97adf5e144f3d65005eff0870257693e`;
- `CENNS10AnlAEfficiency.txt`: SHA256 `21ce25451c1ed552752ff4a22496deab3ff5dba178bf360813eaff1d25be89e2`.

## Machine evidence

The hosted audit found:

- measurement source names an **extended maximum likelihood**, RooFit, profiling language, and a `-2 Δ ln L` null statistic;
- release source provides 3D binned arrays and identifies `cevnspdf.txt`, `brnpdf.txt`, `delbrnpdf.txt`, and `bkgpdf.txt`;
- release source describes Gaussian constraints;
- release source explicitly delegates use of an **appropriate likelihood procedure** rather than specifying an elementary released binned-Poisson law;
- no provider-explicit shape-template morphing/interpolation rule was recovered from the frozen source union;
- no provider-explicit simultaneous systematic correlation/combination rule was recovered;
- release source contains the steady-state prediction `3152 ± 25`, while the frozen exact-byte YAML contains `3154 ± 25`; no provider precedence/erratum rule was recovered.

The `measurement_three_observables` helper flag returned false because its textual regex was conservative/brittle; this flag was not used to obtain the terminal classification. The measurement source separately establishes the Analysis-A multidimensional observable construction, while F2 was classified from the provider 3D-array/template evidence.

## Frozen F1–F7 disposition

- **F1 elementary objective/statistical law — PARTIAL_OR_MISSING.** Extended-ML naming does not uniquely specify how the released binned arrays enter the elementary likelihood, and the release delegates an `appropriate likelihood procedure`.
- **F2 observables/support/binning/template identity — COMPLETE** within this semantic gate.
- **F3 nuisance inventory/constraints — STRONGLY ANCHORED BUT NOT USED AS A TERMINAL CLOSURE CLAIM.** The machine classifier returned COMPLETE from the exact YAML normalization anchors plus provider Gaussian-constraint semantics. Conservatively, the preregistration requires a complete nuisance list; unresolved shape-systematic wiring is preserved under F4/F6 and F3 is not promoted into permission to fit.
- **F4 nuisance-to-template coupling — PARTIAL_OR_MISSING.** Nominal and ±1σ templates exist, but no provider-defined interpolation/morphing rule was recovered.
- **F5 profiling/minimization and null statistic — COMPLETE.** Provider source supplies profiling language and `-2 Δ ln L` null-statistic semantics.
- **F6 systematic-template combination/correlation rule — PARTIAL_OR_MISSING.** A set of alternative systematic fits does not define a simultaneous combination/correlation contract.
- **F7 numerical anchors/reproduction target — PARTIAL_OR_MISSING.** The frozen provider discrepancy `3152 ± 25` versus `3154 ± 25` has no allowed analyst-side precedence rule.

Because the preregistered PASS rule required all seven fields COMPLETE, the terminal classification is:

`BLOCKED_0105A6I_ARGON_LIKELIHOOD_IMPLEMENTATION_AUTHORITY_INCOMPLETE`

This is an **authority/implementation BLOCKED result, not a Standard-Model scientific FAIL and not BSM evidence**.

## Consequences

- `SM_NULL_REPRODUCTION_PERMISSION: 0%` under the provider-faithful Analysis-A contract.
- `OBSERVED_BSM_RESIDUAL_PERMISSION: 0%`.
- A numerical fit may not be opened by choosing a conventional Poisson/χ², RooFit default, interpolation rule, covariance convention, or a preferred value of the `3152/3154` discrepancy.
- The next scientifically allowed route is a new prospective external-authority acquisition gate targeting the exact Analysis-A RooFit/statistical implementation and shape-systematic wiring from a provenance-qualified COHERENT collaboration/institutional source. Any thesis, code mirror, or secondary source must first pass a provenance/scope gate and cannot be silently elevated to collaboration-release authority.
