# 0101 sterile-neutrino parameter-authority audit

Date: 2026-09-09
Status: RESEARCH NOTE — DOES NOT CREATE A TERMINAL PARAMETER LOCK

## Question

What external authority can prospectively define a reproducible terminal parameter point or scan domain for `NMIR-BENCHMARK-0101` without pretending that unrelated one-dimensional limits form a joint 3+1 likelihood?

## Result of current audit

No single current public source identified in this audit simultaneously provides all of the following for the full `(theta14, theta24, theta34, Delta m^2_41)` benchmark:

1. a modern joint 3+1 fit;
2. coverage/correlation treatment suitable for a statistical claim;
3. a public immutable likelihood or equivalent machine-readable fit object;
4. sufficient information to reproduce all active-sterile mixing directions used by 0101.

Therefore **no `0101_sterile_parameter_terminal_lock.json` is created yet**. The existing terminal ceiling remains `BLOCKED_0101_STERILE_PARAMETER_AUTHORITY_UNPINNED`.

## Candidate A — 2026 electron-disappearance SBI global fit

Reference:
- Villarreal, Woodward, Hardin, Conrad et al., *Machine learning-informed 3+1 sterile neutrino global fits using posterior density estimation of electron disappearance data*, EPJC 86, 326 (2026), DOI `10.1140/epjc/s10052-026-15488-4`.

Strengths:
- modern simulation-based treatment motivated by the failure of naive Wilks assumptions in oscillatory small-signal searches;
- explicitly defines an electron-disappearance training grid in `U_e4` and `Delta m^2_41`;
- combines several electron-disappearance experiments.

Limitations for 0101:
- it is an **electron-disappearance** global fit, not a complete joint authority for `U_mu4` and `U_tau4`;
- the paper's Data Availability and Code Availability statements say the generated/analyzed data and software are available on reasonable request rather than as an immutable public release.

Decision: useful authority for designing the `theta14` axis, but **insufficient by itself for a full terminal 0101 lock**.

## Candidate B — 2025 frequentist SBI muon-disappearance global fit

Reference:
- Villarreal, Woodward, Hardin, Conrad, *A frequentist simulation-based inference treatment of sterile neutrino global fits*, Machine Learning: Science and Technology 6 (2025) 035053, DOI `10.1088/2632-2153/ae040c`.

Strength:
- uses trials-based/SBI methodology to avoid blindly relying on Wilks' theorem;
- directly addresses a subset of muon-flavor disappearance sterile-neutrino data.

Limitation:
- it is still a subset fit, not a complete `(U_e4,U_mu4,U_tau4,Delta m^2_41)` authority.

Decision: candidate cross-check for the `theta24`/mass-splitting sector, not a standalone full terminal authority.

## Candidate C — IceCube DeepCore 7.5-year 3+1 constraints

Reference:
- IceCube Collaboration, *Search for a light sterile neutrino with 7.5 years of IceCube DeepCore data*, Phys. Rev. D 110, 072007 (2024), DOI `10.1103/PhysRevD.110.072007`.

Published result relevant to a conservative authority envelope:
- for `Delta m^2_41 >= 1 eV^2`, the reported 90% CL limits are `|U_mu4|^2 < 0.0534` and `|U_tau4|^2 < 0.0574`.

Strength:
- directly constrains the muon/tau sterile-mixing directions that an electron-only fit cannot close.

Limitation:
- these published limits do not supply the missing electron-mixing authority and must not be multiplied with an electron-disappearance confidence region and relabeled as a joint confidence level without a joint likelihood.

Decision: acceptable as a separately labelled **experimental constraint axis**, not as a fabricated global likelihood.

## Candidate D — 2026 ICARUS first muon-disappearance result

Reference:
- ICARUS Collaboration, *First search for sterile neutrino oscillation leading to nu_mu disappearance in the Booster Neutrino Beam at ICARUS*, accepted to Phys. Rev. D on 2026-07-09, DOI `10.1103/2vms-z2j8`, arXiv `2603.22557`.

Strength:
- latest direct SBN muon-disappearance information identified in this audit.

Limitation:
- the first result is explicitly systematics-limited and reports a two-neutrino-approximation exclusion contour; it is not a four-parameter global 3+1 likelihood.

Decision: retain as an external consistency check, not the sole terminal parameter authority.

## Prospective terminal strategy

A terminal 0101 benchmark should use one of two honest routes:

### Route 1 — reproducible joint likelihood

Use a specific global fit only if its likelihood/posterior-density object, experiment inputs, parameter conventions, and correlation treatment can be pinned by immutable public identity/hash. This is preferred if such a release becomes available.

### Route 2 — factorized authority benchmark, explicitly non-global

If a public joint likelihood is unavailable, preregister a **factorized experimental-envelope benchmark** before execution:

- `theta14` / `Delta m^2_41`: pinned electron-disappearance authority;
- `theta24`, `theta34`: pinned muon/tau disappearance authority;
- define a finite grid prospectively;
- report each experimental authority axis separately;
- make **no combined confidence-level claim**;
- do not call the Cartesian product a global allowed region;
- retain all source-profile, spectrum, detector and G9 guards from the parent funnel.

This route can test whether the 3+1 Hamiltonian can occupy the NMIR design region while preserving honest authority semantics, even if the community has not published one reproducible four-dimensional likelihood.

## Next authority task

Locate and pin a machine-readable electron-disappearance fit/contour or experimental likelihood that can define `theta14` and `Delta m^2_41` without plot digitization. Until that object is identified, 0101 remains authority-BLOCKED, not physics-FAIL.
