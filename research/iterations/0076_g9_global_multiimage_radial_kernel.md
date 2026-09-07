# Iteration 0076 — G9 global multi-image transparent-Sun radial kernel

Date: 2026-09-07
Prospective contract: `research/prereg/0076_g9_global_multiimage_radial_kernel.md`, commit `05a3354dd2f8cdbba1f2dd04342161b515a10304`.

## Classification

**SCIENTIFIC_FAIL_G9_GLOBAL_MULTIIMAGE_KERNEL**

The frozen scan-grid/sign-change algorithm does not satisfy its prospective global-kernel validation criteria. This is a scientific/method failure, not an infrastructure failure and not a physical no-go for transparent-Sun focusing.

## Authoritative hosted evidence

- run/job: `34149715242 / 101829231239`
- head: `e6bf01e281d5f4f70c54e6ca74c23f27c3bdf776`
- artifact: `10029092681`, `nmir-g9-0076-result`, 2640 bytes
- artifact ZIP SHA256: `759f9b79acf8d4a990190c63389571e912b2c7afa619cec055ed13094a68f26c`
- raw `g9_global_kernel_result.json` SHA256 printed by the job: `66a99ff6abc86aaae465568086c6e6efb1b277dbab95ce58bfc1508bdb735340`
- dedicated tests: `5 passed in 0.03s`

The raw decoded job log was inspected directly. The benchmark intentionally exited 1 after writing/uploading the scientific result, so the red workflow status is the expected fail-closed scientific classification.

## Frozen criteria versus result

PASS:
- generating-root recovery;
- root uniqueness;
- finite/non-negative/monotone aperture-area invariants.

FAIL:
- grid refinement: maximum base-vs-once-bisected cumulative-area relative difference `0.7391843634769288`, versus frozen `0.005` maximum;
- local-authority containment: at the `b0/Rsun=0.024`, `a=100 m` control the global result is `5.936834234353704e7`, while the already validated exact one-ring result is `6.987541896262653e7`; relative error `0.1503687101283685`, and the global interval set does not contain the exact one-ring contribution.

The 1 m and 10 m local controls reproduce the containing one-ring interval accurately, so the failure localizes to missed narrow preimages/crossings as support grows through radial structure rather than to the signed-map formula itself.

## Diagnosis and scope

The 0076 algorithm inserts signed-map zero roots, but `|y|-r` crossings are still discovered by sign changes on the chosen scan grid. Near a radial extremum/caustic, a narrow accepted interval can occur entirely between two same-sign scan nodes. Bisecting the grid then discovers such an interval, producing O(1) base/refined disagreement. Therefore the algorithm is not grid-independent enough to support the later finite-source convolution.

No tolerance was relaxed, no old 0075 utility value was recycled, and no `mu>=2` survivor/strong-negative claim is made.

## Next action

A genuinely new numerical geometry contract is allowed: explicitly find radial turning points of the signed mapping, partition the full aperture into monotone segments, and solve `y=0` and `|y|=r` once per monotone segment. The next gate must be frozen prospectively and must retain the same 0.5% local/refinement requirements or stronger, rather than patching 0076 after seeing its result.
