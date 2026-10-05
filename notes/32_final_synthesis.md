# Final synthesis

**Date:** 2026-10-05
**Status:** Memo. No new runs. Closed branches stay closed.

Evidence chain: notes 08 through 31 in this repo. Parent operator control is grok-notes-version-2, free spectrum gap 0.500000 at L=4, r=1, m=0.5.

## 1. Positive controls

A sign-changing mass on a chiral discretization binds a zero when the setting matches the defect.

- Jackiw-Rebbi, 201 points: exact zero. Weight inside |x|<1 grows from 0.34 at v=0.5 to 0.74 at v=2.
- Pair split versus half-separation: 0.098 at d=1.5, 0.037 at 2, 0.005 at 3, 0.00068 at 4, 0 at 6.
- 2D kink, periodic along the wall: zero, strip weight 0.84.
- 2D vortex: zero, core weight 0.61.
- 3D vortex line, no Wilson term: zero, core weight 0.62. A line, not a point.
- 4D Gamma_5 kink: gap 0.34 at L=4, zero at L=5.

Chirality of the numerical Jackiw-Rebbi kernel was not resolved.

## 2. Hedgehog failures on tested boxes

- Wilson r=1, open cube L=10 to L=12: pair 0.001172 to 0.001098. Core weight 0.064 to 0.050. rms 4.87 to 5.86.
- Spectral flow, cube: nearest pair 0.150, 0.00227, 0.00621. Sign flips 0. Window count in (0, 0.2) starts at 2 and ends at 2.
- Boundary-mass pin: inert.
- Ball, invertible shell: closest 0.00034, then 0.00248. Flips 0.
- r=0 beside the frozen point: gap stays 0.539. Approach disappears.
- Overlap index, anticommuting grading: 0 at L=4 and L=6, cube and ball. Light mode not core-bound.
- Domain wall, L=4, six slices: twelve modes below 0.05, center weight 0.014.
- No-Wilson ball: eight modes below 0.05. Doubler kernel, not index 1.
- Midpoint parabola on the L=8 path: vertex at s=0.718, value 0.00134. A local well, not a kernel.

Overlap tracking of eigenvectors failed, minimum overlap 0. Those flips are not crossings.

## 3. Framework separation

- Continuum Callias: odd-dimensional R^n, |Phi| invertible outside a ball, index equals degree of U on the sphere at infinity. Gesztesy-Waurick, arXiv:1506.05144.
- Anghel, Commun. Math. Phys. 128, 77 (1990): same count on an infinite warped end, mass radially frozen and invertible. Not a cube.
- Atiyah-Singer: closed even-dimensional manifold, index equals the integral of A-hat ch. APS is the boundary version. The cylinder index of partial_s + H(s) was not computed.
- Lattice Wilson-Dirac index: Kubota, Ann. Henri Poincare 23, 1297 (2022), torus, gauge topology. Hip's real-eigenvalue count is the same setting. Reinhardt-Tok is a hedgehog of Wilson lines, not a scalar mass on an open box.

None of these equals the tested open hedgehog boxes.

## 4. Scoped conjecture

On the finite open lattices and the operator families in section 2, hedgehog degree on a shell does not force a nonzero spectral index. Geometric degree can be present. The spectral count can be zero. Near-zero pairs or clutter appear instead of one protected core mode. This does not refute continuum Callias. That operator was not built.

## Table

| Setup | Theorem setting | Control | Observed count | Localization | Reading |
|-------|-----------------|---------|----------------|--------------|---------|
| Jackiw-Rebbi | 1D kink | positive | 0 exact | tightens with v | counted |
| Pair of walls | 1D hybridization | positive | split falls with d | near walls | interaction, not a new defect |
| 2D kink | wall, periodic along it | positive | 0 | strip 0.84 | counted |
| 2D vortex | winding in plane | positive | 0, twofold | core 0.61 | bound, index not proved |
| 3D vortex line | line, no Wilson | positive | 0 | core 0.62 | line, not hedgehog |
| 4D kink L=5 | Gamma_5 wall | positive | 0 | not a bulk invariant | counted; L=4 was not |
| Wilson cube flow | not Callias | negative | net flow 0 | core ~0.05 | avoided crossing |
| Overlap L=6 | not torus AS | negative | index 0 | rms ~ half box | no count |
| Domain wall | not Shamir index | negative | 12 below 0.05 | center 0.014 | clutter |
| No-Wilson ball | not continuum | negative | 8 below 0.05 | core 0.59 | doublers |

## Not authorized

Another shell scan, overlap variant, cube-size tweak, or radial family. Quantum gravity stays the lowest assessment until a counted core mode exists on an operator that meets the Callias hypotheses.
