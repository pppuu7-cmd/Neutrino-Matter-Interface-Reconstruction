# NMIR pre-result amendment 0066 — concurrent G8 evidence correction

Date: 2026-09-07
Status: PRE-RESULT AMENDMENT to `research/prereg/0066_bsm_unlock_readiness_audit.md`.

## Why amendment is mandatory
The 0066 preregistration was frozen from reconciled RECOVERY/FUNNEL state that treated G8 as `BLOCKED_ENTRANCE_STRENGTH through 0064`. However, before the 0066 prereg commit (`77ecef8795ccdcd7ec990b2f280fdf39012c5c15`, 2026-09-07T01:53:17Z), a concurrent prospectively frozen G8 follow-up had already been completed:
- G8 prereg commit `3e52add9f3881f96b8409fb7474af564f114a395` at 01:49:18Z;
- G8 authority ledger commit `4d64aa7a95f1f794af303c467aa81fd9752fa2a2` at 01:50:19Z;
- G8 result commit `b6553966b90cbe6a35662ba975507217ca6f04c9` at 01:50:46Z.

A separate auto-research G3 prereg/result was concurrently assigned the same numeric iteration 0065 and later became the reconciled RECOVERY pointer. The duplicate number is a namespace collision only; it does not invalidate either prospective scientific contract. The earlier G8 prereg must therefore be included in the 0066 survivor audit as evidence that existed before 0066 was frozen.

## Scientific correction
The concurrent G8 result is `PASS_G8_CU63_PROVENANCE_REOPENED` for the exact channel

`63Cu(g.s.,3/2-) + anti-nu_e + e_K -> 63Ni*(87.220 keV,5/2-)`.

Independent inputs reconstruct `E_R=162.496486 keV`, consistent with the 2026 RIOEC comparator, and a target-specific shell-model B(GT) ensemble exists for the exact crossed transition. The remaining uncertainty includes a mandatory ~23.6x model envelope in reverse B(GT).

Therefore G8 can no longer be classified in 0066 simply as `BLOCKED_NOT_ACTIONABLE` on entrance-strength provenance. At least the `63Cu` sub-branch is now **OPEN_ACTIONABLE** because the next gate can be executed with currently available primary authority: recover/materialize the Standard-Model thermal-solar electron-antineutrino differential spectrum at `E_nu≈162.5 keV` and test the spectral-overlap/rate fold under the full strength envelope.

## Effect on the frozen 0066 criteria
The original 0066 criterion remains unchanged:
> If any principal SM residual is still quantitatively unbounded and actionable with existing authority, BSM remains locked and that SM gate stays higher priority.

This amendment does not weaken or rewrite that criterion. It only corrects the pre-existing evidence set to which the criterion must be applied.

Unless the 0066 audit can independently show that the newly reopened 63Cu thermal-solar sub-branch is already non-actionable or quantitatively closed by authority existing before classification, G8 must be recorded as `OPEN_ACTIONABLE` and the prospective classification must be `FAIL_KEEP_BSM_LOCKED_OPEN_SM_ACTIONABLE`.

## Guards
- Do not treat the 162.5-keV resonance as evidence of useful solar rate; the thermal-solar spectrum peaks at eV-keV energies and the high-energy tail must be audited quantitatively.
- Do not extrapolate a plotted spectrum by eye. If the primary spectrum is unavailable or invalid at 162.5 keV, classify the tail gate as an authority blocker rather than invent a flux.
- Do not use ordinary solar pp neutrinos as RIOEC entrance particles; the channel requires electron antineutrinos.
- Do not erase either concurrent 0065 record. Reconcile the namespace explicitly after 0066.
