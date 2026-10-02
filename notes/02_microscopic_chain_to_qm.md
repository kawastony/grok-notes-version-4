# Microscopic chain, up to the v2 QM link

**Date:** 2026-10-02
**Status:** v4 brought to the same connection point v2 earned. Not past it.

The diagrams in `media/` are the corrected v2 drawings. This note is the operator underneath them. Each step is the smallest object that still forces the next one.

## 0. What is not the QM object

Archetype tubes, the r=1.25 knife-edge, raw ⟨γ₅⟩, and the Forman feed window are not the QM connection. v2 `Eight_component_algebra_and_free_spectrum.md` and v3 note 48 already closed those doors. v4 does not reopen them.

## 1. Algebra, before any lattice

Continuum target, locked in v2:

H = α·p ⊗ 1_τ + β ⊗ (v f(r) τ·x̂)

Eight components: Dirac 4 ⊗ isospin 2. A 4-component embedding was ruled out algebraically. The 8-component checks passed exactly: anticommutators of α and β, (β ⊗ τ_a)² = I, and M(n)² = ‖n‖² I. The three mass matrices β ⊗ τ_a supply the nontrivial π₂ for a Callias hedgehog of degree N_def.

Grading caveat, kept: in the representation used, γ⁵ ⊗ 1 and β ⊗ 1 commute, so {γ⁵ ⊗ 1, M} ≠ 0. Local chirality is spectral asymmetry or an involution that anticommutes with the full H. Raw ⟨γ₅⟩ is not the index proxy. This does not touch the existence of the Callias index.

## 2. Healthy UV point

Free 8-component Wilson spectrum, periodic, no hedgehog: L=4, m=0.5, r=1.

Lowest |λ| = 0.500000, matching the analytic gap. No mode below 10⁻⁶. Doubler corner at 6.50. Isospin doubles the degeneracy, 8 = 4 × 2. Then r is frozen. It is a regulator, not a phase coordinate.

That point is the QM object: a lattice Dirac operator in the Callias / Jackiw–Rossi class.

## 3. Defect, index, and what the phases are microscopically

Hedgehog mass, n=3:

Φ(r) = v f(r) n̂(θ,φ)·τ, f(r) → 1 at infinity.

Callias: Index(L) equals the degree of the map S² → S² given by n̂, up to sign. Unit hedgehog → one protected zero mode. Hedgehog plus antihedgehog → total index 0, with a soft hybridized pair when the separation is not much larger than the correlation length. Only the asymptotic class of Φ enters. Core deformations that keep invertibility at infinity do not change the index.

Along any path that preserves that winding,

d/ds Index(L(s)) = 0,

while individual eigenvalues may move. That is the continuum backbone of activity without an identity change.

v4 reading of the same fact:

| Microscopic object | Phase |
|--------------------|-------|
| Asymptotic winding held, soft multiplet bound to the defect, membership b fixed | A, active |
| Winding still held, eigenvalues moving, feed present, lock not held | P1, transitional pause |
| Hybridized pair, early slope under the stall threshold, exit only by a deformation that is still admissible | P2, stalled pause |

P2 is not a change of index. Leaving P2 without preserving invertibility at infinity would be a different operator, and is not an allowed transfer. The conservation law v⁺ = v⁻, I⁺ = I⁻ is the lattice shadow of spectral motion at fixed index. b⁺ ∈ B_adm is the residual gate plus the winding constraint.

Lattice status carried from v2 `Chiral_density_and_Callias_index.md`: residual-gated soft modes on Wilson–Dirac plus hedgehog at L=8–12 are consistent with Index ≈ N_def for single defects. The continuum proof for the cone mass is still open. Chirality diagnostics probe orientation, not a measured index theorem.

## 4. Where the diagrams sit on this chain

`media/01_path_active_two_pauses.svg` is the path at fixed index. Standing span = active evolution on the locked defect. Broken deck = P1, intensity still there, membership soft. Open lattice = P2, the structure you reattach to, not a new destination with a new winding.

`media/02_relative_depth.svg` is the depth ruler on the same operator. Relative depth F_mid − F̄ sets which band the bridge is in. It does not set the index. Numbers on the path diagram are the operator-scale feeds already loaded in `notes/01_one_real_data_pass.md`.

## 5. The connection point, same as v2

Earned, and the place v4 now stops:

1. r=1, residual gate, 8-component Wilson–Dirac. This is the QM object.
2. The QM link is the index: soft-mode count versus N_def on single defects, after the gate. Not tilt. Not Forman feed. Not an r scan.
3. The F^rel mediation (patchy v2 window, R² = 0.439 on the L=10 tubes) is a lattice geometry fact. It becomes a QM statement only if the same ordering survives at r=1, larger L, gate held. v2’s G sign survived to L=12 (G = −0.176 at L=10, G = −0.045 at L=12, four modes). The center-feed window did not. So the index link is earned. The phase-band link is not yet a continuum statement.
4. Pause memory, Wilson-regime language, and ⟨γ₅⟩ as the phase variable stay off the QM side.

Helical density and Callan–Harvey inflow sit beside this, not under it. The minimal parity-odd density H = χ ĉ·(ε × ∂_t ε) is a symmetry construction. κ is not fixed. It is not used as the QM connection.

## 6. What the next microscopic test is, if one is run

Not another archetype battery. Not an r sweep.

Spectral-flow index on the lattice hedgehog: vary a continuous mass deformation, count crossings through zero, compare with N_def, gate held, r=1. That is the same next calculation v2 already named. A pass there is what lets the active/pause reading sit on the QM object instead of beside it.
