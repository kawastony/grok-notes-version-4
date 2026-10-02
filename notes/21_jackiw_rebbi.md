# Jackiw-Rebbi defects

**Date:** 2026-10-02
**Status:** One-dimensional control. Not a count of the three-dimensional hedgehog.

## What it is

A Dirac operator in one dimension with a mass that changes sign,

H = -i sigma_x d/dx + sigma_z m(x),

m(x) = v tanh(x), has an exact zero mode bound at the wall. The mode is chiral. Its decay is set by the integral of the mass. An antikink binds the opposite chirality. Two walls close together hybridize the zeros into a small pair. This is the one-dimensional ancestor of the Callias defect, not the three-dimensional theorem.

## Run

201 points from -10 to 10.

| v | min abs | next | rms | weight inside abs(x)<1 |
|---|---------|------|-----|-------------------------|
| 0.5 | 0 | 0.522 | 2.76 | 0.34 |
| 1 | 0 | 1.003 | 1.57 | 0.53 |
| 2 | 0 | 1.731 | 0.91 | 0.74 |

The zero stays. Stronger kink, tighter mode. Antikink also binds a zero. A kink plus an antikink, walls near +3 and -3, lifts the exact zero to 0.005, four-fold at that scale, with 0.55 of the weight near the walls.

Flow from a constant mass 0.8 to the kink: the gap falls from 0.80 to 0 and stays there. Negative count stays 201, half the dimension, because the spectrum is symmetric. The zero appears. It does not change the negative count.

## What it does not say

A chirality expectation computed with sigma_y came out zero and is not used. This control does not transfer to the closed r=1 Wilson branch, the overlap index of 0, or the twelve-fold domain-wall pile. It says only that a chiral one-dimensional kink is counted by this method.
