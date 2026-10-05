# Prefactor attempt

**Date:** 2026-10-05
**Status:** Exponent kept. Prefactor not closed. No anchor.

Tail argument: walls at ±d, asymptotic mass v, hybridization e^{-2 v d}. The simplest coefficient is 2v, so Delta E = 2v exp(-2 v d).

Continuum grid, 801 points on [-16, 16]. Lowest absolute eigenvalue against that formula.

| v | d | measured | 2v exp(-2vd) | ratio |
|---|---|----------|--------------|-------|
| 0.5 | 2 | 0.0864 | 0.1353 | 0.64 |
| 0.5 | 3 | 0.0318 | 0.0498 | 0.64 |
| 1.0 | 2 | 0.0354 | 0.0366 | 0.97 |
| 1.0 | 3 | 0.00494 | 0.00496 | 1.00 |
| 2.0 | 2 | 0.00376 | 0.00134 | 2.80 |
| 2.0 | 3 | 0.000074 | 0.000025 | 2.99 |

The ratio is stable in d and depends on v. The exponent is the derived piece. The prefactor is not 2v except near v=1. No analytic coefficient is written. No a or m0 is inserted.
