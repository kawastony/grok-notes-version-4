# Skyrmion topology

**Date:** 2026-10-05
**Status:** Profile charge only. Not a spectral index. Hedgehog branch stays closed.

A skyrmion is a map from compactified R^3 to SU(2), classified by pi_3(S^3) = Z. The hedgehog ansatz U = exp(i tau . n-hat F(r)), with F(0) = pi and F(inf) = 0, has baryon number

B = (2/pi) integral sin^2(F) (-F') dr.

## Run

F = pi / (1+r), out to 20. B = 0.9993. Gradient energy 10.815, in units of the Skyrme scale. No f_pi, no dimensionless Skyrme coupling e.

Physical mass is (f_pi / e) times that number. Both constants are external. The run does not produce 18.7 eV. Forcing that energy through hc/E still gives 66.3 nm, as in notes 37 and 38.

## Map

| Object | Charge computed | Spectrum | Packet |
|--------|-----------------|----------|--------|
| Skyrme profile | B = 0.999 | not diagonalized | no |
| Jackiw-Rebbi kink | Q = 1 | zero mode | yes |
| Hedgehog Dirac | degree on the shell | flow 0 | no |

Baryon number on a classical profile is not the Callias count. The closed Wilson branch is not reopened by this integral.
