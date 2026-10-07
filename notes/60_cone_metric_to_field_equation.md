# Cone metric to field equation

**Date:** 2026-10-08
**Source:** Paper 1 Appendix L, Paper 1 asymptotic formula. Not previously filed on v4.
**Status:** Geometric equation written. Rotation-curve formula not derived from it.

## Metric

Paper 1 Appendix A, n=1: ds^2 = dr^2 + r^2 dtheta^2.

Appendix L, n=3:

ds^2 = dr^2 + r^2 (dpsi1^2 + sin^2(psi1) dpsi2^2 + sin^2(psi1) sin^2(psi2) dpsi3^2).

Volume weight sqrt(g) = r^3 sin^2(psi1) sin(psi2) on the angle ranges of a 3-sphere. If the angles are fibers of fixed length, r is the cone radius.

## Chaining

A phase theta_i with metric coefficient g_ii has decay constant f_i^2 = g_ii.

f1^2 = r^2,
f2^2 = r^2 sin^2(psi1),
f3^2 = r^2 sin^2(psi1) sin^2(psi2).

Instanton actions inherit the same factors: S2/S1 = sin^2(psi1), S3/S2 = sin^2(psi2). That is the chaining theorem. It is a statement about the kinetic coefficients, not about galaxies.

The variational condition partial_psi |f_i - f_j|^2 = 0 pushes psi_k to pi/2. The paper's 82.8 degrees is a small departure from that fixed point. The cosmic-clock reading of the angles is marked not derived.

## Field equation

Action for one radial scalar, no potential yet:

S = integral sqrt(g) (1/2) g^{rr} (d phi/dr)^2.

On the n=1 cone, sqrt(g) = r, g^{rr} = 1, so

S = integral r dr (1/2) (phi')^2.

Variation gives the radial equation

(1/r) d/dr ( r d phi/dr ) = 0,

if there is no potential and no source. First integral: r phi' = const. The pause condition phi' = 0 is the special case const = 0. It does not by itself pick r_p = 1/mu.

With a potential V(phi) and a baryonic source J,

(1/r) d/dr ( r phi' ) = dV/dphi - J.

The pause r_p is then the radius where phi' = 0, so dV/dphi = J there. The paper states r_p = 1/mu and does not write V or J.

## Where v_inf is not reached

The galactic formula v_inf = (Lambda_*^2 G M mu)^(1/4) is not a solution of the equation above. Lambda_* and mu are calibrated. The profile factor 1 - exp(-mu r) is stated, not obtained by integrating the cone equation.

## MOND, filed because it was not

MOND deep regime: v^4 = G M a0, a0 about 1.2e-10 m s^-2, by changing the force law. TAFA: v^4 = Lambda_*^2 G M mu, G unchanged, two galactic constants. They match on the quarter power if a_eff = Lambda_*^2 mu. Appendix H calls a_swirl = v_inf^2 / r_p that match. The frozen ruler 1.41e-10 is the same order, not this derivation.

Neither formula is the kink split. a and m0 of the packet stay unfixed.
