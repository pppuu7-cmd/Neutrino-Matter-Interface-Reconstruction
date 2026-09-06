# NMIR Iteration 0004 — Gravitational Neutrino Focusing

Date: 2026-09-06 (Europe/Stockholm)

## New branch

A gravitational-focusing branch is added to test whether spacetime curvature can concentrate a neutrino flux onto a receiver containing a high-capture-probability atom or material.

The combined architecture is

`source -> gravitational magnification mu_nu -> microscopic absorber -> deposited energy`.

The lensing branch multiplies the local neutrino flux; it does not replace the need for a strong microscopic capture channel.

## Baseline equations

For an ultrarelativistic neutrino in weak Schwarzschild lensing,

`alpha ~= 4 G M /(b c^2)`.

The approximate axis-crossing distance for a point/outer-ray lens is

`f ~= b/alpha = b^2 c^2/(4 G M)`.

Using solar mass and radius gives

`f_solar_limb ~= 547.741 AU`,

reproducing the standard solar-gravitational-lens scale for a grazing outer ray.

Because neutrinos can traverse the Sun, a transparent extended-mass lens can use interior trajectories. Published transparent-Sun calculations give a minimum focal distance near `23.5 +/- 0.1 AU`, which becomes the first extended-profile benchmark for NMIR.

## Important physical distinction

The Sun cannot be used as an ordinary downstream lens to focus its *own* neutrinos onto a focus behind itself: the source and lens coincide. The transparent-Sun lens is useful for neutrinos from a more distant source.

To gravitationally focus solar neutrinos, a separate lens mass distribution must lie between the Sun and receiver.

## Phase-space gate

Point-source geometric-optics magnification formally diverges on an exact caustic, but this is not infinite physical power. Finite source size, wave effects, detector size, lens profile and alignment regularize the divergence. Collisionless gravitational lensing preserves phase-space density / surface brightness under Liouville evolution.

Therefore the physical NMIR quantity is finite receiver-integrated gain, not the point-caustic value.

## New code

`src/nmir/gravity_focusing.py`
- leading null-limit deflection;
- weak point-lens focal distance;
- solar-limb focal-distance benchmark;
- point-lens magnification with explicit exclusion of the singular `u=0` input;
- required lensing gain relative to a specified deposited-power target.

`tests/test_gravity_focusing.py`
- checks the `547.741 AU` solar-limb benchmark;
- checks `f=b/alpha` consistency;
- point-lens magnification normalization;
- far-offset `mu -> 1` behavior;
- rejects the unregularized exact-caustic input.

## Candidate geometries to test

1. Sun as transparent lens for distant neutrino sources.
2. Planet/star as separate lens for solar neutrinos.
3. White-dwarf/neutron-star lenses.
4. Black-hole strong lensing / caustics.
5. Binary or compound lenses with caustic networks.
6. Artificial mass distribution as a theoretical engineering bound.
7. Only after GR baseline: exotic/modified spacetime geometry, with stress-energy and stability gates.

## Combined energy implication

The present Ga-71 solar-capture normalization is of order `9e-23 W/kg` for an optimistic reference deposition of `1 MeV/capture`. Therefore gravitational magnification alone would require an absurd gain of order `1e22` to reach `1 W/kg` if microscopic capture physics remained unchanged.

So gravitational focusing is not expected to solve the problem by itself. Its value is multiplicative: even a large but finite `mu_nu` may become important if the production↔absorption branch discovers a much stronger resonant/nuclear capture mechanism.

## Next calculations

1. Implement a transparent spherical lens with realistic projected mass density and reproduce the `23.5 AU` solar minimum focal distance.
2. Integrate magnification over a finite source disk rather than use a point-source caustic.
3. Compute realistic lensing gains for selected source-lens-observer configurations.
4. Evaluate wave-optics/coherence conditions for MeV neutrinos.
5. Couple `mu(E)` directly to the inverse-transition catalog and deposited-power objective.
6. Test whether any separate planetary/stellar lens can usefully focus solar neutrinos at an accessible receiver location.

## Maturity effect

The branch is scientifically legitimate but currently early. It increases NMIR breadth while adding a strong geometric upper-bound problem.

Overall NMIR maturity remains approximately **15–16%**; gravitational focusing branch itself is **~8%** complete.
