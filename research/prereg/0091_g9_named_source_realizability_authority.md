# Preregistration 0091 — G9 named-source realizability / alignment authority

Date frozen: 2026-09-08
Parent: 0090f `PASS_G9_FULL_GRID_FINITE_NONZERO_SURVIVORS`, immutable record `research/iterations/0090f_g9_full_grid_finite_nonzero_survivors_pass.md`.

## Question
Does at least one independently selected real astrophysical neutrino-source class have sufficiently authoritative source morphology, direction/astrometry, spectrum and alignment/station-keeping geometry to map into the 0090f numerical survivor region without substituting electromagnetic source size/centroid for the neutrino-emitting region unless a primary source explicitly authorizes that identification?

This is a realizability gate. It must not multiply the 0090f magnification into detector event rates, interaction probabilities or neutrino-supplied power.

## Frozen numerical parent
Use only 0090f authority:
- observer distance family near `23.97–24.26 AU`;
- source angular-radius grid `1e-18 <= theta <= 1e-6 rad`;
- nonzero source-plane offsets `d={0.01,0.1,1,10,100} m`;
- all 1125 nonzero-offset grid rows satisfy `mu>=2` and therefore numerical survivor status;
- no interpolation/extrapolation beyond the frozen theta/offset support for a PASS claim.

For a sky-angle centre misalignment `beta`, use the same small-angle projection as the source radius:

`d = z * AU * beta`.

Thus a real source is geometrically inside the frozen nonzero-offset support only if its relevant centre-offset/alignment uncertainty can be compared to the interval represented by `0.01–100 m`; exact equality to a grid node is not required for actionability, but no numerical magnification may be interpolated between nodes in 0091. 0091 asks overlap/actionability only.

## Candidate selection frozen before source-result search
Do not choose sources by whichever one best matches 0090f after inspecting morphology results.

Evaluate exactly three independently defined source classes/candidates:
1. **Steady high-energy astrophysical neutrino candidate:** the individually named source with the strongest/most significant steady-source evidence in the latest primary IceCube point-source/source-catalog result available as of 2026-09-08. If the primary result itself ranks sources differently under multiple predeclared analyses, take the source with the smallest reported pre-trial p-value in its principal steady-source table and record the ambiguity rather than selecting by 0090f fit.
2. **Time-dependent high-energy benchmark:** `TXS 0506+056`, frozen because it is the canonical independently established time-dependent/blazar neutrino-association benchmark, not because of its expected angular size.
3. **MeV burst class:** a generic Galactic core-collapse supernova benchmark at `10 kpc`, with source size/morphology taken only from a primary neutrino/CCSN calculation or review that explicitly states the physical neutrino-emitting/neutrinosphere scale. This is a class-level benchmark, not a claim that a currently exploding named Galactic supernova exists.

If the latest steady-source primary catalog names TXS 0506+056 as the strongest steady candidate too, do not substitute a cherry-picked third high-energy source; retain the duplication and note that the independent selection rules converge.

## Source authority requirements
For each candidate/class recover from primary/authoritative sources, with citations/provenance:
- distance or redshift-derived distance range sufficient to understand physical-to-angular morphology;
- neutrino energy/flavor regime and whether propagation through the solar lens model is within the approximation used by G9;
- physical or angular size of the **neutrino-emitting** region, or an explicit authoritative upper bound;
- neutrino-emission centroid/direction uncertainty or a justified relation to an independently measured EM/radio centroid;
- temporal persistence/duration relevant to line tracking.

A telescope point-spread-function/localization region is not automatically the physical neutrino source size. An electromagnetic emitting-region size is not automatically the neutrino emitting-region size.

## Alignment/station-keeping authority
For each candidate compute only transparent geometry from sourced inputs:
- frozen source-radius overlap test: `theta_real` against `[1e-18,1e-6] rad`;
- frozen maximum nonzero offset angle `beta_100 = 100 m/(z*AU)` across the 0090f observer range;
- if authoritative centroid uncertainty `sigma_dir` is available, compare it to `beta_100` without treating statistical localization as physical source size;
- characterize the lateral focal-line tracking velocity/acceleration requirement for a `~24 AU` observer using source direction and Solar/System ephemeris geometry only if a reliable dynamical formulation can be prospectively specified. If this requires a separate orbital simulation, classify that subpart `OPEN_ORBITAL_TRACKING_GATE` rather than inventing a duty cycle.

Do not claim practical duty cycle from angular geometry alone.

## Frozen classifications per candidate
- `PASS_G9_NAMED_SOURCE_MORPHOLOGY_OVERLAP`: neutrino-emitting angular size is directly authoritative and lies within 0090f theta support; neutrino centroid/alignment information is sufficiently authoritative to define a path into the <=100 m offset support; relevant spectrum is compatible. This still does not imply practical station keeping.
- `BLOCKED_G9_NAMED_SOURCE_NEUTRINO_MORPHOLOGY_AUTHORITY`: source is neutrino-associated but the physical neutrino-emitting size/centroid cannot be bounded from primary authority tightly enough to map to 0090f without an EM proxy.
- `BLOCKED_G9_NAMED_SOURCE_ALIGNMENT_AUTHORITY`: morphology/spectrum are adequate but direction/centroid alignment cannot be tied to the <=100 m frozen offset support.
- `SCIENTIFIC_FAIL_G9_NAMED_SOURCE_OUTSIDE_FROZEN_SUPPORT`: authoritative source angular size exceeds `1e-6 rad` or another explicit physical incompatibility places it outside the frozen G9 model support.
- `INFRASTRUCTURE_FAIL_G9_0091`: source retrieval/provenance failure prevents classification.

For the generic CCSN class, replace “named source” wording semantically with class benchmark but use the same PASS/BLOCKED/FAIL logic.

## Gate-level classification
- `PASS_G9_REAL_SOURCE_MORPHOLOGY_PATH`: at least one candidate/class passes morphology/alignment/spectrum authority sufficiently to justify a separately preregistered orbital/duty realizability calculation.
- `BLOCKED_G9_REAL_SOURCE_AUTHORITY`: none passes, but one or more are blocked by missing neutrino morphology/centroid authority rather than physically excluded.
- `SCIENTIFIC_FAIL_G9_REAL_SOURCE_FROZEN_SET`: all three are authoritatively outside/incompatible with frozen support.
- `INFRASTRUCTURE_FAIL_G9_0091`: no valid scientific classification is possible.

## Next action
On PASS, preregister a dedicated orbital/alignment-duty gate before any practical gain statement. On BLOCKED, record G9 as numerically surviving but externally non-actionable pending source-morphology/centroid authority. On scoped FAIL, close the frozen candidate set without searching post hoc for another source; a broader source census would require a new prospective rule.

## Guards
No detector gain multiplication. No BSM multiplication. No EM morphology silently promoted to neutrino morphology. No use of IceCube angular resolution as physical source radius. No result-selected fourth source. No numerical interpolation of 0090f magnification in 0091.
