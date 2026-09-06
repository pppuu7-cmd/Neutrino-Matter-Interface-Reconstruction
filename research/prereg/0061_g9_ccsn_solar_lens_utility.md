# NMIR 0061 preregistration — distant core-collapse-supernova neutrino solar-lens utility

Date: 2026-09-07
Gate: G9 / F3-F7 distant-source physical gravitational focusing utility
Status at preregistration: OPEN

## Question
Can transparent-Sun gravitational focusing produce a physically useful increase in neutrino interaction/event rate for a real distant source once the unlensed source fluence, finite emitting region, lens geometry, receiver integration, alignment probability and duty cycle are included prospectively?

## Frozen source class
Use a Galactic core-collapse supernova (CCSN) burst as the first real distant-source benchmark because its MeV neutrino burst is a Standard-Model source class with established detector literature and a compact emitting region. The benchmark source distance is fixed to `D_s = 10 kpc`; this is a normalization benchmark, not a claim that the next Galactic CCSN will occur at 10 kpc.

Before any result-dependent utility calculation, freeze locally in `data/` with recoverable primary provenance:
1. one primary/authoritative CCSN neutrino fluence or luminosity+spectral model covering the burst;
2. source-emission radius/size relevant to the neutrino-emitting region;
3. burst duration or time profile;
4. Galactic CCSN occurrence-rate authority or an observational upper/lower range sufficient for a duty-cycle interpretation.

If these cannot be frozen without mixing incompatible models, classify `BLOCKED_SOURCE_AUTHORITY` rather than inventing numbers.

## Lens authority and geometry
Reuse only previously validated G9 transparent-Sun authority and formulas from the repository. The approximately `23.5 AU` focal-scale benchmark is a prerequisite, not the utility result.

For a distant source behind the Sun, compute using an extended transparent-Sun lens rather than a point-mass caustic. Preserve Liouville/surface-brightness constraints and finite-source regularization.

The source angular radius is `theta_s = R_src / D_s` (or the appropriate projected finite-source profile). The receiver must have finite transverse size/acceptance; report receiver-integrated magnification, not point-caustic peak magnification.

## Frozen outputs
At minimum report:
- unlensed burst fluence at the lens/observer normalization point in `cm^-2` and source-resolved energy convention;
- finite-source angular radius;
- observer distance from the Sun and physical focal-plane scale;
- receiver-integrated magnification `mu_rec` for explicit receiver radii/areas;
- angular alignment tolerance corresponding to each reported `mu_rec`;
- sky/alignment probability or equivalent duty factor for a random Galactic CCSN direction relative to the Sun at burst time;
- expected time-averaged useful gain `mu_rec * duty` or the correctly normalized burst-expectation analogue;
- resulting interaction/event-rate multiplier only for a frozen already-validated target/channel; do not multiply detector/metastable/structure gains;
- if a neutrino-only deposited-power score is quoted, enforce `0 <= E_dep,nu <= E_nu`.

## Prospective acceptance criteria
### PASS_G9_USEFUL_DISTANT_SOURCE_SURVIVOR
Only if a receiver-integrated finite-source magnification greater than unity survives and, after the physical alignment/duty factor is included, the expected useful event/fluence gain remains `>= 2` relative to the same detector operated without solar-lens alignment. This is intentionally a utility criterion, not merely proof that lensing exists.

### PASS_G9_PHYSICAL_BUT_STRONG_NEGATIVE_UTILITY
If finite-source receiver-integrated magnification exists but the alignment/duty-weighted expected gain is `< 2`, or if useful enhancement requires an alignment/receiver configuration whose occurrence-weighted exposure is smaller than the unlensed baseline. Record the physical magnification separately from utility.

### BLOCKED_SOURCE_AUTHORITY
If source fluence/size/time/rate authority cannot be frozen consistently enough to evaluate the criterion.

### SCIENTIFIC_FAIL_MODEL
If the extended-Sun finite-source calculation fails a previously validated focal-scale/Liouville control. Do not repair by weakening the criterion; preregister a new model only after diagnosing the physics error.

## Guards
- No point-caustic divergence is admissible.
- Solar-neutrino self-lensing is forbidden; the source must be behind the Sun relative to the receiver.
- Magnification of flux is not creation of surface brightness.
- A large instantaneous `mu` is not useful if alignment probability/duty removes the gain.
- Do not count source energy, detector stored energy, or reset energy as neutrino-supplied gain.
- Do not multiply G9 with G2 metastable amplification, G8 resonance, G10 geometry, or any other unvalidated factor.
- A 10-kpc normalization is not an occurrence prediction.

## Scientific-vs-infrastructure failure
Numerical ray tracing/integration should have dedicated tests and a fail-closed hosted workflow when practical. A green workflow alone is infrastructure evidence. Scientific PASS/negative classification requires raw result/artifact inspection against the criteria above and consistency with the frozen primary source/lens inputs.

## Exact next action
1. Freeze the CCSN source authority set in `data/` with citations/provenance.
2. Reuse/extend the existing extended-Sun finite-source lens code, adding receiver integration and alignment/duty accounting.
3. Run prospective benchmark and classify exactly as `PASS_G9_USEFUL_DISTANT_SOURCE_SURVIVOR`, `PASS_G9_PHYSICAL_BUT_STRONG_NEGATIVE_UTILITY`, `BLOCKED_SOURCE_AUTHORITY`, or `SCIENTIFIC_FAIL_MODEL`.
4. On a strong-negative utility result, move to G8 if its source/entrance-strength blocker is resolvable; otherwise return to the remaining G3 contact-coefficient residual or formal BSM unlock audit only when its prerequisites are met.
