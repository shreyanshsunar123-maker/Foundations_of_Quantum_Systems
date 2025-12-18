import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh
from Src.Model.Hamiltonian import hamiltonian

def normalize(psi, dx):
    return psi / np.sqrt(np.sum(np.abs(psi)**2) * dx)

# Grid
N = 1000
L = 5
x = np.linspace(-L, L, N)
dx = x[1] - x[0]

# Hamiltonian
H = hamiltonian(x, dx)
energies, states = eigh(H)


# Eigenstates

plt.figure(figsize=(7,5))
for n in range(4):
    psi = normalize(states[:, n], dx)
    plt.plot(x, psi, label=f"n={n}")

plt.xlabel("x")
plt.ylabel(r"$\psi_n(x)$")
plt.title("Quantum Harmonic Oscillator Eigenstates")
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig("Results/figures/eigenstates.png", dpi=300)
plt.show()


# Probability Densities

plt.figure(figsize=(7,5))
for n in range(4):
    psi = normalize(states[:, n], dx)
    rho = np.abs(psi)**2
    plt.plot(x, rho, label=f"n={n}")

plt.xlabel("x")
plt.ylabel(r"$|\psi_n(x)|^2$")
plt.title("Quantum Harmonic Oscillator Probability Densities")
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig("Results/figures/probability_density.png", dpi=300)
plt.show()
