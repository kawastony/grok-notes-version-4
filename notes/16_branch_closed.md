# Closure: r=1 finite-volume defect index

**Date:** 2026-10-02
**Status:** Closed. Do not add another boundary variant of this operator.

For the frozen r=1 finite lattice operator, hedgehog degree is visible geometrically but not counted spectrally. Observed low modes are delocalized near-zero pairs with zero net flow. No finite-volume defect-index bridge has been established.

## Tested

- Free control, L=4, r=1, m=0.5: gap 0.500000, doubler corner 6.50, no kernel.
- Open cube, L=6 to L=12: light pair, not bound to the core. L=10 to L=12 stalled at about 0.0011. Core weight about 0.05.
- Spectral flow, cube: nearest pair 0.150, 0.00227, 0.00621. Flips 0.
- Boundary-mass pin: inert. Outer amplitude was already O(1).
- Spherical shell, invertible mass: closest pair 0.00034, then 0.00248. Flips 0.
- r=0 beside the frozen point: gap stays 0.539. No hidden mode released.
- Two flow methods: overlap tracking failed, minimum overlap 0. Window count in (0, 0.2) starts at 2 and ends at 2.

## Ruled out as the cause

- Operator drift. The free control matches v2.
- Vanishing boundary amplitude.
- Cube faces alone.
- A spherical outer shell with invertible mass.
- Wilson lifting as the thing hiding a crossing. Turning it off removes the approach.
- Sorted sign flips as a count. Those flips were matching artifacts.

## Remains open, elsewhere

- A counted mode on a different operator with a credible index mechanism.
- Larger-L F^rel ordering on the real tube.
- Joint DESI plus Pantheon+ chi-squared. Note 04 stays the reduced score.
- Quantum gravity. Stays the lowest assessment until a counted mode exists.

## What would count as new evidence

A different operator class, not another boundary of this one. An overlap or domain-wall operator, or a continuum Fredholm construction before any lattice. On that operator, a windowed or APS count whose net flow equals N_def, and a light mode bound to the core.

Not new evidence: more cube tweaks, more shell pinning, more r scans, more branch tracking on this path.
