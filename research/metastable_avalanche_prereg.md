# NMIR G2 preregistration — passive metastable / avalanche trigger gate

Date: 2026-09-06
Status: prospectively frozen before hosted benchmark inspection.

## Question
Can a passive non-convex/metastable medium use a tiny neutrino interaction to produce a macroscopically large output, and if so does that evade the NMIR neutrino-supplied-energy ceiling or only amplify detection/control by releasing stored medium free energy?

## General first-law accounting
Take a passive medium initially in a metastable state with energy/free-energy `F_m`, and a relaxed state `F_s <= F_m`. Define stored releasable medium energy

`DeltaF_store = F_m - F_s >= 0`.

A neutrino interaction deposits trigger energy `epsilon_nu`, with the NMIR accounting guard

`0 <= epsilon_nu <= E_nu`.

With no simultaneous external power input, total energy delivered to detector/bath during the triggered relaxation obeys

`E_out <= epsilon_nu + DeltaF_store`.

Decompose the source ledger:

`E_out,nu <= epsilon_nu <= E_nu`,

`E_out,medium <= DeltaF_store`.

Thus a large signal/trigger amplification

`G_signal = E_out / epsilon_nu <= 1 + DeltaF_store/epsilon_nu`

is physically allowed and can be enormous, while the neutrino-supplied energy amplification satisfies

`G_nu_energy = E_out,nu/epsilon_nu <= 1`.

If the device is reset to the metastable state for cyclic operation, the external recharge work is at least the replenished stored free energy in an ideal reversible accounting and larger in a dissipative real device. That recharge energy is not neutrino-supplied power.

## Barrier condition
Let `DeltaF_barrier` be the activation barrier measured from the metastable state along the relevant reaction coordinate. A deterministic one-shot energy trigger requires at least

`epsilon_nu >= DeltaF_barrier`

unless thermal/quantum fluctuations or active biasing supply part of the barrier-crossing energy. If fluctuations/bias do so, their energy/noise contribution must be accounted separately. A sub-barrier neutrino can still change a stochastic switching probability, which is a detector/control effect, not extra neutrino energy.

## Toy avalanche benchmark
Use an abstract metastable reservoir characterized by:
- neutrino trigger `epsilon_nu`;
- stored release `DeltaF_store`;
- barrier `DeltaF_barrier`;
- optional external assist `epsilon_assist`.

A trigger is energetically eligible if `epsilon_nu + epsilon_assist >= DeltaF_barrier`.
For an eligible ideal relaxation:

`E_out_total = epsilon_nu + epsilon_assist + DeltaF_store`,

but source-resolved outputs remain

`E_out_nu = epsilon_nu`,
`E_out_assist = epsilon_assist`,
`E_out_medium = DeltaF_store`.

## Frozen hosted checks
1. For `epsilon_nu=1 eV`, `DeltaF_store=1 MeV`, `barrier=0.5 eV`, no assist: event output amplification must be `1,000,001`, while neutrino-energy gain is exactly `1`.
2. Scaling `DeltaF_store` over `1 eV -> 1 GeV` at fixed trigger must change signal gain linearly but leave neutrino-energy gain exactly `1`.
3. If `epsilon_nu < barrier` and no assist, deterministic trigger must fail closed.
4. If assist supplies the missing barrier energy, trigger may occur but assist energy must appear explicitly in the ledger.
5. Recharge ledger for repeated cycles: ideal external reset work must be at least `DeltaF_store`; therefore steady-state useful output beyond neutrino deposition cannot be attributed to neutrino power.
6. Randomized positive ledgers must satisfy source-resolved energy conservation to `<1e-12` relative tolerance.

## Classification contract
- `PASS_METASTABLE_AVALANCHE_LEDGER` if all accounting/trigger checks pass.
- Scientific interpretation for **energy harvesting**: **STRONG-NEGATIVE scoped** against counting metastable avalanche energy as neutrino-supplied power.
- Scientific interpretation for **detection/control**: **PASS-SURVIVOR**. Metastability/avalanche remains a potentially valuable neutrino event amplifier if a real microscopic neutrino-trigger channel and acceptable noise/reset rate can be demonstrated.
- Real material candidates, switching kinetics, dark counts, thermal/quantum activation and microscopic coupling remain OPEN.
