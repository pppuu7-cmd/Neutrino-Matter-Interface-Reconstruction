# NMIR preregistration amendment 0062a — validity of the finite partial-wave sum

Date frozen: 2026-09-07
Status at freeze: **PRE-RESULT / scientific run 34071960179 was still in progress; no benchmark artifact/result had been inspected.**
Parent contract: `research/prereg/0062_g3_contact_inclusive_unitarity_ceiling.md`.

## Why this amendment is necessary
The parent contract correctly freezes the per-partial-wave unitarity ceiling

`sigma_l <= 4*pi*(2l+1)/k^2`.

Standard scattering-theory sources derive this directly from `sin^2(delta_l)<=1`. However, a second logically independent step is required before summing it into a coefficient-independent full cross-section ceiling: one needs a rigorous, assumption-compatible finite set of partial waves.

The commonly used impact-parameter rule `l ~ kR` and the low-energy statement that higher partial waves are suppressed for short-range potentials are physical/semiclassical threshold statements. They are not, by themselves, an exact theorem that `S_l=1` identically for every `l>ceil(kR)` for an arbitrarily strong finite-range interaction. The parent numerical benchmark currently uses exactly such a hard `lmax=ceil(kR)` truncation.

Because 0062 is explicitly trying to remove any bound on the contact coefficient/interaction strength, NMIR must not silently promote the semiclassical `kR` estimate to a universal theorem.

## Frozen pre-result validity gate
The already-running 0062 numerical result may be retained as a **diagnostic finite-l ceiling**, but it may receive `PASS_CONTACT_RESIDUAL_BOUND_BELOW_1WKG` or `PASS_UNITARITY_BOUND_VALID_BUT_TOO_WEAK` as a *universal coefficient-independent scientific classification* only if an independent scattering-theory authority justifies a finite partial-wave truncation/bound strong enough for the stated no-coefficient-prior class.

Otherwise the scientific classification is

`FAIL_UNITARITY_MODEL / HARD_LMAX_NOT_COEFFICIENT_INDEPENDENT`

and the contact residual remains OPEN.

This is a fail-closed correction, not a post-result tightening: it is frozen while hosted run `34071960179` is still `in_progress`, before its benchmark artifact is available or inspected.

## What remains valid regardless
- the per-partial-wave limit `sigma_l <= 4*pi*(2l+1)/k^2` remains a valid normalization/control;
- the finite-l numerical fold, source provenance and unit tests remain useful diagnostics;
- if the finite-l numerical ceiling is already `>=1 W/kg`, that independently demonstrates that this particular optimistic unitarity route is too weak even before confronting the hard-lmax issue;
- if the finite-l numerical ceiling is `<1 W/kg`, it still cannot close the residual unless the hard-lmax step is independently justified.

## No post-result repair allowed
After inspecting the hosted result, NMIR may not choose a smaller `lmax`, smaller unitarity coefficient, smaller radius, remove low-energy solar flux, or introduce EFT-naturalness/fitted-current priors to obtain a preferred classification. A future rigorous bound must be prospectively preregistered as a new gate.
