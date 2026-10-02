# Two spectral-flow methods, same path

**Date:** 2026-10-02
**Status:** Both recommendations run. Neither is an APS cylinder index. r=1 held.

## Path

Open L=8 cube, r=1, s from constant mass along z to the hedgehog. Eleven samples. Eight modes from shift-invert around 0. The eighth mode sits between 0.19 and 0.44, so a window of 0.2 does not contain every computed mode at every sample. The pair near 0.001 is inside it.

## Continuous branches

Eigenvectors matched by absolute overlap, greedy. Minimum overlap on the path was 0. The reported sign flips, including a pair exchange near s=0.65 and an edge swap at s=1, are matching failures. They are not crossings. This method did not finish.

## Windowed count

Phillips-style reduction: number of eigenvalues in (0, 0.2).

Start: 2. End: 2. Delta: 0. The count rises to 4 near s=0.9 and returns. Net flow in this window is 0.

## Cylinder

The operator partial_s + H(s) on this grid is about 40,000 dimensional. Its index was not computed. The windowed count is the substitute, not the APS index.

## Call

The reliable half agrees with notes 09 through 13: net flow 0 in the near-zero window. The branch tracker did not produce a count. Fredholm hypotheses are still absent. r stays 1.
