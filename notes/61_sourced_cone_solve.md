# Sourced cone scalar, solved

**Date:** 2026-10-08
**Status:** Linear model run. No pause. No flat curve.

Action, n=1 cone, axial scalar:

S = integral r dr dtheta [ (1/2)(d phi/dr)^2 - (1/2) mu^2 phi^2 + J(r) phi ].

Equation:

phi'' + (1/r) phi' - mu^2 phi = -J(r).

Source used: J = J0 exp(-r/Rd). Boundary: phi'(0)=0, phi(large)=0. Units mu=1.

Four runs, (J0, Rd) = (1,1), (1,2), (1,0.5), (5,1). No zero of phi' in any run. The derivative keeps one sign. A pause does not appear.

Cumulative phi(0)-phi(r), normalized, versus 1-exp(-mu r): rms 0.14 at Rd=1, 0.07 at Rd=0.5, 0.25 at Rd=2. A resemblance at one disk scale, not the stated factor.

r phi' is briefly steady over about one length, then decays with the K1 tail. No extended 1/r force.

mu is still the mass term, not a cone output. Lambda_* is not in the action. The kink packet is not in this solve.
