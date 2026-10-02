# What Callias does, and what this spectral flow said

**Date:** 2026-10-02
**Parents:** notes 08 and 09. r=1 held. No new operator.

## The theorem, stripped

Callias (1978) is an index theorem for a Dirac operator on odd-dimensional Euclidean space, perturbed by a Hermitian matrix potential Phi.

L = Q + Phi, Q = sum_j gamma_j d_j.

Two hypotheses do the work.

1. Phi is invertible at infinity: |Phi(x)| >= c > 0 for |x| large.
2. Derivatives of Phi decay fast enough that L is Fredholm on L2.

Then

Index(L) = dim ker L - dim ker L* = degree of U on the sphere at infinity,

where U = Phi/|Phi|. Only the asymptotic class enters. A smooth change of the core that keeps the winding and the invertibility does not change the index.

For the hedgehog Phi = v f(r) n-hat . tau, with f -> 1 at infinity and n-hat of degree N_def, the degree is N_def. Unit hedgehog: one protected zero mode, up to the sign convention. Hedgehog plus antihedgehog: total index 0, with a soft hybridized pair if the separation is not large compared with the correlation length.

Callias does not fix the energy of a mode that is only almost zero. Lattice spacing, finite volume, and a Wilson term are allowed to lift it. It does not produce a_eff, mu_*, or Lambda. It does not identify the sphere at infinity with a horizon.

## Spectral flow, stripped

Spectral flow of a path L(s) is the net number of eigenvalues crossing zero, counted with sign. If every L(s) stays Fredholm and the ends differ only by a class the theorem sees, the flow equals the change in index. Along a path that preserves winding and invertibility,

d/ds Index(L(s)) = 0,

while individual eigenvalues may still move. Motion without a crossing is activity at fixed index. A crossing is an index change, or a failure of the Fredholm hypothesis.

An avoided crossing is the third case. The eigenvalue approaches zero and turns back. Net flow is zero. The index, if it is defined, did not jump. The near-zero pair is not a kernel.

## What this run was

Open cube, L=8, r=1 Wilson-Dirac, eight components. s=0: constant invertible mass along z, geometric degree 0. s=1: hedgehog. Shell on the larger box covers all 8 octants, so the field carries degree 1. The operator path does not.

Nearest pair: 0.150 at s=0, 0.00227 at s=0.62, 0.00621 at s=1. Sorted-sign flips: 0. Negative count among the four tracked modes: 2 throughout.

That is an avoided crossing. Spectral flow is 0.

## Why the theorem does not force a crossing here

The degree-to-index step needs a sphere at infinity on which Phi is invertible, and a Fredholm operator. This run has a cube, a boundary, and a Wilson term. The mass profile tanh(rad/R) does not define U on a large sphere outside the box. The boundary term and r=1 can lift a would-be kernel without changing the shell winding. So the geometric degree and the operator index are different objects in this realization. Note 08 already said the light pair is delocalized: core weight about 0.05, rms growing with the box. A Callias mode would sit on the defect.

## What the flow said, in one line

The hedgehog degree is on the shell. The r=1 Wilson operator on this cube does not convert it into a zero crossing. The low pair approaches zero and turns back, so the result is an avoided crossing, not a counted mode, and not N_def=1.

## What it did not say

The geometry did not disappear. The free r=1 control is still the right operator. r does not move. A closed branch does not reopen. The finite-volume defect bridge stays unconfirmed.
