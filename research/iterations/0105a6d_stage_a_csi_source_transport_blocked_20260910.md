# 0105a6d Stage-A — CsI arXiv source transport/identity BLOCKED

Date: 2026-09-10
Gate: `NMIR-V2-0105A6D`
Classification: `BLOCKED_0105A6D_AUTHORITY_BYTE_MISMATCH_OR_TRANSPORT`
Scope: authority acquisition/inventory only; NONDISCOVERY.

## Frozen parent

Preregistration: `research/prereg/0105a6d_coherent_official_likelihood_implementation_authority.md`.
The frozen authority scope requires the exact arXiv source archives for `1708.01294v1` and `2003.10630v7`, in addition to the two official COHERENT Zenodo releases. No SM/null likelihood construction or observed BSM residual is authorized in this stage.

## Hosted execution consumed

Execution head: `4c69bba66885f442d5872a8bc1602daadde8ebfd`
Run/job: `34478709634 / 102875777045`
Artifact: `10152705473`, `nmir-v2-0105a6d-coherent-official-likelihood-authority`
Provider artifact digest: `sha256:7030fc5f1b4bfb136ba8bb014bdcc6c2d9a29989da497f0a5db39a22db8748f1`
Independently downloaded ZIP SHA256: `7030fc5f1b4bfb136ba8bb014bdcc6c2d9a29989da497f0a5db39a22db8748f1`
Inner `official_authority_inventory.json` SHA256: `2c5830a092c3f13a4085f86e76577f33ee784d0d4433a8979c7f39a7dc760a72`
Inner `run_stdout.txt` SHA256: `6863401e2c00ff7bee9fa64e772435910049c15f6c5f236dfa33e26c24f5e397`
Inner `inventory_sha256.txt` SHA256: `e2d1f66fa5f3d336280bd1fd810086fb2c089f7de1aa7cdea379a9cb0d24ebbb`

The GitHub workflow conclusion was green, but green CI is not promoted to scientific/authority PASS.

## Exact blocker

The Ar source `2003.10630v7` was retrieved as a parseable tar archive with text members including `main.tex` and `supplemental.tex`.

The CsI entry `1708.01294v1` was not recovered as a source archive. The emitted inventory has `members=[]`; its retrieved byte SHA256 is `a47539271203e0d0ea71a45ede2535011bcd2b0cdb2a846beecb1f54302fe9fc`, the same byte identity already observed for the frozen CsI PDF rather than a source tar/member bundle. The collector treated an unparseable binary response as an empty-member source instead of failing closed.

Therefore the deterministic source-member inventory required by the frozen preregistration is incomplete. This is exactly the frozen `BLOCKED_0105A6D_AUTHORITY_BYTE_MISMATCH_OR_TRANSPORT` route, not a likelihood-semantics conclusion and not a Standard-Model scientific failure.

## Authorized repair

Repair only transport/identity handling: reject PDF-magic responses for a requested arXiv source archive; try only official arXiv source/e-print endpoints for the same exact versioned identifier; require a tar archive or a decodable single source file with at least one member; record every endpoint attempt, resolved URL, byte size and SHA256. If all official source endpoints fail to yield source bytes, preserve the BLOCKED classification.

No likelihood criterion, nuisance convention, binning, normalization, threshold, benchmark, operator family or residual rule may change.

`SM_NULL_REPRODUCTION_PERMISSION = 0%`

`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`
