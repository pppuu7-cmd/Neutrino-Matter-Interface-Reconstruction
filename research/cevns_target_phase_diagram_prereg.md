# Prospective contract — real-nucleus solar CEvNS target/threshold phase diagram

Date frozen: 2026-09-06
Gate: G2 inverse target design
Parent result: iteration 0045

## Question

Is the non-monotonic winner sequence found in iteration 0045 a stable full-solar inverse-design structure? Locate the threshold intervals and crossover points where the ideal per-kg CEvNS-optimal real nucleus changes, and identify the solar source regime responsible for each interval.

## Frozen scope

Physics-only Standard-Model ideal CEvNS counts per kg. This gate does **not** include detector/nucleation efficiency, natural abundance, chemistry, backgrounds, dead time, reset/preparation energy or stored-energy amplification.

## Frozen inputs

Exactly reuse iteration 0045 authority:

- `data/cevns_target_candidates_exact_mass.csv` — same 23 nuclei and exact frozen masses;
- `data/cevns_target_exact_mass_provenance.md`;
- `data/solar_flux_b16.csv`, B16-GS98 branch;
- `data/solar_spectrum_manifest.csv` and pinned spectrum commit/blob provenance;
- `data/be7_bahcall1994_ground_profile.csv`;
- same weak charge convention and `sin^2 theta_W=0.23857`;
- same Helm form factor and recoil integration convention;
- same source list: pp, Be7-ground, Be7-excited, pep, N13, O15, F17, B8, hep;
- exact target masses in both kinematics and nuclei/kg.

No post-result target additions or physics-tolerance changes are allowed in this gate.

## Prospectively frozen scan

Coarse threshold grid [eV]:

`0.5, 1.0, 1.5, ..., 15.0, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 45, 50, 60, 80, 100`.

At each threshold compute all 23 full-solar rates and record:

1. winner and runner-up;
2. total ideal events/(kg day);
3. fractional winner margin `(R1-R2)/R1`;
4. winner's dominant source and source-resolved rate vector;
5. Helm/no-Helm winner rate ratio.

Every change of winner between adjacent coarse points defines a crossover bracket. Refine each bracket by bisection on the difference of the two endpoint-winning target rates until bracket width is `<=0.02 eV`, unless a third target becomes larger inside the bracket; in that case split the bracket and resolve the actual adjacent winners.

## Stability check

Repeat transition classification on an independent half-step grid over every coarse bracket containing a winner change. A crossover is stable when:

- the same adjacent winner identities are recovered; and
- refined crossover location changes by `<=0.05 eV` or `<=2%`, whichever is larger.

## Frozen scientific acceptance

### PASS_PHASE_DIAGRAM
All winner transitions in 0.5–100 eV are bracketed/refined, stability criteria pass, and every interval has a source-dominance classification.

### PARTIAL_PHASE_DIAGRAM
Some transitions are robust but one or more intervals are numerically unresolved or exhibit near-degenerate multi-target competition. Report those intervals explicitly; do not force a single winner.

### FAIL_NONROBUST_WINNER_SEQUENCE
Grid refinement changes the qualitative winner topology enough that the 0045 `Pb -> Xe -> Se -> Pb` picture is not stable. Preserve 0045 but classify the six-point sequence as under-resolved.

Infrastructure/download/hash failures are `INFRASTRUCTURE_FAIL`, not scientific FAIL. They must be fixed without altering the frozen scientific inputs or acceptance criteria.

## Mandatory interpretation

The result must distinguish:

- a target/threshold optimum from interaction enhancement;
- source-regime switching from new microphysics;
- ideal interaction rate from detector accepted rate;
- detector signal amplification from neutrino-energy gain.

No target winner is a practical material recommendation until a real detector transfer function is applied.

## PASS next action

Freeze a real metastable detector transfer-function gate:

`R_acc/kg = sum_s integral dE_nu Phi_s(E_nu) integral dT (d sigma_s/dT) epsilon_nuc(T)`

with measured/primary-source nucleation or trigger efficiency, threshold distribution/stability, backgrounds/dark counts, live fraction/dead time, reset/preparation cost and stored-free-energy accounting.

## FAIL/PARTIAL next action

Increase only numerical resolution inside prospectively identified ambiguous brackets; do not change physics inputs, target set, source set or acceptance definition.
