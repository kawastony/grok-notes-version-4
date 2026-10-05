# 2D kink against a 3D vortex

**Date:** 2026-10-05
**Status:** New line defect. Not the closed hedgehog branch.

A 3D vortex is a line: winding in the xy plane, uniform along z. A hedgehog is a point. This note does not rerun the hedgehog.

## 3D vortex run

Four-component Dirac, no Wilson term. Hops counted once. Box 11 by 11 by 6, periodic along the line. Mass v tanh(r/1.5) (x-hat beta + y-hat alpha_x), v=1.5. Dimension 2904.

Lowest abs 0. Modes below 0.05: 8. Core weight inside r<=2: 0.621.

## Comparison

| | 2D kink | 3D vortex line |
|--|---------|----------------|
| Defect | sign change across a line | winding around a line |
| Extra direction | periodic along the wall | periodic along the vortex |
| Operator | two-component, no Wilson | four-component, no Wilson |
| Lowest abs | 0 | 0 |
| Multiplicity below 0.05 | 4 | 8 |
| Weight | 0.84 in the wall strip | 0.62 in the core disk |

Both bind. The kink weight sits on a wall. The vortex weight sits on the line. The extra multiplicity in 3D is the symmetric pair times the line direction, not eight defects.

## Not transferred

The r=1 Wilson hedgehog still has net flow 0, overlap index 0, and a delocalized pair. A no-Wilson line defect binding a zero does not reopen that branch.
