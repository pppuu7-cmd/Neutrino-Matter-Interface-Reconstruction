# NMIR preregistration — G8 experimentally grounded resonance positive control

Date: 2026-09-06
Gate: G8 target-specific resonance
Status at preregistration: formal integrated-area gate PASS; target-specific reality control OPEN

## Purpose
NMIR has accumulated several negative resonance/collective-energy bounds. This gate asks the converse question: does known Standard-Model physics contain a real neutrino-matter resonance whose cross section is parametrically large, and what exactly prevents that mechanism from solving the solar-energy branch?

Two controls are frozen before implementation.

## Control A — observed Glashow resonance
Reaction:

`anti-nu_e + e- -> W- -> anything`.

Use the standard resonance kinematics

`E_res = M_W^2/(2 m_e)`

and the hadronic peak Breit-Wigner cross section

`sigma_peak_had = 24*pi*Br(W->e nu)*Br(W->had)/M_W^2`

with conversion `1 GeV^-2 = 0.389379e-27 cm^2`.

Freeze rounded literature inputs used by the analytic-control paper:
- `M_W = 80.4 GeV`;
- `Br(W->e nu)=0.106`;
- `Br(W->had)=0.674`;
- `m_e=0.51099895 MeV`.

Published control values:
- resonance energy `~6.3 PeV`;
- hadronic peak cross section `3.4e-31 cm^2`.

Prospective acceptance:
- `|E_res/6.3 PeV - 1| < 0.02`;
- `|sigma_peak/3.4e-31 - 1| < 0.10`.

Experimental authority: IceCube, Nature 591 (2021) 220, reports a `6.05 +/- 0.72 PeV` shower consistent with the Glashow resonance.

Record but do not overinterpret:
- energy mismatch factor relative to the frozen NMIR solar ceiling `E_nu<=20 MeV`;
- cross-scale ratio relative to the 1-MeV Xe-132 CEvNS benchmark. These compare scales, not equal-energy/equal-target efficiencies.

Classification if controls pass:
`G8_REAL_RESONANCE_POSITIVE_CONTROL_PASS`, but `SOLAR_APPLICATION_FAIL_KINEMATICS` because the known elementary SM resonance is far outside the solar spectrum.

## Control B — real narrow solar-line overlap in crossed 7Li <-> 7Be
Use only the already validated iteration-0023 B16+MSW result. For GS98:
- total Li7 rate `19.3488133336 SNU`;
- total neutrino-energy moment `77.5070777600 SNU MeV`;
- thermally broadened Be7-line contribution `4.07166111 SNU` and `3.51461158 SNU MeV`.

Record exact fractions:
- event fraction `Be7_rate/total_rate`;
- energy-moment fraction `Be7_moment/total_moment`.

This is NOT a Breit-Wigner nuclear resonance. It is a narrow-source-line / crossed-threshold overlap control showing what an actually matched solar line does in a validated target.

Prospective interpretation:
- if event fraction > energy fraction by >3x, classify `NARROW_LINE_EVENT_GAIN_NOT_ENERGY_GAIN`, consistent with the NMIR distinction between detection/event enhancement and energy harvesting.

## Comparison with proposed Mössbauer antineutrinos
Literature reports a proposed 18.6-keV H3-He3 recoilless resonant capture with idealized cross section around `5e-32 cm^2`, but solid-state broadening/phonon effects are expected to strongly suppress the ideal resonance and the bound-state source route is not an established practical absorber. Record it as `THEORY_POSITIVE / MATERIAL_REALIZATION_UNVALIDATED`, not as a PASS-SURVIVOR.

## Scope guards
1. A real resonance at the wrong source energy is not a solar-capture solution.
2. Peak cross section is not flux-integrated power; iteration-0025 area/source-overlap theorem remains active.
3. The Li7-Be7 control is threshold/line matching, not a Breit-Wigner resonance.
4. No Glashow or Mössbauer gain may be multiplied with solar Li7 power.
5. This gate is deliberately a positive control: it establishes that strong resonant neutrino coupling exists in known physics when the required kinematics are supplied.
