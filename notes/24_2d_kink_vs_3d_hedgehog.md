# 2D kink against the 3D hedgehog

**Date:** 2026-10-05
**Status:** Comparison only. No new 3D run. Closed branches stay closed.

## Side by side

| | 2D kink | 2D vortex | 3D hedgehog, r=1 Wilson |
|--|---------|-----------|-------------------------|
| Operator | two-component, no Wilson | same | eight-component Wilson |
| Defect | sign change of a scalar mass | winding-1 mass texture | hedgehog, degree on a shell |
| Boundary | periodic along the wall | open box | cube, then ball |
| Lowest abs | 0 | 0 | 0.0011 at L=12, not through 1e-6 |
| Multiplicity | 4, symmetric pair | 2 | pair, delocalized |
| Where the weight sits | 0.84 in the wall strip | 0.61 in the core | 0.05 in the core, rms grows with the box |
| Net flow | not needed; the zero is there | not computed | 0 |
| Counts N_def | the wall mode is the 1D ancestor | not a proved index | no |

## What differs

The 2D kink is the Jackiw-Rebbi wall with one extra periodic direction. The mass changes sign across a line. The mode is bound to that line. Removing the double-counted hop was enough to see it.

The 3D hedgehog asks for a sphere at infinity and a Fredholm operator. The runs had a cube or a ball, a Wilson term, and a light pair that spread with the volume. Spectral flow was an avoided crossing. Overlap index was 0. Domain wall gave twelve near-zeros, not one core mode.

Same word, defect, two different objects. The 2D zero does not license a reread of notes 09 through 20.

## Shared fact

A chiral operator with a sign-changing mass can bind a zero in one and two dimensions, on this discretization. The three-dimensional finite-volume bridge remains unconfirmed.
