# NMIR — Neutrino Production ↔ Absorption Duality

## Motivation

A central NMIR hypothesis is that the best way to identify efficient neutrino-capture channels may be to classify the microscopic processes that produce neutrinos and systematically construct the corresponding inverse channels.

The guiding principle is not that every observed decay can simply be run backwards in the laboratory. Rather, microscopic weak-interaction amplitudes obey crossing/microreversibility relations, while the observable reverse rate is controlled by phase space, occupation factors, thresholds, linewidths, recoil, medium response and kinematics.

Schematic map:

\[
A \to B + \nu
\qquad \Longleftrightarrow \qquad
\nu + B \to A.
\]

For beta processes:

\[
n \to p + e^- + \bar\nu_e,
\]

with the inverse-beta channel

\[
\bar\nu_e + p \to n + e^+,
\]

and electron capture

\[
p + e^- \to n + \nu_e
\]

paired with charged-current neutrino absorption

\[
\nu_e + n \to p + e^-.
\]

In nuclei, replace free nucleons by nuclear initial/final states and include the appropriate Fermi/Gamow–Teller/forbidden matrix elements.

## Core NMIR question

For every neutrino-emission channel, determine whether its inverse channel can be engineered into a large-opacity or large-energy-deposition regime.

This creates a new search direction:

\[
\text{emission catalog}
\to
\text{inverse-reaction catalog}
\to
\text{resonance/threshold engineering}
\to
\sigma_{\rm abs}(E_\nu)
\to
P_{\rm dep}.
\]

## Detailed balance / response relation

For a medium operator \(O\), define the dynamic structure factor

\[
S_O(\mathbf q,\omega)
=\frac{1}{Z}\sum_{i,f}e^{-\beta E_i}
|\langle f|O(\mathbf q)|i\rangle|^2
2\pi\delta[\omega-(E_f-E_i)].
\]

Thermal microreversibility implies

\[
S_O(\mathbf q,-\omega)
=e^{-\beta\omega}S_O(-\mathbf q,+\omega)
\]

for the appropriate Hermitian/equilibrium case. Thus emission and absorption are not independent pieces of physics: they are two directions through the same spectral response.

For NMIR this is important because a medium known to emit neutrinos through a transition contains, in principle, the matrix element needed for the inverse absorption process. The practical problem is whether the incoming neutrino energy and momentum can overlap the available spectral weight strongly enough.

## Resonant inverse reactions

If the production process is effectively two-body and monoenergetic, a narrow inverse resonance may occur. Historical examples proposed recoil-free resonant neutrino/antineutrino absorption in crystals, analogous to Mössbauer spectroscopy.

The ideal resonance logic is

\[
E_\nu^{\rm source}\simeq E_\nu^{\rm absorber},
\qquad
\Gamma_{\rm line}\ \text{small},
\]

so that the same weak transition matrix element that emits the neutrino also absorbs it in reverse.

A narrow line can make the *peak* cross section much larger than a broad continuum value, but NMIR must track the integrated spectral strength and usable bandwidth. Narrowing a line does not create unlimited total oscillator strength.

## Physical gates

### D1 — Matrix-element gate
A candidate inverse channel must inherit a nonzero weak matrix element from an allowed production/decay process.

### D2 — Kinematic gate
The incident solar/reactor/source neutrino spectrum must overlap the threshold/resonance. A beautiful inverse transition at the wrong energy is useless for the chosen flux.

### D3 — Width gate
Compute natural, thermal, chemical, magnetic, inhomogeneous and lattice broadening. Resonant enhancement survives only if source and absorber spectral profiles overlap.

### D4 — Recoil/phonon gate
For a solid-state realization, determine the recoil-free fraction and the probability of phononless source/absorber transitions. Lattice deformation associated with changing nuclear species can strongly suppress the usable resonance.

### D5 — Integrated-strength gate
Check sum rules / unitarity / detailed balance. A high peak cross section is not by itself a large broadband opacity.

### D6 — Energy-deposition gate
For capture, calculate what fraction of the incoming neutrino energy remains in charged particles, photons, nuclear excitation, phonons or heat. This branch is intrinsically more attractive for energy capture than a single meV-scale magnon excitation.

## Why this changes NMIR priorities

The previous spin/magnon branch remains scientifically important for low-threshold detection, but one-magnon events typically deposit a collective-mode energy \(\omega_{\rm mag}\) far below a MeV-scale solar-neutrino energy. For example,

\[
\omega_{\rm mag}\sim 1\ {\rm meV},\qquad E_\nu\sim1\ {\rm MeV}
\]

gives a one-event deposited fraction

\[
\eta_{\rm dep}\sim10^{-9}.
\]

Unless the opacity or multiplicity becomes enormous, this is unlikely to be an efficient energy-harvesting channel.

Charged-current or resonant nuclear absorption can instead deposit keV–MeV energy per successful event and should therefore be promoted to a co-primary NMIR branch.

## Production-channel inventory to build

1. free neutron beta decay ↔ inverse beta / charged-current nucleon reactions;
2. nuclear beta-minus decay ↔ antineutrino charged-current capture;
3. electron capture ↔ electron-neutrino nuclear capture;
4. beta-plus decay ↔ corresponding inverse charged-current channels;
5. bound-state beta decay ↔ monoenergetic resonant absorption candidates;
6. nuclear de-excitation / neutral-current pair emission ↔ neutral-current excitation/absorption;
7. thermal plasma neutrino processes ↔ inverse in-medium weak absorption;
8. pion/muon/tau weak decays ↔ crossed high-energy reactions;
9. resonant electroweak channels (e.g. Glashow resonance) as proof that neutrino capture can be dramatically enhanced at a precisely matched center-of-mass energy.

## Immediate computational program

For every candidate transition store

\[
\{Q,\ E_\nu^{\rm res},\ J_i^\pi,J_f^\pi,\ M_F,\ M_{GT},\Gamma_{\rm nat},\Gamma_{\rm env},\sigma_{\rm peak},\int\sigma dE,\eta_{\rm dep}\}.
\]

Then rank candidates using at least two objectives:

\[
\mathcal F_{\rm detect}=\int dE\,\Phi_\nu(E)\sigma(E),
\]

\[
\mathcal F_{\rm energy}=\int dE\,\Phi_\nu(E)\sigma(E)E\eta_{\rm dep}(E).
\]

This explicitly separates a good detector from a good energy absorber.

## Status

This branch is OPEN and now considered co-primary with the axial spin-response branch. Historical resonant-neutrino proposals demonstrate that the inverse-production intuition is physically legitimate; NMIR's task is to determine whether any realizable transition survives linewidth, recoil, material and flux-overlap constraints strongly enough to matter.
