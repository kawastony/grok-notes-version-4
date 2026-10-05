# Berry curvature, Skyrme statistics, Callias

**Date:** 2026-10-05
**Status:** Three charges. Hedgehog spectral branch stays closed.

## Berry curvature in a crystal

A Bloch band has a Berry connection on the Brillouin zone. Its curl is the Berry curvature. The Chern number is that curvature integrated over the zone, divided by 2 pi.

Qi-Wu-Zhang two-band model, d = (sin kx, sin ky, m + cos kx + cos ky), 31 by 31 grid.

| m | Chern |
|---|-------|
| -3 | 0.001 |
| -1 | 0.982 |
| 0.5 | -0.970 |
| 1 | -0.982 |
| 3 | -0.001 |

The invariant is 0, +1, or -1 according to the mass window. It is a property of the filled band, not of a real-space defect. v2's Berry plaquette on the soft subspace was path-coherent and was not this integral. It stays rejected as a phase flux.

## Skyrme baryon statistics

Note 39 gave B = 0.999 for the static profile. Statistics are a further fact. Witten: a 2 pi rotation of the skyrmion picks up a phase from the Wess-Zumino term, exp(i N_c pi). For odd N_c the soliton is a fermion. For N_c = 3 it is the nucleon. That phase was not computed here. B = 1 does not by itself choose the statistics. f_pi and e remain external, so 18.7 eV is still not produced.

## Callias

Callias counts the degree of the mass map on the sphere at infinity, in odd dimension. It is not a Brillouin-zone Chern number and not a Wess-Zumino phase. The continuum statement stands. The Wilson hedgehog path has net flow 0. It is not this count.

## Placement

| Charge | Lives on | Here |
|--------|----------|------|
| Chern | Brillouin zone | computed, about 0 or 1 |
| Skyrme B | real-space profile | 0.999 |
| Skyrme statistics | Wess-Zumino phase | not computed |
| Callias | sphere at infinity | not counted on the lattice |
