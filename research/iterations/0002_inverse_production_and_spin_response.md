# NMIR Iteration 0002 — Production↔Absorption Duality + Spin-Response Triage

Date: 2026-09-06 (Europe/Stockholm)

## Question introduced

Can the microscopic mechanism that *produces* a neutrino identify the best way to capture it through the inverse weak process?

Answer: **yes as a valid organizing principle**, with an important qualification. Weak amplitudes admit crossed/inverse channels, but the observable reverse rate depends on thresholds, phase space, occupancy, recoil, linewidths and medium response. The inverse process is not automatically efficient.

## Main conceptual result

NMIR now contains a formal production↔absorption map:

`emission channel -> inverse channel -> resonance/threshold conditions -> cross section -> deposited energy`.

Examples:

- neutron beta decay ↔ inverse beta decay;
- electron capture ↔ electron-neutrino charged-current absorption;
- bound-state beta decay ↔ proposed recoilless resonant antineutrino absorption;
- weak electroweak resonance (Glashow) as empirical proof that precisely matched neutrino capture can be resonantly enhanced.

The medium response formulation makes this duality precise: positive- and negative-frequency spectral functions are related by thermal detailed balance in equilibrium.

## New high-priority branch

**Resonant inverse nuclear transitions** are promoted to co-primary status with the axial spin/magnon branch.

Why: a successful charged-current/nuclear capture event can deposit keV–MeV, while a single meV-scale magnon excited by a MeV neutrino deposits only ~1e-9 of the incident energy.

## Spin/magnon branch triage

Retained for:
- low-threshold detection;
- directional/polarization effects;
- possible redistribution of axial spectral weight;
- possible multi-excitation or nonequilibrium regimes.

Preliminary negative energy-capture gate:
- one soft collective excitation alone has an intrinsically tiny deposited-energy fraction;
- any energy-harvesting claim therefore requires enormous opacity, repeated scattering, high-multiplicity excitation, or coupling to a harder absorptive channel.

## Resonant-absorption historical gate

Recoilless resonant neutrino/antineutrino absorption has been proposed previously. The H-3/He-3 Mössbauer-antineutrino realization is strongly challenged by lattice deformation, phonon excitation and inhomogeneous line broadening. Therefore NMIR will not rediscover it naively; it will treat those effects as explicit design constraints and scan alternative inverse transitions.

## New code

`src/nmir/duality.py`
- thermal detailed-balance factor;
- one-event deposited-energy fraction;
- unit-area Lorentzian resonance line and peak-width scaling.

`tests/test_duality.py`
- reference energy-deposition ratios;
- detailed-balance normalization at omega=kT;
- inverse-linewidth peak scaling;
- input validation.

## New theory notes

- `theory/PRODUCTION_ABSORPTION_DUALITY.md`
- `theory/SPIN_MAGNON_RESPONSE.md`

## Immediate next calculations

1. Build a machine-readable inverse-transition catalog with `Q`, neutrino resonance/threshold energy, half-life/width, transition type and decay matrix-element proxy.
2. Start with free IBD as an exact normalization anchor.
3. Add candidate two-body electron-capture / bound-beta systems and compute source-absorber line-overlap penalties.
4. Derive a Breit-Wigner/integrated-strength gate carefully enough that peak-cross-section claims cannot be confused with broadband opacity.
5. Freeze solar-neutrino component spectra and calculate flux overlap for every candidate transition.
6. In parallel, implement a toy axial `S_AA(q,w)` model with sum-rule-preserving magnon + continuum spectral weight and compare event-rate vs deposited-power objectives.

## Updated maturity audit

- Problem formulation: 45%
- Operator inventory: 25%
- Many-body response taxonomy: 22%
- Numerical framework: 18%
- Constraint/literature ledger: 18%
- Standard-Model ceiling: 4%
- Engineered-medium scan: 5%
- Production↔absorption branch: 12%
- BSM residual search: 0%

Overall NMIR research maturity: **~12%**.

No claim of practical neutrino energy harvesting is established. The result of this iteration is a sharper search strategy and a newly prioritized physically legitimate inverse-reaction branch.
