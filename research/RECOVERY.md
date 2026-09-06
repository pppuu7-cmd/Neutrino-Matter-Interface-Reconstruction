# NMIR Recovery / Source-of-Truth State

Last reconciled: 2026-09-06 Europe/Stockholm
Program: Neutrino–Matter Interface Reconstruction (NMIR)
Repository: `pppuu7-cmd/Neutrino-Matter-Interface-Reconstruction`

## Mission

Reconstruct the most general low-energy neutrino↔matter interface, separate state control from detection and irreversible energy deposition, establish Standard-Model bounds, and only then identify any BSM coupling structures needed to exceed those bounds.

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

with `S^{ab}` the dynamic structure factor and/or the corresponding retarded susceptibility. The admissible response space must obey positivity, detailed-balance where applicable, Kramers–Kronig/causality, conservation laws, sum rules, and stability.

## Research gates

| Gate | Question | Status |
|---|---|---|
| G0 | Do all normalizations reproduce known weak/CEvNS limiting scales? | PARTIAL — baseline code/tests implemented; GitHub CI queued |
| G1 | Can static coherence increase total interaction probability beyond ordinary nuclear coherence? | PARTIAL NEGATIVE — naive whole-crystal elastic `N^2` branch excluded under local-potential/Born sum-rule assumptions |
| G2 | What density/spin/current response channels can deposit energy into phonons, magnons, quasiparticles or nuclear excitations? | OPEN — operator/response basis seeded |
| G3 | What is the maximum SM deposited power from solar neutrinos in passive organized matter? | OPEN — primary target |
| G4 | Can polarization, resonances, periodic media or nonequilibrium preparation increase the useful deposition fraction parametrically? | OPEN — polarized axial/spin branch prioritized |
| G5 | If SM is insufficient, what minimal BSM operator/mediator structure is required? | LOCKED until G3 |
| G6 | Does any BSM candidate survive laboratory, stellar, supernova and cosmological constraints? | LOCKED until G5 |

## Iteration-1 benchmark results

1. **Xe-132 ideal CEvNS benchmark, 1 MeV:** `Q_W ≈ 75.5311`, `sigma ≈ 2.405e-41 cm^2`.
2. **Liquid-Xe-like mean free path:** for density `2.94 g/cm^3`, `lambda ≈ 3.08e16 m` in the same ideal low-q benchmark.
3. **Optical-depth-one mass column:** `Sigma_tau=1 ≈ 9.07e18 g/cm^2` at 1 MeV in that benchmark.
4. **Minimal Dirac magnetic moment benchmark:** `mu_nu ≈ 1.6e-20 mu_B` for `m_nu=0.05 eV`.
5. **Direct magnetic precession scale:** first ideal maximum over `L=1 m` requires `B ≈ 3.35e17 T`; direct laboratory magnetic coupling through the minimal moment is therefore a baseline no-go route.
6. **Static crystal coherence gate:** published sum-rule work finds total force/scattering effect linear in scatterer number for local-potential Born scattering, despite directional coherent peaks. NMIR therefore does not treat ordinary whole-crystal coherence as a macroscopic-opacity mechanism.
7. **Promising branch retained:** external field → polarized/magnetically ordered medium → axial/spin response `S_AA(q,w)` → inelastic magnon/spin/nuclear excitation.

## Initial physical facts to preserve

1. CEvNS provides a real coherence enhancement at the nuclear level; near `qR << 1`, the weak charge is approximately `Q_W = N - (1-4 sin^2 theta_W) Z`, and the total low-energy cross section scales approximately as `Q_W^2 E_nu^2`.
2. A low detector threshold is not equivalent to a larger total cross section.
3. Flavor/spin conversion (MSW, magnetic precession, parametric conversion) can control the neutrino state without extracting substantial energy.
4. A static macroscopic crystal does not automatically provide an `N^2` total-rate enhancement over all scattering centers; any claimed macroscopic coherence must pass momentum-transfer, phase-space and sum-rule checks.
5. Electromagnetic neutrino form factors and BSM light mediators are allowed branches of the reconstruction, but they are constrained and must not be used to bypass the Standard-Model baseline.

## Current repository components

- `README.md` — scientific charter and gates.
- `research/ROADMAP.md` — staged program.
- `research/LITERATURE_LEDGER.md` — provenance/constraint seed ledger.
- `theory/OPERATOR_BASIS.md` — initial weak/EM/NSI/light-mediator response basis.
- `src/nmir/baseline.py` — CEvNS, mean-free-path and magnetic-precession benchmarks.
- `tests/test_baseline.py` — scaling and numerical normalization tests.
- `.github/workflows/ci.yml` — automated baseline tests.
- `research/iterations/0001_initial_gates.md` — first physical-gate record.

## Current maturity estimate

- Problem formulation: 35%
- Operator inventory: 20%
- Many-body response taxonomy: 12%
- Numerical framework: 12%
- Constraint ledger: 10%
- Standard-Model ceiling: 2%
- Engineered-medium scan: 3%
- BSM residual search: 0%

Overall NMIR research maturity (audit estimate): **~9%**.

## Immediate next iteration

1. Derive the inclusive vector/axial response rate in a convention that can be coded directly.
2. Derive applicable zeroth- and first-frequency-moment sum rules for `S_AA(q,w)` and `S_VV(q,w)`.
3. Test whether magnons/spin waves can increase total deposited energy or merely move fixed spectral weight to lower thresholds.
4. Add discrete nuclear charged-current/neutral-current transition strengths as a competing absorption branch.
5. Freeze a solar-neutrino spectrum/flux dataset with primary-source provenance and start the G3 deposited-power integral.
