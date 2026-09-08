# 0090 implementation amendment — exact aligned point-source control

Date: 2026-09-08
Parent preregistration: `research/prereg/0090_g9_persistent_finite_source_global_convolution.md`, commit `cf8ffbcca69477939430272777f573d94e4b1e24`.

Frozen before any 0090 Model-S finite-source result was inspected.

The dedicated `theta_s=0`, `delta_y=0` control required by prereg item 3 has a discontinuous 0/1 azimuth acceptance indicator. It therefore MUST NOT be evaluated by smooth-subinterval Simpson merely to force convergence at the indicator boundary. Instead, for that dedicated point control only:

1. On each already-certified 0089c monotone branch solve the exact signed targets `y=+a` and `y=-a` by the same branch-local bisection used for transition authority.
2. Partition the branch by those crossings and the certified branch endpoints.
3. Classify each open partition by its midpoint against `|y|<=a`.
4. Sum every accepted annulus exactly as `pi*Rsun^2*(b_hi^2-b_lo^2)`.
5. Form the inherited comparison `mu=1+A/(pi*a^2)`.

This is an implementation conformance clarification, not a scientific change: the source grid, receiver radii, observer controls, thresholds, 0.5% point-control requirement and all 0090 classifications remain exactly as preregistered. Finite nonzero source/offset rows continue to use the frozen transition-split Simpson convolution.