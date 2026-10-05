# What counts as a packet

**Date:** 2026-10-05
**Status:** Standard written. Kink rerun. Mediator not derived from it.

A packet on the operator side is earned only when a spectral jump completes and a unit is stated. Approach is not enough.

| Case | Reaches zero | Protected | Stated unit | Packet |
|------|--------------|-----------|-------------|--------|
| Free Wilson gap 0.500000 | no | n/a | lattice unit | parked gap only |
| Jackiw-Rebbi kink | yes | yes, sign change | lattice unit only | yes, as a zero |
| Pair of walls | split falls with d | hybridization | lattice unit | shared gap, not a new defect |
| Hedgehog path | no, turns back at 0.00227 | no | none earned | no |

## Kink rerun

H = -i sigma_y d/dx + v tanh(x) sigma_z, 401 points on [-12, 12].

| v | lowest abs | rms |
|---|------------|-----|
| 0.5 | 7e-17 | 1.571 |
| 1.0 | 3e-16 | 0.907 |
| 2.0 | 1e-15 | 0.567 |

Stronger kink, tighter mode. Zero is stable. Pair of walls, mass v tanh(|x|-d): split 0.091 at d=1.5, 0.035 at 2, 0.0049 at 3, 0.00067 at 4, 0 at 6. Same law as note 22.

## 18.7 eV

Not produced by this run. A completed zero has energy 0 in the lattice unit. Turning the rms into a length needs an external spacing. Forcing 18.7 eV through E = hc/lambda gives 66.3 nm. That is a conversion, not a derivation, and it is not the kink width. The mediator stays an external scale. It is not the packet.

Hedgehog branch stays closed. No Delta W8 to eV map.
