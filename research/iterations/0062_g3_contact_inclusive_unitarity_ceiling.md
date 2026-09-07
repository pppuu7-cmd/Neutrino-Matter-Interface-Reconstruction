# NMIR iteration 0062 — coefficient-independent contact unitarity ceiling

Date: 2026-09-07
Classification: **FAIL_UNITARITY_MODEL / HARD_LMAX_NOT_COEFFICIENT_INDEPENDENT; DIAGNOSTIC_BOUND_TOO_WEAK / RESIDUAL_OPEN**

## Funnel target
G3 / F4–F6: test whether S-matrix partial-wave unitarity plus finite nuclear size and frozen solar spectra can close the remaining absolute short-range/contact-current deposited-power residual without EFT naturalness, fitted LECs, selected-nucleus anchors, or regulator/scheme-dependent coefficient priors.

## Prospective authority
Parent preregistration was frozen before implementation/result inspection:
- `research/prereg/0062_g3_contact_inclusive_unitarity_ceiling.md`
- prereg commit `9b8bf25e8f152bf4cb75936e4d50f7ac34df7b87`.

A fail-closed amendment was then frozen **while hosted run 34071960179 was still in progress and before its benchmark artifact/result was inspected**:
- `research/prereg/0062a_unitarity_lmax_validity_amendment.md`
- amendment commit `440d4739ad2b5a35bd44b568f421d1ebcddf2426`.

The amendment recognized that the per-partial-wave bound

`σ_l <= 4π(2l+1)/k²`

is valid, but the hard truncation `l_max = ceil(kR)` is not by itself a coefficient-independent theorem for an arbitrarily strong finite-range interaction. Therefore a universal closure was prospectively forbidden unless independent scattering authority justified such a finite partial-wave truncation/bound.

## Implemented diagnostic finite-l ceiling
The implementation uses

`k = Eν/(ħc)`,

`R(A) = r0 A^(1/3)`,

`σ_unit(E,A) = 4π(l_max+1)²/k²`,

with the frozen conservative total-cross-section normalization and

`P_unit(A)=N_T(A) ∫ dE Φ_solar(E) σ_unit(E,A) Eν`,

where `E_dep,ν=Eν` maximizes the neutrino-supplied deposited-energy ceiling. No F9 multiplication is present.

The code retains `r0 = 1.2, 1.4, 1.6 fm`, floor-vs-ceil controls, energy-grid convergence, A-grid controls, source-resolved contributions, locally pinned solar spectra, and representative physical-A controls.

## Hosted scientific result
Dedicated workflow:
- run `34071960179`
- job `101590826472`
- workflow head `1173c0e030616ed3472446c5c565cc5d08961612`
- artifact `10000809024`
- artifact ZIP SHA256 `316b03ef097529333039fd342cecba20aef45b0093bb84e1875d2b0f413f0caf`.

Raw hosted job log was inspected directly. Dedicated regression tests: **6 passed**. Benchmark and artifact upload both completed successfully. The artifact ZIP was downloaded and inspected directly; it contains `contact_unitarity_ceiling_result.json` and its ZIP hash matches the hosted digest.

## Numerical diagnostic result
The finite-l benchmark itself reports

`scientific_ceiling_w_per_kg = 520819.2495826213`,

at the continuous-class winner `A=1`, dominated by pp neutrinos:

`pp = 507061.31839021284 W/kg`.

Other source contributions at the winner include
- Be7 ground: `9681.535016629838 W/kg`;
- Be7 excited: `2487.2447002891836 W/kg`;
- N13: `908.2545738651708 W/kg`;
- O15: `478.05874371276695 W/kg`;
- pep: `188.58247169378453 W/kg`;
- B8: `1.955270088378531 W/kg`.

The diagnostic distance above the 1-W/kg objective is therefore

`520819.2495826213 ×`.

Even the stricter floor-control finite-l construction at `A=1` gives

`130204.81239565533 W/kg`,

still over five orders of magnitude above the objective.

The low-energy pp behavior is not a numerical artifact: the benchmark reports

`pp_below_0p1mev_w_per_kg_at_winner = 65600.60878656227`,

and the maximum 32-to-64 energy-grid refinement change is only

`2.372850402203757e-7`,

well inside the frozen `0.005` tolerance. A-grid refinement residual is zero for the reported winner.

## Scientific classification
Two distinct conclusions must not be conflated.

1. **Universal coefficient-independent model:** `FAIL_UNITARITY_MODEL / HARD_LMAX_NOT_COEFFICIENT_INDEPENDENT`.
   The preregistered hard finite partial-wave truncation needed to turn per-wave unitarity into a finite total ceiling is not justified as a coefficient-independent theorem in the no-strength-prior class. The pre-result amendment explicitly requires this fail-closed classification absent such authority.

2. **Diagnostic usefulness of the proposed route:** `DIAGNOSTIC_BOUND_TOO_WEAK / RESIDUAL_OPEN`.
   Even granting the aggressive finite-l truncation, the resulting solar deposited-power ceiling is `~5.21e5 W/kg`, so this unitarity route is far too weak to constrain the 1-W/kg bridge. This conclusion does not rely on repairing the hard-lmax issue: a valid universal ceiling could only be at least as permissive unless new independent assumptions are introduced.

Thus 0062 does **not** close the absolute contact-current residual, but it does retire naive finite-l partial-wave unitarity as a useful coefficient-independent route to the NMIR 1-W/kg objective.

## Scope guards
- No claim is made that actual Standard-Model solar-neutrino deposited power is remotely near this ceiling; previous explicit SM folds remain many orders smaller.
- No contact coefficient theorem is claimed.
- No smaller `l_max`, radius, unitarity normalization, low-energy cutoff, fitted LEC prior, or EFT-naturalness assumption may be introduced post hoc to rescue this gate.
- The result does not reopen long-range/growing-coordination physics closed in 0060.
- Event/detection, metastable, resonance, gravitational and structured-matter gains are not multiplied.

## Next funnel action
Per the frozen parent contract, because the coefficient-independent unitarity route is too weak and the universal finite-l model itself fails, keep the G3 contact residual OPEN and move to the next independent highest-value gate rather than inventing a tighter coefficient prior.

Current next independent gate: G2 measured comparable underground topology rejection × CEvNS-like bulk acceptance anchor, unless a newer repository reconciliation identifies a higher-value class-level route.

`NMIR_READINESS` receives no increase for 0062 because the principal physical residual remains open; the iteration nevertheless records a reproducible negative route and prevents future overclaim/repetition.
