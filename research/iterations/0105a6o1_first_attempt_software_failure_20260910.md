# 0105a6o1 — first hosted attempt: software-only failure

Date: 2026-09-10
Classification: **INFRASTRUCTURE/SOFTWARE FAILURE — NO D1/D2/D3 SCIENTIFIC CLASSIFICATION**

## Frozen parent diagnostic

- preregistration: `research/prereg/0105a6o1_argon_optimizer_convergence_diagnostic_preregistration.md`
- preregistration commit: `1588298dbd04e4cc4c451b3993f43f61080d1339`
- implementation head executed: `79359380411644111283de496d876c1769839967`
- run/job: `34503706125/102960529111`
- artifact: `10162922127`, `nmir-v2-0105a6o1-argon-optimizer-diagnostic`
- provider artifact digest: `sha256:bfd7f8603e9cd988210acbfe6a5cf234bc68e4382719e6b38ad47e61eb9a10b2`
- independently downloaded artifact ZIP SHA256: `bfd7f8603e9cd988210acbfe6a5cf234bc68e4382719e6b38ad47e61eb9a10b2`
- inner `result.json` SHA256: `307805df6e14abf0c61b8c4e6830c9b46610f00018107f17e23e701047227d9c`

## Failure

The hosted workflow itself completed, but the diagnostic payload stopped before D1/D2/D3 adjudication with:

`TypeError: grad() takes 4 positional arguments but 5 were given`

Cause: `scipy.optimize.minimize` forwards the objective's complete `args=(n,s,B0,None)` tuple to the supplied `jac` callable. The analytic `grad` helper accepted only `(theta,n,s,B0)`.

This is a call-signature defect only. It does **not** change or test the frozen objective, exact input bytes, anchors, deterministic starts, bounds, optimizer settings, or D1-D3 thresholds. Therefore the first hosted attempt is not a scientific BLOCKED/FAIL and cannot be used to infer optimizer behavior or Standard-Model agreement.

## Minimal repair

Repair commit: `911703e13f68cac8d83ddef31a6ae93ed5dd863a`.

Only the analytic-gradient call signature was made compatible with the parent objective's fifth `fixed_nc` slot; that slot is ignored because 0105a6o1 is central-fit diagnostic only. No scientific criterion was changed.

A single replacement hosted execution is permitted under the unchanged preregistration. No publication-target classification, systematic excursion, or observed BSM/model-agnostic residual is authorized.

`OBSERVED_BSM_RESIDUAL_PERMISSION_PERCENT = 0`.
