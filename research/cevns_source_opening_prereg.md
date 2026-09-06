# CEvNS source-opening threshold preregistration

Date: 2026-09-06
Gate: G2 / F0-F3 / metastable detection survivor

## Question
For a passive metastable detector with nuclear-recoil threshold `T_thr`, which solar-neutrino source components are kinematically capable of producing a CEvNS recoil above threshold? This is a detection/state-control gate, not an energy-harvesting gain.

## Frozen kinematics
For neutrino energy `E` and nuclear mass `M`,

`T_max(E,M) = 2 E^2 / (M + 2E)`.

The exact inverse source-opening energy for a recoil threshold `T` is

`E_min(T,M) = 0.5 * ( T + sqrt(T^2 + 2 M T) )`.

A monoenergetic/line component is kinematically OPEN iff `T_thr <= T_max(E_line,M)`. A continuous component is OPEN iff its endpoint exceeds `E_min(T_thr,M)`; this gate does not claim a rate without folding the physical spectrum and CEvNS differential cross section.

## Frozen controls
1. Forward/inverse round-trip must agree to relative error <= 1e-12 for positive test points.
2. `T_max` must increase monotonically with `E` and decrease with `M`.
3. At `T_thr = T_max(E,M)`, the inverse must return `E` to <=1e-12 relative error.
4. For an Ar-40 mass approximation `M = 39.9623831237 u`, evaluate source-opening thresholds for representative solar energies: pp endpoint 0.420 MeV, Be7 0.8618 MeV, pep 1.44 MeV, B8 endpoint 16.36 MeV.
5. Evaluate the special `T_thr = 40 eV` Ar case. Classification must remain purely kinematic: source OPEN/CLOSED at F3, no event-rate or W/kg claim.

## Scientific discipline
- Metastability may amplify observability but never multiplies neutrino-supplied energy.
- No cross-section enhancement is inferred from lowering a detector threshold.
- Spectral tails/thermal broadening near a boundary must be treated in a later physical-spectrum fold, not by moving this preregistered criterion after seeing results.
