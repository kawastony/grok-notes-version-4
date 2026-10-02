# Small r=1 index check

**Date:** 2026-10-02
**Code:** `code/index_r1_small.py`
**Status:** Free control passes. Hedgehog count does not yet match N_def. Not a proxy for the L=10 Colab tubes.

## Operator

Same class as v2 `Eight_component_algebra_and_free_spectrum.md`.

H = alpha.p (x) 1_tau + beta (x) mass, Wilson r=1.
Eight components. Dense eigh. Gate on the free run is 1e-6. Hedgehog gate used below is 1e-2, because nothing reached 1e-6.

No r scan. No gamma_5 proxy. No archetype tube.

## Free control

L=4, m=0.5, r=1, periodic, no hedgehog.

Lowest |lambda| = 0.500000, eight-fold. Modes below 1e-6: 0. Doubler corner 6.500000.

Matches the v2 health call. Operator class did not drift.

## Hedgehog

Mass beta (x) (v f tau.n), f = tanh(rad/Rcore), Rcore=1, v=2, L=6.

| Boundary | lowest |lambda| | n < 1e-2 | n < 1e-3 |
|----------|------------------|----------|----------|
| open | 0.0083, 0.0083 | 2 | 2 |
| periodic | 0.0363 (six) | 0 | 0 |

Open-boundary flow in v, L=6, r=1. Negative-eigenvalue count stays 864, half the dimension, at every sample. No net crossing is resolved. A pair dips under 1e-2 only at v=2.00 (min |lambda|=0.0083) and is gone at v=2.25. That is not a gated zero mode tracking N_def=1.

## Call

Fail against the pre-registered success condition on this volume. Gated soft-mode count does not match N_def. The free operator is the right one. The defect count is a small-volume miss, not a new index theorem and not a license to change r.

Larger-L F^rel ordering was not rerun. L=10 is 8000-dimensional dense; L=12 is the Colab shift-invert that already failed in the sandbox. A stand-in would be the proxy this fork forbids.

## BAO note

`notes/04_bao_mean_chi2.md` stays a reduced, mean-level, fixed-input score. No Pantheon+. Not promoted.
