# Preregistration amendment 0099a — feasible-mass interval closure

Date frozen: 2026-09-09
Parent prereg: `research/prereg/0099_v2_g9_discrete_power_architecture_fork.md`
Parent prereg commit: `7792fb3412eb9f3c932bc04f8ae357bdc4c0129f`
Timing: frozen before 0098 execution and before any 0099 result.

## Defect found by pre-execution algebra audit
The parent 0099 text initially defined propellant mass by evaluating at `M0_max = n_active*T/a_hover`, the maximum mass allowed by thrust. That is not a required spacecraft mass; it is only a ceiling. Evaluating xenon throughput at that ceiling can create an artificial throughput failure even when a lower initial mass satisfies both fixed hardware and throughput constraints.

No 0099 parent result exists. This amendment is therefore prospective and independent of outcome.

## Correct frozen closure
For each already frozen discrete configuration retain:
- `n_active in {1,2,4}`;
- two installed strings per active lane;
- integer MMRTG count from the 25% EODL electrical-reserve rule;
- all component proxy masses;
- exact inherited `f_prop`, `a_hover`, thrust and Isp;
- conservative `450 kg` xenon throughput per used propulsion string.

Define fixed dry hardware represented in this gate:

`M_fixed = N_MMRTG*45 kg + M_propulsion_hardware`.

For any candidate initial spacecraft mass `M0`, ideal ten-year xenon mass is

`M_prop(M0) = f_prop*M0`.

A non-negative unmodeled-spacecraft residual requires

`M0*(1-f_prop) - M_fixed >= 0`,

so the exact lower mass bound is

`M0_lower = M_fixed/(1-f_prop)`.

Thrust gives

`M0_thrust_upper = n_active*T_point/a_hover`.

Two sequential strings per active lane imply `2*n_active` used strings over the frozen ten-year hours model. The conservative throughput constraint is

`f_prop*M0/(2*n_active) <= 450 kg`,

hence

`M0_throughput_upper = 900 kg*n_active/f_prop`.

The admissible upper bound is

`M0_upper = min(M0_thrust_upper, M0_throughput_upper)`.

Define

`mass_interval_exists = (M0_upper > M0_lower)`.

At the largest admissible initial mass, record

`M_residual_at_upper = M0_upper*(1-f_prop) - M_fixed`

and

`f_residual_at_upper = M_residual_at_upper/M0_upper`.

Also record which ceiling is active (`THRUST` or `THROUGHPUT`, or `TIE` within machine equality).

## Corrected discrete mass-power/throughput subgate
A configuration survives iff:
- integer electrical power closure holds by construction;
- `mass_interval_exists == true`;
- all values are finite and positive where required.

For each of the three observer controls at least one of the prospectively frozen operating-point / `n_active` configurations must survive. Otherwise classify:
`SCIENTIFIC_FAIL_V2_G9_0099_DISCRETE_MASS_POWER_OR_THROUGHPUT`.

If one or more configurations survive for every observer control, continue to the already frozen MMRTG isotope/thermal authority and fission-alternative classification.

## Interpretation guard
`M0_upper` is not a recommended spacecraft mass. `M_residual_at_upper` is not payload mass. The interval test proves only that the frozen integer power/propulsion hardware and ideal xenon fraction do not algebraically consume all available mass before thrust/throughput ceilings are reached.

All omitted tank, thermal, structure, avionics, communications, detector/payload and reliability sectors remain omitted exactly as declared in 0099 and cannot be inferred from a positive interval.
