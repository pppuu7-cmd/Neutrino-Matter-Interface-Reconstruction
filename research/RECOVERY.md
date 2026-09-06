# NMIR Recovery / Source-of-Truth State

Last reconciled: 2026-09-06 Europe/Stockholm
Program: Neutrino–Matter Interface Reconstruction (NMIR)
Repository: `pppuu7-cmd/Neutrino-Matter-Interface-Reconstruction`

## Mission

Reconstruct the most general low-energy neutrino↔matter interface, separate state control from detection and irreversible energy deposition, establish Standard-Model bounds, and only then identify any BSM coupling structures needed to exceed those bounds.

A second organizing principle is now frozen:

**production ↔ absorption / crossed-channel reconstruction** — catalog how neutrinos are produced by weak processes, construct the corresponding inverse/crossed channels, and test whether resonance, threshold or medium engineering can make any channel unusually absorptive.

## Central observable

For incident differential neutrino flux `Phi(E)`, define deposited power per illuminated area

\[
\frac{P_{\rm dep}}{A}=\int dE_\nu\,\Phi(E_\nu)\int d\omega\;\omega\,\frac{dP_{\rm int}}{d\omega}(E_\nu),
\]

or for a slab with effective optical depth `tau(E)` and mean deposited fraction `eta_dep(E)`:

\[
\frac{P_{\rm dep}}{A}=\int dE_\nu\,\Phi(E_\nu)E_\nu\,\eta_{\rm dep}(E_\nu)\,[1-e^{-\tau(E_\nu)}].
\]

The useful-capture problem is therefore not solved merely by making an excitation detectable. Both `tau` and `eta_dep` matter.

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

A major NMIR route is now frozen from published neutrino-capture theory: for unpolarized beta transitions, the beta-decay and crossed neutrino-capture process use the same invariant weak amplitude.

In the long-wavelength regime the capture rate can be related to beta-decay observables. For allowed/superallowed cases, in the source natural-unit convention,

\[
\sigma_{\rm NCB}v_\nu
=2\pi^2\ln2\,\frac{p_eE_eF(Z,E_e)}{ft_{1/2}}.
\]

NMIR will not deploy this numerically until one published benchmark is reproduced with explicit SI/unit conversion and corrections. The significance is methodological: measured `ft` values can be used to scan known nuclei for intrinsically strong inverse/crossed neutrino-capture channels.

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
2. **Real-world production/capture pairs:** Ar-37 electron capture ↔ nu_e capture on Cl-37; Ge-71 electron capture ↔ nu_e capture on Ga-71. These are not hypothetical: they underlie classic solar-neutrino radiochemical detection.
3. Capture thresholds used as benchmarks: `Cl-37 ~0.814 MeV`, `Ga-71 ~0.233 MeV`.
4. A machine-readable seed catalog now includes Cl-37/Ar-37, Ga-71/Ge-71, H-3/He-3 and Ho-163/Dy-163.
5. The combined historical gallium solar capture rate `66.1 SNU` corresponds, for isotopically pure Ga-71, to approximately `5.61e-10 captures/s/kg`.
6. If each successful capture were assigned an optimistic reference deposition of exactly `1 MeV`, that rate corresponds to only `~8.99e-23 W/kg`.
7. Reaching `1 W/kg` from that normalization requires an enhancement of approximately `1.11e22`. This is a scale benchmark, not a claim about actual mean Ga capture deposition energy.
8. The energy-harvesting problem therefore requires a **parametric change** in opacity×deposition, not incremental detector optimization.

## Initial physical facts to preserve

1. CEvNS provides a real coherence enhancement at the nuclear level; near `qR << 1`, the weak charge is approximately `Q_W = N - (1-4 sin^2 theta_W) Z`, and the total low-energy cross section scales approximately as `Q_W^2 E_nu^2`.
2. A low detector threshold is not equivalent to a larger total cross section.
3. Flavor/spin conversion (MSW, magnetic precession, parametric conversion) can control the neutrino state without extracting substantial energy.
4. A static macroscopic crystal does not automatically provide an `N^2` total-rate enhancement over all scattering centers; any claimed macroscopic coherence must pass momentum-transfer, phase-space and sum-rule checks.
5. Electromagnetic neutrino form factors and BSM light mediators are allowed branches of the reconstruction, but they are constrained and must not be used to bypass the Standard-Model baseline.
6. Production↔absorption/crossing identifies candidate matrix elements, but does **not** imply that an inverse process is efficient: threshold, linewidth, recoil, phase space and integrated spectral strength remain mandatory gates.
7. Peak resonant cross section and flux-integrated capture are distinct observables.
8. Exact time reversal and a crossed weak reaction are not always the same external-particle process. NMIR must classify both correctly rather than use informal “reverse” language in final physics claims.

## Current repository components

- `README.md` — scientific charter and gates.
- `research/ROADMAP.md` — staged program.
- `research/LITERATURE_LEDGER.md` — provenance/constraint ledger including inverse-reaction, `ft` reconstruction and resonant-capture sources.
- `data/inverse_transition_seed.csv` — first machine-readable inverse/crossed transition catalog.
- `theory/OPERATOR_BASIS.md` — initial weak/EM/NSI/light-mediator response basis.
- `theory/PRODUCTION_ABSORPTION_DUALITY.md` — inverse-production/crossing framework and resonance gates.
- `theory/BETA_DECAY_INVERSE_CAPTURE.md` — measured beta-decay `ft` → capture-strength reconstruction logic.
- `theory/SPIN_MAGNON_RESPONSE.md` — axial spin/magnon branch and energy-deposition triage.
- `src/nmir/baseline.py` — CEvNS, mean-free-path and magnetic-precession benchmarks.
- `src/nmir/duality.py` — detailed-balance, deposited-fraction and normalized resonance-line utilities.
- `src/nmir/capture_metrics.py` — SNU→captures/s/kg→W/kg normalization metrics.
- `tests/test_baseline.py` — baseline scaling/normalization tests.
- `tests/test_duality.py` — duality/line-shape/deposition diagnostics.
- `tests/test_capture_metrics.py` — radiochemical capture/power normalization tests.
- `.github/workflows/ci.yml` — automated tests.
- `research/iterations/0001_initial_gates.md` — initial physical gates.
- `research/iterations/0002_inverse_production_and_spin_response.md` — inverse-production branch and spin-response triage.
- `research/iterations/0003_decay_to_capture_reconstruction.md` — measured-decay reconstruction and energy-gap benchmark.

## Current maturity estimate

- Problem formulation: 50%
- Operator inventory: 28%
- Production↔absorption formalism: 28%
- Many-body response taxonomy: 22%
- Numerical framework: 24%
- Constraint/literature ledger: 22%
- Inverse-transition catalog: 8%
- Standard-Model ceiling: 7%
- Engineered-medium scan: 5%
- BSM residual search: 0%

Overall NMIR research maturity (audit estimate): **~15%**.

## Immediate next iteration

1. Reproduce one published allowed-transition neutrino-capture cross section from a measured `ft` value with full SI conversion.
2. Reproduce Cl-37 and Ga-71 benchmark capture cross sections/rates from primary literature.
3. Expand `inverse_transition_seed.csv` from evaluated nuclear data rather than hand-entered candidates.
4. Rank known transitions by both capture-event rate and deposited-power objective.
5. Derive a Breit–Wigner / integrated-strength resonance gate and explicitly include source/absorber linewidth mismatch.
6. Freeze a primary-source solar-neutrino spectrum/flux dataset and compute flux overlap for every candidate transition.
7. In parallel implement a sum-rule-preserving toy `S_AA(q,w)` with magnon + continuum spectral weight, comparing event-count and deposited-power objectives.
