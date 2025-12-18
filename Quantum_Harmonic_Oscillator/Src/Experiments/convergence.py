from scipy.linalg import eigh
import numpy as np
from Src.Model.Hamiltonian import hamiltonian

for N in [200, 400, 800, 1600]:
    x = np.linspace(-5, 5, N)
    dx = x[1] - x[0]
    E0 = eigh(hamiltonian(x, dx), eigvals_only=True)[0]
    print(f"N={N}, E0={E0:.6f}")
