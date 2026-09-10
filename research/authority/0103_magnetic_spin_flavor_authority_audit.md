# 0103 magnetic spin-flavor authority audit

Date: 2026-09-10
Status: RESEARCH NOTE — TERMINAL LOCK NOT CREATED
Benchmark: `NMIR-BENCHMARK-0103`
Parent preregistration: `research/prereg/0103_known_model_benchmark_magnetic_spin_flavor_preflight.md`

## Question

Can the 0103 magnetic spin-flavor benchmark be moved from a generic two-input authority block to a finite set of separately testable moment, basis/convention, and magnetic-field-profile authority gates?

## Result

Yes. The authority problem separates cleanly into three distinct layers:

1. **MAGNETIC_MOMENT_AUTHORITY** — an experimentally bounded magnetic/transition moment with an explicit basis and statistical convention;
2. **DIRAC_MAJORANA_AND_BASIS_CONVENTION** — the six-state NMIR coupling must be tied to a physical interpretation rather than only a synthetic matrix;
3. **FIELD_PROFILE_AUTHORITY** — a path-dependent transverse field `B_perp(r)` with geometry/orientation provenance, not merely a photospheric field-strength measurement.

None of these layers may be substituted for another.

## Borexino magnetic-moment authority

A robust experimental reference is the Borexino Phase-II solar-neutrino analysis:

- M. Agostini et al. (Borexino Collaboration), *Limiting neutrino magnetic moments with Borexino Phase-II solar neutrino data*, Phys. Rev. D 96, 091103(R) (2017).
- DOI: `10.1103/PhysRevD.96.091103`.
- Reported effective solar-neutrino limit: `mu_nu^eff < 2.8e-11 mu_B` at 90% CL.

The publication explicitly distinguishes Dirac and Majorana moment matrices. For Majorana neutrinos the magnetic-moment matrix is antisymmetric and only transition moments are allowed; for Dirac neutrinos the matrix is general.

### Specific Majorana transition-element bounds in the mass basis

The same Borexino paper writes the effective solar-neutrino moment in the mass-eigenstate basis and, because the relevant terms enter as positive contributions for the incoherent solar mixture, derives individual 90% CL upper bounds (units `1e-11 mu_B`):

- `|mu_12| <= 2.8`
- `|mu_13| <= 3.4`
- `|mu_23| <= 5.0`

These are materially stronger authority candidates for NMIR 0103 than treating the scalar `mu_nu^eff` as if it were a transition-matrix element.

### Interpretation guard

The Borexino transition bounds above are given in the **mass basis**. The frozen synthetic 0103 transition matrix is described as an `e-mu` transition-flavor matrix. Therefore even these specific experimental bounds cannot be inserted directly into the current matrix without prospectively declaring and validating the basis transformation.

The preflight value `mu_nu = 1e-11 mu_B` remains only a mathematical fixture. Its numerical location below the published transition-element upper bounds does not turn the synthetic flavor-basis matrix into an experimentally authorized terminal point.

## Basis/convention issue exposed by the audit

The 0103 preflight uses

`Psi = (nu_e, nu_mu, nu_tau, anti-nu_e, anti-nu_mu, anti-nu_tau)`

and an antisymmetric synthetic transition-flavor matrix. This is deliberately acceptable for a code-path preflight, but a terminal physical claim needs more specificity.

For a **Majorana transition-moment** interpretation, an antisymmetric magnetic-moment matrix is structurally natural and spin-flavor conversion may connect neutrino and antineutrino sectors. For a **Dirac** interpretation, a helicity flip generally produces a right-handed sterile state rather than an active antineutrino state, so the present six-active-sector interpretation cannot simply be relabelled Dirac without an amended state-space contract.

**Recommended terminal branch:** if 0103 is kept on the present six-state `nu/anti-nu` architecture, preregister it explicitly as a Majorana transition-moment benchmark. Prefer a mass-basis single-transition fixture tied directly to one of the Borexino bounds, or freeze an exact unitary basis transformation and demonstrate probability-level basis invariance before translating that bound into a flavor-basis magnetic block.

This is a convention clarification, not evidence that neutrinos are Majorana particles.

## Betelgeuse magnetic-field authority

Direct spectropolarimetry provides genuine evidence for a weak magnetic field at Betelgeuse's surface/atmosphere:

- Auriere et al. (2010) reported the first direct detection, with a surface-averaged longitudinal field of order `1 G`.
- Subsequent monitoring over 2009-2017 continued to find fields of order `1 G` and variable polarization signatures, consistent with a complex convective/local-dynamo origin.
- A 2023 review summarizes Betelgeuse atmospheric magnetic fields as approximately `1 G` from circular-polarization/Zeeman measurements.

This is useful boundary information, but it is **not** a terminal `B_perp(r)` profile.

### Why the surface measurement does not close FIELD_PROFILE_AUTHORITY

The frozen spin-flavor Hamiltonian depends on the magnetic-field component transverse to the neutrino path at each propagation point. A surface-averaged longitudinal line-of-sight measurement supplies neither:

- the internal radial dependence of field magnitude;
- the vector orientation relative to the neutrino trajectory;
- the sign/domain structure;
- a unique continuation from interior to photosphere;
- an immutable stellar-model snapshot co-registered with the `rho(r), Ye(r)` source profile.

Therefore substituting `B=1 G` everywhere, extrapolating it inward by an arbitrary power law, or identifying a longitudinal photospheric field with `B_perp` would violate the NMIR authority discipline.

## Model-based magnetic profiles

Published MHD/wind and local-dynamo models for Betelgeuse do exist. Some take an observed surface field of order `1 G` as an input and predict circumstellar/wind magnetic structure, while convection-driven dynamo calculations generate nontrivial internal/surface fields.

These are candidate *model authorities*, not direct measurements of a unique radial field. A future terminal branch may use such a profile only if all of the following are frozen prospectively:

1. exact publication/model identity;
2. exact numerical profile or reproducible simulation artifact;
3. stellar parameters/snapshot;
4. coordinate/basis definition of the magnetic vector;
5. mapping to the neutrino path and `B_perp(r)`;
6. compatibility or explicit regridding against the pinned NMIR `rho(r), Ye(r)` source snapshot;
7. uncertainty/stress-test semantics.

## Current authority classification

- `MAGNETIC_MOMENT_SCALE_AUTHORITY`: **AVAILABLE**.
- `MASS_BASIS_MAJORANA_TRANSITION_ELEMENT_AUTHORITY`: **AVAILABLE AS PUBLISHED NUMERIC AUTHORITY; BYTE-LEVEL PIN STILL REQUIRED**.
- `FLAVOR_TO_MASS_BASIS_MAPPING_FOR_0103`: **NOT YET FROZEN/VALIDATED**.
- `DIRAC_MAJORANA_TERMINAL_CONVENTION`: **NOT YET FROZEN**.
- `BETELGEUSE_SURFACE_FIELD_AUTHORITY`: **AVAILABLE AS BOUNDARY EVIDENCE**.
- `BETELGEUSE_INTERNAL B_perp(r) AUTHORITY`: **NOT YET PINNED**.

Overall terminal status therefore remains

`BLOCKED_0103_MAGNETIC_AND_FIELD_AUTHORITY_UNPINNED`.

No physics FAIL is inferred.

## Strong methodological consequence

The 0103 funnel should reject a common but invalid shortcut:

> `mu_nu` has an experimental upper limit and Betelgeuse has an observed ~1 G surface field, therefore a terminal spin-flavor prediction can be run.

That conclusion does not follow. The experiment constrains an effective or basis-resolved moment, while the stellar measurement constrains a surface-projected field. The propagation observable requires a correctly mapped transition moment and a path-resolved transverse magnetic field.

## Next deterministic tasks

1. Byte-pin the Borexino authority and prospectively choose one mass-basis Majorana transition component (or freeze/test the exact basis transform to the existing flavor-basis representation).
2. Identify a reproducible Betelgeuse stellar/dynamo/MHD artifact that contains vector magnetic-field information across the relevant propagation region, rather than only a photospheric scalar measurement.
3. Only after both are pinned, preregister the Majorana/basis transformation and terminal `B_perp(r)` extraction rule and create `research/locks/0103_magnetic_field_terminal_lock.json` (or a successor lock schema that separately hashes moment and field authority).
