# NMIR Research Roadmap

## Stage A — Baseline physics and normalization

Goal: establish a trusted Standard-Model reference layer.

### A1. Weak low-energy EFT
Derive charged-current and neutral-current amplitudes below the electroweak scale, including electron and nuclear targets.

### A2. CEvNS reference
Implement the `qR << 1` limit, nuclear form factors, recoil kinematics and loss of coherence.

### A3. Electromagnetic properties
Implement magnetic moment, electric dipole/millicharge/charge-radius/anapole structures with explicit separation between established SM radiative effects and BSM parameters.

### A4. Matter-induced evolution
Implement MSW-like vector potentials, polarized-medium axial potentials, magnetic spin evolution and periodic/Floquet matter profiles. These are state-control modules and are not counted as capture unless an inelastic energy sink is present.

Exit criterion: all modules reproduce literature limiting formulas and dimensional/scaling tests.

---

## Stage B — Universal medium response

Goal: replace a list of materials with a common response language.

Decompose the target response into at least:

- vector density response `S_VV(q,w)`;
- axial/spin response `S_AA(q,w)`;
- vector–axial interference;
- electromagnetic charge/current response;
- nuclear transition strength distributions;
- lattice/phonon response;
- magnon/spin-wave response;
- electronic band/interband response;
- superconducting quasiparticle/collective response.

Required checks:

- positivity of inclusive spectral functions;
- detailed balance where appropriate;
- Kramers–Kronig relations;
- f-sum and spin/density sum rules where available;
- kinematic support in `(q,w)` for solar/reactor/supernova/CNB neutrinos.

Exit criterion: a single numerical rate API can accept a neutrino kernel plus a medium response and return scattering rate and deposited-energy spectrum.

---

## Stage C — Standard-Model ceiling

Primary research question:

\[
\sup_{S\in\mathcal A_{\rm passive}}\frac{P_{\rm dep}}{A}
\]

for a specified incident neutrino spectrum, especially solar neutrinos.

The admissible set must respect known sum rules and realistic density/energy scales. We first seek an analytic bound, then test how closely explicit materials can approach it.

Possible scientific outcomes:

1. a useful no-go theorem for passive matter;
2. a previously overlooked response window with parametric enhancement;
3. a proof that only low-threshold detection improves, while total energy-transfer probability remains weak-interaction limited.

---

## Stage D — Engineered-medium search

Only after Stage C.

Candidate classes:

- spin-polarized and magnetically ordered targets;
- antiferromagnets, ferromagnets and spin liquids;
- superconductors and superfluids;
- resonant nuclear targets;
- periodic/graded matter profiles;
- driven/non-equilibrium media;
- hybrid structures combining state conversion and an inelastic sink.

For every candidate compute separately:

`state conversion`, `total interaction probability`, `mean deposited energy`, `deposited power`, `required external preparation power`.

A driven medium must be rejected as an energy source if the output is merely conversion of externally supplied drive energy.

---

## Stage E — BSM residual reconstruction

If the SM ceiling is too low, infer the minimal new operator needed to obtain a target interaction response.

Explore scalar, pseudoscalar, vector, axial-vector, tensor and electromagnetic portals. For light mediators retain full propagator dependence rather than prematurely using a contact interaction.

Inverse problem:

\[
\mathcal O_{\rm BSM}^{\rm min}=\arg\min_{\mathcal O}\{\text{new structure}\}
\]

subject to achieving a specified enhancement and all known bounds.

---

## Stage F — Global constraint funnel

A BSM candidate is not viable until checked against, as applicable:

- neutrino–electron scattering;
- CEvNS and reactor measurements;
- oscillation/matter-effect data;
- invisible/rare particle decays;
- stellar cooling and plasmon processes;
- supernova transport/energy loss;
- BBN and CMB;
- laboratory fifth-force/electromagnetic constraints;
- consistency with neutrino mass generation and gauge symmetry.

---

## Publication targets

Potential Paper 1: **A response-function framework and Standard-Model bounds for neutrino energy deposition in organized matter.**

Potential Paper 2: **Collective and resonant neutrino coupling in quantum materials: which enhancements survive sum rules and kinematics?**

Potential Paper 3 (conditional): **Model-agnostic reconstruction of new neutrino–matter interactions required for macroscopic opacity.**

No paper title or claim is considered frozen before the corresponding gate passes.
