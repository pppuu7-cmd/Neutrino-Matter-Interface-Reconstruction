# Iteration 0041 — CEvNS source-opening threshold gate

Date: 2026-09-06
Funnel gate: G2 / F0-F3
Prospective contract: `research/cevns_source_opening_prereg.md`
Prereg commit: `4d42397aced8817714472e5d52e79b69f0361d7e`
Scientific workflow head: `f733d9979878a10bd46d1b0f7aab96f6c33652c9`
Hosted run: `34049714420`
Hosted job: `101530992980`
Artifact: `9994165815`
Artifact ZIP SHA256: `bbeb8ecd3d8c8b003ec7f2218ec962437e3e2f38fc5e6eba00364958cdbb92c2`

## Question
After iteration 0040 established metastable avalanche media as a genuine detection/control survivor but not a neutrino-energy amplifier, what recoil threshold is required for a CEvNS event from each solar source class to be kinematically observable?

This is a class-level source-opening gate, not a material optimization and not an energy-harvesting gain.

## Exact kinematics
For neutrino energy `E` and nuclear mass `M`,

`T_max(E,M) = 2 E^2 / (M + 2E)`.

The exact inverse threshold is

`E_min(T,M) = 0.5 [ T + sqrt(T^2 + 2 M T) ]`.

A line source is kinematically open iff `T_thr <= T_max`. A continuum is open iff its physical endpoint exceeds `E_min`. No event rate is inferred until the physical source spectrum and differential CEvNS response are folded.

## Hosted validation
Raw job log inspected. Dedicated tests: `4 passed in 0.01s`.

Using `M(Ar-40)=39.9623831237 u`, a `40 eV` nuclear-recoil threshold requires

`E_nu >= 0.8628609380456526 MeV`.

Representative Ar-40 recoil endpoints are:
- pp endpoint 0.420 MeV -> `9.477358035997204 eV` -> CLOSED at 40 eV;
- Be7 reference line 0.8618 MeV -> `39.90169806276378 eV` -> CLOSED at 40 eV by only `0.09830193723622216 eV`;
- pep line 1.44 MeV -> `111.40120588745857 eV` -> OPEN;
- B8 endpoint 16.36 MeV -> `14367.57704446474 eV` -> OPEN.

The forward/inverse identity and monotonicity tests passed at the preregistered `1e-12` relative criterion.

## Scientific interpretation
The approximately 40-eV Ar threshold is genuinely special: the central Be7 line lies only about `0.10 eV` below the exact recoil threshold in this frozen reference convention. Therefore a step-function treatment of the line is scientifically inadequate for the next stage. The already-frozen thermally shifted/broadened solar Be7 profile must be folded with the CEvNS differential recoil spectrum and detector threshold/efficiency.

This does not alter iteration 0040 energy accounting. Lowering a bubble threshold can increase the fraction of weak events that become observable, but it does not increase the weak cross section and it does not multiply neutrino-supplied energy.

## Classification
**CEVNS_SOURCE_OPENING_KINEMATICS_PASS / DETECTION_SURVIVOR / ENERGY_GAIN_NONE.**

At 40 eV on Ar-40, pp is kinematically closed, pep and B8 are open, and the Be7 central line is a near-boundary case requiring the physical line-profile fold rather than post-hoc threshold adjustment.

## Exact next gate
Fold the primary/frozen thermally broadened Be7 solar-neutrino line through the Standard-Model CEvNS differential cross section on Ar-40, including the 40-eV recoil cut. Report above-threshold cross section, fraction of line-profile events capable of producing `T>=40 eV`, expected events/kg/day for the frozen solar flux, and threshold sensitivity. Keep this a detection score; do not count avalanche reservoir energy as neutrino-supplied power.
