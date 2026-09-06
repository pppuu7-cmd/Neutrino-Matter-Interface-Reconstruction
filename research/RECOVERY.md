# NMIR Recovery / Source-of-Truth State

Last reconciled: 2026-09-06 Europe/Stockholm
Program: Neutrino–Matter Interface Reconstruction (NMIR)
Repository: `pppuu7-cmd/Neutrino-Matter-Interface-Reconstruction`

## Mission

Reconstruct the most general low-energy neutrino↔matter interface, separate state control from detection and irreversible energy deposition, establish Standard-Model bounds, and only then identify any BSM coupling structures needed to exceed those bounds.

Four organizing principles are now frozen:

1. **response reconstruction** — optimize physically admissible material response functions rather than guess materials;
2. **production ↔ absorption / crossed-channel reconstruction** — use known weak production/decay processes to infer inverse capture channels;
3. **gravitational focusing** — test whether spacetime curvature can multiply the local neutrino flux before microscopic capture;
4. **staggered-layer response engineering** — test whether shifted atomic/isotopic layers can redistribute or enhance useful neutrino response without confusing projected geometric coverage with weak-interaction opacity.

## Central observable

For incident differential neutrino flux `Phi(E)`, define deposited power per illuminated area

\[
\frac{P_{\rm dep}}{A}=\int dE_\nu\,\Phi(E_\nu)\int d\omega\;\omega\,\frac{dP_{\rm int}}{d\omega}(E_\nu),
\]

or for a slab with effective optical depth `tau(E)` and mean deposited fraction `eta_dep(E)`:

\[
\frac{P_{\rm dep}}{A}=\int dE_\nu\,\Phi(E_\nu)E_\nu\,\eta_{\rm dep}(E_\nu)\,[1-e^{-\tau(E_\nu)}].
\]

With gravitational magnification `mu(E,x)`, the microscopic capture branch becomes

\[
R=N_T\int dE\,\mu(E,\mathbf x)\Phi_\nu(E)\sigma_{\rm cap}(E),
\]

\[
P_{\rm dep}=N_T\int dE\,\mu(E,\mathbf x)\Phi_\nu(E)\sigma_{\rm cap}(E)E_{\rm dep}(E).
\]

The useful-capture problem therefore depends on the product of **flux magnification × capture probability × deposited-energy fraction**.

## Response formulation

For weak/EM/BSM currents labeled by indices `a,b`, use the inclusive many-body rate structure

\[
\Gamma \propto \int d^3q\,d\omega\;L_{ab}(q,\omega)S^{ab}(q,\omega),
\]

with `S^{ab}` the dynamic structure factor and/or corresponding retarded susceptibility. The admissible response space must obey positivity, detailed balance where applicable, Kramers–Kronig/causality, conservation laws, sum rules, and stability.

For an equilibrium Hermitian response, positive/negative frequency branches are related schematically by

\[
S(-\omega)=e^{-\beta\omega}S(+\omega),
\]

so emission and absorption probe the same microscopic spectral information in opposite directions, modulo phase space and occupation factors.

## Beta-decay ↔ capture reconstruction

For unpolarized beta transitions, the beta-decay and crossed neutrino-capture process use the same invariant weak amplitude. In the long-wavelength regime, measured beta-decay observables can therefore rank inverse capture strength. For allowed/superallowed cases, in the source natural-unit convention,

\[
\sigma_{\rm NCB}v_\nu
=2\pi^2\ln2\,\frac{p_eE_eF(Z,E_e)}{ft_{1/2}}.
\]

NMIR will not deploy this numerically until one published benchmark is reproduced with explicit SI/unit conversion and corrections.

## Gravitational focusing baseline

For an ultrarelativistic neutrino in the weak Schwarzschild limit,

\[
\alpha(b)\simeq\frac{4GM}{bc^2},
\qquad
f\simeq\frac{b^2c^2}{4GM}.
\]

The solar-limb benchmark is

\[
f(R_\odot)\simeq 547.741\ {\rm AU}.
\]

Because neutrinos can traverse the solar interior, a transparent-Sun extended-mass lens can focus distant-source neutrinos much closer; published calculations give a minimum focal distance near `23.5 ± 0.1 AU`. This becomes the first extended-lens benchmark.

**Critical distinction:** the Sun is not an ordinary downstream lens for its own solar neutrinos because the source and lens coincide. Focusing solar neutrinos requires a separate mass distribution between Sun and receiver.

Gravitational lensing preserves collisionless phase-space density / surface brightness. A formal point-source caustic divergence is not infinite usable power. Finite source size, detector size, lens structure, wave effects and alignment must regularize every magnification claim.

## Staggered-layer baseline

For scatterers at positions `r_j`, the elastic lattice amplitude contains

\[
F(\mathbf q)=\sum_j e^{i\mathbf q\cdot\mathbf r_j}.
\]

For shifted planes, layer registry changes the phase factors and can therefore move constructive/destructive peaks. This is physically different from simple projected hard-sphere coverage.

A geometric sanity check with `R_N=5 fm` and transverse lattice spacing `a=3 Angstrom` gives

\[
\pi R_N^2/a^2\simeq 8.73\times10^{-10}
\]

per layer, requiring `~1.15e9` ideally non-overlapping shifted layers merely for unity **geometric nuclear projection**. Real weak opacity is vastly smaller than this geometric analogy.

Published crystal sum-rule work in the local-potential Born regime finds total effects linear in scatterer count despite directional coherent peaks. NMIR therefore rejects simple projected coverage or directional `N^2` peaks as evidence of total opacity enhancement until an integrated-strength loophole is explicitly demonstrated.

## Research gates

| Gate | Question | Status |
|---|---|---|
| G0 | Do all normalizations reproduce known weak/CEvNS limiting scales? | PARTIAL — baseline code/tests implemented; CI active |
| G1 | Can static coherence increase total interaction probability beyond ordinary nuclear coherence? | PARTIAL NEGATIVE — naive whole-crystal elastic `N^2` branch excluded under local-potential/Born sum-rule assumptions |
| G2 | What density/spin/current response channels can deposit energy into phonons, magnons, quasiparticles or nuclear excitations? | OPEN — vector/axial response basis seeded |
| G3 | What is the maximum SM deposited power from solar neutrinos in passive organized matter? | OPEN — primary target; first SNU→W/kg normalization added |
| G4 | Can polarization, resonances, periodic media or nonequilibrium preparation increase useful deposition parametrically? | OPEN — polarized axial/spin + resonant nuclear branches prioritized |
| G5 | If SM is insufficient, what minimal BSM operator/mediator structure is required? | LOCKED until G3 |
| G6 | Does any BSM candidate survive laboratory, stellar, supernova and cosmological constraints? | LOCKED until G5 |
| G7 | Can a neutrino-production process identify an unusually strong inverse/crossed absorption channel? | OPEN — quantitative `ft`-based reconstruction route established |
| G8 | Can resonant peak enhancement overcome the available neutrino flux bandwidth without violating integrated-strength bounds? | OPEN — next key resonance gate |
| G9 | Can gravitational lensing provide a finite, useful neutrino flux gain at an absorber? | OPEN — weak-lens benchmark implemented; transparent-lens/finite-source stages next |
| G10 | Can staggered atomic/isotopic layers increase flux-integrated neutrino capture/deposition at fixed mass column? | OPEN — naive geometric opacity disfavored; structure-factor/multi-isotope variants retained |

## Iteration-1 benchmark results

1. **Xe-132 ideal CEvNS benchmark, 1 MeV:** `Q_W ≈ 75.5311`, `sigma ≈ 2.405e-41 cm^2`.
2. **Liquid-Xe-like mean free path:** for density `2.94 g/cm^3`, `lambda ≈ 3.08e16 m` in the same ideal low-q benchmark.
3. **Optical-depth-one mass column:** `Sigma_tau=1 ≈ 9.07e18 g/cm^2` at 1 MeV in that benchmark.
4. **Minimal Dirac magnetic moment benchmark:** `mu_nu ≈ 1.6e-20 mu_B` for `m_nu=0.05 eV`.
5. **Direct magnetic precession scale:** first ideal maximum over `L=1 m` requires `B ≈ 3.35e17 T`; direct laboratory magnetic coupling through the minimal moment is therefore a baseline no-go route.
6. **Static crystal coherence gate:** published sum-rule work finds total force/scattering effect linear in scatterer number for local-potential Born scattering, despite directional coherent peaks. NMIR therefore does not treat ordinary whole-crystal coherence as a macroscopic-opacity mechanism.
7. **Promising branch retained:** external field → polarized/magnetically ordered medium → axial/spin response `S_AA(q,w)` → inelastic magnon/spin/nuclear excitation.

## Iteration-2 results: production↔absorption duality

1. Weak-production mechanisms have physically meaningful inverse/crossed channels; inverse beta decay is the canonical benchmark.
2. Electron capture / bound-state beta decay suggest narrow two-body source lines whose inverse nuclear transitions can, in principle, be resonantly enhanced.
3. Historical recoilless/Mössbauer-neutrino proposals establish that this is not a category error; practical problems are recoil-free fraction, lattice deformation, environmental broadening and source/absorber line overlap.
4. A narrow resonance can strongly increase peak cross section but cannot be counted as broadband opacity without tracking integrated line strength.
5. The observed Glashow resonance at ~6.3 PeV is an empirical high-energy example of dramatically resonant neutrino interaction at a matched center-of-mass energy. It is proof-of-principle, not a solar-energy candidate.
6. **Energy-deposition triage:** a one-magnon event at `1 meV` struck by a `1 MeV` neutrino deposits only `1e-9` of incident energy. Low-energy collective modes remain interesting for detection but are disadvantaged for bulk energy capture.
7. Charged-current/resonant nuclear absorption is promoted to co-primary status because a successful event can leave keV–MeV in charged particles/nuclear/atomic excitations.

## Iteration-3 results: measured decay → predicted capture

1. Published neutrino-capture theory explicitly relates beta-decay observables to neutrino capture on the corresponding beta-decaying nucleus; for allowed/superallowed transitions the measured `ft` value is a direct ranking variable.
2. **Real-world production/capture pairs:** Ar-37 electron capture ↔ nu_e capture on Cl-37; Ge-71 electron capture ↔ nu_e capture on Ga-71.
3. Capture thresholds used as benchmarks: `Cl-37 ~0.814 MeV`, `Ga-71 ~0.233 MeV`.
4. A machine-readable seed catalog includes Cl-37/Ar-37, Ga-71/Ge-71, H-3/He-3 and Ho-163/Dy-163.
5. The combined historical gallium solar capture rate `66.1 SNU` corresponds, for isotopically pure Ga-71, to approximately `5.61e-10 captures/s/kg`.
6. Assigning an optimistic reference deposition of exactly `1 MeV` per successful capture gives only `~8.99e-23 W/kg`.
7. Reaching `1 W/kg` from that normalization requires an enhancement of approximately `1.11e22`.
8. The energy-harvesting problem therefore requires a **parametric change** in opacity×deposition, not incremental detector optimization.

## Iteration-4 results: gravitational neutrino focusing

1. Gravitational focusing is a physically legitimate multiplicative branch: local capture scales with finite magnification `mu_nu`.
2. Weak-field code reproduces the solar-limb focal-distance benchmark `~547.741 AU`.
3. Neutrino transparency of stellar interiors opens extended-lens geometries unavailable to photons; transparent-Sun literature gives `~23.5 AU` minimum focal distance for distant-source radiation able to cross the core.
4. The Sun cannot focus its own emitted solar neutrinos in the required source→separate-lens→receiver geometry; a separate lens is needed for solar neutrinos.
5. Point-caustic infinite magnification is rejected as unphysical. Finite source/receiver size and Liouville phase-space conservation are mandatory gates.
6. Gravitational focusing alone cannot bridge the current `~1e22` Ga energy-gap normalization unless an implausibly enormous finite magnification were available; its realistic role is to multiply a stronger microscopic capture mechanism if NMIR finds one.
7. Candidate lenses to test: planet, transparent star, white dwarf, neutron star, black hole, binary/compound caustic lens, and purely theoretical engineered mass distributions.

## Iteration-5 results: staggered-layer neutrino metamaterial

1. Shifted atomic planes are physically realizable; ordinary close-packed solids already implement AB/ABC registries.
2. Geometric line-of-sight coverage by atoms is not neutrino opacity. Neutrinos are not hard projectiles excluded by electron-cloud gaps.
3. The correct elastic quantity is the structure factor `F(q)`; layer shifts can create constructive/destructive directions and move reciprocal-lattice peaks.
4. Toy code verifies both fully coherent and destructive limits for staggered planes.
5. With `R_N=5 fm` and `a=3 Angstrom`, the naive nuclear hard-disk projected fraction is `8.73e-10` per layer and requires `~1.15e9` perfectly complementary layers for unity projected nuclear coverage; real weak interaction probabilities are much smaller still.
6. Published sum-rule constraints imply that ordinary coherent directional enhancement does not automatically increase total integrated interaction strength beyond linear-N scaling.
7. A historical magnetic-neutrino crystal calculation did find a configuration-dependent `N^(1/3)` enhancement for that special channel, but it remained experimentally negligible; NMIR will treat this as a concrete benchmark/possible loophole to reproduce.
8. **Promoted variant:** staggered **multi-isotope resonant stacks**, where successive layers use different capture thresholds/resonances and possibly different polarization, to form a spectral-response comb across the solar-neutrino spectrum.

## Initial physical facts to preserve

1. CEvNS provides a real coherence enhancement at the nuclear level; near `qR << 1`, the weak charge is approximately `Q_W = N - (1-4 sin^2 theta_W) Z`, and the total low-energy cross section scales approximately as `Q_W^2 E_nu^2`.
2. A low detector threshold is not equivalent to a larger total cross section.
3. Flavor/spin conversion can control the neutrino state without extracting substantial energy.
4. A static macroscopic crystal does not automatically provide an `N^2` total-rate enhancement over all scattering centers.
5. Electromagnetic neutrino form factors and BSM light mediators are allowed branches but must not bypass the SM baseline.
6. Production↔absorption/crossing identifies candidate matrix elements but does not imply efficient inverse capture.
7. Peak resonant cross section and flux-integrated capture are distinct observables.
8. Exact time reversal and a crossed weak reaction are not always the same external-particle process; NMIR must classify them correctly.
9. Gravitational magnification and microscopic absorption are multiplicative, not interchangeable.
10. Collisionless lensing cannot create arbitrary phase-space brightness; all caustic gains must be finite-source regularized.
11. Projected atomic coverage and weak-interaction opacity are fundamentally different quantities.
12. Any staggered-lattice claim must report both directional structure-factor gain and flux/angle/energy-integrated interaction/deposition gain.

## Current repository components

- `README.md` — scientific charter and gates.
- `research/ROADMAP.md` — staged program.
- `research/LITERATURE_LEDGER.md` — provenance ledger including inverse-reaction and gravitational-lensing sources.
- `data/inverse_transition_seed.csv` — first machine-readable inverse/crossed transition catalog.
- `theory/OPERATOR_BASIS.md` — weak/EM/NSI/light-mediator response basis.
- `theory/PRODUCTION_ABSORPTION_DUALITY.md` — inverse-production/crossing framework.
- `theory/BETA_DECAY_INVERSE_CAPTURE.md` — measured beta-decay `ft` → capture-strength reconstruction.
- `theory/SPIN_MAGNON_RESPONSE.md` — axial spin/magnon branch.
- `theory/GRAVITATIONAL_NEUTRINO_FOCUSING.md` — gravitational-lens formalism, gates and combined capture objective.
- `theory/STAGGERED_LAYER_NEUTRINO_METAMATERIAL.md` — shifted-layer structure-factor and multi-isotope metamaterial branch.
- `src/nmir/baseline.py` — CEvNS, mean-free-path and magnetic-precession benchmarks.
- `src/nmir/duality.py` — detailed-balance, deposited-fraction and resonance-line utilities.
- `src/nmir/capture_metrics.py` — SNU→captures/s/kg→W/kg normalization metrics.
- `src/nmir/gravity_focusing.py` — weak gravitational deflection, focal-distance and point-lens magnification benchmarks.
- `src/nmir/staggered_lattice.py` — staggered-plane geometry and elastic structure-factor toy model.
- automated tests include baseline, duality, capture metrics, gravity focusing and staggered-lattice gates.
- `.github/workflows/ci.yml` — automated tests.
- `research/iterations/0001_initial_gates.md` through `0005_staggered_layer_metamaterial.md` — chronological research record.

## Current maturity estimate

- Problem formulation: 56%
- Operator inventory: 30%
- Production↔absorption formalism: 28%
- Many-body response taxonomy: 27%
- Numerical framework: 31%
- Constraint/literature ledger: 27%
- Inverse-transition catalog: 8%
- Standard-Model ceiling: 8%
- Engineered-medium scan: 12%
- Gravitational focusing branch: 8%
- Staggered-layer branch: 10%
- BSM residual search: 0%

Overall NMIR research maturity (audit estimate): **~18%**.

## Immediate next iteration

1. Reproduce one published allowed-transition neutrino-capture cross section from a measured `ft` value with full SI conversion.
2. Reproduce Cl-37 and Ga-71 benchmark capture cross sections/rates from primary literature.
3. Expand the inverse-transition catalog from evaluated nuclear data.
4. Rank known transitions by both capture-event rate and deposited-power objective.
5. Derive a Breit–Wigner / integrated-strength resonance gate with source/absorber linewidth mismatch.
6. Freeze a primary-source solar-neutrino spectrum/flux dataset and compute flux overlap for every candidate transition.
7. Implement a sum-rule-preserving toy `S_AA(q,w)` with magnon + continuum spectral weight.
8. Implement a transparent spherical gravitational lens and reproduce the published `23.5 AU` solar minimum-focal-length benchmark.
9. Add finite-source magnification and couple `mu(E)` directly to the capture/deposition ranking.
10. For SLNM, map solar-neutrino momentum transfers against reciprocal-lattice scales from Angstrom lattices through nm/moire superlattices.
11. Verify angle/energy-integrated linear-N behavior in the staggered toy and add Debye-Waller disorder/temperature suppression.
12. Couple layer-by-layer isotope choice, spacing and shift to the inverse-transition optimizer to test the multi-isotope spectral-comb concept.
