# NMIR — Gravitational Neutrino Focusing (GNF)

## Motivation

A new NMIR branch asks whether spacetime geometry can be used as a neutrino lens: collect a larger neutrino phase-space bundle into a smaller receiver region and place a high-capture-probability atom/material at the magnified image/caustic.

The mechanism is conceptually independent of microscopic capture enhancement:

\[
\text{source neutrino flux}
\xrightarrow{\text{gravity}}
\mu_\nu\,\Phi_\nu
\xrightarrow{\text{NMIR absorber}}
P_{\rm dep}.
\]

Thus the relevant product is

\[
R_{\rm capture}^{\rm lensed}=\mu_\nu\,R_{\rm capture}^{\rm unlensed},
\]

provided the absorber is smaller than or matched to the magnified flux structure and the lensing geometry is stable.

## Weak-field relativistic deflection

For an ultrarelativistic neutrino passing a compact weak-field lens with impact parameter `b`, the leading GR deflection approaches the null-geodesic result

\[
\alpha(b)\simeq \frac{4GM(<b)}{bc^2},
\]

with corrections suppressed for `m_nu/E_nu << 1` and with the interior mass profile `M(<b)` replacing the point-mass value for a transparent extended lens.

For a point-mass/outer-ray approximation, a ray crossing the optical axis at distance `f` satisfies

\[
f\simeq \frac{b}{\alpha}
=\frac{b^2c^2}{4GM}.
\]

For the solar limb this gives the familiar gravitational-lens scale near `~550 AU`. Neutrinos are different because the Sun is transparent to them at ordinary solar-neutrino energies: trajectories with `b<R_sun` can sample the interior gravitational field. Published transparent-Sun calculations find a minimum focal length near `23.5 AU`, depending on the solar density profile.

## Lens equation and magnification

For thin-lens geometry,

\[
\beta=\theta-\frac{D_{LS}}{D_S}\alpha(\theta),
\]

where `beta` is the unlensed source angle and `theta` an image angle.

For a point lens, define the Einstein angle

\[
\theta_E=\sqrt{\frac{4GM}{c^2}\frac{D_{LS}}{D_LD_S}}.
\]

For a point source at dimensionless offset `u=beta/theta_E`, the total geometric-optics magnification is

\[
\mu(u)=\frac{u^2+2}{u\sqrt{u^2+4}}.
\]

The formal `u->0` divergence is **not** physically realizable as infinite neutrino concentration. It is regularized by finite source size, wave effects, lens-profile structure, detector size, source/lens motion, energy spread and alignment error.

## Phase-space / brightness gate

Gravitational lensing conserves phase-space density (Liouville theorem) in collisionless propagation. It can magnify flux at a chosen location by mapping a larger solid angle/aperture onto it, but it cannot create arbitrarily high intrinsic phase-space brightness.

Therefore NMIR must never interpret a caustic divergence from a point-source geometric-optics formula as infinite usable power.

The correct optimization target is a finite receiver-integrated gain

\[
\mathcal G=\frac{\int_{A_{\rm rec}} dA\,\Phi_{\nu,\rm lensed}}
{\int_{A_{\rm rec}} dA\,\Phi_{\nu,\rm unlensed}}.
\]

## Crucial source-lens distinction

A spherically symmetric object cannot act as an ordinary downstream gravitational lens for neutrinos that it itself emits from the same center in the sense required here. Solar neutrinos originate inside the Sun; using the Sun as a lens is therefore relevant to neutrinos from a *different, more distant source*, not to concentrating the Sun's own neutrino output onto a focus.

To focus solar neutrinos, the lens must be a separate mass distribution between the Sun and receiver: a planet, star, compact object, engineered mass distribution, or (purely theoretically) a controlled spacetime geometry.

## Candidate lens classes

1. **Transparent star / Sun** for neutrinos from a distant source.
2. **Planetary lens** for solar neutrinos: weak but geometrically accessible.
3. **White dwarf / neutron star**: stronger deflection, extreme alignment/focal geometry.
4. **Black hole**: very strong lensing and caustics, but receiver placement/environment become difficult.
5. **Binary/compound gravitational lens**: caustic networks may provide larger finite magnifications.
6. **Engineered mass distribution**: useful as a theoretical bound; practical mass requirements likely prohibitive.
7. **Modified/engineered metric** only after the GR baseline is exhausted; any exotic metric must satisfy stress-energy and stability constraints.

## Combined NMIR objective

For a microscopic absorber with capture cross section `sigma_cap(E)` and local target number `N_T`,

\[
R= N_T\int dE\,\mu(E,\mathbf x)\Phi_\nu(E)\sigma_{\rm cap}(E).
\]

For deposited power,

\[
P_{\rm dep}= N_T\int dE\,\mu(E,\mathbf x)\Phi_\nu(E)\sigma_{\rm cap}(E)E_{\rm dep}(E).
\]

This equation directly couples the GNF branch to the production↔absorption and `ft`-reconstruction branches.

## Research gates

### F1 — Geodesic gate
Reproduce relativistic-neutrino deflection in Schwarzschild geometry and verify the null limit.

### F2 — Transparent extended-lens gate
Use a density profile `rho(r)` and compute

\[
M(<b)=4\pi\int_0^b dr\,r^2\rho(r)
\]

with the correct projected/GR lensing treatment to reproduce a known transparent-Sun focal-length benchmark.

### F3 — Finite-source gate
Replace point-source magnification by integration over the angular source profile. For solar-neutrino production this is mandatory because the emitting region is extended.

### F4 — Wave/packet gate
Check when geometric optics is valid for neutrino de Broglie wavelength and source coherence. Include mass-eigenstate velocity/phase differences only where relevant.

### F5 — Liouville / etendue gate
Prove numerically that finite receiver-integrated gain respects phase-space conservation; reject any apparent infinite-power caustic artifact.

### F6 — Alignment/stability gate
Include source size, lens motion, receiver displacement and finite observation time.

### F7 — Capture-product gate
Compute the actual improvement in `mu * sigma_cap * E_dep`, not magnification alone.

## Immediate benchmarks

1. Point-mass focal distance for a ray at impact parameter `b`.
2. Solar-limb point-mass benchmark `~550 AU`.
3. Literature transparent-Sun minimum focal distance `~23.5 AU` as an extended-profile target.
4. Point-lens magnification as a function of `u` with an explicit finite-`u`/finite-source regularization warning.
5. Required magnification to lift the current Ga-71 normalization from `~9e-23 W/kg` to target powers: even `mu=10^6` or `10^12` remains far below `1 W/kg`; this branch must be combined with a much stronger absorber.

## Status

OPEN. Gravitational focusing is physically legitimate and may multiply event rates, but it does not by itself solve the weak-interaction problem. The highest-value question is whether any realistic astrophysical or engineered lens can supply enough finite magnification to materially change the NMIR capture budget.
