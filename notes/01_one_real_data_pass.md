# One real data pass

**Date:** 2026-10-02
**Status:** Merge of v2 operator graphs with the archetype battery, under the refined reading that the three bridges are one active phase and two pause phases.

The two drawings supplied with this pass are v2 representations. Garbled tags on those sheets (Dδ, Ihb, Sb, Buo, RLlo, and the broken captions on the depth sheet) are generator failures. The geometry is kept. The letters are not.

## The three bridges

From v3 `notes/01_three_bridge_minimal_model.md`: one active, two pause. Same flow. Different relative-depth band.

| Bridge | Phase | v2 operator point | F^rel_mid | early ΔW8 | Drawing |
|--------|-------|-------------------|-----------|-------------|---------|
| A | Active. Membership locked. | Baseline (2, 2), class B | −0.84 | +0.088 | Standing cable-stayed span. Deep funnel. |
| P1 | Transitional pause. Membership soft. | Boost-like T | ~ −0.55 | +0.03 to +0.05 | Broken deck over the gap. Mid bowl. |
| P2 | Stalled pause. Exit needs high α. | Polarized (1.7, 2), class P | −0.33 | ~ 0 | Open lattice. Shallow rings. |

First drawing: path. Standing span, rupture, lattice left for reattachment. That is v3 note 05: active path, boundary, deeper structure for the next lock.

Second drawing: depth ruler for the same three bridges. Deep well, mid span, shallow rings. Active sits in the well. The two pauses are the mid and shallow bands, not two extra active identities.

## Two calibrations, one ordering

Colab replicas scored in v3 (`stream1_real`) gave R0 = 1.11 / 3.31 / 4.79 and baseline dW8 = 1.96. Those files are the same three bridges at archetype scale. They are not a second physics result.

Operator scale is the one that carries the residual gate: dW8 of order 0.09 on A, near zero on P2. Archetype scale is the picture of that ordering, inflated. One pass. Deep feeds, shallow stalls.

## The 3×3 under the new names

Source: v2 `Identity_propagation_3x3_results.md`. L=10, d=3, 8-component Wilson–Dirac + isospin hedgehog. Grid v1, v2 ∈ {1.7, 2.0, 2.3}. All 9 points gated at r_rel ~ 10^−14.

The old class rule (B if R_mid > 1.15 and |P| < 0.15; P if |P| > 0.20 or H_mid > 0; else T) was a first pass. Under v4 those labels are depth bands.

- P2 candidates, old polarized class: mean ΔW_mid = +0.024, mean R_mid = 0.96. Weakest feed. The (1.7, 2) point is the stall: ΔW_mid = −0.001, R_mid = 0.90, signed P = +0.29.
- A is the baseline (2, 2). It sat on the old B/T boundary (|P| = 0.18) and is the strongest feed: ΔW_mid = +0.113, F_mid = −9.28.
- The rest of the grid is P1: feed present, lock not held. Old T mean ΔW +0.058 is inflated because the baseline was filed there.

Constitutive fit on that grid: c1(R_mid) = +0.25, LOO-MAE 0.041. Direction matches the phase law. n=9 is the minimum success v2 already locked. v4 does not rerun the grid. It changes the class rule.

v3 licensed sentence, kept: on residual-gated L=10 tubes, F^rel predicts early feed better than v1 or frozen labels inside a patchy v2 window (onset 1.80–1.85, exit 2.15–2.20). Mediation n=65: R²(F^rel) = 0.439 vs v1 0.013 vs labels 0.035. That window is the active band. Outside it the bridge is already in pause.

## What does not get merged in as a contradiction

- L=12 G sign (v2 `G12_L12_residual_gated_path.md`): G(L=10) = −0.176, G(L=12) = −0.0448, four accepted modes. Sign of the propagation response survived. That is not the center-feed window.
- L=12 feed match (v3 note 50): center peak does not transfer. The active band is an L=10 fact, not yet volume-stable.
- k=8 (v3 note 55): not the v2 observable. Eight-mode G flips to +0.149. Stay at four accepted modes.
- Wilson r: frozen at r=1 after the free-spectrum check (gap 0.500000 at L=4, m=0.5). The r=1.25 knife-edge stays closed.

## Conservation across the pause

v⁺ = v⁻, I⁺ = I⁻, b⁺ ∈ B_adm(b⁻, R, α).

On A, b is fixed and the early slope is the large one (+0.088 operator, +0.113 on the 3×3 baseline). Crossing into P1 keeps v and I and loosens b. P2 is the hollow: early slope under the stall threshold, exit only if α is high enough to reattach onto the lattice. That is the right-hand panel of the path drawing and the ring panel of the depth drawing.

## Not in this pass

Pause memory. v3 note 40 ran carried-weight hysteresis on the L=10 tubes and missed. The drawings show the admissible transfer. They do not show R_return < R_leave.

The real-data claim stops at identity-to-response coherence on the residual-clean operator, with the three bridges as one active and two pauses.
