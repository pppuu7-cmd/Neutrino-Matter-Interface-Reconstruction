# NMIR preregistration — finite-q leading-current multipole envelope

Date: 2026-09-06
Purpose: strengthen G3 beyond the long-wavelength allowed limit without silently claiming closure of all recoil/subleading weak-current terms.

## External formalism anchor
Use the standard charged-current multipole decomposition with Coulomb `M_J`, longitudinal `L_J`, transverse-electric `T_J^el`, and transverse-magnetic `T_J^mag` operators, e.g. the cross-section convention in Progress of Theoretical and Experimental Physics 2018, 123E02, DOI `10.1093/ptep/pty134`.

## Angular/interference bound
In that convention the response bracket has:
- `M` coefficient `1+nu_hat·beta`, absolute upper bound 2;
- `L` coefficient `1-nu_hat·beta+2(nu_hat·q_hat)(q_hat·beta)`, absolute upper bound 4;
- `M-L` interference coefficient with `|q_hat·(nu_hat+beta)|<=2`; using `2|LM|<=|L|^2+|M|^2`, the interference adds at most 2 to each squared-response coefficient;
- transverse outer coefficient `1-(nu_hat·q_hat)(q_hat·beta)<=2`; its interference is bounded the same way, making the whole transverse block <=6 times `|T_el|^2+|T_mag|^2`.

Therefore the full response bracket is bounded by 6 times the sum of squared multipole responses. Integrating the differential prefactor over solid angle gives a conservative ratio `24*pi≈75.40` relative to the usual `G_F^2 V_ud^2/pi * pE F * strength` allowed normalization.

To protect against convention/normalization bookkeeping, freeze an even larger multiplicative kinematic/multipole factor

`C_MULTIPOLE = 128`.

No post-result adjustment is permitted.

## Leading finite-q strength bound
For the leading nonrelativistic charged current,

`J_V^0(q) ~ sum_i tau_i^+ exp(i q·r_i)`,

`J_A(q) ~ g_A sum_i tau_i^+ sigma_i exp(i q·r_i)`.

The phase has unit modulus, so triangle/operator-norm bounds are unchanged at finite q:

`S_V <= A^2`, `S_A <= 3 g_A^2 A^2`.

The multipole expansion only redistributes this finite-q current among Coulomb/longitudinal/transverse sectors. The iteration-0024 target-count, A/Z, zero-threshold, 20-MeV endpoint and artificial `2000 W/m^2` neutrino-energy-flux assumptions are retained unchanged.

Thus the preregistered leading finite-q power envelope is

`P_finite_q_leading <= 128 * P_allowed_0024`.

## Explicitly unresolved one-body current terms
Convection/recoil current, axial charge, weak magnetism, induced pseudoscalar and nuclear-relativistic corrections are **not** claimed to be rigorously included in the leading operator-norm theorem above.

Report a separate non-theorem diagnostic

`P_subleading_stress = 1e6 * P_finite_q_leading`.

The factor `1e6` is an intentionally extreme cross-section-level stress allowance, not a physical uncertainty and not a proof for those operators.

## Prospective classification
- `FINITE_Q_LEADING_STRONG_NEGATIVE` if `P_finite_q_leading < 1e-6 W/kg`.
- Additionally report `MILLIONFOLD_SUBLEADING_STRESS_NEGATIVE` if `P_subleading_stress < 1 W/kg`.
- A global passive-SM no-go remains forbidden unless the omitted one-body terms are independently bounded or absorbed into a rigorous full-current norm.

## Required validation
1. Recompute the iteration-0024 allowed envelope from code; do not hard-code its numerical result.
2. Verify `128 > 24*pi`.
3. Verify finite-q envelope remains above all validated target powers.
4. Hosted raw JSON and same-head baseline CI must be inspected before classification.
