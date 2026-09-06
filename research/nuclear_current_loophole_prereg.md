# NMIR preregistration — subleading nuclear-current loophole gate

Date: 2026-09-06
Gate: G3 full nuclear-current loopholes after iteration 0032
Status at preregistration: OPEN

## Question
Can omitted Standard-Model nuclear weak-current pieces at solar-neutrino energies bridge the iteration-0026 finite-q leading-current power envelope to 1 W/kg?

Authority baseline is `finite_q_leading_multipole_envelope()` from iteration 0026. No post-result retuning of the criteria below is allowed.

## Scope
- charged-current solar-neutrino capture / inelastic weak response;
- `E_nu <= 20 MeV`, `A <= 300`, `Z_f <= 119`;
- Standard Model only;
- neutrino-supplied deposited power only;
- resonance/source-overlap and engineered many-body gains remain separate gates.

## Part A — one-body recoil/induced-current cap
Use the standard nucleon charged weak current decomposed into vector, axial, weak-magnetism and induced-pseudoscalar form factors. In the nonrelativistic reduction the omitted one-body pieces relative to iteration-0026 leading vector charge + axial spin are:
- axial charge `A0 ~ g_A sigma.p/M`;
- convection current `V ~ g_V p/M`;
- weak magnetism `~ (g_V+g_M) sigma x q /(2M)`;
- induced pseudoscalar.

Frozen conservative controls:
- `p/M <= 1` as the edge of the admitted nucleonic/nonrelativistic sector (far more generous than ordinary nuclear Fermi motion);
- zero-threshold kinematics gives `|q| <= E_nu + p_e <= 2 E_nu + m_e`, hence use `q_max = 40.51099895 MeV`;
- `g_V=1`, `g_A=1.2754`, anomalous isovector weak-magnetism coefficient `g_M=3.706`, so `g_V+g_M=4.706`;
- induced-pseudoscalar electron-channel scale is tracked with the conservative beta-decay estimate `m_e E0/m_pi^2`, with `E0=20+m_e MeV`;
- use a triangle component count: leading coefficient scale `C_LO = g_V + 3 g_A`; omitted scale `C_NLO = g_A + 3 g_V + 3(g_V+g_M) q_max/(2M) + 3 g_A m_e E0/m_pi^2`;
- multiply the ratio `C_NLO/C_LO` by an extra frozen safety factor 2 before squaring the total amplitude.

Define `r_1b = 2 C_NLO/C_LO` and power stress `P_1b = P_leading (1+r_1b)^2`.

Prospective criterion:
- `ONE_BODY_SUBLEADING_STRONG_NEGATIVE_SCOPED` if `P_1b < 1e-6 W/kg`.

This is scoped to the admitted one-nucleon current and does not bound genuine two-body/higher-body operators.

## Part B — two-body/current empirical-distance diagnostic
Do NOT promote calculated corrections in selected nuclei into a universal theorem.

Frozen literature anchors:
1. King et al., Phys. Rev. C 102, 025501 (2020), DOI 10.1103/PhysRevC.102.025501: chiral two-body axial currents contribute about 2–3% to most A<=10 weak-transition matrix elements, with 20–30% corrections in suppressed 8Li/8B/8He cases.
2. Warburton, Towner & Brown, Phys. Rev. C 49, 824 (1994), DOI 10.1103/PhysRevC.49.824: first-forbidden axial-charge enhancement factor `epsilon_exp = 1.61 +/- 0.03`; interpret the central excess over impulse approximation as a 0.61 amplitude-scale anchor, not as a universal maximum.
3. Hayen et al./modern recoil-order beta-decay formalism and the 2023 PTEP completion: weak magnetism is typically a few-percent rate correction; induced pseudoscalar in electron beta decay is ~1e-3 relative to leading axial terms; velocity-dependent currents can be important in first-forbidden channels.
4. Krebs, Eur. Phys. J. A 56, 234 (2020), DOI 10.1140/epja/s10050-020-00230-9: nuclear vector/axial currents through N3LO; exchange electroweak currents are systematically subleading and must be consistently regularized.

Define the amplitude needed to bridge the leading finite-q power envelope to 1 W/kg:
`r_bridge = sqrt(1/P_leading) - 1`.

Record gaps `r_bridge/r_anchor` for 0.03, 0.30 and 0.61. These are evidence-distance diagnostics only.

Also record deliberately extreme aggregate omitted-current amplitude stresses `r=10,100,1000` via `P=P_leading(1+r)^2`. These are stress tests, not physical bounds.

Prospective classification:
- `TWO_BODY_DATA_DISTANCE_STRONG_NEGATIVE` if `r_bridge/0.61 > 1e4`;
- nevertheless keep `GLOBAL_TWO_BODY_THEOREM = OPEN` unless a correlation-independent operator/sum-rule bound is separately derived.

## EFT naturalness diagnostic
Because exchange electroweak currents first appear subleading to dominant one-nucleon pieces, record the dimensionless coefficient that would be required if a generic NLO amplitude scaled as `C*(Q/Lambda)` for conservative `Q/Lambda = 0.5`:
`C_required = r_bridge/0.5`.
This is only a breakdown/naturalness diagnostic, not a theorem.

## Pass/fail discipline
- Never multiply this gate with resonance, gravity, material, or focusing gains unless those independently pass F0–F8.
- Suppressed leading transitions may have large *relative* two-body corrections; the relevant question here is absolute integrated strength/power.
- If Part A passes but Part B lacks a theorem, update G3 as `one-body subleading CLOSED scoped; genuine two-body OPEN but quantitatively distant from bridge in known calculations`.
