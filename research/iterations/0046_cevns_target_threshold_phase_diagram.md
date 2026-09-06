# Iteration 0046 — CEvNS target/threshold phase diagram

Date: 2026-09-06
Classification: `PASS_PHASE_DIAGRAM`
Prospective contract: `research/cevns_target_phase_diagram_prereg.md` (commit `37e28276d7fa24039c1ac5114e899b1b8e697f1e`)
Scientific head: `526837aff6e1801e35cd3117c5228838b5bfe9d5`
Hosted run/job: `34052930672` / `101539642497`
Artifact: `9995368376`, ZIP SHA256 `046953d77896362afaaf5da0ff2015ddb36958196c0b921cc5e3f0ff4efe3951`

## Frozen gate
The 0045 exact-mass, actual-Z/N, full frozen solar-source CEvNS model was scanned over 0.5–100 eV at fixed target kg. Every winner transition had to be refined to <=0.02 eV and independently topology-checked. Detector transfer functions, chemistry and abundance were excluded.

## Raw-inspected result
Decoded hosted log: 29 dedicated tests passed and benchmark returned `status=PASS_PHASE_DIAGRAM`. All reported independent stability checks had `topology_match=true` and `pass=true`.

Refined winner crossovers (eV):
- Pb208 -> W184: 3.9453125, bracket width 0.015625
- W184 -> Xe132: 4.4453125, width 0.015625
- Xe132 -> Mo100: 6.3515625, width 0.015625
- Mo100 -> Se82: 6.7265625, width 0.015625
- Se82 -> Ge74: 12.5078125, width 0.015625
- Ge74 -> Ti48: 12.9296875, width 0.015625
- Ti48 -> Ar40: 12.9609375, width 0.015625
- Ar40 -> Pb208: 15.5703125, width 0.015625

On the frozen coarse grid the source regime is Be7-ground dominated below the final transition and B8 dominated from 16 eV upward. Representative validated rates include Pb208 0.0802384 events/(kg day) at 0.5 eV, Se82 0.00821208 at 10 eV, Pb208 0.00422701 at 20 eV, and Pb208 0.00387377 at 40 eV.

## Interpretation
The target optimum is a source/threshold phase diagram, not a monotonic mass rule and not a weak-interaction enhancement. The narrow Ge74 and Ti48 windows near 12.9 eV are genuine in the frozen ideal-physics model because independent refinement preserved topology. Practical detector efficiency, threshold distributions, backgrounds and material feasibility remain a separate gate.
