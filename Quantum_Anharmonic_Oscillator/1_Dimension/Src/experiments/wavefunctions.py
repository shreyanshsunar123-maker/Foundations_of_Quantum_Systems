import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh
from Src.model.hamiltonian import anharmonic_hamiltonian

def normalize(psi, dx):
    return psi / np.sqrt(np.sum(np.abs(psi)**2) * dx)

N = 1000
L = 5
x = np.linspace(-L, L, N)
dx = x[1] - x[0]

H = anharmonic_hamiltonian(x, dx, Lambda=1.0)
energies, states = eigh(H)

Psis = [normalize(states[:, n], dx) for n in range(4)]

for n, Psi in enumerate(Psis):
    plt.plot(x, Psi + 0.6*n, label=f"n={n}")

plt.xlabel("Position")
plt.ylabel("Wavefunction")
plt.legend()
plt.grid()
plt.show()