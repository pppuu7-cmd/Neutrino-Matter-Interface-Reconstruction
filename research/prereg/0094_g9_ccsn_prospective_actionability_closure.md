# Preregistration 0094 — G9 generic-CCSN prospective actionability closure

Date frozen: 2026-09-09

## Purpose
Perform the single mandatory post-0093 real-source actionability gate required by `research/NMIR_V1_READINESS_100_CONTRACT.md` R100-3 for the already frozen generic Galactic CCSN benchmark.

This gate asks only whether a **single observer at the validated ~24-AU G9 focal geometry** has a reproducible prospective route to be inside a numerically supported source-direction footprint when the generic 10-kpc CCSN neutrino burst arrives. It does not optimize a spacecraft, introduce a swarm, select a known progenitor after the fact, repair 0093 topology, repair 0092b-a2 solar transmission, or authorize detector/material/power multiplication.

## Frozen parents
- 0093 prereg commit: `ffaa7706bf335b301833fe49754297b804cf713a`.
- 0093 execution head/run/artifact: `66eb5bcfcc9abf9240cb0b5716665143fbbab8ff` / `34279135188` / `10077508208`.
- independently validated 0093 ZIP SHA256: `1bef56077626433de111870e8c41c6a5460f8c6cc7d332b58171ded2015c73e6`.
- independently validated inner JSON SHA256: `9a5aea9e1d3fd00a16781870e93ee95956a3886ed47edb3a244155ce0dd23a5b`.
- 0093 classification: `BLOCKED_G9_CCSN_ALIGNMENT_TOPOLOGY` with 39 sampled re-entries.
- generic CCSN source authority: `data/g9_ccsn_source_authority_0061.json`, blob `ed2e5ab50375abb1049b86348a2e570b5e7b99f5`, benchmark distance exactly `10 kpc`, frozen neutrino-source radii 21/100 km, 20-s fluence integration horizon, Galactic core-collapse rate 1.63 +/- 0.46 per 100 yr.
- v1 closure contract: `research/NMIR_V1_READINESS_100_CONTRACT.md`, commit `f64bf4d84f176dc532d7e64f45dd224a42e846c1`.

## Frozen numerical footprint treatment
Because 0093 is topology-BLOCKED, no first crossing or later survivor island may be promoted to a global monotone footprint.

For a conservative **necessary-condition** actionability test only, use the most generous map-certified support ceiling already contained in the validated 0093 artifact:

`beta_zero,max = max_family[d_zero / (z * AU)]`.

Here `d_zero` is the prospectively defined strict no-overlap ceiling from 0093. Beyond it `mu=1` exactly within the inherited overlap model. This makes `beta_zero,max` an intentionally lenient angular upper bound: any prospective direction uncertainty larger than it cannot guarantee placement in any G9 survivor region, regardless of the unresolved internal re-entry topology.

Use exact IAU `AU = 149597870700 m` and record the resulting `beta_zero,max` in rad and arcsec. Also record the validated first-contiguous-region descriptors, but do not use them to strengthen a negative conclusion.

## Frozen external authorities
Use these exact authority objects; later more favorable localization papers may be discussed only as sensitivity context and cannot replace them inside this gate:

1. **Prompt neutrino alert timing / SNEWS 2.0:** M. Kara et al., `The SNEWS 2.0 Alert Software for the Coincident Detection of Neutrinos from Core-Collapse Supernovae`, arXiv:2406.17743. Role: a Galactic CCSN neutrino burst is itself the low-latency alert; combined trigger/triangulation follows detected neutrino events and can precede optical emission, not the neutrino wavefront.
2. **10-kpc prompt pointing scale:** C. W. Walter, D. M. Scolnic, A. Slosar, arXiv:1901.01599. Role: Super-Kamiokande pointing for a CCSN at 10 kpc is of order 3 degrees. This is a deliberately concrete published benchmark, not a claim of the ultimate future detector limit.
3. **Pre-supernova directionality scope:** M. Mukhopadhyay et al., arXiv:2004.02045. Role: pre-SN directional sensitivity studied for nearby stars `D < 1 kpc`, with ~60-degree fiducial and ~15-degree improved angular sensitivity.
4. **Operational pre-SN alert reach:** combined KamLAND + Super-Kamiokande pre-supernova alert system, arXiv:2404.09920. Role: a 15-Msun model is resolved within 510 pc at the stated false-alarm target; optimistic Betelgeuse-like warning can reach ~12 h. This authority is frozen to test whether the 10-kpc benchmark has a demonstrated pre-collapse warning route.
5. **Burst duration / occurrence:** frozen 0061 authority above; use the already stored 20-s integration horizon and occurrence-rate ledger. No new rate model is selected.

## Frozen causal/actionability logic
Define `beta_prompt = 3 deg` from authority 2. Record the ratio `beta_prompt / beta_zero,max`.

A prompt neutrino direction is **not prospective positioning information** for the same neutrino burst. The observer is downstream at approximately 24 AU; any alert generated only after terrestrial detection of the burst is carried by causal communication at speed <= c, while the neutrino burst propagates at essentially c. No positive maneuver lead time for the same leading wavefront may be assigned from such an alert. Network/detector latency can only worsen this.

Therefore the generic 10-kpc benchmark can be prospectively actionable only if an independently demonstrated **pre-collapse** direction/identity warning exists early enough to pre-position the observer. Under frozen authorities 3 and 4, do not extrapolate a <=510-pc / <1-kpc pre-SN capability to 10 kpc.

The gate must distinguish:
- a known nearby progenitor monitored before collapse (outside this exact generic 10-kpc benchmark unless prospectively introduced in a new gate);
- the generic 10-kpc future Galactic CCSN used by 0061/0090f/0093.

## Source occurrence/direction probability requirement
R100-3 allows either a source occurrence/direction probability or a rigorous reason no prospective actionable probability can be assigned.

Use the frozen 0061 occurrence rate only as a temporal occurrence fact. Do **not** convert the 0061 thin-disk control into a precise probability of lying in an unresolved multi-band 0093 survivor topology. If the prospective event direction is not known before collapse and 0093 is topology-BLOCKED, classify the exact G9 capture probability as not reproducibly assignable under v1 rather than inventing a uniform-sky or delta-plane probability.

For scale context only, an isotropic spherical-cap probability formed from `beta_zero,max` may be reported as an explicitly non-Galactic geometric control:

`P_iso_cap = (1 - cos(beta_zero,max))/2`.

It may not be called the Galactic CCSN actionability probability.

## Frozen classifications
`PASS_G9_CCSN_PROSPECTIVE_ACTIONABILITY` only if all of the following are established under the frozen authorities without new assumptions:
- a prospective pre-collapse identity/direction route applies to the **10-kpc generic benchmark**;
- its direction uncertainty is <= `beta_zero,max` before the burst reaches the observer;
- the timing provides positive pre-positioning lead time for a single ~24-AU observer;
- the 20-s burst window and observer-position requirement are explicitly compatible;
- an actionable occurrence/direction probability is reproducibly assignable despite 0093 topology.

`SCIENTIFIC_FAIL_G9_CCSN_PROSPECTIVE_ACTIONABILITY_V1` if a necessary condition is contradicted by the frozen authority/causal geometry, including if the demonstrated generic 10-kpc direction information arrives only with the burst and published 10-kpc prompt pointing is broader than the strict 0093 no-overlap angular ceiling, while the frozen pre-SN authorities do not apply at 10 kpc.

`BLOCKED_G9_CCSN_PROSPECTIVE_ACTIONABILITY_AUTHORITY` if available authority is genuinely insufficient to decide a necessary condition without new observational/engineering information, but does not contradict it.

`INFRASTRUCTURE_FAIL_G9_0094` applies only to provenance/calculation failure.

## Interpretation guards
- A negative v1 actionability result is scoped to one observer + generic 10-kpc CCSN + current frozen authority. It is not a theorem against a pre-positioned multi-observer swarm, a specifically monitored nearby progenitor, future sub-arcsecond pre-SN neutrino localization, or a different source class; those require a new prospective v2 assumption/gate.
- 0093 remains topology-BLOCKED and must remain immutable.
- 0092b-a2 remains terminally external-authority BLOCKED for v1; no transparent-Sun inference follows.
- No detector/material/BSM response enhancement or neutrino-supplied-power claim is authorized.
