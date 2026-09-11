# NMIR 0103Q — coherent-state ingest rejection preregistration

Date: 2026-09-12
Benchmark: `NMIR-BENCHMARK-0103`
Scope: `NONTERMINAL_DATA_INTEGRITY_ONLY`

Purpose: verify that a future real 3-D magneto-matter state cannot be silently accepted when magnetic and matter channels are not demonstrably co-registered. This audit is prospectively frozen before implementation/results.

## Minimal coherent-state metadata contract

A state is admissible only if magnetic and matter payloads agree on all of:

- exact `state_id` / snapshot identity;
- coordinate-system identifier and handedness;
- grid shape;
- coordinate arrays on all three axes;
- length unit;
- magnetic-field unit;
- density unit;
- `Ye` convention/version;
- time/snapshot coordinate when present.

## Frozen negative fixtures

Starting from one valid synthetic reference manifest, independently inject exactly one defect per case:

1. mismatched `state_id`;
2. mismatched grid shape;
3. shifted x-coordinate array;
4. reversed handedness;
5. mismatched length unit;
6. missing magnetic-field unit;
7. mismatched density unit;
8. missing `Ye` convention;
9. mismatched snapshot time;
10. non-finite field sample;
11. non-finite density sample;
12. out-of-domain requested ray endpoint.

A positive control uses the untouched coherent manifest/payload.

## Prospective gates

1. Positive control is accepted.
2. Every one of the 12 frozen corruptions is rejected.
3. Each rejection returns a deterministic machine-readable reason code belonging to the expected category.
4. No corrupted fixture reaches propagation.
5. Repeating the full audit yields identical decisions/reason codes.

PASS label: `PASS_0103Q_COHERENT_STATE_INGEST_REJECTION_NONTERMINAL`.

## Scope guard

A PASS only proves fail-closed ingest behavior. It does not provide Betelgeuse data, does not establish that any particular external snapshot is physically appropriate, and cannot authorize terminal spin-flavor propagation.