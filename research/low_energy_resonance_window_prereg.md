# NMIR preregistration — low-energy resonance design window

Date: 2026-09-06
Planned iteration: 0037
Gate: G8 resonance kinematics/design requirement
Status at preregistration: OPEN

## Motivation
Iteration 0036 established a positive control: the observed Glashow resonance proves that a real s-channel intermediate state can raise the neutrino interaction cross-section scale enormously, but its 6.3-PeV kinematics are irrelevant to solar neutrinos. Iteration 0035 established a distinct low-energy route, resonant induced orbital electron capture (RIOEC), in which an atomic+nuclear level combination sets a discrete antineutrino resonance.

This gate asks a kinematic question only:

**What resonance energy/mass scale would an elementary stationary-electron s-channel state or a nuclear/atomic RIOEC transition need in order to overlap the source classes already present in NMIR?**

No new particle, coupling, target or practical absorber is claimed here. BSM remains LOCKED.

## A — stationary-electron s-channel design window
For a negligibly massive incident neutrino/antineutrino on an electron at rest,

`s = m_e^2 + 2 m_e E_nu`.

A single on-shell s-channel intermediate state must therefore have

`M_* = sqrt(m_e^2 + 2 m_e E_nu)`.

Freeze `m_e = 0.51099895 MeV` and these source-energy controls:
- thermal low point: `10 eV`;
- thermal control: `1 keV`;
- pp endpoint control: `0.420 MeV`;
- Be7 dominant-line control: `0.8618 MeV`;
- pep line: `1.442 MeV`;
- NMIR conservative solar ceiling: `20 MeV`.

Also reproduce the Glashow calibration with `M_W=80.4 GeV`, requiring `E_res` within 2% of 6.3 PeV.

Prospective output:
- tabulate `M_*` and excess `Delta=M_*-m_e` for all controls;
- identify the full stationary-electron mass window associated with 0<E_nu<=20 MeV;
- identify the thermal 10 eV–5 keV subwindow motivated by Haxton–Lin thermal solar neutrino/antineutrino flux density being significant below about 5 keV.

Critical scope guard: the equation is kinematics only. Whether a state with the required quantum numbers exists, couples to the relevant neutrino flavor, and survives experimental constraints is a separate F4/F8 question. In the Standard Model the Glashow W resonance specifically requires `anti-nu_e + e-`; do not imply an analogous known `nu_e+e-` state at MeV masses.

## B — RIOEC nuclear/atomic tuning window
For resonant induced orbital electron capture use the 2026 primary-paper condition

`E_R = -Q_epsilon + E_x + E_b`,

where `Q_epsilon` is the ordinary EC Q value, `E_x` daughter nuclear excitation and `E_b` captured orbital-electron binding energy.

Freeze two source windows only as design requirements:
- thermal-solar antineutrino emphasis: `0 < E_R <= 5 keV`, because Haxton–Lin find thermal neutrino/antineutrino flux density per flavor significant below about 5 keV;
- generic below-IBD RIOEC domain: `0 < E_R < 1.8 MeV`.

Define mismatch variable

`delta_tune = E_x + E_b - Q_epsilon = E_R`.

The gate records the required cancellation precision relative to a representative nuclear/atomic scale `S = max(|Q_epsilon|,|E_x|,|E_b|,1 MeV)`. Without a target-specific triplet, report only the generic fact that a keV resonance requires the combination of MeV-scale terms to cancel to ~1e-3–1e-2 relative precision; do not claim this is impossible because the RIOEC paper explicitly identifies candidate nuclides.

## C — no peak-cross-section inference
This gate must NOT convert a design-window match into a rate. Iteration 0025/0035 remains active:

for a smooth continuous source, narrowing a resonance does not create integrated entrance strength; a candidate rate requires evaluated `B0`/weak entrance strength and the source spectral density at `E_R`.

## Prospective classification
If the Glashow calibration and exact stationary-electron mapping pass, classify:

`G8_LOW_ENERGY_RESONANCE_WINDOW_PASS`.

This is a constructive design constraint, not a discovery of a new state. Keep:
- elementary low-mass resonance existence/coupling: OPEN/BSM-LOCKED;
- target-specific RIOEC strength × thermal-solar spectrum: OPEN.
