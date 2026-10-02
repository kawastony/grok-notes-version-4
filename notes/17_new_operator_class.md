# New operator class, first cut

**Date:** 2026-10-02
**Status:** The r=1 Wilson branch stays closed. This is a different operator.

## Why a new class

Note 16 said further boundaries of the frozen Wilson operator are not evidence. The recommendation was a continuum or chiral operator with a real index mechanism.

## Control that the method can see a bound zero

Jackiw-Rebbi, one dimension, no Wilson term:

H = -i sigma_x d/dx + sigma_z tanh(x),

on 81 points from -8 to 8. Lowest |lambda| is 0, twice, then 1.005. Weight inside |x|<1 is 0.51. A chiral continuum discretization does bind a zero mode. The tracker is not blind.

## Three-dimensional naive discretization

Same Dirac-isospin hedgehog, ball of radius 4, no Wilson term, shell pinned. 257 sites.

Eight modes sit below 1e-2. The lightest has core weight 0.55 and rms 1.88. An eight-fold kernel on a naive lattice Dirac operator is the doubler sickness, not a Callias count of N_def=1. This point is not accepted as the bridge.

## Not done

An overlap or domain-wall operator, whose index is defined without a doubler kernel, is the remaining credible lattice class. It is not built here. The Wilson r=1 branch is not reopened.
