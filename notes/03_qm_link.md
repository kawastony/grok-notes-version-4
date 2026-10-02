# QM link — connected

**Date:** 2026-10-02
**Status:** Connected. The v4 phases sit on the Callias operator. They are not a second layer beside it.

Parent chain: `notes/02_microscopic_chain_to_qm.md`. This note is the identification that note left as a stop line.

## The object

The QM object is the residual-gated 8-component Wilson–Dirac operator at r=1, with hedgehog mass

Φ(r) = v f(r) n̂·τ, f → 1 at infinity.

Callias, on odd-dimensional open space, says the Fredholm index is fixed by the asymptotic map only:

Index(L) = degree of U on S²_∞ = N_def

(up to sign). Core shape does not enter. A unit hedgehog carries one protected zero mode. A hedgehog–antihedgehog pair has total index 0 and a soft hybridized pair while sep is not much larger than the correlation length.

v2 already checked the pieces this identification needs:

- 8-component algebra passed. 4-component embedding ruled out.
- Free Wilson spectrum healthy at r=1, m=0.5, L=4: gap 0.500000, no kernel, doublers lifted. r then frozen.
- Soft near-zero sector appears for single defects and, more strongly, for opposite-charge pairs.
- Softness survives changes of profile shape, width, and amplitude. That is the lattice face of “index depends only on asymptotics.”
- At L ≤ 10 and sep/ξ ∼ 1.5–2 the pair stays hybridized. Independent core localization needs sep ≫ ξ.

Continuum extrapolation of Index(D) → N_def for several charges, and a spectral-flow count on a large lattice, remain open. The connection does not wait on them. It uses the structural fact v2 already locked: deformations that keep invertibility at infinity and the asymptotic class do not change the index, while eigenvalues may move.

## Identification

| v4 | QM object | What is conserved | What is free |
|----|-----------|-------------------|--------------|
| A, active | Single defect, winding held, soft multiplet bound, b locked | Index = N_def | Eigenvalues inside the multiplet; early feed |
| P1, transitional pause | Same asymptotic class, eigenvalues moving, lock soft | Index = N_def, and v, I | Membership b |
| P2, stalled pause | Compensated pair in the molecular regime, or a polarized core whose early slope has stalled | Total index (0 for a pair; N_def for a single defect that has not unwound) | Exit, and only through an admissible deformation |

Conservation across pause is spectral motion at fixed index:

d/ds Index(L(s)) = 0, v⁺ = v⁻, I⁺ = I⁻, b⁺ ∈ B_adm.

B_adm is the residual gate plus invertibility at infinity. A transfer that unwinds n̂, or that makes Φ non-invertible at infinity, is a different operator. It is not a pause. That is why P2 “exit needs high α” is a QM statement and not a drawing rule: α has to reattach membership without changing the asymptotic class.

Relative depth does not set the index. F_rel chooses the band (A, P1, P2) inside a fixed topological sector. The operator numbers already loaded stay the band labels, not new index data: A at F_rel = −0.84 with early feed +0.088, P1 near −0.55, P2 at −0.33 with feed ~ 0.

## What this connects, and what it does not

Connected:

- The three bridges are three regimes of one Callias operator, not three destinations.
- Active evolution is activity without identity change. That phrase in v2 (`CALLIAS_INDEX_DETAILS.md`, spectral motion at fixed winding) is the Law of Active Phase.
- The pair’s total index 0, with a hybridized soft sector while sep ~ ξ, is P2. The open lattice in the path diagram is that sector, waiting for a reattachment that does not unwind the map.
- Anomaly inflow is the same asymptotic data as the index. It is the continuum reason a defect can carry a directed response. It is not a second QM link, and κ is still unfixed.

Not connected, and not promoted:

- Spectral-flow index equal to N_def on a lattice large enough that Wilson and finite-volume artefacts are under control. Still open, as in v2.
- The F_rel window as a continuum law. It is a lattice geometry fact on L=10 tubes. G sign survived to L=12. The center-feed window did not.
- Pause memory. Hysteresis on those tubes missed.
- Raw ⟨γ₅⟩ as the phase variable. The grading in this representation does not anticommute with the full mass term.
- 11/72, R_cone, r_p. Untouched.

## Sentence

The QM link in v4 is the Callias index of the residual-gated 8-component operator: the active phase and both pauses are spectral motion at fixed N_def, and a pause ends only by a deformation that leaves that index alone.
