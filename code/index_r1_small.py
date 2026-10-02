"""Small r=1 index check. Same 8-component Wilson-Dirac class as v2.

Free control: L=4, m=0.5, r=1, periodic, no hedgehog.
Hedgehog: beta (x) (v f tau.n), f=tanh(rad/Rcore), r=1.
Dense eigh. Not the L=10 residual-gated Colab tube.
"""
import numpy as np
from numpy.linalg import eigh

sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=complex)
Z2 = np.zeros((2, 2), dtype=complex)

def blk(a, b, c, d):
    return np.block([[a, b], [c, d]])

alpha = [blk(Z2, s, s, Z2) for s in (sx, sy, sz)]
beta = blk(I2, Z2, Z2, -I2)
mass_ops = [np.kron(beta, t) for t in (sx, sy, sz)]
alpha8 = [np.kron(a, I2) for a in alpha]
beta8 = np.kron(beta, I2)

def build(L, m, r, v=0.0, Rcore=1.0, bc="periodic"):
    N = L**3 * 8
    H = np.zeros((N, N), dtype=complex)
    c0 = (L - 1) / 2

    def idx(x, y, z):
        return ((x * L + y) * L + z) * 8

    for x in range(L):
        for y in range(L):
            for z in range(L):
                i0 = idx(x, y, z)
                rx, ry, rz = x - c0, y - c0, z - c0
                rad = np.sqrt(rx * rx + ry * ry + rz * rz)
                if v == 0 or rad < 1e-12:
                    M = m * beta8
                else:
                    f = np.tanh(rad / Rcore)
                    n = np.array([rx, ry, rz]) / rad
                    M = v * f * (n[0] * mass_ops[0] + n[1] * mass_ops[1] + n[2] * mass_ops[2])
                H[i0:i0 + 8, i0:i0 + 8] += M + 3 * r * beta8
                for d, (dx, dy, dz) in enumerate(((1, 0, 0), (0, 1, 0), (0, 0, 1))):
                    xx, yy, zz = x + dx, y + dy, z + dz
                    if bc == "periodic":
                        xx, yy, zz = xx % L, yy % L, zz % L
                    elif not (0 <= xx < L and 0 <= yy < L and 0 <= zz < L):
                        continue
                    j0 = idx(xx, yy, zz)
                    hop = -0.5j * alpha8[d] - 0.5 * r * beta8
                    H[i0:i0 + 8, j0:j0 + 8] += hop
                    H[j0:j0 + 8, i0:i0 + 8] += hop.conj().T
    return 0.5 * (H + H.conj().T)

def report(label, H, gate):
    ev = eigh(H, UPLO="U")[0]
    absort = np.sort(np.abs(ev))
    print(label, "lowest", np.round(absort[:8], 6), "n<gate", int(np.sum(absort < gate)), "max", ev.max())
    return ev

if __name__ == "__main__":
    report("free L4 r=1", build(4, 0.5, 1.0), 1e-6)
    report("open L6 v=2", build(6, 0.0, 1.0, v=2.0, Rcore=1.0, bc="open"), 1e-2)
    report("periodic L6 v=2", build(6, 0.0, 1.0, v=2.0, Rcore=1.0, bc="periodic"), 1e-2)
