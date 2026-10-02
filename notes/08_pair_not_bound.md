# The open pair is not a bound defect mode

**Date:** 2026-10-02
**Status:** Diagnostic continuation of note 07. Same operator. r=1. No proxy.

## What was tested

Open box, v=2, r=1, f=tanh(rad/1.5), shift-invert around 0. Localization of the lightest mode: weight inside rad<=1.5, and rms radius.

## Result

| L | Lightest pair | Weight in core | rms radius | Below 1e-6 |
|---|---------------|----------------|------------|------------|
| 10 | 0.001172 | 0.064 | 4.87 | 0 |
| 12 | 0.001098 | 0.050 | 5.86 | 0 |

The pair does not keep falling. L=10 to L=12 moves it by 0.00007. The core holds about 5 to 6 percent of the mode. The rms radius grows with the box, about half the linear size.

## Reading

The spectral effect is real and symmetric. It is not a Callias zero mode bound to the hedgehog. A bound mode would concentrate on the core and lighten toward the gate as L grows. This one spreads with the volume and stalls above 1e-3.

Periodic boxes remain the wrong topology for a single-defect index. Open boxes produce a delocalized pair, lifted by the Wilson term and by the boundary. Neither is N_def=1 under the gate.

## What this does not reopen

r stays 1. No gamma_5 proxy. No archetype tube. No SPARC residual pass. No claim that the macro pause is this pair. Fork A remains the fork, and this particular finite-volume bridge stays unconfirmed.

Percentages in the prompting note are an assessment, not a row in the ledger.
