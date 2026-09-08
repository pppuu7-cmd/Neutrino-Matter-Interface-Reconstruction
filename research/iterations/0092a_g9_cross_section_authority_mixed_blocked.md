# Iteration 0092a — G9 cross-section authority mixed BLOCKED with TeV transparent-Sun FAIL

Date: 2026-09-08
Gate classification: `BLOCKED_G9_0092A_CROSS_SECTION_AUTHORITY_MIXED`

## Frozen contract
Preregistration: `research/prereg/0092a_g9_cross_section_authority.md`.
Prereg commit: `c6820c20ad96ea189d5bb15439f5155bbdeaaf82`.
Parent density/column authority: 0092 `PASS_G9_0092_MODEL_S_COLUMN_AUTHORITY`, record commit `dab1a5c0ea08c4d2dcbcdc53947027b9d18be21c`.

The frozen solar nucleon column used here is exactly

`N_N = 1.7659857664161126e36 cm^-2`

for `b/Rsun=0.024`. No alternate solar model, column, uncertainty multiple, source energy or post-result threshold was substituted.

## Hosted authority
Execution head: `b8396e9f1440cbb80e9ee8e664e61fde00615603`.
Run/job: `34276868882 / 102231933804`.
Artifact: `10076044489` (`nmir-g9-0092a-cross-section-authority`).
Dedicated tests: `2 passed`.

Raw Actions job log was inspected before classification. The artifact was then downloaded independently.

Validated hashes:
- artifact ZIP SHA256: `8b7fa8fc988327de2a4242edcb04a273fc9bbf939967d99ca7ea233194218557`;
- inner `g9_0092a_cross_section_authority.json` SHA256: `ead1e74ae32410b0bcf307632606b2f77cbabd10d056ab5cd311068d56227bfe`.

Both independent hashes exactly match the values printed by the hosted run.

## NGC 1068 frozen low-end TeV sentinel
Primary direct authority frozen prospectively: FASER Collaboration, PRL 133, 021802 (2024), arXiv:2403.12520, reporting the nu_mu charged-current cross-section coefficient over `520–1760 GeV` as `(0.5 +/- 0.2)e-38 cm^2 GeV^-1`.

The preregistered conservative one-sided sentinel at `E=1.5 TeV` uses central-minus-1sigma:

`sigma_CC_lower/E = 0.3e-38 cm^2 GeV^-1`

so

`sigma_CC_lower(1.5 TeV) = 4.5e-36 cm^2`.

With the validated Model-S column,

`tau_CC_lower = N_N * sigma_CC_lower = 7.946935948872507`,

and therefore

`T0 <= exp(-tau_CC_lower) = 3.5374439669189366e-4`.

Because even this deliberately conservative CC-only lower optical depth is already `>=1`, the frozen source-regime classification is

**`SCIENTIFIC_FAIL_G9_TRANSPARENT_SUN_ASSUMPTION`**

for the 1.5-TeV NGC-1068 endpoint on the exact `b/Rsun=0.024` reference ray.

This is a failure of the transparent/unattenuated-Sun approximation for that source-energy/ray regime. It is not a failure of the 0090f gravitational focusing geometry. Adding NC interactions cannot restore unscattered transparent propagation.

## TXS 0506+056 290-TeV sentinel
Classification remains

`BLOCKED_G9_0092A_HIGH_ENERGY_AUTHORITY`.

Cooper-Sarkar/Mertsch/Sarkar and the IceCube 6.3–980 TeV absorption measurement were retained as consistency authorities, but this subgate deliberately did not manufacture an exact 290-TeV numerical cross section by post-result interpolation/extrapolation. A separate exact-value authority gate is required before assigning a numerical 290-TeV optical depth under this contract.

## CCSN 5–50 MeV branch
Classification remains

`BLOCKED_G9_0092A_MEV_TOTAL_CROSS_SECTION_AUTHORITY`.

The preregistration requires an authority-backed conservative upper bound on the *total* low-energy interaction optical depth, including coherent nuclear scattering where relevant. The validated Model-S `cptrho` density table does not itself freeze the chord composition. A DIS formula is forbidden at MeV energies. No post-result composition was guessed.

This blocker is scientifically important because the CCSN morphology from 0091 overlaps the 0090f numerical source-size support, while the high-energy named sources are already morphology-authority blocked and the NGC-1068 TeV transparent-Sun approximation now independently fails.

## Gate-level interpretation
The correct overall classification is mixed BLOCKED, not all-energy FAIL:
- NGC 1068 1.5 TeV reference-ray transparency: scientific FAIL;
- TXS 290 TeV exact numerical authority: BLOCKED;
- CCSN 5–50 MeV total-opacity upper-bound authority: BLOCKED.

Do not state that TeV solar opacity kills the MeV CCSN branch. Do not erase the 0090f finite-source survivor PASS. Do not multiply 0090f magnification into detector/material/BSM response.

## Next admissible step
The highest-value G9 follow-on is a prospectively frozen CCSN-MeV solar-composition + total-interaction optical-depth authority gate on the same validated Model-S chord. It must freeze composition authority and all included low-energy weak channels before computing a thinness classification. The independent 290-TeV exact cross-section authority can proceed separately but is lower priority because TXS is already blocked by neutrino morphology authority in 0091.
