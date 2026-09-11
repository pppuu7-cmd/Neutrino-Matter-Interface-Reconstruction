# 0103 current gate snapshot — superseding status note

Date: 2026-09-12
Benchmark: `NMIR-BENCHMARK-0103`
NMIR v1 status: `100% CLOSED / IMMUTABLE`

This note supersedes older narrow wording that named only `B_perp(r)` as the remaining Betelgeuse blocker. The stronger requirement exposed by the co-registration work is a coherent magneto-matter state: vector B and matter variables must belong to one documented numerical state before a Betelgeuse-specific terminal propagation can be authoritative.

## Closed / PASS layers

- Borexino magnetic-moment upper-bound authority: byte-pinned.
- Conditional Majorana single mass-basis `mu_12` branch: frozen; upper-envelope benchmark only.
- Majorana mass/flavor basis invariance: `PASS_0103_MAJORANA_MU12_BASIS_INVARIANCE_NONTERMINAL`.
- NuFIT 6.1 full three-flavor numerical integration: PASS for prospectively retained NO and IO branches; official PDF byte-pin remains an archival/TLS issue.
- Generic native Pencil 3-D vector ingestion: PASS on the separate mdwarf regression fixture.
- 0103C field/matter co-registration audit: GitHub Actions run `34654908394` — success.
- 0103R path reproducibility audit: run `34654920412` — success.
- 0103E six-state end-to-end surrogate audit: run `34654934565` — success.
- 0103M coherent synthetic magneto-matter end-to-end pipeline: run `34657252656` — PASS.
- 0103X six-state stress/convergence matrix: run `34657252689` — PASS.
- Baseline repository CI on implementation commit `8340994380ceaf55621b74f74f9cc393f04e4776`: run `34657252673` — success, including full pytest and `python -m nmir.baseline`.

## What M/X changed

0103M demonstrates that one co-registered 3-D state can be sampled on one frozen ray, converted to `B_perp`, combined with co-located matter variables and propagated through the six-state solver with interpolation/geometric/Hermiticity/unitarity/repeatability gates all passing.

0103X demonstrates convergence over couplings `[0,1e-3,1e-2,1e-1,1]`, resolutions `[64,128,256,512,1024]`, and `N_ref=4096`; the worst N=1024 probability error versus reference is `1.1071636862869383e-07`, below the preregistered `1e-6` ceiling.

These results materially reduce internal numerical/interface uncertainty. They do not create astrophysical authority.

## Remaining terminal blocker

A Betelgeuse-specific calculation still requires a recoverable state/snapshot satisfying at minimum:

- machine-readable `B(x,y,z)` or enough native state information to derive it;
- co-registered matter density and electron/composition information sufficient for the matter Hamiltonian;
- one shared coordinate system/grid or a prospectively frozen, auditable co-registration map;
- units and normalization;
- snapshot/run identity and provenance;
- deterministic ray/orientation contract.

No indexed public full state satisfying this contract has yet been recovered from the Dorch/Betelgeuse search.

Current terminal ceiling:

`BLOCKED_0103_BETELGEUSE_COHERENT_MAGNETO_MATTER_STATE_AUTHORITY`

No physics FAIL is inferred. If the original/compatible full state is eventually recovered, the internal NMIR pipeline is now substantially prepared to consume it without inventing an internal magnetic profile. If the archive/author route is exhausted, the Betelgeuse-specific terminal branch should be classified external-data-limited rather than forced.
