# Preregistration 0092 — G9 solar transmission authority

Date frozen: 2026-09-08
Parent immutable result: `research/iterations/0091_g9_named_source_realizability_blocked.md`, record commit `8bc8898fda7d0919fc4f7f0dc9bfd1eadb33b0ff`, classification `BLOCKED_G9_REAL_SOURCE_AUTHORITY`.
Numerical parent: 0090f `PASS_G9_FULL_GRID_FINITE_NONZERO_SURVIVORS`.

## Question
Does ordinary Standard-Model neutrino propagation through the solar matter traversed by the frozen G9 ray family remain compatible with the transparent/unattenuated-Sun approximation in the source-energy regimes already present in NMIR?

This gate tests transmission only. It does not change the 0090f lens map and does not authorize detector-event, interaction-gain, material-response, deposited-energy or power claims.

## Frozen ray / solar authority
Primary sentinel ray is the existing NMIR Model-S reference ray:
- impact parameter `b/Rsun = 0.024`;
- focal distance `z = 24.073780819657056 AU` from the frozen earlier G9 authority.

Solar density authority must be Christensen-Dalsgaard et al. Model S (1996), using the official tabulated `r/Rsun, rho` data from the author's Aarhus solar-model archive. No constant-density or hand-fit solar profile may replace it for the terminal result.

The mass column on a straight chord is

`Sigma(b) = 2*Rsun*integral_0^sqrt(1-b^2) rho(sqrt(b^2+x^2)) dx`,

with `x`, `b` and the tabulated radius expressed in units of `Rsun`, `rho` in `g cm^-3`, and `Rsun` in cm.

For high-energy DIS, the nucleon column sentinel is `N_N = Sigma/m_u`. Composition refinements may be added only as a separately reported correction; they may not weaken a robust opacity classification obtained from the frozen conservative calculation.

## Frozen energy regimes
No post-result source/energy substitution is allowed.

1. **CCSN / MeV regime**: use the already frozen NMIR generic Galactic CCSN authority. The gate must establish at least a conservative thinness bound across a representative `5–50 MeV` window. At these energies the terminal calculation must use an interaction authority appropriate to MeV neutrinos; the high-energy DIS linearization may not be extrapolated downward.
2. **NGC 1068 regime**: use `1.5–15 TeV`, inherited from the primary IceCube NGC 1068 evidence analysis as the principal contribution to the measured excess.
3. **TXS 0506+056 high-energy sentinel**: include `290 TeV` as the IceCube-170922A-scale sentinel. This is a transmission sentinel only and does not replace the frozen 0091 time-dependent-source semantics.

A logarithmic diagnostic scan may additionally be reported from `10 MeV` to `1 PeV`, but the frozen classifications must be made on the source regimes above.

## Cross-section authority
For the TeV/PeV regimes use Standard-Model neutrino/antineutrino nucleon CC+NC cross sections from a primary/review authority valid in the corresponding energy range. Measured high-energy cross-section results (FASER/IceCube) may be used as independent sentinels.

For a conservative absorption no-go at TeV energies, a CC-only optical depth is admissible: if even a supported lower/conservative CC cross section gives `tau_CC >= 1`, adding NC interactions cannot restore the transparent/unattenuated approximation.

For MeV energies use appropriate weak-interaction cross-section authority and report the most conservative interaction channel needed to demonstrate or reject `tau <= 0.1`.

## Frozen transmission statistics
`tau(E,b) = N_target(b) * sigma(E)`

`T0(E,b) = exp(-tau)`

`T0` is the unscattered/unabsorbed sentinel. If NC scattering is non-negligible, a later transport calculation may redistribute rather than simply remove neutrinos; such regeneration cannot be silently counted as unchanged-energy transparent propagation.

## Frozen classifications
Per energy regime:
- `PASS_G9_SOLAR_TRANSMISSION_THIN` if an authority-backed upper/conservative total optical depth satisfies `tau <= 0.1` over the frozen regime (`T0 >= exp(-0.1)`).
- `ESCALATE_G9_SOLAR_TRANSPORT_NONNEGLIGIBLE` if `0.1 < tau < 1` and a transport treatment is required before using an unattenuated source spectrum.
- `SCIENTIFIC_FAIL_G9_TRANSPARENT_SUN_ASSUMPTION` if `tau >= 1` for a source-relevant energy/ray under an authority-backed conservative calculation. This invalidates the transparent/unattenuated-Sun assumption for that regime, not gravitational focusing in general.
- `BLOCKED_G9_SOLAR_TRANSMISSION_AUTHORITY` if the required external density/cross-section authority cannot be made reproducible.
- `INFRASTRUCTURE_FAIL_G9_0092` only for non-scientific execution failure.

Gate-level summary may be mixed across source regimes; do not collapse MeV and TeV results into a single all-energy PASS/FAIL.

## Numerical reproducibility requirements
- obtain the official Model-S table directly from its primary archive during the authority run;
- preserve the exact downloaded bytes or SHA256 hash in the result artifact;
- parse the official `r/Rsun` and `rho` columns;
- sort/deduplicate radius values deterministically;
- interpolate density in a documented deterministic way (linear interpolation in `rho` is the primary frozen method; log-rho interpolation may be reported only as a sensitivity check);
- compute the chord integral with two independently tighter numerical tolerances or discretizations and require relative agreement `<= 1e-4` for `Sigma`;
- report `Sigma`, `N_N`, cross-section authority/values, `tau`, `T0` and the frozen classification.

If the primary archive cannot be fetched in the execution environment, the gate is `INFRASTRUCTURE_FAIL_G9_0092`; do not replace it post hoc with a different solar model.

## Guards
- no detector PSF/localization as physical source size;
- no EM source size as neutrino size;
- no post-hoc fourth 0091 source;
- no multiplication of 0090f magnification by source flux, detector rate, material response or deposited energy;
- no statement that TeV opacity kills the MeV CCSN branch;
- no statement that opacity of the straight ray proves a general no-go for every possible solar-neutrino lens trajectory unless separately demonstrated.
