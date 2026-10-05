# Skyrme, insulator, hedgehog

**Date:** 2026-10-05
**Status:** Comparison. No new Dirac diagonalization.

## Skyrme dynamics

The model is a chiral field U(x) in SU(2). The Lagrangian has a two-derivative term and a four-derivative term. The second stops the soliton shrinking. The static hedgehog of note 39, F = pi/(1+r), has B = 0.999 and gradient energy 10.815 in Skyrme units.

Dynamics on that background are rigid motions of the same profile. A spatial rotation does not change B. A vibration changes the energy and not the integer, while F(0) and F(inf) stay at the boundary values. Quantizing the rotation gives the nucleon-delta split. That split needs f_pi and e, which are external. No time-dependent simulation was run. B is a constraint on the motion, not a packet.

## Topological insulator

A topological insulator is a gapped band structure whose invariant lives on the Brillouin zone. In two dimensions the invariant is a Chern number. In three dimensions it is a Z2 invariant. The protected object is a boundary mode, not a baryon.

The 4D kink in note 26 is the closest object already built. A Gamma_5 mass that changes sign binds a zero at L=5. That is a domain wall of an insulator, not a skyrmion. No Z2 invariant was computed.

## Against the hedgehog

| | Skyrmion | Dirac hedgehog | Insulator wall |
|--|----------|----------------|----------------|
| Field | U in SU(2) | fermion mass n-hat . tau | Gamma_5 mass |
| Charge | pi_3, B = 0.999 on the profile | pi_2, degree 1 on the shell | sign change |
| Spectrum here | not diagonalized | Wilson flow 0, core weight ~0.05 | zero at L=5 |
| Packet | no | no | yes, as a wall mode |

The same word hedgehog covers two maps. The Skyrme map winds R^3 onto SU(2). The Callias map winds the sphere at infinity onto the mass sphere. Note 39 computed the first. The closed branch failed to count the second. A shared shape does not transfer the packet.
