# NMIR-0103C — field↔matter co-registration gate

Status: PREREGISTERED BEFORE AUTOMATED CLASSIFIER RESULT

## Purpose
Freeze the admissibility rules for combining the 0103 magnetic-field authority with the matter/source environment used by NMIR-BENCHMARK-0100.

## Facts known before this preregistration
- The 0100 structure/source environment is the Farmer et al. 25 Msun presupernova model `25_79_0p005_ml`.
- The desired 0103 magnetic authority is a Betelgeuse-like Dorch nonlinear MHD star-in-a-box state; the numerical state has not yet been recovered.
- These are different stellar/model identities.

## Frozen terminal-admissibility rules
1. A terminal Betelgeuse-specific propagation may use a magnetic field and matter state only when they are co-located in the same simulation/model state, or when an independent prospectively specified mapping authority establishes their co-registration.
2. A recovered Dorch `B(x,y,z)` without co-located matter (`rho` and sufficient composition/Ye information) does not by itself close the terminal gate.
3. Farmer `25_79_0p005_ml` matter + Dorch/Betelgeuse magnetic field is classified as `MIXED_MODEL_ROBUSTNESS_ONLY`, never as a terminal Betelgeuse prediction.
4. No post-result radial stretching, density renormalization, radius matching, field renormalization, or hand-selected mapping is permitted to upgrade a mixed-model calculation to terminal status.
5. A green CI result means only that the classifier correctly enforces these rules. It does not mean the Betelgeuse authority gate is scientifically closed.

## Expected current classification
With the currently available sources the terminal status is expected to be

`BLOCKED_0103_BETELGEUSE_COHERENT_MAGNETO_MATTER_STATE_AUTHORITY`.

The automated audit must fail if it accidentally labels the current Farmer+Dorch combination terminal-admissible.
