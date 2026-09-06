# Exact isotope-mass provenance for CEvNS real-nucleus optimization

Frozen: 2026-09-06
Local numerical authority: `data/cevns_target_candidates_exact_mass.csv`

## Source
National Institute of Standards and Technology (NIST), **Atomic Weights and Isotopic Compositions for All Elements**:
`https://physics.nist.gov/cgi-bin/Compositions/stand_alone.pl`

The table values were transcribed from the isotope-mass column for the exact nuclides named in the local CSV. Parenthetical NIST uncertainties are not used in the CEvNS ranking because they are negligible compared with the detector-threshold/systematic scales of this gate; the central atomic masses are frozen verbatim to the shown digits.

Selected cross-checks that motivated the correction:
- Ar-40: `39.9623831237 u`;
- Ca-40: `39.962590863 u`;
- C-12: `12.00000000000 u` by definition in the NIST table;
- Xe-132: `131.9041550856 u`.

## Why this file exists
Iteration 0044 prospectively required the integer-mass approximation `M=A m_u` to reproduce the already-authoritative Ar-40 / physical-Be7 40-eV endpoint rate within 1%. It failed by about 30% because the surviving recoil phase space is extremely small near endpoint.

Therefore iteration 0045 freezes exact isotope masses before any corrected full-solar target ranking is inspected. This is a physically motivated replacement of a falsified approximation, not a relaxation of the 1% gate.

## Scope
The values are **atomic** isotope masses. Using atomic rather than bare nuclear masses introduces electron-mass/binding bookkeeping differences much smaller than the broad CEvNS target-ranking purpose here; importantly, the same atomic-mass convention reproduces the iteration-0042 Ar-40 authority. Any future precision-electroweak calculation may prospectively replace this by a nuclear-mass convention with explicit electron subtraction/binding corrections.
