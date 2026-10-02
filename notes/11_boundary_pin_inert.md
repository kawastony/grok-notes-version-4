# Boundary-mass pin does not create the crossing

**Date:** 2026-10-02
**Status:** Next check after note 10. r=1 held.

## Question

Note 10 said the flow missed Callias because the mass is not invertible on a sphere at infinity. The amplitude half of that can be tested without moving r: force |Phi| >= 1.5 on the outer layer of the cube, and repeat the L=8 flow.

## Result

The pin does not bind. On this profile, tanh(rad/1.5) is already about 1 on the outer layer, so v f is already above 1.5 at s=1. The tracked spectrum is identical to note 09.

| s | Nearest pair | Flips |
|---|--------------|-------|
| 0.00 | 0.150 | 0 |
| 0.62 | 0.00227 | 0 |
| 1.00 | 0.00621 | 0 |

Net spectral flow remains 0. Negative count remains 2.

## What that isolates

The avoided crossing is not caused by a vanishing boundary amplitude. The mass on the outer layer was already invertible. What is still missing is the sphere at infinity, and the Wilson term is still present. Pinning a cube face does not supply the sphere.

## Call

The finite-volume bridge stays unconfirmed. r stays 1. No proxy. The next gap, if one is opened, is a spherical outer boundary with the same operator, not a change of r and not a reread of this cube.
