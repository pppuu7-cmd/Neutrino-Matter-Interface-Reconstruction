# 0105a5b R1b — DeepCore B4RITM machine-schema audit: BLOCKED

Date: 2026-09-10
Scope: NMIR v2 only. NMIR v1 remains frozen and unchanged.

## Classification

`BLOCKED_0105A5B_R1B_MACHINE_SCHEMA_OR_STRUCTURE_INCOMPLETE`

Specific frozen stopping condition observed in the hosted execution:

`BLOCKED_0105A5B_R1B_MC_COORDINATES_OUTSIDE_OBSERVED_GRID`

This is an authority/schema BLOCKED result. It is not an infrastructure failure, not a physical/scientific FAIL, and not a scientific PASS. No oscillated expectation, likelihood fit, nuisance fit, observed-minus-null residual, or BSM quantity was computed.

## Exact execution provenance

- execution head: `6c6a6e684b053a8464096483455da1a56efde239`
- workflow run: `34438000882`
- job: `102747000226`
- artifact: `10136879193` (`deepcore-0105a5b-r1b`)
- GitHub provider artifact digest: `sha256:cb259543e5e8d46d091b06a99e0d0f43252b03de9ba4100ee7b75d9e8ebbf85d`
- independently downloaded inner `result.json` SHA256: `ec64aad10b40435227e55b6f8be5429854032879aabe9e7107f4be0ae78c0833`
- dedicated frozen tests: `2 passed`

The provider digest is the artifact-service authority. A locally downloaded ZIP may be repackaged by the provider and therefore its container-byte SHA256 is not used as an equality requirement against the provider digest; the inner result payload was independently hashed above.

## Frozen result facts

The byte barrier against the previously locked B4RITM Saved Original representation passed before CSV parsing. The structural audit then found:

- observed cells: exactly `200`
- observed unique analysis coordinates: exactly `200`
- observed axis cardinality: `10 x 10 x 2`
- MC unique analysis coordinates: exactly `200`
- direct MC-coordinate subset of observed-coordinate grid: `false`
- open external computational dependencies: `7`

Representative MC coordinates outside the literal observed-coordinate tuples include:

- `(-0.95, 4.0, -1.0)`
- `(-0.95, 4.0, 1.0)`
- `(-0.95, 6.0, -1.0)`
- `(-0.95, 6.0, 1.0)`
- `(-0.95, 9.0, -1.0)`

The equality of the two 200-count cardinalities is not treated as evidence of a valid mapping. In particular, no post-result assumption is permitted that one representation is a bin center while another is a bin edge/range until that semantic relation is established from frozen experimental authority.

## Nuisance authority status

Seven directions remain `OPEN_EXTERNAL_COMPUTATIONAL_AUTHORITY`, with no allowed fallback:

- BarrWP
- BarrWM
- BarrYP
- BarrYM
- BarrZP
- BarrZM
- DIS-CSMS

The six Barr directions require an exact MCEq/Barr atmospheric-flux response authority or an IceCube-authoritative equivalent consistent with the frozen B4RITM conventions. DIS-CSMS requires an authoritative CSMS implementation/table and exact variable convention. These blockers are independent of the coordinate-semantics blocker and are not resolved by any future coordinate mapping PASS.

## Historical infrastructure attempt

The preceding hosted candidate `34434226467 / 102735863762` failed before scientific execution because `pytest` was unavailable. That run remains classified strictly as infrastructure failure. Commit `6c6a6e684b053a8464096483455da1a56efde239` repaired only runtime provisioning; the R1b scientific criteria were not changed. The present BLOCKED result therefore comes from the first successfully executed frozen audit after that transport/runtime repair.

## Interpretation guard

This result does not authorize DeepCore standard-3nu/null reproduction. It does not authorize nuisance-orthogonal residual construction, model-agnostic residual reconstruction, NSI/magnetic/light-mediator observed scans, significance calculation, or BSM interpretation.

`OBSERVED_BSM_RESIDUAL_PERMISSION: 0%`

## Exact next scientific-authority question

Before a likelihood reproduction can proceed, the relationship between B4RITM observed-cell coordinates/bin definitions and the MC `reco_coszen`, `reco_energy`, `pid` analysis coordinates must be established prospectively from the frozen B4RITM experimental authority, without inferring a mapping from the observed result. A separate preregistration is required before inspecting/deriving that semantic mapping.
