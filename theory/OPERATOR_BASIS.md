# Initial neutrino–matter operator basis

Status: working basis for Stage A; not yet frozen.

## 1. Standard-Model low-energy weak interaction

Below the electroweak scale, neutrino scattering from a fermionic target `f` can be organized schematically as

\[
\mathcal L_{\rm weak}^{\rm NC}=-\frac{G_F}{\sqrt 2}
[\bar\nu\gamma_\mu(1-\gamma_5)\nu]
[\bar f\gamma^\mu(g_V^f-g_A^f\gamma_5)f].
\]

For electron-flavor charged-current processes include the corresponding four-fermion charged-current operator. Nuclear targets require matching the quark current onto nucleon/nuclear currents and form factors.

The natural material-response decomposition is therefore into vector density/current, axial spin/current, and vector–axial interference channels.

## 2. Coherent nuclear vector response

For elastic scattering at momentum transfer small compared with the inverse nuclear size,

\[
Q_W\simeq N-(1-4\sin^2\theta_W)Z,
\]

and, in the ideal coherent low-energy limit,

\[
\sigma_{\rm CE\nu NS}\simeq \frac{G_F^2 Q_W^2 E_\nu^2}{4\pi}
\]

up to recoil, form-factor, radiative and convention-dependent refinements. The working code treats this formula as a normalization benchmark, not as the final precision prediction.

## 3. Electromagnetic neutrino vertex

The general electromagnetic neutrino vertex can contain charge/millicharge, charge-radius/anapole and dipole structures. The dipole term is represented schematically by

\[
\mathcal L_{\rm dipole}=\frac12\bar\nu_i(\mu_{ij}+i\epsilon_{ij}\gamma_5)
\sigma^{\mu\nu}\nu_j F_{\mu\nu}.
\]

Dirac/Majorana restrictions must be imposed before phenomenology. In particular, diagonal electromagnetic moments are not generically interchangeable between Dirac and Majorana cases.

A magnetic field can generate spin or spin-flavor evolution through a term of scale

\[
H_B\sim \mu_\nu B_\perp,
\]

but this is a **state-control** effect until an inelastic matter channel extracts energy.

## 4. Matter potentials

Forward weak scattering generates an effective refractive Hamiltonian. For ordinary unpolarized electron matter, the familiar flavor-dependent term includes

\[
V_e=\sqrt2G_F N_e.
\]

A polarized target introduces axial/spin-dependent expectation values. NMIR will derive the full vector/axial matter Hamiltonian from the underlying currents rather than treating an engineered 'neutrino field' as an independent force.

## 5. General low-energy non-standard interactions

A conventional neutral-current NSI parameterization is

\[
\mathcal L_{\rm NSI}=-2\sqrt2G_F\,\epsilon_{\alpha\beta}^{fP}
(\bar\nu_\alpha\gamma_\mu P_L\nu_\beta)
(\bar f\gamma^\mu P f).
\]

For the inverse reconstruction we will use a wider Lorentz basis including scalar, pseudoscalar, vector, axial and tensor structures where consistent with the neutrino field content. Gauge-invariant UV completion/matching is a later gate and cannot be skipped for a final candidate.

## 6. Light mediators

If a mediator mass is comparable to or below momentum transfer, retain the propagator explicitly, e.g.

\[
\mathcal M_X\propto \frac{g_\nu g_m}{q^2-m_X^2+i m_X\Gamma_X}.
\]

A contact approximation is permitted only when its hierarchy is demonstrated.

## 7. Universal medium response

For an operator basis `O_a`, define target spectral functions

\[
S_{ab}(\mathbf q,\omega)=\int dt\,d^3x\;e^{i(\omega t-\mathbf q\cdot\mathbf x)}
\langle O_a(t,\mathbf x)O_b(0)\rangle.
\]

Then the inclusive rate takes the generic form

\[
\Gamma=\sum_{ab}\int d\Pi\;K_{ab}(E_\nu,q,\omega)S_{ab}(q,\omega),
\]

where `K_ab` is fixed by the microscopic neutrino operator and phase space.

This separation is the central NMIR interface:

\[
\text{neutrino microphysics}\;K_{ab}
\quad\times\quad
\text{material microphysics}\;S_{ab}.
\]

## 8. Candidate response sectors

The first full decomposition will include:

1. nuclear coherent density response;
2. nuclear spin response;
3. discrete nuclear transitions / charged-current capture;
4. atomic electron ionization/excitation;
5. electronic band response;
6. phonons and lattice modes;
7. magnons/spin waves and other spin collective modes;
8. superconducting quasiparticles and collective modes;
9. superfluid density/spin modes;
10. driven/non-equilibrium response.

## 9. Mandatory gates for every claimed enhancement

For any candidate enhancement factor `R`:

- specify whether `R` applies to differential rate, total rate, deposited energy, or detector visibility;
- integrate over all allowed final states before claiming a total-rate enhancement;
- verify momentum/energy conservation and coherence length;
- check response sum rules;
- account for the external energy cost of preparing/driving the material;
- compare against an equal-mass/equal-volume Standard-Model reference target;
- propagate current laboratory and astrophysical bounds for any non-SM coupling.
