# Gamma properties of A(v)

**Date:** 2026-10-05

A(v) = 4^v Gamma(v+1/2) / (sqrt(pi) Gamma(v)).

Used facts. Gamma(z+1) = z Gamma(z). Gamma(1) = 1. Gamma(1/2) = sqrt(pi). Gamma(3/2) = sqrt(pi)/2. No poles for v > 0.

Recurrence, exact:

A(v+1) = 4 (v+1/2)/v A(v).

Checked at v = 0.25, 0.5, 1, 1.5, 2, 3, 4. The recurrence reproduces A(v+1).

Special values. A(1) = 2. A(2) = 12. A(1/2) = 2/pi.

Small v. Gamma(v) ~ 1/v, Gamma(v+1/2) ~ sqrt(pi), so A(v) ~ v. The split vanishes with the mass.

Large v. Gamma(v+1/2)/Gamma(v) ~ sqrt(v), so A(v) ~ 4^v sqrt(v/pi). At v=4 the Stirling form is 289 against 280.

These are properties of the coefficient. They do not supply a or m0.
