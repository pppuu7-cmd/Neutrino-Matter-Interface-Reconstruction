# Preregistration amendment 0097a — downstream solar-lens focal half-line

Date frozen: 2026-09-09
Branch: NMIR v2
Parent preregistration: `research/prereg/0097_v2_g9_betelgeuse_line_tracking_architectures.md`
Parent prereg commit: `53863048c2d5b5803c9e120794c21fe415f1b319`
Execution timing: frozen before authoritative 0096 reaches a terminal result and before any 0097 execution.

## Authority defect being corrected
The parent 0097 preregistration treated the two intersections of a passive circular heliocentric orbit with the infinite Betelgeuse–Sun line as two usable solar-lens crossings per orbit.

That is geometrically too generous. The solar gravitational lens is a **focal half-line downstream of the Sun from the source**. For radiation arriving from the source, only the observer location on the extension `source -> Sun -> observer` lies in the relevant downstream focal region. The antipodal intersection is on the source side of the Sun and is not a second usable focal window for the same source.

NASA/primary authority:
- V. R. Eshleman (1979), *Gravitational lens of the sun - Its potential for observations and communications over interstellar distances*, NASA NTRS 19790065362: the solar lens produces magnification along a **semi-infinite focal line**.
  `https://ntrs.nasa.gov/search.jsp?R=19790065362`
- NASA NIAC Solar Gravitational Lens Phase I report (2018), NTRS 20180006788: a probe on the focal line observes distant objects on the **opposite side of the Sun**.
  `https://ntrs.nasa.gov/citations/20180006788`
- NASA Science description of the SGL: the Sun focuses light at a point on the **opposite side** from the source.
  `https://science.nasa.gov/universe/exoplanets/want-to-see-the-surface-of-another-earth-use-our-sun/`

This correction is frozen prospectively and is not chosen in response to a 0096 or 0097 numerical result.

## Frozen correction
Retain all source astrometry, 10-year horizon, 50-mas support, observer-distance controls, active architecture equations, and all terminal status names from 0097.

For Architecture B only:

1. The circular orbit has two geometric intersections with the infinite source–Sun line, but exactly **one usable downstream solar-lens crossing per orbit** for the frozen source.
2. Retain the already frozen exact single-window duration
   `t_cross = 2*asin(d_support/r)/omega`.
3. Replace the parent duty fraction
   `f_duty = 2*t_cross/T_orb`
   with
   `f_duty = t_cross/T_orb`.
4. Retain
   `N_continuous = ceil(1/f_duty)`
   for the idealized equally phased fleet diagnostic, now based on one usable focal window per orbit.
5. Record both:
   - `geometric_line_intersections_per_orbit = 2`;
   - `usable_downstream_lens_crossings_per_orbit = 1`.

## Effect on classifications
The Architecture-B PASS/FAIL rule is unchanged: a single passive observer passes continuous unknown-event coverage only if `f_duty >= 1`.

Therefore this amendment cannot make passive coverage easier to pass; it only removes a factor-of-two overestimate in passive availability and correspondingly increases the idealized fleet count.

Architecture A is unchanged.

## Interpretation guard
This amendment does not imply that the optical SGL focal distance (~548 AU) applies to the transparent-Sun neutrino lens used by NMIR. The cited SGL sources are used only for the directional fact that gravitational focusing of radiation from a specified source is downstream of the lens, i.e. a focal **half-line**, not two antipodal useful observer locations. NMIR's ~24 AU neutrino focal-distance controls remain inherited from its own transparent-Sun calculation.
