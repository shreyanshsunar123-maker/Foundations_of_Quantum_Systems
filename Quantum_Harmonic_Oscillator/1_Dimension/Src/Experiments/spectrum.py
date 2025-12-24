import numpy as np
from scipy.linalg import eigh
from Src.Model.Hamiltonian import hamiltonian

N = 1000
L = 5
x = np.linspace(-L, L, N)
dx = x[1] - x[0]

H = hamiltonian(x, dx)
energies, _ = eigh(H)

for n in range(6):
    print(f"n={n}, E_n ≈ {energies[n]:.4f}")
