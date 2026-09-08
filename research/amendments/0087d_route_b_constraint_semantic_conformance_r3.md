# NMIR amendment 0087d-r3 — Route B constraint-semantic conformance

Date: 2026-09-08

## Trigger
Hosted 0087d-r2 run 34181665826 corrected literal B-minus-L recognition, but its Route B candidate list still contained differential-rate and binned-rate figures merely because their captions mention the B-L benchmark and a fixed mediator mass. This violates the already-frozen 0087d Route B requirement that a qualifying figure/caption explicitly correspond to the B-L **coupling-versus-mediator-mass constraint analysis**.

The r2 scientific classification is therefore not authoritative and is reclassified as `INFRASTRUCTURE_FAIL_ROUTE_B_CONSTRAINT_SEMANTIC_CONFORMANCE`.

## Allowed repair
Only the Route B figure-environment semantic predicate may be made conformant to the original preregistration:
- retain exact literal B-minus-L recognition from r2;
- retain starred/unstarred `includegraphics` support from r1;
- require explicit constraint/exclusion/limit semantics **and** a coupling-versus-mediator-mass plane/range identity in the same caption/figure environment;
- generic event-rate, binned-rate, spectrum, benchmark-point, or recoil-rate figures must not qualify merely because they contain `B-L` and `M_{Z'}` tokens.

No source bytes, x-axis tick reconstruction, >=3-major-tick requirement, >=2-decade span, 0.015-decade residual tolerance, 1.5-coordinate frame tolerance, 0.03-decade cross-route threshold, target interval, threat rule, classification consequence, or any scientific guard may change.

No new x-axis numerical coordinates were inspected to define this repair. The repair follows directly from the frozen wording of Route B and the r2 false-positive candidate membership.

## Required r3 validation
A synthetic mixed-caption test must prove that rate/binned-rate figures are rejected while a literal B-L excluded/constraint coupling-versus-mass figure is retained. A new hosted run must evaluate the unchanged 0087d scientific contract after this semantic filter. Green CI alone is not a scientific PASS; raw log and uploaded artifact must be inspected.
