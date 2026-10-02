# Wilson term, and one diagnostic beside the frozen point

**Date:** 2026-10-02
**Status:** Diagnostic only. r=1 remains the frozen operator. The r=1.25 scan stays closed.

## What the Wilson term is

On the lattice the naive Dirac hopping has doublers: extra zeros at the corners of the Brillouin zone. The Wilson term adds a momentum-dependent mass,

(r/2) beta sum_mu (2 - T_mu - T_mu dagger),

so a corner mode of lattice momentum pi picks up a mass of order r times the number of directions. At r=1, m=0.5, L=4, that corner sat at 6.50, which is the free-control check. The same term breaks chiral symmetry explicitly. A continuum Callias zero can be lifted by it. That was the live suspect after the ball still avoided crossing.

## Diagnostic

Same ball as note 12. Radius 5, shell pinned, flow from constant mass to hedgehog. r=1 repeated. r=0 run once beside it. r=0 is not a new phase and is not the operator.

| r | s=0 pair | closest pair | s=1 pair | flips |
|---|----------|--------------|----------|-------|
| 1 | 0.110 | 0.00042 at s=0.88 | 0.00248 | 0 |
| 0 | 1.507 | 0.539 at s=1 | 0.539 | 0 |

## What it said

Removing the Wilson term does not release a crossing. It removes the approach. The near-zero pair is a feature of the r=1 operator, not a zero that r=1 is holding up. At r=0 the gap stays O(0.5) and the doublers are back, so that point is not a Callias continuum limit either.

The avoided crossing is therefore not explained by Wilson lifting alone. Geometry was already not enough. Amplitude was already not enough. The Wilson on/off switch is not enough. What remains is the finite lattice realization as a whole: no sphere at infinity, no Fredholm continuum limit, and a symmetric pair that approaches and turns back.

## Frozen

r=1 stays the operator. This diagnostic does not reopen a scan.
