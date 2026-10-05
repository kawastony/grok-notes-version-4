# Stirling expansion of A(v)

**Date:** 2026-10-05

Stirling: ln Gamma(z) ~ (z-1/2) ln z - z + (1/2) ln(2 pi) + 1/(12z) - 1/(360 z^3) + ...

For the ratio in the prefactor,

Gamma(v+1/2)/Gamma(v) ~ sqrt(v) (1 - 1/(8v) + 1/(128 v^2) + 5/(1024 v^3) + ...).

So

A(v) ~ 4^v sqrt(v/pi) (1 - 1/(8v) + 1/(128 v^2) + 5/(1024 v^3)).

| v | exact | 0 terms | 1 | 2 | 3 |
|---|-------|---------|---|---|---|
| 1 | 2 | 2.257 | 1.975 | 1.992 | 2.003 |
| 2 | 12 | 12.766 | 11.968 | 11.993 | 12.001 |
| 4 | 280 | 288.865 | 279.838 | 279.979 | 280.001 |
| 8 | 102960 | 104580 | 102946 | 102959 | 102960.02 |

Three terms recover the coefficient. The expansion is the large-mass form of the same split. It does not choose a or m0.
