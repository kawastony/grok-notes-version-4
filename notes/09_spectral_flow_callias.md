# Spectral flow against the Callias count

**Date:** 2026-10-02
**Status:** Flow run. Zero crossings. Index bridge still unconfirmed.

## Callias, as used here

On odd-dimensional space the index of L = Q + Phi is the degree of the unitarized mass on the sphere at infinity, provided Phi is invertible out there. A unit hedgehog has degree 1, so Index = N_def = 1, up to sign. Spectral flow is the lattice proxy: eigenvalues may move, and the net number of zero crossings equals the change in index, if the asymptotics stay in the Fredholm class.

This box does not meet that hypothesis. The boundary is a cube, not a sphere at infinity. The Wilson term at r=1 is explicit chiral breaking. Note 08 already found the light pair delocalized.

## Shell

On L=12, sites with radius in [3, 4): 144 sites, all 8 octants occupied, mean direction about 0. The geometric hedgehog is present. That is the topological side of Callias. It is not yet an operator index.

## Flow

Open L=8, r=1. s=0 is a constant invertible mass along z, degree 0. s=1 is the hedgehog. Shift-invert, four modes nearest zero.

| s | Nearest pair | Sign flips |
|---|--------------|------------|
| 0.00 | 0.150 | 0 |
| 0.62 | 0.00227 | 0 |
| 0.75 | 0.00240 | 0 |
| 1.00 | 0.00621 | 0 |

Sorted-sign flips over the whole path: 0. The pair approaches zero and turns back. Negative count among the four stays 2. No spectral flow.

## Agreed reading, implemented

Diagnostic, not validation. The light pair is not a bound defect zero mode, does not realize N_def=1, and does not move through the gate. From L=10 to L=12 it shifted by about 7e-5, core weight fell from 0.064 to 0.050, and the rms radius grew. A bound mode would sit on the core and fall. This one spreads and stalls.

The flow adds the missing half. The geometric degree is on the shell. The operator does not count it: no crossing. Periodic boxes were already the wrong topology. Open boxes give a delocalized symmetric pair, lifted by the Wilson term and the boundary.

Percentages in the prompting note are an assessment, not a ledger row.

## Still closed

r=1. No proxy. No SPARC residual pass. No macro inheritance from this pair. Fork A remains the fork. The finite-volume defect bridge stays unconfirmed.
