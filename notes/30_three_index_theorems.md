# Three index theorems, not one

**Date:** 2026-10-05
**Status:** Investigation. No new diagonalization.

## Wilson-Dirac index

On a lattice, the object with a proved index is the Wilson-Dirac operator on a torus, not an open cube. Kubota, Ann. Henri Poincare 23, 1297 (2022), shows that the index of a twisted continuum Dirac operator on the standard torus is recovered from the corresponding lattice Wilson-Dirac operator, by higher index theory of almost flat bundles. Hip, hep-lat/9712015, conjectures the practical count: the difference between real eigenvalues of the Wilson matrix with positive and negative chirality, in the physical branch. Both are gauge-field topology on a closed manifold.

The r=1 hedgehog runs did not compute this. They had an open box, a scalar mass texture, and no torus gauge field. Overlap index 0 on L=4 and L=6 is a number from a different operator, not this theorem.

## Anghel

Anghel, Commun. Math. Phys. 128, 77 (1990), extends Callias off flat R^n. The manifold is an odd-dimensional spin manifold with a warped end W = (eps, infinity) x_f N, with the warping f(r) going to infinity. The perturbation A is skew-Hermitian, independent of the radial coordinate for large r, and -A^2 is positive at infinity. Then D + A is Fredholm and

index(D + A) = integral over N of A-hat(N) wedged with the Chern character of the positive eigenbundle of A.

The sphere at infinity is replaced by the cross-section N, but the end is still infinite, and the mass is still invertible and radially frozen out there. A finite cube is not a warped end. The extension does not license the closed hedgehog branch.

## Atiyah-Singer

Atiyah-Singer is the closed-manifold theorem. For a Dirac operator on a compact even-dimensional spin manifold, twisted by a bundle E,

index(D_E) = integral of A-hat(M) ch(E).

The index is dim ker D_E minus dim ker D_E adjoint. It needs a compact manifold without boundary, or a boundary version (Atiyah-Patodi-Singer) with spectral boundary conditions. Callias is the open-space cousin: the topological input moves from the bulk characteristic class to the degree of the mass on the sphere at infinity. Spectral flow of a path equals the index of partial_s + H(s) on the cylinder, which is the APS form used in note 15. That cylinder index was not computed.

## Placement

Wilson-Dirac index: torus, gauge topology, not computed here. Anghel: infinite warped end, not a cube. Atiyah-Singer: closed manifold, not an open hedgehog box. Note 27's conjecture stays about the tested boxes only.
