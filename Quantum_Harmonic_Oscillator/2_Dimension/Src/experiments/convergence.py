import numpy as np
from scipy.sparse.linalg import eigsh
from Src.model.operators import second_derivative_operator
from Src.model.hamiltonian import harmonic_hamiltonian

m = 1.0
omega = 1.0
hbar = 1.0
x_max = 6.0

for N in [400, 800, 1200]:
    x = np.linspace(-x_max, x_max, N)
    dx = x[1] - x[0]
    D2 = second_derivative_operator(N, dx)
    H = harmonic_hamiltonian(D2, x, m, omega, hbar)
    E, _ = eigsh(H, k=1, which="SA")
    print(f"N={N}, Ground state E={E[0]:.6f}")