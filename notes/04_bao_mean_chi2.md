# Mean-level DESI DR2 BAO chi-squared

**Date:** 2026-10-02
**Status:** Not the joint likelihood. Pantheon+ covariance is not in the repo and is not scored.

## Pre-registered bar, this file only

Score the frozen pair against flat LCDM on the published DESI DR2 BAO means, same inputs, no retune.

Pass on this reduced test if chi2(geo_phi) <= chi2(LCDM). That is a mean-level ordering, not a DESI+SN verdict.

## Recipe

Data: DESI DR2 Table 4 cosmology rows, arXiv:2503.14738. BGS uses D_V/r_d only. LRG1, LRG2, LRG3+ELG1, ELG2, QSO, Lya use (D_M/r_d, D_H/r_d) with the published correlation r_M,H. LRG3 and ELG1 alone are excluded, as in the paper. Bin-to-bin covariance is not published in that table and is not included.

Inputs, not outputs: Omega_m = 0.31, H0 = 67.4 km s^-1 Mpc^-1, r_d = 147.09 Mpc. Flat. CPL w(z) = w0 + wa z/(1+z).

Frozen pair: w0 = -phi/2 = -0.809017, wa = -1/phi = -0.618034.

N_data = 13.

## Result

| Model | chi2 |
|-------|------|
| geo_phi, Om=0.31 | 10.55 |
| LCDM, Om=0.31 | 42.72 |
| LCDM, Om=0.334 (not the locked input) | 28.14 |

Delta chi2 (geo_phi minus LCDM, Om=0.31) = -32.17.

Per-bin geo_phi: BGS 0.12, LRG1 3.75, LRG2 3.85, LRG3+ELG1 0.58, ELG2 0.48, QSO 0.43, Lya 1.35.

## Call

Reduced test: pass on the pre-registered ordering. geo_phi fits these means better than LCDM at the same locked inputs.

Not claimed: joint DESI+Pantheon+ chi2, a theorem for (w0, wa), or a CMB likelihood. The LCDM baseline is handicapped by freezing Om and H0. Official DESI+CMB preference for evolving DE is a different analysis. This file does not replace it.
