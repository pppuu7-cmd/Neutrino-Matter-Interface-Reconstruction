# 0105a5b R1d preregistration — DeepCore external computational authority

Date frozen: 2026-09-10
Scope: NMIR v2 only. NMIR v1 remains frozen and unchanged.
Parent: R1c `PASS_0105A5B_R1C_COORDINATE_SEMANTICS_AUTHORITY_NONDISCOVERY`.

## Purpose

Resolve only the seven external computational dependencies exposed prospectively by R1b before any standalone standard-3nu likelihood reproduction:

- `BarrWP`
- `BarrWM`
- `BarrYP`
- `BarrYM`
- `BarrZP`
- `BarrZM`
- `DIS-CSMS`

This is an authority/provenance gate, not a fit and not a residual calculation.

## Frozen authority order

For each dependency, evidence must be sought in this order:

1. exact byte-locked B4RITM v1.0 release-native documentation and `example.ipynb`;
2. the exact IceCube analysis publication authority, Phys. Rev. D 108, 012014 (2023), arXiv:2304.12236, including its explicit references;
3. only the original upstream computational/model authority explicitly cited by the IceCube release/publication for that dependency.

Secondary tutorials, community implementations, later sterile analyses, guessed package defaults, or QKL28Z are forbidden substitutes.

## Frozen questions per dependency

R1d must determine, before any oscillated expectation is built:

1. exact semantic definition of the nuisance direction;
2. exact upstream authority/package/model required to evaluate it;
3. whether a reproducible version/revision or immutable source state can be pinned;
4. required input variables and units;
5. nominal/reference state corresponding to zero nuisance displacement;
6. sign convention for positive/negative displacement where applicable;
7. interpolation/reweighting rule explicitly authorized by IceCube or the cited original authority;
8. whether the released MC columns contain all event-level inputs required by that rule.

## Frozen PASS criterion

`PASS_0105A5B_R1D_EXTERNAL_COMPUTATIONAL_AUTHORITY_NONDISCOVERY` requires all seven dependencies to have a complete, reproducible, authority-backed implementation contract with immutable provenance. No dependency may rely on an unpinned software default, guessed convention, post-data tuning, or undocumented interpolation.

PASS permits only implementation of the seven frozen nuisance transformations as a separate conformance stage. It does not yet authorize the standard-3nu likelihood reproduction or any observed residual.

## Frozen BLOCKED criterion

`BLOCKED_0105A5B_R1D_EXTERNAL_COMPUTATIONAL_AUTHORITY_INCOMPLETE` if one or more of the seven dependencies lacks enough authority to define a reproducible transformation without assumption. The result must list every missing dependency and the exact missing semantic/provenance element.

Missing authority is not permission to delete that nuisance or replace it with a Gaussian normalization.

## Frozen structural/scientific FAIL criterion

`SCIENTIFIC_FAIL_0105A5B_R1D_RELEASE_INPUTS_INSUFFICIENT` only if the authority fully specifies a required transformation but the exact byte-locked B4RITM release demonstrably lacks a required event-level input needed to evaluate it.

This is a reproduction-path structural FAIL, not a statement about BSM physics.

## Infrastructure taxonomy

`INFRASTRUCTURE_FAIL_0105A5B_R1D` is reserved for transport/runtime/artifact failures before the authority criterion can be evaluated. Repair may change transport/runtime only.

## Explicit prohibitions

R1d must not compute or inspect an oscillated 3nu expectation, likelihood/chi-square, nuisance best fit, observed-minus-null residual, BSM residual, NSI/magnetic/light-mediator fit, significance, or Wilks threshold.

No bins, normalizations, nuisance deletions, parameter ranges, or thresholds may be selected from residual behavior.

`OBSERVED_BSM_RESIDUAL_PERMISSION: 0%`.
