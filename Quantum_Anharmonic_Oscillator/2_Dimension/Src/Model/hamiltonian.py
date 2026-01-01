import numpy as np
from scipy.sparse import diags

def anharmonic_mode_hamiltonian(diff_op, q: np.ndarray, m: float, hbar: float, lam: float, A: float):
    """
    H = -(ħ^2/2m) d^2/dq^2 + 0.5*lam*q^2 + A*q^4
    Matches your exp.py model exactly (anharmonicity in normal-mode coordinates).
    """
    V = 0.5 * lam * q**2 + A * q**4
    V_op = diags(V, 0, format="csr")
    T_op = -(hbar**2) / (2*m) * diff_op
    return T_op + V_op