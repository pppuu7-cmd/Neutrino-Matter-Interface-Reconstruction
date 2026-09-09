# NMIR v2 Recovery — known-progenitor G9 branch

Last reconciled: 2026-09-09
Repository: `pppuu7-cmd/Neutrino-Matter-Interface-Reconstruction`

## Immutable parent
NMIR v1 is closed at `NMIR_READINESS: 100%` under `research/NMIR_V1_READINESS_100_CONTRACT.md` and `research/iterations/0095_nmir_v1_readiness_100_closure.md`. Nothing in v2 relabels any v1 PASS/FAIL/BLOCKED classification.

The v2 branch is motivated by the explicit scope guard in 0094: its generic-future-10-kpc-CCSN actionability FAIL is not a no-go for a specifically monitored nearby progenitor with pre-positioning or a different observer architecture.

## 0096 — Betelgeuse central-support certification
Preregistration:
- file `research/prereg/0096_v2_g9_betelgeuse_central_support_certification.md`
- frozen prereg commit `5e8048a3d77b504bba6a79a077a1c9e153f8cb19`

Frozen source-position envelope:
- Betelgeuse benchmark, already named prospectively in 0094;
- `beta_target = 50 mas = 0.050 arcsec` radial envelope;
- source-distance controls 190 pc and 222 pc from Harper et al. 2017;
- neutrino-source radii 21 km and 100 km inherited from NMIR CCSN authority;
- 3 inherited observer-distance controls x 3 receiver radii x 2 source distances x 2 source radii = 36 families;
- 4097 fixed linear radial offsets per primary family over `[0,d_target(z)]`;
- global worst primary family must be rerun on the fixed 8193-point sensitivity grid;
- inherited 0090e/0090f ray-centric finite-source/finite-receiver evaluator only.

Frozen terminal labels include `PASS_V2_G9_BETELGEUSE_CENTRAL_SUPPORT_50MAS`, `SCIENTIFIC_FAIL_V2_G9_BETELGEUSE_CENTRAL_SUPPORT_50MAS`, source-authority BLOCKED, and infrastructure FAIL.

Implementation provenance:
- parent ray-centric evaluator blob pinned to `4bedc9431b428292f1b09613f603bea82597f9b5`;
- initial implementation was performance-audited before any scientific result;
- science grid was not changed; work was repartitioned from 9 large jobs into 36 one-family primary jobs and four deterministic sensitivity chunks whose union is exactly all 8193 frozen nodes;
- current script commit `146b1ddace20f68e322fdb907da84928ca0e1cb2`;
- current aggregator commit `02a00d64a50a2c38d10ca994fe5e50fcd07c35b9`;
- current workflow commit/head `eff5996612f31c093e82a9ae0cdfdb859da8cb9a`.

Authoritative 0096 Actions run:
- workflow `0096 v2 G9 Betelgeuse central support`;
- run id `34319781596`;
- authoritative head `eff5996612f31c093e82a9ae0cdfdb859da8cb9a`.

Only that run is authoritative for the current 0096 implementation. Earlier transitional runs `34319282089`, `34319699247`, and `34319741478` must not be used for a terminal science verdict.

State at this reconciliation: primary family jobs are running/queued and no authoritative 0096 artifact has yet been produced. Do not infer PASS from preregistration, code, job progress, or the descriptive 0093 first crossing.

## 0097 — conditional Betelgeuse line-tracking architecture gate
Preregistration:
- file `research/prereg/0097_v2_g9_betelgeuse_line_tracking_architectures.md`
- prereg commit `53863048c2d5b5803c9e120794c21fe415f1b319`
- frozen before the 0096 result was known.

Execution condition:
- run only if 0096 returns `PASS_V2_G9_BETELGEUSE_CENTRAL_SUPPORT_50MAS`;
- otherwise terminally record `NOT_RUN_V2_G9_0097_PARENT_NOT_PASSED`;
- 0097 may use only the preregistered 50-mas support even if 0096 later reveals a much wider numerical region.

Architecture A: ideal active heliocentric line tracking over exactly 10 Julian years. Frozen source astrometry from Harper et al. 2017: `mu_alpha*cos(delta)=26.42 +/- 0.25 mas/yr`, `mu_delta=9.60 +/- 0.12 mas/yr`, conservative 2.4-mas cosmic-noise term per coordinate. Three-sigma propagated source-center authority must remain within 50 mas. Compute solar-gravity hover acceleration, ten-year ideal hover delta-v, transverse proper-motion tracking speed and acceleration. Finite kinematics is not engineering feasibility.

Architecture B: most favorable single passive circular heliocentric orbit whose plane contains the source-Sun line. Compute exact/linear crossing duration, two crossings per orbit, passive duty fraction and ideal equal-phase node count for continuous coverage. A pre-SN alert cannot rescue an observer already out of orbital phase.

Implementation:
- script `scripts/g9_betelgeuse_line_tracking_0097.py`, commit `a882aa0d0e02882499cd8bc0d945c89a479985dd`;
- conditional workflow `.github/workflows/0097-v2-g9-betelgeuse-line-tracking.yml`, commit `b6ba9bb76fe31348a3228888db1ad207d468c283`;
- automatic trigger is gated specifically to authoritative 0096 head `eff5996612f31c093e82a9ae0cdfdb859da8cb9a`, preventing superseded 0096 runs from launching 0097.

Constants frozen in implementation:
- astronomical unit `149597870700 m`, exact under IAU 2012 Resolution B2;
- nominal solar mass parameter `(GM)^N_sun = 1.3271244e20 m^3 s^-2`, exact nominal conversion constant under IAU 2015 Resolution B3.

Pre-result diagnostic only, not terminal authority: for z about 24 AU, 50 mas is about 870 km transverse radius; the frozen 10-year astrometric 3-sigma envelope evaluates to about 13.15 mas; ideal solar-gravity hover demand is about 3.2 km/s delta-v over 10 yr; a single circular passive orbit crosses the +/-50-mas corridor for only about 4.8 minutes per passage and has duty fraction about 1.54e-7. These values must not be promoted to the 0097 terminal result until the parent PASS and authoritative 0097 artifact exist.

## External authority already frozen
- Harper et al., `An Updated 2017 Astrometric Solution for Betelgeuse`, arXiv:1706.06020: 2.4-mas cosmic noise, nominal 222 pc solution, 190 pc sensitivity solution, about 44-mas stellar angular diameter, proper-motion authority above.
- KamLAND + Super-Kamiokande, `Combined Pre-Supernova Alert System with KamLAND and Super-Kamiokande`, arXiv:2404.09920: an operational combined pre-SN alert system; optimistic Betelgeuse-like model may provide warning up to about 12 h. This is context only, not proof that a spacecraft can be sent to 24 AU after the alert.

## Exact next actions
1. Inspect authoritative run `34319781596` only.
2. When `nmir-v2-g9-0096-authoritative` exists, download and independently hash `g9_0096_result.json`.
3. Verify 36 primary families, 4097 primary nodes per family, exactly 8193-node sensitivity union, global-worst-family identity, parent evaluator/blob provenance, and terminal status.
4. Commit an immutable 0096 iteration record with run/job/artifact IDs and hashes.
5. If and only if 0096 PASS, allow the already-preregistered 0097 workflow to execute and independently validate its artifact. If 0096 does not PASS, do not shrink the 50-mas envelope or substitute a different progenitor inside 0097.
6. Only after 0097 is terminal decide prospectively whether a separate engineering-authority gate or a new MeV solar-transport authority gate is the highest-value v2 continuation.

## Critical interpretation guards
- Betelgeuse's ~44-mas photospheric diameter is not the neutrino-source size; the neutrino-emitting core remains the frozen 21/100-km physical source control.
- A 50-mas PASS would certify only numerical central alignment support, not global 0093 topology.
- Finite active stationkeeping kinematics is not spacecraft feasibility.
- A pre-SN alert is not equivalent to post-alert ability to deploy to 24 AU.
- Do not infer explosion timing/probability for Betelgeuse.
- Do not reopen the v1 MeV solar-transport BLOCKED result without a new prospective authority route.
- Never equate lens magnification with detector event gain, interaction gain, deposited energy, or useful power.
