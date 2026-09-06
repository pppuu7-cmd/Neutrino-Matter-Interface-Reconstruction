# NMIR passive allowed-SM upper-bound preregistration

Date: 2026-09-06
Gate: G3 target-space passive Standard-Model upper bound, first allowed-current stage.

## Question
Can any ordinary passive **nuclear charged-current target**, restricted to the leading allowed one-body Fermi + Gamow–Teller response, reach remotely macroscopic solar-neutrino-supplied power even if nuclear strength and incident flux are bounded in deliberately over-generous ways?

This is **not** yet a theorem for forbidden multipoles, resonant line capture, engineered coherence, active media, gravitational focusing, or BSM interactions. Those remain separate gates.

## Frozen neutrino-energy accounting
Every successful reaction is credited at most the incident neutrino energy,

`E_dep,nu <= E_nu`.

Daughter decay energy, target nuclear-mass release, preparation energy, and externally supplied energy are excluded.

## Analytic point-Coulomb phase-space bound
For an emitted electron with total energy `E` and momentum `p`, the attractive point-Coulomb factor is

`F_pc = x/(1-exp(-x))`, `x = 2*pi*alpha*Z_f*E/p > 0`.

From `exp(x) >= 1+x` follows `1-exp(-x) >= x/(1+x)`, hence

`F_pc <= 1+x`.

Therefore

`p E F_pc <= p E + 2*pi*alpha*Z_f*E^2 <= (1+2*pi*alpha*Z_f) E^2`.

The hosted calculation must use this inequality directly; it must not fit a Coulomb factor to any target result.

## Correlation-independent operator-norm strength bound
For a nucleus of mass number `A`, the one-body allowed operators are sums over at most `A` nucleons. Using only the triangle/operator-norm inequality gives the intentionally loose closure bounds

`S_F <= A^2`,

`S_GT <= 3 A^2`,

so that the total leading allowed strength obeys

`S_allowed <= A^2 * (1 + 3 g_A^2)`.

This is deliberately much weaker than physical Fermi/Ikeda systematics and therefore cannot be interpreted as a realistic nuclear-strength prediction.

## Known-nuclei stress domain
Freeze the following over-generous domain before execution:

- `A <= 300`;
- daughter charge `Z_f <= 119`;
- all capture thresholds and excitation energies are set to zero when maximizing phase space;
- all solar neutrinos are allowed energies up to `E_nu,max = 20 MeV` (above the physical hep endpoint ~18.8 MeV);
- incident neutrino energy flux is granted an artificial ceiling `F_nu <= 2000 W/m^2`, larger than the measured electromagnetic total solar irradiance (~1361 W/m^2) and vastly above the actual B16 solar-neutrino energy flux;
- target-count conversion receives an additional 2% upward safety factor relative to `1000 N_A/A` nuclei/kg.

The purpose is not to estimate a realistic material, but to create a one-sided envelope that strongly favors neutrino energy harvesting.

## Secondary six-decade omitted-physics stress factor
After the analytic allowed point-Coulomb bound is computed, report a separate diagnostic equal to that bound multiplied by `10^6`.

This factor is **not** part of the theorem and does not represent a measured uncertainty. It is an intentionally enormous robustness stress allowance for omitted finite-size/atomic/shape/interference corrections. The analytic result and the x10^6 stress diagnostic must be reported separately.

## Prospective classification
- **STRONG NEGATIVE (scoped)** if the x10^6 stress diagnostic remains below `1e-3 W/kg` (still >=1000 times below 1 W/kg).
- **NEGATIVE (scoped)** if the analytic bound is below `1 W/kg` but the x10^6 stress diagnostic is >=`1e-3 W/kg`.
- **NO NEGATIVE BOUND** if the analytic allowed-current envelope reaches or exceeds `1 W/kg`.

No result from this gate may close global G3 by itself. Before a global passive-SM claim, NMIR must separately address forbidden multipoles and G8 resonance integrated-strength/bandwidth overlap.

## Required validation
1. Unit tests for the algebraic bound and input guards.
2. Bound must sit above all currently validated Li7, Se82, Ga71, and Cl37 W/kg values.
3. Hosted workflow result/raw artifact must be inspected before classification.
4. No acceptance threshold may be changed after seeing hosted output.
