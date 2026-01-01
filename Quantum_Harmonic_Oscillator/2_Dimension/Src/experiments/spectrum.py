import numpy as np
from scipy.sparse.linalg import eigsh
from Src.model.operators import second_derivative_operator
from Src.model.hamiltonian import harmonic_hamiltonian

# Parameters
m = 1.0
omega = 1.0
hbar = 1.0
N = 1200
x_max = 6.0

x = np.linspace(-x_max, x_max, N)
dx = x[1] - x[0]

D2 = second_derivative_operator(N, dx)
H = harmonic_hamiltonian(D2, x, m, omega, hbar)

E, _ = eigsh(H, k=6, which="SA")
E = np.sort(E)

print("Lowest energy levels:")
for n, e in enumerate(E):
    print(f"n={n}, E={e:.6f}")