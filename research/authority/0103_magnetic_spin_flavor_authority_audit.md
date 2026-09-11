# 0103 magnetic spin-flavor authority audit

Date: 2026-09-12
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
- arXiv: `1707.09355v3`.
- Reported effective solar-neutrino limit: `mu_nu^eff < 2.8e-11 mu_B` at 90% CL.

The publication explicitly distinguishes Dirac and Majorana moment matrices. For Majorana neutrinos the magnetic-moment matrix is antisymmetric and only transition moments are allowed; for Dirac neutrinos the matrix is general.

### Specific Majorana transition-element bounds in the mass basis

The same Borexino paper writes the effective solar-neutrino moment in the mass-eigenstate basis and, because the relevant terms enter as positive contributions for the incoherent solar mixture, derives individual 90% CL upper bounds (units `1e-11 mu_B`):

- `|mu_12| <= 2.8`
- `|mu_13| <= 3.4`
- `|mu_23| <= 5.0`

These are materially stronger authority candidates for NMIR 0103 than treating the scalar `mu_nu^eff` as if it were a transition-matrix element.

### Byte-level authority pin completed

The dedicated authority probe `.github/workflows/0103-authority-pin-probe.yml` completed successfully at run `34648625242`, job `103425304459`, head `a39f6444fd87d522f1d298d117859c1d95f077e5`, artifact `10282473288`.

Pinned Borexino payloads:

- arXiv v3 PDF: 536898 bytes, SHA256 `e7d5279fc62892832756ea12a3c1e704092774d915d1d9ecf04c7ec8039c259c`;
- arXiv v3 source bundle: 92917 bytes, SHA256 `cb0bbadd01bbbc62399b6bd039f2947509b00499faf0ad85e2194b10332459bb`;
- uploaded probe artifact ZIP SHA256 `8a862ab55dc505c471aa7acd5976459d6a94779b75ced3dd664fe2be67d361ee`.

Canonical machine-readable record: `research/authority/0103_borexino_majorana_transition_manifest.json`.

### Prospective benchmark component

For the present six-state Majorana conditional branch, NMIR now selects a **single mass-basis `mu_12` transition component** for the next terminally eligible benchmark design. This avoids pretending that the scalar effective limit is a flavor-basis matrix element and avoids an unnecessary magnetic-moment flavor-to-mass inference.

The published `|mu_12| <= 2.8e-11 mu_B` value is an **upper-limit authority**, not a measured central value. A future propagation calculation may use the boundary value only if it is preregistered explicitly as an upper-envelope/boundary benchmark. Such use cannot be worded as evidence for a nonzero moment.

### Interpretation guard

The Borexino transition bounds are given in the **mass basis**. The frozen synthetic 0103 preflight transition matrix is described as an `e-mu` transition-flavor matrix. The published value therefore still may not be inserted directly into that old magnetic block.

For terminal work, either:

1. formulate the magnetic interaction as the single `mu_12` transition in a common mass-basis representation while transforming all other Hamiltonian terms consistently; or
2. freeze an exact unitary transformation and demonstrate probability-level basis invariance before translating the interaction into a flavor-basis implementation.

The preflight value `mu_nu = 1e-11 mu_B` remains only a mathematical fixture and is not promoted to terminal physical authority.

## Basis/convention issue exposed by the audit

The 0103 preflight uses

`Psi = (nu_e, nu_mu, nu_tau, anti-nu_e, anti-nu_mu, anti-nu_tau)`

and an antisymmetric synthetic transition-flavor matrix. This remains acceptable for code-path preflight, but a terminal physical claim needs an explicit conditional particle convention.

For a **Majorana transition-moment** interpretation, an antisymmetric magnetic-moment matrix is structurally natural and spin-flavor conversion may connect neutrino and antineutrino sectors. For a **Dirac** interpretation, a helicity flip generally produces a right-handed sterile state rather than an active antineutrino state, so the present six-active-sector interpretation cannot simply be relabelled Dirac without an amended state-space contract.

**Prospective 0103 branch decision:** preserve the current six-state `nu/anti-nu` architecture only as a **conditional Majorana transition-moment benchmark** and use the single mass-basis `mu_12` authority above. This is a benchmark convention, not evidence that neutrinos are Majorana particles.

A dedicated basis-invariance implementation test is still required before terminal propagation.

## Betelgeuse magnetic-field authority

Direct spectropolarimetry provides genuine evidence for a weak magnetic field at Betelgeuse's surface/atmosphere:

- Auriere et al. (2010) reported the first direct detection, with a surface-averaged longitudinal field of order `1 G`.
- Subsequent monitoring continued to find fields of order `1 G` with complex variable signatures.

This is useful boundary information, but it is **not** a terminal `B_perp(r)` profile.

### Pinned 3-D MHD publication authority

The 0103 authority probe also byte-pinned the Dorch 2004 Betelgeuse-like full 3-D MHD publication:

- SDU PDF: 682550 bytes, SHA256 `a5ea2282ef2fbac21dd45ca61a7d5887ac890663d5f67eb194c088552ce9a97b`;
- arXiv `astro-ph/0403321v1` PDF: 582957 bytes, SHA256 `43fd08f61cd981fb64ffe2a2b4f126954562273361fc3843b2e31fb5817c6543`.

The paper establishes a relevant `star-in-a-box` 3-D MHD model and reports nonlinear dynamo fields, but the authority recovered so far does **not** include a released machine-readable numerical vector snapshot from which NMIR can reconstruct `B(x,y,z)` along a neutrino ray.

Canonical audit: `research/authority/0103_betelgeuse_vector_field_artifact_audit.md`.

### Why the surface measurement or publication figures do not close FIELD_PROFILE_AUTHORITY

The spin-flavor Hamiltonian depends on the magnetic-field component transverse to the neutrino path at each propagation point. A surface-averaged longitudinal measurement, a quoted simulated surface amplitude, or a plotted surface map supplies neither:

- a machine-readable internal vector field;
- the vector orientation relative to the neutrino trajectory;
- the sign/domain structure along the path;
- an immutable numerical snapshot co-registered with the `rho(r), Ye(r)` source profile.

Therefore substituting `B=1 G` everywhere, extrapolating it inward by an arbitrary power law, rasterizing a published figure, or promoting the Dorch saturated surface amplitude to the true Betelgeuse interior field would violate the NMIR authority discipline.

## Current authority classification

- `MAGNETIC_MOMENT_SCALE_AUTHORITY`: **AVAILABLE**.
- `MASS_BASIS_MAJORANA_TRANSITION_ELEMENT_AUTHORITY`: **BYTE-PINNED**.
- `PROSPECTIVE_0103_TRANSITION_COMPONENT`: **FROZEN TO SINGLE MASS-BASIS mu_12 FOR CONDITIONAL MAJORANA BENCHMARK DESIGN**.
- `DIRAC_MAJORANA_TERMINAL_CONVENTION`: **CONDITIONAL MAJORANA BRANCH SELECTED; NOT AN EMPIRICAL CLAIM**.
- `BASIS_INVARIANCE_IMPLEMENTATION_TEST`: **STILL REQUIRED BEFORE TERMINAL PROPAGATION**.
- `BETELGEUSE_3D_MHD_PUBLICATION_AUTHORITY`: **BYTE-PINNED**.
- `BETELGEUSE_SURFACE_FIELD_AUTHORITY`: **AVAILABLE AS BOUNDARY EVIDENCE**.
- `BETELGEUSE_MACHINE_READABLE_3D_VECTOR_SNAPSHOT`: **NOT RECOVERED**.
- `BETELGEUSE_INTERNAL B_perp(r) AUTHORITY`: **BLOCKED**.

The old broad status `BLOCKED_0103_MAGNETIC_AND_FIELD_AUTHORITY_UNPINNED` is superseded.

Current narrow status:

`BLOCKED_0103_BETELGEUSE_PATHWISE_VECTOR_FIELD_AUTHORITY`

No physics FAIL is inferred.

## Strong methodological consequence

The 0103 funnel should reject a common but invalid shortcut:

> `mu_nu` has an experimental upper limit and Betelgeuse has an observed ~1 G surface field, therefore a terminal spin-flavor prediction can be run.

That conclusion does not follow. The moment authority is now reproducibly pinned, but the propagation observable still requires a path-resolved transverse magnetic field. Publication-level evidence that a 3-D MHD model exists is not equivalent to release of its numerical vector state.

## Next deterministic tasks

1. Add a small basis-invariance test for the chosen conditional Majorana `mu_12` implementation, without running any Betelgeuse terminal prediction.
2. Conduct a dedicated archive/source search for a released Dorch/Pencil-Code or successor Betelgeuse-like numerical vector snapshot exposing `B(x,y,z)` and coordinates.
3. If a suitable snapshot is recovered, byte-pin it and preregister the ray/orientation/regridding rule before computing probabilities.
4. If no suitable numerical vector authority can be recovered, close the present Betelgeuse-specific branch as externally data-limited; do **not** fabricate `B_perp(r)`.
5. Keep any future synthetic magnetic-profile stress test as a separately labeled model-conditional benchmark, not as a Betelgeuse prediction.
