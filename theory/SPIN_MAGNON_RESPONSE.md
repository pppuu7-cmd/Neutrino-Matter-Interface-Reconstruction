# NMIR — Axial Spin / Magnon Response Branch

## Purpose

Test whether an externally polarized or magnetically ordered material can increase the *useful* neutrino-matter coupling through the axial weak current, and distinguish three different effects:

1. neutrino state control / forward-scattering potential;
2. improved detectability via low-energy collective excitations;
3. genuine increase of total deposited energy / opacity.

Only (3) is directly relevant to an energy-harvesting interpretation.

## Weak axial coupling to a medium

At low energies the neutral-current interaction can be written schematically as

\[
\mathcal H_{\rm int}
=\frac{G_F}{\sqrt2}\,\ell_\mu J^\mu_{\rm weak},
\]

with leptonic current

\[
\ell_\mu=\bar\nu\gamma_\mu(1-\gamma_5)\nu.
\]

For a nonrelativistic many-body target, the weak current decomposes into vector-density/current and axial-spin pieces. The inclusive inelastic rate is therefore organized by response functions such as

\[
S_{VV}(\mathbf q,\omega),\qquad
S_{AA}^{ij}(\mathbf q,\omega),\qquad
S_{VA}^{i}(\mathbf q,\omega).
\]

A magnetically ordered medium can concentrate axial spectral weight into collective spin excitations.

## One-magnon model

As a first controlled model, represent a sharp magnon branch by

\[
S_{AA}(\mathbf q,\omega)
\simeq 2\pi Z_{\mathbf q}
\delta(\omega-\omega_{\mathbf q})
+S_{\rm cont}(\mathbf q,\omega).
\]

The weak rate then samples the neutrino kinematic kernel at the magnon dispersion \(\omega_{\mathbf q}\). An external magnetic field may change:

- polarization;
- magnon gap;
- mode occupation;
- spin susceptibility;
- anisotropy and directionality.

The field therefore acts on the material first, not on the neutrino magnetic moment directly.

## Sum-rule gate

Collective order can redistribute spectral weight but cannot create arbitrary total response. For each relevant operator define moments

\[
m_n(q)=\int_0^\infty d\omega\,\omega^n S(q,\omega).
\]

The zeroth moment is an equal-time correlator,

\[
m_0(q)=\langle O_{\mathbf q}O_{-\mathbf q}\rangle,
\]

while the first moment is controlled by a double commutator,

\[
m_1(q)=\frac12\langle[O_{-\mathbf q},[H,O_{\mathbf q}]]\rangle
\]

up to convention factors.

NMIR must therefore test any apparent enhancement against both \(m_0\) and \(m_1\): a narrow magnon peak can produce a large differential response without increasing the integrated weak strength.

## Energy-deposition diagnostic

For a single excitation of energy \(\omega\), the maximum deposited fraction per scattering is

\[
\eta_{\rm dep}=\frac{\omega}{E_\nu}.
\]

Reference scales:

- \(\omega=1\,\mathrm{meV}\), \(E_\nu=1\,\mathrm{MeV}\): \(\eta=10^{-9}\);
- \(\omega=1\,\mathrm{eV}\), \(E_\nu=1\,\mathrm{MeV}\): \(\eta=10^{-6}\);
- \(\omega=1\,\mathrm{keV}\), \(E_\nu=1\,\mathrm{MeV}\): \(\eta=10^{-3}\).

Thus ultralow-threshold collective modes can be excellent *sensors* while remaining poor *energy absorbers* unless repeated scattering, multi-excitation production or a separate absorptive channel provides large total transfer.

## Research questions

### S1 — Does polarization increase total axial spectral weight?
Compute the equal-time spin correlator for representative ordered phases and compare unpolarized, ferromagnetic and antiferromagnetic states under fixed target density.

### S2 — Can a field tune the response into solar-neutrino kinematics?
Scan \(B\), anisotropy and exchange parameters and determine where the neutrino kernel overlaps the magnon/spin-wave branch.

### S3 — Is there a many-excitation regime?
Determine whether one neutrino can efficiently create multi-magnon, spin-continuum or coupled spin-phonon states carrying a parametrically larger \(\omega\).

### S4 — Can repeated scattering help?
Repeated small-energy-loss scattering requires optical depth \(\tau\gg1\). Calculate whether any Standard-Model spin-response enhancement can approach that regime before material/sum-rule bounds are saturated.

### S5 — Compare with nuclear absorption
Use the same flux-weighted deposited-power objective to compare magnons against charged-current and resonant nuclear transitions. Do not compare only detector event rates.

## Preliminary gate

The spin/magnon branch remains OPEN for detector physics and for possible collective enhancement of differential response. For bulk energy capture, the tiny excitation-energy ratio is a strong preliminary disadvantage. NMIR should not call this branch an energy solution unless it passes both the integrated-strength and deposited-energy gates.
