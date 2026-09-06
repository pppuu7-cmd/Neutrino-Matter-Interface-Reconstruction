# Iteration 0001 — Initial physical gates

Date: 2026-09-06
Status: exploratory; all quantitative claims remain benchmark-level until independently reproduced by CI and precision modules.

## Question

Can an external field or organized material provide a qualitatively stronger handle on neutrinos than ordinary incoherent weak scattering?

## Result 1 — brute-force magnetic precession is not a laboratory capture mechanism

Using

\[
\phi_B=\frac{\mu_\nu B L}{\hbar c},
\]

the first ideal spin-precession maximum occurs at `phi_B=pi/2`.

For the minimal Dirac benchmark

\[
\mu_\nu\simeq3.2\times10^{-19}(m_\nu/{\rm eV})\mu_B,
\]

and `m_nu = 0.05 eV`, the baseline code gives

\[
\mu_\nu=1.6\times10^{-20}\mu_B,
\]

and for `L=1 m`

\[
B_{\pi/2}\approx3.35\times10^{17}\;{\rm T}.
\]

Interpretation: a direct static magnetic field acting only through the minimal magnetic moment is not a plausible laboratory route. This does **not** exclude a field acting indirectly by preparing a polarized or collective material response.

## Result 2 — ideal nuclear coherence remains far from macroscopic opacity

For Xe-132-like `(Z,N)=(54,78)` at `sin^2 theta_W=0.23857`,

\[
Q_W\approx75.5311.
\]

The ideal low-q CEvNS benchmark at `E_nu=1 MeV` gives

\[
\sigma\approx2.405\times10^{-41}\;{\rm cm^2}.
\]

For liquid-Xe-like density `2.94 g/cm^3`, the independent-scatterer mean free path is

\[
\lambda\approx3.08\times10^{16}\;{\rm m}.
\]

The corresponding mass column for optical depth one is approximately

\[
\Sigma_{\tau=1}\approx9.07\times10^{18}\;{\rm g/cm^2}.
\]

Interpretation: even genuine nuclear `Q_W^2` coherence leaves an enormous gap to neutrino opacity at MeV scale.

## Result 3 — static crystal N^2 enhancement is an explicit no-go branch

Aharonov, Avignone, Casher and Nussinov, Phys. Rev. Lett. 58, 1173 (1987), derived a Born-approximation sum rule for local-potential neutrino scattering from a crystal. The total force scales linearly with the number of scattering centers; exotic macroscopic coherent enhancement is not obtained.

NMIR therefore marks the naive branch

`ordinary static crystal + elastic coherence -> macroscopic total-rate N^2`

as **DISFAVORED/NO-GO within the assumptions of that sum rule**.

This gate is assumption-specific and does not automatically cover inelastic, resonant, driven, nonlocal or BSM interactions.

## Result 4 — periodic matter is a state-control mechanism, not automatically an absorber

Periodic matter-density profiles can parametrically enhance neutrino flavor oscillations. This demonstrates that an engineered spatial profile can coherently manipulate neutrino state evolution.

However, the forward-scattering potential is refractive. NMIR will not count parametric flavor enhancement as energy capture unless it is coupled to a distinct inelastic sink.

## Result 5 — polarized media provide a credible 'field-like' interface

General matter-interaction analyses show that vector/axial contributions depend on medium properties and that in a polarized medium additional spin-sensitive structures can appear; general tensor interactions can generate transverse potentials capable of spin flip.

This motivates the first serious engineered branch:

\[
B_{\rm ext}\to \text{spin-polarized medium}\to S_{AA}(q,\omega)
\to \text{inelastic spin/collective excitation}.
\]

The scientific question is not whether polarization changes a neutrino Hamiltonian — it can — but whether the *inclusive inelastic spectral weight* can be increased enough to matter while satisfying sum rules.

## Candidate hierarchy after iteration 1

1. **Axial/spin collective response in polarized or magnetically ordered matter** — PRIORITY A.
2. **Discrete nuclear charged-current / neutral-current resonances** — PRIORITY A.
3. **Low-threshold phonon/electronic/superconducting response** — PRIORITY B; likely excellent for detection, total-opacity enhancement unproven.
4. **Periodic matter / Floquet control followed by an inelastic sink** — PRIORITY B.
5. **Direct magnetic moment in laboratory B field** — PRIORITY C / baseline no-go for minimal moment.
6. **Naive whole-crystal elastic N^2 enhancement** — PRIORITY X under local-potential sum-rule assumptions.

## Next calculation

Derive an inclusive vector/axial response rate and use spectral sum rules to bound

\[
\int d\omega\;\omega\,S_{AA}(q,\omega)
\]

for candidate spin systems. The key question is whether magnons/spin collective modes can redistribute spectral weight into experimentally favorable `(q,omega)` without increasing the sum-rule-limited total coupling, or whether a genuine enhancement of deposited power is possible.
