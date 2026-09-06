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
| G0 | Do all normalizations reproduce known weak/CEvNS limiting scales? | OPEN — benchmark code being added |
| G1 | Can static coherence increase total interaction probability beyond ordinary nuclear coherence? | OPEN |
| G2 | What density/spin/current response channels can deposit energy into phonons, magnons, quasiparticles or nuclear excitations? | OPEN |
| G3 | What is the maximum SM deposited power from solar neutrinos in passive organized matter? | OPEN — primary target |
| G4 | Can polarization, resonances, periodic media or nonequilibrium preparation increase the useful deposition fraction parametrically? | OPEN |
| G5 | If SM is insufficient, what minimal BSM operator/mediator structure is required? | LOCKED until G3 |
| G6 | Does any BSM candidate survive laboratory, stellar, supernova and cosmological constraints? | LOCKED until G5 |

## Initial physical facts to preserve

1. CEvNS provides a real coherence enhancement at the nuclear level; near `qR << 1`, the weak charge is approximately `Q_W = N - (1-4 sin^2 theta_W) Z`, and the total low-energy cross section scales approximately as `Q_W^2 E_nu^2`.
2. A low detector threshold is not equivalent to a larger total cross section.
3. Flavor/spin conversion (MSW, magnetic precession, parametric conversion) can control the neutrino state without extracting substantial energy.
4. A static macroscopic crystal does not automatically provide an `N^2` total-rate enhancement over all scattering centers; any claimed macroscopic coherence must pass momentum-transfer, phase-space and sum-rule checks.
5. Electromagnetic neutrino form factors and BSM light mediators are allowed branches of the reconstruction, but they are constrained and must not be used to bypass the Standard-Model baseline.

## First benchmark targets

- CEvNS low-energy total cross section for a user-specified `(Z,N,E_nu)`.
- Mean free path for a material of density `rho` and molar mass `A`.
- Magnetic spin-precession scale `mu_nu B L/(hbar c)` and the field required for the first conversion maximum.
- Explicit unit tests for unit conversions and scaling laws.

## Current maturity estimate

- Problem formulation: 20%
- Operator inventory: 10%
- Many-body response taxonomy: 5%
- Numerical framework: 5%
- Constraint ledger: 5%
- Standard-Model ceiling: 0%
- Engineered-medium scan: 0%
- BSM residual search: 0%

Overall NMIR research maturity (audit estimate): **~5%**.

## Immediate next iteration

1. Freeze the low-energy operator basis.
2. Add baseline CEvNS/mean-free-path/spin-precession code and tests.
3. Derive the response-channel decomposition into vector density, axial spin, charge/current, nuclear transition and collective condensed-matter sectors.
4. Construct a literature/constraint ledger with provenance.
5. Begin G3 with a theorem-style upper-bound attempt before scanning materials.
