import numpy as np
from scipy.linalg import eigh
from Src.model.hamiltonian import anharmonic_hamiltonian

for N in [200, 400, 800, 1600]:
    L = 5
    x = np.linspace(-L, L, N)
    dx = x[1] - x[0]

    H = anharmonic_hamiltonian(x, dx)
    E0 = eigh(H, eigvals_only=True)[0]

    print(f"N={N:4d}, Ground energy ≈ {E0:.6f}")