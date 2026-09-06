# NMIR iteration 0033 — subleading nuclear-current loophole gate

Date: 2026-09-06
Classification: **ONE_BODY_SUBLEADING_STRONG_NEGATIVE_SCOPED / TWO_BODY_DATA_DISTANCE_STRONG_NEGATIVE / GLOBAL_TWO_BODY_THEOREM OPEN**

## Prospective contract
`research/nuclear_current_loophole_prereg.md`, commit `da68f1d8f89aa11045f587aeec0332da62fdea2c`.

## Baseline
Iteration-0026 finite-q leading-current envelope:

`P_leading = 1.2056895107775174e-9 W/kg`.

This baseline is already deliberately loose: A<=300, Z_f<=119, E_nu<=20 MeV, a large frozen multipole factor, and 2000 W/m^2 neutrino-energy-flux stress input.

## Part A — full omitted one-body recoil/induced-current stress
The standard low-energy one-nucleon charged weak current adds axial charge, convection, weak magnetism and induced pseudoscalar terms to the leading vector charge + axial spin components.

Frozen controls:
- `p/M <= 1`;
- `q_max = 2 E_nu + m_e = 40.51099895 MeV`;
- `g_V=1`, `g_A=1.2754`, `g_V+g_M=4.706`;
- electron-channel pseudoscalar scale `m_e E0/m_pi^2`;
- triangle component count plus an extra factor-2 amplitude safety.

Raw omitted/leading component-amplitude ratio:

`0.9494073224324683`.

Frozen safe amplitude ratio:

`r_1b = 1.8988146448649366`.

Therefore

`P_1b = P_leading (1+r_1b)^2 = 1.0131561292246442e-8 W/kg`,

still a deficit

`9.870147069684981e7`

to 1 W/kg.

Classification: **ONE_BODY_SUBLEADING_STRONG_NEGATIVE_SCOPED**.

This closes recoil/convection/weak-magnetism/induced-pseudoscalar rescue inside the admitted one-nucleon SM current sector. It does not constrain genuine two-body/higher-body operators.

## Part B — genuine two-body distance to the bridge
Required extra amplitude ratio to turn the frozen leading envelope into 1 W/kg:

`r_bridge = sqrt(1/P_leading)-1 = 28798.321671367867`.

Literature-calibrated amplitude-scale anchors, deliberately not promoted to universal maxima:
- ordinary chiral two-body axial corrections in A<=10: 2–3%;
- suppressed 8Li/8B/8He GT cases: 20–30%;
- axial-charge meson-exchange excess from epsilon_exp=1.61: 0.61 relative excess.

Bridge gaps:
- versus 0.03: `959944.0557`;
- versus 0.30: `95994.40557`;
- versus 0.61: `47210.36340`.

Deliberately extreme aggregate amplitude stresses:
- `r=10` -> `1.4588843080e-7 W/kg`;
- `r=100` -> `1.2299238699e-5 W/kg`;
- `r=1000` -> `1.2081020955e-3 W/kg`.

Even a thousand-times-leading omitted amplitude does not reach 1 W/kg.

For a generic NLO amplitude `C (Q/Lambda)` with the deliberately large `Q/Lambda=0.5`, the bridge would require

`C = 57596.64334`.

This is an EFT-naturalness/breakdown diagnostic, not a theorem.

## Literature authority
- G. B. King et al., Phys. Rev. C 102, 025501 (2020), DOI 10.1103/PhysRevC.102.025501: two-body axial currents are typically 2–3% in the studied light-nucleus matrix elements, reaching 20–30% where the impulse-approximation GT matrix element is suppressed.
- E. K. Warburton, I. S. Towner, B. A. Brown, Phys. Rev. C 49, 824 (1994), DOI 10.1103/PhysRevC.49.824: axial-charge enhancement `epsilon_exp=1.61+/-0.03` in A~16 first-forbidden beta decay / muon capture.
- H. Krebs, Eur. Phys. J. A 56, 234 (2020), DOI 10.1140/epja/s10050-020-00230-9: systematic chiral-EFT nuclear currents through N3LO.
- Modern recoil-order beta-decay formalism: weak magnetism is typically a few-percent rate effect, while induced pseudoscalar is ~1e-3 of leading axial terms in electron beta decay; first-forbidden velocity-dependent terms can be important and therefore were not discarded in the one-body stress.

## Hosted validation
Workflow run `34042934477`, job `101512822458`, artifact `9992226798`.
Raw log inspected:
- `9 passed in 0.03s`;
- numerical benchmark emitted the values above;
- workflow conclusion SUCCESS.

## Scope conclusion
1. **One-body omitted SM current rescue: closed scoped.**
2. **Known two-body-current physics: quantitatively tens of thousands of amplitude factors short of the bridge.**
3. **Global correlation-independent two-body/higher-body theorem remains OPEN.**
4. No gain from this iteration is composed with resonance, gravity, structured matter or active media.
