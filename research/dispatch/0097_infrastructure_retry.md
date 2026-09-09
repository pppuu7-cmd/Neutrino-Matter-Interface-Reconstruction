# 0097 one-use infrastructure retry

Date: 2026-09-09

Purpose: trigger the repaired 0097 workflow after run `34336438408` failed before any science calculation because `numpy` was missing from the runner environment.

Frozen parent remains unchanged:
- 0096 authoritative run: `34319781596`
- 0096 authoritative head: `eff5996612f31c093e82a9ae0cdfdb859da8cb9a`
- 0096 terminal status: `PASS_V2_G9_BETELGEUSE_CENTRAL_SUPPORT_50MAS`

The infrastructure repair commit `1db7093596360909189fb84381d3e05d47a74979` only installs the runtime dependencies required by the already-frozen evaluator. No 0097 scientific input, threshold, equation, horizon, astrometry value, architecture definition, terminal label, or preregistration/amendment was changed.
