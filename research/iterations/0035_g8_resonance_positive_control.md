# NMIR iteration 0035 — experimentally grounded G8 resonance positive control

Date: 2026-09-06
Classification: **G8_REAL_RESONANCE_POSITIVE_CONTROL_PASS / SOLAR_APPLICATION_FAIL_KINEMATICS / NARROW_LINE_EVENT_GAIN_NOT_ENERGY_GAIN**

## Prospective contract
`research/g8_positive_control_prereg.md`, commit `be5dc071f6c10f0c00f02f62210e540e4923ffd5`.

## Control A — Glashow resonance
Known Standard-Model reaction:

`anti-nu_e + e- -> W- -> anything`.

Frozen rounded control inputs:
- `M_W=80.4 GeV`;
- `m_e=0.51099895 MeV`;
- `Br(W->e nu)=0.106`;
- `Br(W->had)=0.674`.

Analytic resonance kinematics:

`E_res=M_W^2/(2m_e)`.

Hadronic peak Breit-Wigner control:

`sigma_peak_had=24*pi*Br(W->e nu)*Br(W->had)/M_W^2`.

Hosted result:
- `E_res = 6.32502278136 PeV`;
- relative error to frozen `6.3 PeV` control: `0.3972%`;
- `sigma_peak_had = 3.24479529916e-31 cm^2`;
- relative error to frozen `3.4e-31 cm^2` control: `4.565%`.

Both prospective controls PASS.

Experimental authority: IceCube reported a `6.05 +/- 0.72 PeV` shower consistent with the Glashow-resonance interpretation (Nature 591, 220, 2021).

Scale diagnostics only:
- resonance energy / NMIR solar ceiling 20 MeV = `3.16251139068e8`;
- hadronic peak cross-section / 1-MeV Xe-132 CEvNS benchmark = `1.34925231286e10`.

The latter is not an equal-energy/equal-target efficiency comparison; it simply demonstrates that known physics does contain a resonant neutrino interaction scale many orders larger than ordinary MeV weak cross sections.

Classification: **G8_REAL_RESONANCE_POSITIVE_CONTROL_PASS**, but **SOLAR_APPLICATION_FAIL_KINEMATICS**.

## Control B — validated Li7 <-> Be7 narrow solar-line overlap
This is not a Breit-Wigner resonance. It is the already validated crossed ground-state transition sampled by the thermally broadened solar Be7 line.

Frozen iteration-0023 GS98+MSW authority:
- total Li7 rate `19.3488133336 SNU`;
- total energy moment `77.5070777600 SNU MeV`;
- Be7 line contribution `4.07166111 SNU`;
- Be7 line energy moment `3.51461158 SNU MeV`.

Derived fractions:
- event fraction = `0.210434667997` (~21.04%);
- energy-moment fraction = `0.045345685602` (~4.535%);
- event/energy fraction ratio = `4.64067673045`.

Thus narrow line/threshold matching is genuinely useful for event rate, but much less useful for harvested neutrino energy because the high-energy B8 continuum dominates the Li7 energy moment.

Classification: **NARROW_LINE_EVENT_GAIN_NOT_ENERGY_GAIN**.

## Control C — proposed H3-He3 Mössbauer antineutrinos
Literature proposes recoilless resonant capture near `18.6 keV` with an idealized peak cross section around `5e-32 cm^2`, much larger than ordinary same-energy weak cross sections. However solid-state broadening, lattice deformation and phonon/recoil-free-fraction issues prevent promotion to a validated material absorber.

Classification: **THEORY_POSITIVE / MATERIAL_REALIZATION_UNVALIDATED**.

## Hosted validation
Workflow run `34043513182`, job `101514377131`, artifact `9992391097`.
Raw log inspected:
- `6 passed in 0.02s`;
- benchmark values above reproduced;
- workflow conclusion SUCCESS.

## Scientific consequence
NMIR now has an explicit positive control proving that the search for a strong neutrino coupling is not conceptually empty: **known Standard-Model resonance physics can make neutrino interactions dramatically stronger when the center-of-mass energy hits a real intermediate state.**

The unresolved problem is therefore sharpened from

`Can neutrinos ever interact strongly?`

to

`Can a real or engineered resonance with sufficiently large entrance strength exist in the solar-neutrino energy domain, and can its integrated strength survive physical linewidth/source-overlap/material constraints?`

This is exactly the domain for the next G8 low-energy resonance design/search gate. No Glashow, Li7 or proposed Mössbauer gain is composed with any other NMIR gain.
