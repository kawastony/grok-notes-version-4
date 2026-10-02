# Spherical outer boundary

**Date:** 2026-10-02
**Status:** The cube reread is closed. This is the same operator on a ball.

## Setup

Sites of the L=12 cube with radius <= 5. 552 sites, dimension 4416. Outer shell, rad >= 4, has f=1 and |Phi| pinned at or above 1.5. r=1. Flow from a constant mass along z to the hedgehog. Shift-invert, four modes nearest zero.

This is a lattice ball, not a continuum sphere at infinity. The Wilson term is still on.

## Flow

| s | Nearest pair | Flips |
|---|--------------|-------|
| 0.00 | 0.110 | 0 |
| 0.62 | 0.00482 | 0 |
| 0.75 | 0.00153 | 0 |
| 0.88 | 0.00034 | 0 |
| 1.00 | 0.00248 | 0 |

Sorted-sign flips: 0. Negative count stays 2. The pair gets closer than on the cube (0.00034 against 0.00227) and still turns back.

## Call

A spherical outer shell with invertible mass is not enough. Spectral flow remains 0. The remaining structural piece in this operator is the Wilson term at r=1, which this fork does not move. The finite-volume defect bridge stays unconfirmed.
