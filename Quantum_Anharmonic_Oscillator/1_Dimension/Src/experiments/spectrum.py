import numpy as np
from scipy.linalg import eigh
from Src.model.hamiltonian import anharmonic_hamiltonian

N = 1000
x_range = 5
x = np.linspace(-x_range, x_range, N)
dx = x[1] - x[0]

H = anharmonic_hamiltonian(x, dx)
energy, _ = eigh(H)

for i in range(4):
    print(f"Energy level {i}: {energy[i]:.4f}")