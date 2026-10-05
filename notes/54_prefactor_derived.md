# Prefactor derived

**Date:** 2026-10-05
**Status:** Closed inside the lattice. No anchor.

The single-wall zero mode is N sech(x)^v, with

N^2 = Gamma(v+1/2) / (sqrt(pi) Gamma(v)).

The far tail is N 2^v e^{-v|x|}. Walls at ±d. The product of the tails supplies

Delta E = [4^v Gamma(v+1/2) / (sqrt(pi) Gamma(v))] exp(-2 v d).

At v=1 this is 2 exp(-2d), the same as the old 2v guess. At other v it is not.

Continuum grid, 801 points on [-16, 16]. Ratio of measured lowest absolute eigenvalue to this formula:

| v | d=2 | d=3 |
|---|-----|-----|
| 0.5 | 1.003 | 1.002 |
| 1.0 | 0.965 | 0.996 |
| 1.5 | 0.948 | 0.996 |
| 2.0 | 0.933 | 0.997 |

At d=3 the coefficient is the tail normalization. At d=2 the walls are not yet in the asymptotic regime, and the ratio sits a few percent low. The exponent and the prefactor are both accounted for. No a or m0 is inserted.
