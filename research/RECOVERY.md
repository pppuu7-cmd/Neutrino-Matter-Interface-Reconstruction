# NMIR Recovery / Source-of-Truth State

Last reconciled: 2026-09-06 Europe/Stockholm
Program: Neutrino–Matter Interface Reconstruction (NMIR)
Repository: `pppuu7-cmd/Neutrino-Matter-Interface-Reconstruction`

## Mission

Reconstruct the most general low-energy neutrino↔matter interface, separate state control from detection and irreversible energy deposition, establish Standard-Model bounds, and only then identify any BSM coupling structures needed to exceed those bounds.

Four organizing principles are frozen:

1. **response reconstruction** — optimize physically admissible material response functions rather than guess materials;
2. **production ↔ absorption / crossed-channel reconstruction** — use known weak production/decay processes to infer inverse capture channels;
3. **gravitational focusing** — test whether spacetime curvature can multiply local neutrino flux before microscopic capture;
4. **staggered-layer response engineering** — test shifted atomic/isotopic layers without confusing projected geometric coverage with weak opacity.

## Central observables

For incident differential flux `Phi(E)`,

\[
\frac{P_{\rm dep}}{A}=\int dE_\nu\,\Phi(E_\nu)\int d\omega\;\omega\,\frac{dP_{\rm int}}{d\omega}(E_\nu),
\]

or for a slab,

\[
\frac{P_{\rm dep}}{A}=\int dE_\nu\,\Phi(E_\nu)E_\nu\,\eta_{\rm dep}(E_\nu)[1-e^{-\tau(E_\nu)}].
\]

With gravitational magnification `mu(E,x)`,

\[
R=N_T\int dE\,\mu(E,\mathbf x)\Phi_\nu(E)\sigma_{\rm cap}(E),
\]

\[
P_{\rm dep}=N_T\int dE\,\mu(E,\mathbf x)\Phi_\nu(E)\sigma_{\rm cap}(E)E_{\rm dep}(E).
\]

The useful-capture problem is the product of **flux magnification × capture probability × deposited-energy fraction**.

## Many-body response formulation

For weak/EM/BSM currents,

\[
\Gamma \propto \int d^3q\,d\omega\;L_{ab}(q,\omega)S^{ab}(q,\omega),
\]

with admissible response satisfying positivity, detailed balance where applicable, Kramers–Kronig/causality, conservation laws, sum rules and stability. For equilibrium Hermitian response, schematically

\[
S(-\omega)=e^{-\beta\omega}S(+\omega).
\]

## Measured beta decay → capture normalization

For allowed/superallowed long-wavelength beta transitions,

\[
\sigma_{\rm NCB}v_\nu=2\pi^2\ln2\,\frac{p_eE_eF(Z,E_e)}{ft}.
\]

Iteration 0006 restored units explicitly. With `p_e,E_e` in MeV and `ft` in seconds,

\[
\sigma(v_\nu/c)[\mathrm{cm}^2]=C_{ft}\,\frac{p_eE_eF}{ft},
\]

\[
C_{ft}=2\pi^2\ln2\,\frac{\hbar(\hbar c)^2}{m_e^5}\simeq1.00645\times10^{-40}\ \mathrm{cm^2\,s/MeV^2}.
\]

For H-3 with evaluated `Q_beta=18.5906 keV`, `log10(ft/s)=3.0524`, daughter `Z=2`, and a transparent point-Coulomb Fermi function, NMIR obtains

\[
\sigma(v/c)\simeq7.785\times10^{-45}\ \mathrm{cm^2},
\]

within about 0.7% of the published measured-ft result `7.84e-45 cm^2` from Cocco–Mangano–Messina (2007). The remaining difference is consistent with the intentionally simplified Coulomb treatment; precision ranking must freeze one finite-size/screening convention.

Authoritative validation: GitHub Actions run `34004890286`, job `101410168170`, head `865dd2a9ecf945633e965be062b30bde21f818a5`: `29 passed` and baseline executable succeeded.

The preceding failure run `34002127072`, job `101402748769`, was diagnosed as **test/reference-data infrastructure failure**, not scientific FAIL: two stored rounded benchmark constants were slightly outside overly tight tolerances. Formulas were unchanged and corrected references now pass.

## Gravitational focusing baseline

For an ultrarelativistic neutrino in weak Schwarzschild lensing,

\[
\alpha(b)\simeq\frac{4GM}{bc^2},\qquad f\simeq\frac{b^2c^2}{4GM}.
\]

Solar-limb benchmark: `f(R_sun) ≈ 547.741 AU`. A transparent extended-Sun calculation in the literature gives a minimum focal distance near `23.5 ± 0.1 AU` for distant-source neutrinos crossing the solar interior. The Sun cannot act as an ordinary separate downstream lens for its own solar neutrinos. Finite source/receiver size, wave effects, alignment and Liouville phase-space conservation regularize all caustic claims.

## Staggered-layer baseline

For scatterers at `r_j`,

\[
F(\mathbf q)=\sum_j e^{i\mathbf q\cdot\mathbf r_j}.
\]

Shifted layers can move constructive/destructive reciprocal-space peaks but projected atomic coverage is not weak opacity. A geometric sanity check with nuclear radius `5 fm` and transverse spacing `3 Å` gives projected nuclear hard-disk fraction `8.73e-10` per layer and about `1.15e9` perfectly complementary layers for unity geometric nuclear projection; actual weak opacity is vastly smaller.

For `E_nu=1 MeV`, `lambda_nu≈1.23984e-12 m`; at `d=3 Å`, first-order Bragg kinematics gives `theta≈0.118396 deg`. Directional coherence must never be promoted to total-opacity gain without angle/energy integration and sum-rule checks.

## Research gates

| Gate | Question | Status |
|---|---|---|
| G0 | Do normalizations reproduce known weak/CEvNS/capture scales? | PARTIAL PASS — CEvNS plus explicit tritium ft→capture benchmark validated |
| G1 | Can static coherence increase total interaction probability beyond ordinary nuclear coherence? | PARTIAL NEGATIVE — naive whole-crystal elastic N² opacity excluded under current sum-rule assumptions |
| G2 | Can density/spin/current response deposit useful energy into collective/nuclear modes? | OPEN |
| G3 | Maximum SM deposited power from solar neutrinos in passive organized matter? | OPEN — Ga SNU→W/kg normalization only |
| G4 | Can polarization/resonance/periodicity/nonequilibrium increase useful deposition parametrically? | OPEN |
| G5 | Minimal BSM structure needed if SM ceiling is insufficient? | LOCKED until G3 |
| G6 | Does BSM survive laboratory/stellar/SN/cosmological constraints? | LOCKED until G5 |
| G7 | Can a production/decay process identify a strong inverse/crossed capture channel? | PARTIAL PASS — measured-ft numerical route validated on tritium |
| G8 | Can resonant peak enhancement beat source bandwidth while respecting integrated strength? | OPEN |
| G9 | Can finite gravitational lensing provide useful flux gain at absorber? | OPEN |
| G10 | Can staggered/multi-isotope layers increase flux-integrated capture/deposition at fixed mass column? | OPEN — geometric-opacity version disfavored, structure-factor/spectral-comb variants retained |

## Chronological results preserved

### Iteration 0001 — initial gates
- Xe-132 ideal CEvNS at 1 MeV: `Q_W≈75.5311`, `sigma≈2.405e-41 cm^2`.
- Liquid-Xe-like mean free path: `~3.08e16 m`; optical-depth-one mass column `~9.07e18 g/cm^2`.
- Minimal Dirac magnetic moment at `m_nu=0.05 eV`: `~1.6e-20 mu_B`; first ideal magnetic-precession maximum over 1 m requires `~3.35e17 T`.
- Naive whole-crystal N² total-opacity route not accepted.

### Iteration 0002 — production↔absorption and spin response
- Inverse weak channels are physically real; inverse beta decay is canonical.
- Recoilless/Mössbauer-neutrino proposals establish resonant inverse absorption as legitimate but vulnerable to linewidth, recoil-free fraction, lattice deformation and source/absorber overlap.
- A 1-meV magnon produced by a 1-MeV neutrino deposits only `1e-9` of incident energy; good detection is not equivalent to useful capture.

### Iteration 0003 — decay→capture seeds
- Real crossed pairs include Ar-37 EC ↔ capture on Cl-37 and Ge-71 EC ↔ capture on Ga-71.
- Seed thresholds: Cl-37 `~0.814 MeV`, Ga-71 `~0.233 MeV`.
- Historical gallium rate `66.1 SNU` for pure Ga-71 corresponds to `~5.61e-10 captures/s/kg`.
- Optimistic 1-MeV deposition gives `~8.99e-23 W/kg`; `1 W/kg` would require `~1.11e22` enhancement over that normalization.

### Iteration 0004 — gravitational focusing
- Solar-limb weak-lens benchmark reproduced.
- Transparent-interior lensing is retained for distant sources; finite gain only.
- Focusing multiplies microscopic capture and cannot substitute for it.

### Iteration 0005 — staggered-layer metamaterial
- Shifted atomic planes are physically realizable (AB/ABC-like registries).
- Geometric line-of-sight coverage is not neutrino opacity.
- Structure factor and Bragg kinematics are the correct wave-language; ordinary directional coherence does not automatically raise integrated interaction strength.
- Multi-isotope resonant spectral-comb stack retained as a high-value variant.

### Iteration 0006 — explicit ft normalization
- Diagnosed and repaired rounded-reference CI failure without changing physics.
- Implemented unit-explicit measured-ft capture normalization in `src/nmir/ft_capture.py`.
- Reproduced published tritium capture normalization to ~1% using a deliberately simple point-Coulomb Fermi factor.
- CI authoritative PASS: run `34004890286`, job `101410168170`, `29 passed`.

## Initial physical facts to preserve

1. CEvNS gives real nuclear-level coherence, not automatic macroscopic N² opacity.
2. Low detector threshold is not a larger total cross section.
3. State conversion can occur without substantial energy extraction.
4. Production↔absorption/crossing identifies matrix elements but does not imply efficient capture.
5. Peak resonant cross section and flux-integrated capture are distinct observables.
6. Exact time reversal and a crossed reaction are not always the same external-particle process.
7. Gravitational magnification and microscopic absorption are multiplicative, not interchangeable.
8. Collisionless lensing cannot create arbitrary phase-space brightness.
9. Projected atomic coverage and weak-interaction opacity are different quantities.
10. Any staggered-lattice claim must report both directional structure-factor gain and flux/angle/energy-integrated gain.
11. BSM/light mediators remain constraint-ledger inputs until G3 closes.

## Current repository components

- `README.md`, `research/ROADMAP.md`, `research/LITERATURE_LEDGER.md`, `research/RECOVERY.md`.
- `research/iterations/0001_...md` through `0006_ft_capture_normalization.md`.
- `data/inverse_transition_seed.csv`.
- theory: operator basis, production/absorption duality, beta-decay inverse capture, spin/magnon response, gravitational focusing, staggered-layer metamaterial.
- code: `baseline.py`, `duality.py`, `capture_metrics.py`, `gravity_focusing.py`, `staggered_lattice.py`, `ft_capture.py`.
- tests cover all current numerical benchmark modules; CI is `.github/workflows/ci.yml`.

## Current maturity estimate

Stable audit estimate after iteration 0006: **NMIR_READINESS: 21%**.

Increase from 18% is credited only to: (i) root-caused CI repair preserving frozen physics, (ii) explicit natural-unit→cm² conversion, (iii) published tritium capture normalization reproduced and CI-regression-tested. No readiness credit is assigned merely for prose or unvalidated ideas.

## Immediate next iteration

1. Freeze a primary-source solar-neutrino flux/spectrum dataset with provenance and units.
2. Reproduce Ga-71 and Cl-37 benchmark capture rates/cross sections with explicit oscillation and transition conventions.
3. Expand evaluated inverse-transition catalog and rank by event rate and W/kg.
4. Implement Breit–Wigner/source–absorber overlap and integrated-strength gate.
5. Implement sum-rule-preserving axial response toy model.
6. Reproduce transparent-Sun `~23.5 AU` extended-lens benchmark and then finite-source gain.
7. For staggered layers, explicitly compare angle/energy-integrated response against the same atoms at fixed mass column, including disorder/Debye–Waller suppression.
8. Couple multi-isotope layer choices to solar spectra only after items 1–3 are frozen.
