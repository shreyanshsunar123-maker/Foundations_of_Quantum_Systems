import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse.linalg import eigsh
from Src.model.operators import second_derivative_operator
from Src.model.hamiltonian import harmonic_hamiltonian

m = 1.0
omega = 1.0
hbar = 1.0
N = 1200
x_max = 6.0

x = np.linspace(-x_max, x_max, N)
dx = x[1] - x[0]

D2 = second_derivative_operator(N, dx)
H = harmonic_hamiltonian(D2, x, m, omega, hbar)

E, psi = eigsh(H, k=4, which="SA")
idx = np.argsort(E)
psi = psi[:, idx]

for n in range(4):
    norm = np.sqrt(np.sum(np.abs(psi[:, n])**2) * dx)
    psi[:, n] /= norm
    plt.plot(x, psi[:, n], label=f"n={n}")

plt.legend()
plt.grid(True)
plt.title("1D Harmonic Oscillator Eigenfunctions")
plt.show()