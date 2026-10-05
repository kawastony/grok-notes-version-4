# Midpoint tool, used as in v2

**Date:** 2026-10-05
**Status:** Local diagnostic. Not an index. Closed branches stay closed.

## How v2 used it

ENDPOINT_WELL_DEEPENING.md treats two endpoints at u_star plus or minus Delta, midpoint fixed, and reads a decreasing separation as a deepening well. It says the picture is not a potential derived from the action, and that r_p and (w0, wa) are not forced by it.

G12_avoided_crossing_fit.md fits a two-level form mid(s) plus or minus sqrt(half(s)^2 + V^2). V came out about 1e-6. The fit missed the dip. The note says a two-level model is not enough, and it does not lock integer spectral flow.

The quadratic identity used here is the same class of tool. For f(x) = ax^2 + bx + c,

(f(m+h) - f(m-h)) / (2h) = f'(m).

It recovers a midpoint slope from the endpoints. It does not recover a kernel.

## Applied to the recorded flow

Nearest-pair magnitudes on the L=8, r=1 path, at s = 0.60, 0.70, 0.80: 0.00484, 0.00142, 0.00303.

Parabola: a = 0.252, b = -0.361, c = 0.131. Secant slope -0.00905. Midpoint derivative -0.00905. The identity holds. Vertex at s = 0.718, value 0.00134.

## What it makes visible

The turn-back is a local well of the eigenvalue, bottom at about 0.0013, not at zero. A sign census cannot see it, which is the same fact as the negative count staying flat. v2's two-level fit missed an analogous dip for the same reason: the soft window is not a single Landau-Zener gap.

## What it does not do

It does not produce Callias index 1. It does not replace the Dirac solve. It does not reopen the hedgehog branch. A local curvature of |lambda|(s) is not a degree on a sphere at infinity.
