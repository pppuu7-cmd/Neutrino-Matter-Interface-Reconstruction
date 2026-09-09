# Preregistration 0096 — NMIR v2 G9 Betelgeuse central-support certification

Date frozen: 2026-09-09
Branch: NMIR v2

## Purpose
Open NMIR v2 without modifying any NMIR v1 classification. Test whether the already validated G9 solar-neutrino focusing map contains a **prospectively certified contiguous central region** large enough to cover a conservative astrometric envelope for a specifically known nearby CCSN progenitor benchmark.

The source benchmark is **Betelgeuse (alpha Orionis)** because Betelgeuse was already named prospectively in the frozen 0094 authority set as the canonical nearby pre-supernova alert example. This is not a post-result search over favorable stars.

This gate addresses only geometry/topology near the exact source-Sun-observer axis. It does not claim solar MeV transparency, detector event gain, useful power, spacecraft feasibility, explosion-date predictability, or complete mission actionability.

## Immutable v1 parents
- NMIR v1 closure: `research/iterations/0095_nmir_v1_readiness_100_closure.md`.
- NMIR v1 remains `NMIR_READINESS: 100%` under its own frozen scope.
- 0090f: `PASS_G9_FULL_GRID_FINITE_NONZERO_SURVIVORS`.
- 0093: `BLOCKED_G9_CCSN_ALIGNMENT_TOPOLOGY`; 39 sampled re-entries prohibit promoting its sparse full-range scan to a global monotone footprint.
- 0094: `SCIENTIFIC_FAIL_G9_CCSN_PROSPECTIVE_ACTIONABILITY_V1`, scoped to one observer + generic future 10-kpc CCSN + frozen v1 authority. 0094 explicitly does not establish a no-go for a specifically monitored nearby progenitor or a different v2 architecture.

No v1 result may be relabeled by this gate.

## Frozen external source authority
Use the following source-side authority only to define the pre-computation alignment envelope:

1. G. M. Harper et al., `An Updated 2017 Astrometric Solution for Betelgeuse`, arXiv:1706.06020. The combined optical/radio solution discusses a characteristic astrometric `Cosmic Noise` scale of 2.4 mas and a stellar angular diameter of about 44 mas.
2. KamLAND + Super-Kamiokande, `Combined Pre-Supernova Alert System with KamLAND and Super-Kamiokande`, arXiv:2404.09920. Betelgeuse-like models are an explicitly studied nearby pre-SN benchmark and may provide hours of early warning; this authority is context only in 0096 and is not used to claim mission timing PASS.

## Frozen Betelgeuse angular envelope
Define a deliberately conservative **50 mas radial alignment envelope** around the adopted stellar astrometric center before seeing the 0096 lens calculation.

Rationale: 50 mas is larger than the cited ~44 mas full photospheric diameter and much larger than the 2.4 mas astrometric cosmic-noise scale. Treating an entire 50 mas radius as the target envelope is intentionally conservative; it must not later be tightened to obtain PASS.

`beta_target = 50 mas = 0.050 arcsec` exactly for this gate.

Convert with the exact arcsecond-to-radian relation and the inherited frozen observer distances from the validated G9 map. For each observer distance `z`, define

`d_target(z) = z * AU * tan(beta_target)`.

The gate must report the target transverse radius for every inherited observer-distance control. No small-angle replacement is required, although the small-angle value may be reported as a check.

## Frozen source-size controls
Do not introduce a new stellar-photosphere source size into the neutrino lens convolution. The neutrino-emitting core remains the source object.

Use two physical neutrino-emission radius controls already frozen in NMIR:
- 21 km fiducial CCSN neutrino-source radius;
- 100 km conservative CCSN neutrino-source radius.

For the Betelgeuse distance conversion, use the Harper et al. nominal radio+HIAD distance solution `222 pc` as the primary source distance and `190 pc` as a sensitivity control from the radio-proper-motion/HIAD solution quoted in the same authority. Convert these physical radii to angular source radii explicitly. Both must remain inside the already validated 0090f angular source-size support before the gate can proceed.

No distance may be selected after seeing magnification results.

## Frozen receiver / observer family
Use the same three observer-distance controls and the same three receiver-radius controls inherited by 0093. Do not add or remove a family after seeing results.

The Cartesian family is therefore:
- 3 inherited observer distances;
- 3 inherited receiver radii;
- 2 Betelgeuse distance controls (190 pc, 222 pc);
- 2 neutrino-source radii (21 km, 100 km).

Total: 36 families.

## Prospective central-certification grid
The purpose is to certify only the compact interval required by the frozen 50-mas source-position envelope, not to repair or reinterpret the entire 0093 topology.

For each family evaluate magnification on a deterministic radial offset grid over

`d in [0, d_target(z)]`.

Use exactly 4097 linearly spaced radial offsets including both endpoints. The 4097-point choice is frozen before execution and may not be increased after seeing the result inside 0096.

At every radial point use the inherited ray-centric finite-source/finite-receiver evaluator and its frozen numerical settings from the successful 0090e-r1/0090f path. No source-centered convolution may be revived.

In addition, independently evaluate the exact endpoint `d_target(z)` and exact axis `d=0` with the same evaluator and record both values.

## Numerical convergence control
For the family with the smallest sampled magnification, rerun that family on an independently frozen sensitivity grid of exactly 8193 linearly spaced offsets over the same interval, without changing any lens quadrature/order/tolerance.

Define
- `mu_min_4097` = minimum magnification on the primary grid;
- `mu_min_8193` = minimum magnification on the sensitivity grid.

Require both minima to be >=2 for a scientific PASS. Report their relative difference as a diagnostic; do not average them.

If either grid exposes any `mu<2`, the gate FAILS for the 50-mas envelope. A later v2 gate may study a smaller envelope only if prospectively justified by new external source-position authority; it may not silently shrink 50 mas here.

## Frozen classifications
`PASS_V2_G9_BETELGEUSE_CENTRAL_SUPPORT_50MAS` iff all conditions hold:
- every physical source angular radius lies inside the inherited 0090f validated theta range;
- all 36 primary families complete;
- every one of the 4097 primary offsets in every family has `mu>=2`;
- exact-axis and exact-endpoint values have `mu>=2` in every family;
- the independently rerun 8193-point sensitivity family also has `mu_min>=2`;
- provenance and deterministic output hashes are preserved.

`SCIENTIFIC_FAIL_V2_G9_BETELGEUSE_CENTRAL_SUPPORT_50MAS` if any valid family/grid point has `mu<2` inside the frozen 50-mas interval.

`BLOCKED_V2_G9_BETELGEUSE_SOURCE_AUTHORITY` if the frozen source authority cannot support the stated conversions without introducing a post-result proxy/assumption.

`INFRASTRUCTURE_FAIL_V2_G9_0096` applies only to execution/provenance failure.

## Interpretation guards
- PASS would certify a compact 50-mas **numerical alignment-support region only** for the frozen family. It would not prove that Betelgeuse will explode on a useful timescale or that an observer can remain on the line.
- PASS would not repair the globally multi-band 0093 topology and would not relabel 0093.
- FAIL would reject this 50-mas v2 central-envelope test but would not disprove gravitational focusing itself.
- 0092b-a2 MeV solar transport remains externally-authority BLOCKED unless separately reopened under a new prospective v2 authority gate.
- Do not equate magnification with detector event gain, interaction gain, deposited energy, or useful power.

## If PASS: exact next v2 gate
Preregister a separate mission-actionability gate for a known Betelgeuse-like progenitor. It must propagate source-center proper-motion/astrometric uncertainty over an explicitly frozen waiting horizon and compare at least two prospectively specified observer architectures: (a) active radial stationkeeping and (b) passive/orbital coverage. No mission/actionability conclusion is permitted inside 0096.
