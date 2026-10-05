# Continuum Callias operator

**Date:** 2026-10-05
**Status:** Theorem recorded. Lattice discretization of it is not the index. Closed branches stay closed.

## Statement

On odd-dimensional Euclidean space, L = Q + Phi, with Q the Dirac operator and Phi Hermitian. If |Phi| is bounded below by a positive constant outside a ball, and the first derivatives of Phi decay as 1/|x| and the second as 1/|x|^{1+eps}, then L is Fredholm. Its index equals the degree of U = Phi/|Phi| on the sphere at infinity. In three dimensions a unit hedgehog has degree 1, so the index is 1 up to sign. In even dimensions the index vanishes for algebraic reasons. A change of the core that keeps the winding and the invertibility does not change the index. Gesztesy and Waurick, arXiv:1506.05144.

The continuum operator this fork has not built is that L on R^3, with Phi = v f(r) n-hat . tau, f -> 1, |Phi| >= c outside a compact set.

## What was computed

A ball of radius 4, 257 sites, no Wilson term, shell pinned to f=1, eight-component Dirac-isospin. Lowest abs 0. Eight modes below 0.05. Core weight of the lightest 0.587.

An eight-fold kernel on a naive lattice Dirac operator is the doubler sickness already rejected in note 17. It is not Index = 1. The sphere at infinity is still a lattice shell. The Fredholm hypothesis is not met.

## Not claimed

This does not say the continuum theorem is false. It says this discretization does not compute it. The conjecture in note 27 stands for the tested finite lattices only.
