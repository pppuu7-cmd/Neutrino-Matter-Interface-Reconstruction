# 0103 magnetic spin-flavor authority audit

Date: 2026-09-12
Status: RESEARCH NOTE — TERMINAL LOCK NOT CREATED
Benchmark: `NMIR-BENCHMARK-0103`
Parent preregistration: `research/prereg/0103_known_model_benchmark_magnetic_spin_flavor_preflight.md`

## Current result

The 0103 authority problem has now been narrowed substantially. The magnetic-moment scale, its mass-basis Majorana transition convention, the mass/flavor representation map, the full three-flavor oscillation-parameter integration, and the generic native-Pencil 3-D magnetic-vector ingestion interface have all been made explicit and machine-tested. The remaining dominant Betelgeuse-specific terminal blocker is the absence of a recoverable path-dependent vector magnetic field from which `B_perp(r)` can be derived without an invented profile.

This is not a physics FAIL.

## 1. Borexino magnetic-moment authority — closed

Reference: M. Agostini et al. (Borexino Collaboration), *Limiting neutrino magnetic moments with Borexino Phase-II solar neutrino data*, Phys. Rev. D 96, 091103(R) (2017), DOI `10.1103/PhysRevD.96.091103`, arXiv `1707.09355v3`.

The paper reports `mu_nu^eff < 2.8e-11 mu_B` at 90% CL and gives individual Majorana transition-moment bounds in the mass basis:

- `|mu_12| <= 2.8e-11 mu_B`
- `|mu_13| <= 3.4e-11 mu_B`
- `|mu_23| <= 5.0e-11 mu_B`

For the conditional six-state Majorana 0103 branch, NMIR prospectively selects the single mass-basis `mu_12` component. The published number is an upper limit, not a measured nonzero moment. Any propagation using the boundary value must be described as an upper-envelope/boundary benchmark.

Byte-level authority is pinned in `research/authority/0103_borexino_majorana_transition_manifest.json` from run `34648625242`, job `103425304459`:

- arXiv v3 PDF SHA256 `e7d5279fc62892832756ea12a3c1e704092774d915d1d9ecf04c7ec8039c259c`;
- arXiv v3 source SHA256 `cb0bbadd01bbbc62399b6bd039f2947509b00499faf0ad85e2194b10332459bb`.

The old synthetic preflight value `mu_nu=1e-11 mu_B` remains only a code fixture and is not physical authority.

## 2. Majorana state-space and basis convention — implementation PASS

The six-state architecture is retained only as a **conditional Majorana transition-moment benchmark**:

`Psi=(nu_e,nu_mu,nu_tau,anti-nu_e,anti-nu_mu,anti-nu_tau)`.

For a Dirac interpretation a helicity flip generally produces a right-handed sterile state, so the current six-active-sector architecture must not be relabelled Dirac.

The dedicated preregistered audit `research/prereg/0103_majorana_mu12_basis_invariance.md` tested the coordinate contract

- `nu_f = U nu_m`,
- `anti_nu_f = U* anti_nu_m`,
- `T6=block_diag(U,U*)`,
- `M_f = U M_m U^T`.

Authoritative execution: run `34649315896`, job `103427496108`, artifact `10283163796`, ZIP SHA256 `95ece0995d7d3dd501b9c023520e1dd0262c7340dedb7c114af965d699228571`.

Status: `PASS_0103_MAJORANA_MU12_BASIS_INVARIANCE_NONTERMINAL`.

Key residuals:

- evolved-state basis residual `4.910462595695867e-16`;
- probability residual `3.3306690738754696e-16`;
- transformed magnetic-block congruence residual `0.0`;
- zero-magnetic-coupling antineutrino leakage `0.0`.

Canonical result: `research/authority/0103_majorana_mu12_basis_invariance_result.md`.

Therefore basis-representation ambiguity is no longer an implementation blocker.

## 3. Full three-flavor oscillation parameters — integration PASS, PDF byte pin pending

The production solar kernel previously contained only the reduced 1-2 MSW parameter subset. For 0103 a full three-flavor parameter layer has now been frozen from NuFIT 6.1, using the `IC24 with SK atmospheric data` fit and carrying **both** normal and inverted mass orderings prospectively.

Canonical manifest: `research/authority/0103_nufit61_three_flavor_manifest.json`.

The ordering rule is strict: both NO and IO are emitted as separate branches and no ordering may be selected after seeing magnetic-propagation results.

Frozen central values:

### Normal ordering

- `sin^2(theta12)=0.3088`
- `sin^2(theta23)=0.470`
- `sin^2(theta13)=0.02248`
- `delta_CP=212 deg`
- `Delta m^2_21=7.537e-5 eV^2`
- `Delta m^2_31=+2.511e-3 eV^2`

### Inverted ordering

- `sin^2(theta12)=0.3088`
- `sin^2(theta23)=0.550`
- `sin^2(theta13)=0.02262`
- `delta_CP=274 deg`
- `Delta m^2_21=7.537e-5 eV^2`
- `Delta m^2_32=-2.483e-3 eV^2`

The preregistered integration audit passed for both orderings in run `34650187509`, job `103430262679`, artifact `10283258274`, ZIP SHA256 `1e2bfdbc68c711dddafaaa1f32050c3976a8ef802ffeda5c3774ecc7a1b179b7`.

Status: `PASS_0103_NUFIT61_PMNS_INTEGRATION_NONTERMINAL`.

All PMNS/T6 unitarity, angle reconstruction, ordering-specific mass-splitting reconstruction, and transformed `mu_12` antisymmetry gates passed. No ordering postselection was used.

Canonical result: `research/authority/0103_nufit61_pmns_integration_result.md`.

### NuFIT TLS caveat

The earlier workflow `.github/workflows/0103-nufit61-authority-pin.yml`, run `34649480505`, did **not** byte-pin the official NuFIT PDFs: GitHub-hosted `curl` rejected the `nu-fit.org` TLS certificate chain. Its green conclusion is infrastructure-only and must not be cited as an authority PASS. The official numerical table has been independently verified and integration-tested, but the NuFIT PDF byte-level pin remains pending.

This is an archival/reproducibility issue, not a physics uncertainty and not a reason to alter the frozen fit values.

## 4. Betelgeuse magnetic-field authority — critical blocker remains

Direct spectropolarimetry establishes a weak, complex surface/atmospheric field of order `1 G`, but this is not the path-dependent transverse internal field required by the spin-flavor Hamiltonian.

The Dorch 2004 Betelgeuse-like nonlinear 3-D MHD publication has been byte-pinned:

- SDU PDF SHA256 `a5ea2282ef2fbac21dd45ca61a7d5887ac890663d5f67eb194c088552ce9a97b`;
- arXiv `astro-ph/0403321v1` PDF SHA256 `43fd08f61cd981fb64ffe2a2b4f126954562273361fc3843b2e31fb5817c6543`.

The publication establishes that a relevant full 3-D MHD model existed, but no released machine-readable vector snapshot containing `B(x,y,z)` plus sufficient coordinate/time metadata has yet been recovered.

Canonical field audit: `research/authority/0103_betelgeuse_vector_field_artifact_audit.md`.

A historical predecessor gives an exact hydrodynamic sequence identifier `dst33gm06n03` (`127^3`, 120 snapshots over 7.5 simulated years), recorded in `research/authority/0103_betelgeuse_dataset_identifier_search.md`. That sequence is hydrodynamic input to an earlier kinematic dynamo calculation and is **not** the nonlinear 2004 magnetic vector state. Recovering it alone would not close 0103 field authority.

The archive search has also recovered indexed Stockholm Observatory FTP traces of Dorch-era material, including papers and PostScript field figures. Figure files are useful provenance evidence but cannot be rasterized into terminal `B_perp(r)` because they do not preserve the required vector field and would introduce reconstruction choices.

A precise external acquisition contract is now frozen in `research/authority/0103_dorch_archive_acquisition_contract.md`. The preferred recovery target is a native Pencil full-state snapshot or full `A(x,y,z)`/`B(x,y,z)` state from the nonlinear run, ideally around the published `t=695 yr` or `t=732 yr` states, together with grid, units and run metadata. The original author/institutional route remains actionable, so the branch is not yet classified as permanently data-limited.

## Why surface/figure information is insufficient

The spin-flavor Hamiltonian requires the magnetic-field component transverse to the neutrino trajectory at each propagation point. A surface-averaged longitudinal measurement, a quoted simulated surface amplitude, or a plotted surface map does not provide:

- a machine-readable internal vector field;
- vector orientation relative to the chosen ray;
- sign/domain structure along the path;
- an immutable numerical snapshot co-registered with the matter profile.

Therefore the following remain prohibited for a Betelgeuse-specific terminal claim:

- `B=1 G` everywhere;
- arbitrary dipole/radial/power-law extrapolation;
- raster extraction from Dorch figures;
- promoting a simulated hundreds-of-gauss surface amplitude to Betelgeuse's true internal field;
- silently replacing the missing Dorch state with a different star-in-a-box calculation.

## 5. Native Pencil 3-D vector ingestion — PASS on a separate surrogate

The model-conditional benchmark `NMIR-BENCHMARK-0103S` was preregistered specifically to answer whether the NMIR workflow can consume an authentic native Pencil MHD state without inventing a radial field law.

External source: pinned `pencil-code/pencil-code` commit `1a672b5cb2983b3e286503a789dd36bf7d6d1141`, sample `samples/mdwarf`.

The first execution successfully built and ran the MHD sample but failed only because the Python postprocessor lacked `matplotlib`. The rerun changed only reader dependencies; no physical sample setting or gate changed.

Authoritative run `34650666488`, job `103431814298`, artifact `10283931487`, ZIP SHA256 `3711dc174eb4d9eb8e8dd4ff09f0e9a65f8be6aee7c84bd7ae7f896ef4403482` passed all preregistered gates.

Status: `PASS_0103S_PENCIL_MDWARF_VECTOR_INTERFACE_NONTERMINAL`.

The official pinned Pencil reader derived `bb=curl(aa)` from the native final snapshot:

- `bb_shape=[3,32,32,32]`;
- coordinate extents `[-1.5,1.5]` on all axes;
- all components finite;
- nonzero field present;
- `|B|_max=4.687900321192166e-05` code units;
- RMS `|B|=4.490911276462364e-06` code units.

Canonical result: `research/authority/0103s_pencil_mdwarf_vector_interface_result.md`.

This proves that the remaining 0103 obstacle is **not** a generic inability to read a native Pencil 3-D magnetic state. The unresolved issue is the physical/data authority of the Betelgeuse-specific vector state.

Strict scope: 0103S is a fully-convective-star regression fixture, not Betelgeuse and not the Dorch 2004 nonlinear run.

## 6. Prospectively frozen next interface tests

Two additional model-conditional audits have been preregistered without changing Betelgeuse authority:

### 0103G — giant-star native vector interface

`research/prereg/0103g_pencil_giant_vector_interface.md` freezes the public Pencil `samples/star-in-a-box-giant-Kprof` model at the same external commit. It is a `64^3` MHD giant-star sphere-in-a-box sample using the `RGB-1Msun-11.7` gravity potential. The first execution was infrastructure-only blocked because the hosted runner lacked OpenMPI (`mpirun` and `mpif.h`); physical sample-file hashes were recorded before the failure. A rerun installs OpenMPI only and leaves all four frozen sample files unchanged.

0103G remains model-conditional and cannot become Betelgeuse authority.

### 0103P — deterministic vector-to-pathwise-`B_perp` geometry

`research/prereg/0103p_pencil_pathwise_bperp_interface.md` freezes a central x-directed ray through the already reproducible mdwarf sphere, exact target `y=z=0`, a fixed bilinear transverse interpolation rule, and

`B_perp=sqrt(By^2+Bz^2)`

with an independent invariant check `B_perp^2=|B|^2-(B dot n)^2`.

This test is intended to remove ray/interpolation postselection from the technical interface before any Betelgeuse vector state is obtained.

## Current authority classification

- `MAGNETIC_MOMENT_SCALE_AUTHORITY`: **AVAILABLE**.
- `MASS_BASIS_MAJORANA_TRANSITION_ELEMENT_AUTHORITY`: **BYTE-PINNED**.
- `PROSPECTIVE_0103_TRANSITION_COMPONENT`: **FROZEN TO SINGLE MASS-BASIS mu_12**.
- `DIRAC_MAJORANA_CONVENTION`: **CONDITIONAL MAJORANA BRANCH FROZEN; NOT AN EMPIRICAL CLAIM**.
- `MAJORANA_MU12_BASIS_INVARIANCE`: **PASS**.
- `FULL_3FLAVOR_NUFIT61_NUMERIC_INTEGRATION`: **PASS FOR BOTH NO AND IO**.
- `NUFIT61_OFFICIAL_PDF_BYTE_PIN`: **PENDING — TLS INFRASTRUCTURE BLOCK ONLY**.
- `GENERIC_NATIVE_PENCIL_3D_VECTOR_INGESTION`: **PASS_0103S**.
- `GIANT_STAR_PENCIL_VECTOR_INTERFACE`: **PREREGISTERED; INITIAL RUN INFRASTRUCTURE-BLOCKED BY MISSING MPI; INFRASTRUCTURE-ONLY RERUN ACTIVE**.
- `PATHWISE_BPERP_EXTRACTION_INTERFACE`: **PREREGISTERED / ACTIVE**.
- `BETELGEUSE_3D_MHD_PUBLICATION_AUTHORITY`: **BYTE-PINNED**.
- `BETELGEUSE_SURFACE_FIELD_AUTHORITY`: **AVAILABLE AS BOUNDARY EVIDENCE**.
- `BETELGEUSE_MACHINE_READABLE_3D_VECTOR_SNAPSHOT`: **NOT RECOVERED**.
- `BETELGEUSE_INTERNAL B_perp(r) AUTHORITY`: **BLOCKED**.
- `DORCH_ORIGINAL_AUTHOR_ARCHIVE_ACQUISITION_ROUTE`: **ACTIONABLE**.

Current narrow terminal status:

`BLOCKED_0103_BETELGEUSE_PATHWISE_VECTOR_FIELD_AUTHORITY`

No physics FAIL is inferred.

## Next deterministic tasks

1. Complete the preregistered 0103G giant-vector and 0103P pathwise-geometry audits without altering their frozen scientific configurations.
2. Continue the targeted acquisition route for the Dorch/Pencil-Code nonlinear Betelgeuse vector state, prioritizing native snapshots/full vector arrays over figures or scalar summaries.
3. If a historical Betelgeuse vector snapshot is recovered, byte-pin it and apply a separately frozen Betelgeuse ray/orientation/regridding/co-registration contract before computing any spin-flavor probability.
4. If the actionable author/institution archive route is exhausted without recovery, classify the **Betelgeuse-specific** terminal branch as externally data-limited rather than fabricate `B_perp(r)`.
5. Keep all surrogate results explicitly model-conditional; they validate machinery but cannot be promoted to empirical Betelgeuse predictions.
