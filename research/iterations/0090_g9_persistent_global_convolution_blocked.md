# Iteration 0090 — G9 persistent known-direction finite-source global convolution

Date: 2026-09-08
Classification: **`BLOCKED_G9_PERSISTENT_CONVOLUTION_NUMERICS`**
Readiness effect: none (`NMIR_READINESS` remains 98%).

## Frozen authority
Prospective preregistration: `research/prereg/0090_g9_persistent_finite_source_global_convolution.md`, commit `cf8ffbcca69477939430272777f573d94e4b1e24`.
Implementation-only point-control amendment: commit `f4d6538c551d724949089435707137d7155fd6ed`; it changed no scientific threshold.
Hosted head: `48b9313aa10fd13f63ed7b3b2c98d0ac12428ff6`.

## Hosted evidence consumed before classification
Workflow run: `34241211305`.
Aggregate job: `102112686829`.
Representative shard jobs inspected directly: `102111829597` (`x0` control 0, receiver 0) and `102111829669` (control 2, receiver 2).
Aggregate artifact: `10062169885`, `nmir-g9-0090-persistent-global-convolution`.
Independent downloaded artifact ZIP SHA256: `607220c60161046caf2ac36e4bbd9be487e756a34624c6931f7ce6a558e909bb`.
Independent inner `g9_0090_result.json` SHA256: `1dfdf40a86cf099d32c278a0bb963b7f4f55f8b852fd2637ffbe38b1d2303326`.
The independently computed ZIP hash exactly matches the upload digest printed by the aggregate raw Actions log.

Preflight dedicated regression suite was green, but green CI was not used as scientific authority. All nine scientific shards returned the preregistered numerical-blocked class and uploaded machine-readable shard artifacts. Aggregate recorded `unique_shards=9`, `shard_count=9`, `row_count=0`, expected `1350`, with reason `at least one shard could not certify frozen convolution numerics`.

## Why this is scientific numerical BLOCKED, not infrastructure failure
Raw shard `102111829597` returned `source quadrature refinement exceeds frozen threshold`. Raw shard `102111829669` returned `composite Simpson convergence exhausted`.

Both failure modes were prospectively frozen in 0090:
- primary source quadrature `12x24` versus refined `24x48` must agree in final `mu_real-1` to relative `<=0.005` when the larger excess is `>=1e-10` (or absolute magnification `<=1e-10` below that scale);
- transition-split composite Simpson must converge at `<=1e-8`, starting at 8 panels and doubling only to the frozen maximum 4096; exhaustion is explicitly `BLOCKED_G9_PERSISTENT_CONVOLUTION_NUMERICS`.

Therefore the terminal result is a valid reproducible scientific numerical blocker under the frozen taxonomy. It is not evidence that persistent focusing is absent, and the zero aggregate row count must not be interpreted as zero surviving physical points.

## Scientific interpretation
The 0089b/0089c/0089e continuous transparent-Sun geometry remains authoritative. 0090 establishes that the particular preregistered equal-area source quadrature plus transition-split composite-Simpson convolution cannot certify the finite-source class map under its fixed convergence controls. No tolerance, source grid, observer control, receiver radius, positioning-error grid, branch geometry or PASS condition is changed after seeing the result.

0090 remains permanently BLOCKED in its exact scope. Any continuation must be a separately preregistered independent numerical method; it may not retroactively promote 0090.

## Guards
No named source, occurrence rate, duty-cycle realizability, detector/material gain or BSM multiplier was evaluated. BSM response/enhancement remains LOCKED. No `mu_real>=2` survivor or strong-negative conclusion is authorized from 0090 because the full 1350-row class map never passed numerical certification.
