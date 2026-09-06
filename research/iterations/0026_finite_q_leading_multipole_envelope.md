# NMIR iteration 0026 — finite-q leading-current multipole envelope

Date: 2026-09-06
Status: **FINITE_Q_LEADING_STRONG_NEGATIVE**
Secondary non-theorem stress: **MILLIONFOLD_SUBLEADING_STRESS_NEGATIVE**
Readiness after promotion: `NMIR_READINESS: 50%` (audit estimate)

## Question
Iteration 0024 bounded only the leading allowed long-wavelength Fermi/GT sector. Iteration 0026 asks whether finite momentum transfer and redistribution among the full charged-current Coulomb/longitudinal/transverse multipoles can evade that result for the **leading vector-charge plus axial-spin one-body current**.

The standard charged-current multipole decomposition contains Coulomb `M_J`, longitudinal `L_J`, transverse-electric `T_J^el`, and transverse-magnetic `T_J^mag` responses. The acceptance contract was frozen before hosted output in `research/finite_q_multipole_prereg.md`.

## Prospective bound
Bounding all angular factors and interference terms with `|a·b|<=1` and `2|ab|<=a^2+b^2` gives a conservative full-angular factor `24*pi≈75.398` relative to the usual allowed normalization. To protect against convention bookkeeping, the preregistered factor was enlarged to

`C_MULTIPOLE = 128`.

For the leading nonrelativistic finite-q currents,

`J_V^0(q) ~ sum_i tau_i^+ exp(i q·r_i)`,

`J_A(q) ~ g_A sum_i tau_i^+ sigma_i exp(i q·r_i)`.

Since the phase has modulus one, the correlation-independent operator-norm caps remain the same as iteration 0024:

`S_V<=A^2`, `S_A<=3 g_A^2 A^2`.

The iteration-0024 intentionally excessive target-space assumptions are inherited unchanged: `A<=300`, daughter `Z<=119`, zero threshold/excitation, `E_nu<=20 MeV`, artificial neutrino energy flux `2000 W/m^2`, and +2% target-count safety.

Thus

`P_finite_q_leading <= 128 * P_allowed_0024`.

Convection/recoil, axial charge, weak magnetism, induced pseudoscalar and relativistic nuclear corrections are not claimed to be rigorously included. A separate preregistered `x1e6` cross-section stress factor is reported for these omitted terms only as a robustness diagnostic, not as a theorem or uncertainty.

Prospective classification:
- `FINITE_Q_LEADING_STRONG_NEGATIVE` if leading result `<1e-6 W/kg`;
- `MILLIONFOLD_SUBLEADING_STRESS_NEGATIVE` if the separate x1e6 diagnostic remains `<1 W/kg`.

## Hosted authority
Implementation chain:
- preregistration `c3a29bc01b2af4f68ca1a6cf55447c6200e28c81`;
- code `caa98e8a9320280102c19a9def5334d89d061cd4`;
- tests `5bbce4f7c784a9347b3d4838bc07d78774e75903`;
- benchmark `916b306b57a9688ebcb9547fb5610b5cddbe51d6`;
- hosted head `e04fa0d9907f62c0bf020317a79cee330b832ec6`.

Scientific workflow:
- run `34038882486`;
- job `101501885143`;
- artifact `9991038179`;
- artifact ZIP SHA256 `d281d3057ce5976545fda62888395a95cf6acfc183e2b64999dfb0c8b849f89f`.

Dedicated regression tests: **4 passed**. Same-head baseline CI run `34038882497`: SUCCESS. Raw benchmark output was inspected before classification.

## Result

| quantity | result |
|---|---:|
| inherited iteration-0024 allowed envelope | `9.419449302949355e-12 W/kg` |
| derived raw angular factor `24*pi` | `75.39822368615503` |
| frozen multipole safety factor | `128` |
| **leading finite-q envelope** | **`1.2056895107775174e-9 W/kg`** |
| deficit to 1 W/kg | **`8.2940092873e8`** |
| separate subleading-current stress | `1e6` |
| x1e6 stressed diagnostic | **`1.2056895107775173e-3 W/kg`** |
| stressed deficit to 1 W/kg | **`829.4009287`** |
| leading classification | **FINITE_Q_LEADING_STRONG_NEGATIVE** |
| stress classification | **MILLIONFOLD_SUBLEADING_STRESS_NEGATIVE** |

## Scientific interpretation
Finite momentum transfer and parity-changing redistribution among leading Coulomb/longitudinal/transverse vector-charge and axial-spin multipoles do not rescue passive solar-neutrino energy harvesting. The conservative finite-q leading-current envelope is almost nine orders of magnitude below 1 W/kg even after multiplying the already extreme iteration-0024 target-space envelope by 128.

More strikingly, multiplying this finite-q result by another million as a deliberately non-rigorous stress allowance for all omitted subleading one-body current terms still gives only `~1.2 mW/kg`, about 829 times below 1 W/kg. This is useful robustness evidence but **must not be promoted to a proof** for recoil/weak-magnetism/axial-charge/induced-pseudoscalar terms.

The remaining path to a genuine global passive-SM nuclear no-go is therefore narrower:
1. rigorously norm-bound the omitted subleading one-body weak-current operators, or obtain a full-current inclusive bound;
2. complete G8 numerically for genuine resonant inverse channels with measured `Gamma_in`/ft and physical solar line profiles;
3. keep engineered collective response, focusing and material architecture as separate multiplicative/interface gates.
