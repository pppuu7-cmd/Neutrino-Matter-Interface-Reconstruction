# 0105a6o — Tier-B Ar central/null reproduction: optimizer-stability BLOCKED

Date: 2026-09-10
Classification: **BLOCKED_0105A6O_TIERB_ARGON_CENTRAL_NULL_REPRODUCTION_EXECUTION_OR_STRUCTURAL_FAILURE**

## Frozen provenance

- numerical preregistration commit: `a94cbdf5a65618545bd4b1fb4f9fd6c120ae340e`
- exact-input gate 0105a6p: PASS 14/14, record commit `3ae609acbeacf58ff5fa1e90c3e85792527106f1`
- execution head: `ac400354ff7227063fb133fdaec96b15e9c0517c`
- run/job: `34498878828/102944274947`
- numerical guards: `5 passed`
- artifact: `10160971263`, `nmir-v2-0105a6o-argon-tierb-central-null`
- artifact ZIP SHA256: `f917cac0d201a841cf9250d62af46f4cc900efec99a60764d03ad9a59141dd92`
- inner `result.json` SHA256: `88686ffc68d2beb44c22235af690c8a3907cf295902175330d4d01f19432ff65`

## Result

The hosted execution reached the prospectively frozen numerical fit but stopped fail-closed at the multi-start optimizer-stability guard:

`RuntimeError: frozen multi-start stability gate failed`.

The frozen 0105a6o rule required every successful L-BFGS-B start to agree with the minimum-Q solution within both:

- `1e-4` event in every fitted normalization;
- `1e-7` in Q.

The execution script intentionally raised before publication-target or dual-anchor classification when that guard failed. Therefore this record does **not** infer whether the underlying release-consistent likelihood agrees or disagrees with the published Analysis-A benchmark.

## Interpretation

This is presently a **numerical optimizer-stability BLOCKED**, not:

- a Standard-Model failure;
- evidence for BSM physics;
- evidence for a new neutrino model;
- a publication-target mismatch.

Because the result artifact intentionally did not retain the individual pre-failure start solutions, a separate prospectively frozen diagnostic gate is required to distinguish ordinary finite-difference convergence tolerance from a substantive objective/identifiability problem. The frozen 0105a6o result itself is not rerun with relaxed criteria and is not reclassified.

## Permissions

- systematic-excursion preregistration permission: `0%`
- `OBSERVED_BSM_RESIDUAL_PERMISSION_PERCENT = 0`
- observed residual inspected: **false**
