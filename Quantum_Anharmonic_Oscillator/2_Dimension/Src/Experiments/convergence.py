import numpy as np
from scipy.sparse.linalg import eigsh

from Src.Model.operators import second_derivative_operator
from Src.Model.hamiltonian import anharmonic_mode_hamiltonian

# --- Parameters (mirror exp.py defaults) ---
kx, ky, kxy = 1.0, 1.0, 0.5
m, hbar = 1.0, 1.0
A = 1.0
num_states = 2  # only need lowest couple for convergence

# Convergence sweeps
N_list = [600, 900, 1200, 1500]
qmax_list = [4.5, 5.5, 6.0, 7.0]

# --- Normal modes from stiffness matrix ---
K = np.array([[kx, kxy],
              [kxy, ky]], dtype=float)
lam, R = np.linalg.eigh(K)
lambda1, lambda2 = lam

def lowest_E(lam_i, N_q, q_max):
    q = np.linspace(-q_max, q_max, N_q)
    dq = q[1] - q[0]
    diff = second_derivative_operator(N_q, dq)
    H = anharmonic_mode_hamiltonian(diff, q, m, hbar, lam_i, A)
    E, _ = eigsh(H, k=num_states, which="SA")
    return np.sort(E)

if __name__ == "__main__":
    print("Normal-mode lambdas:", lam)
    print("A =", A)

    print("\n--- Sweep N_q (fixed q_max = 6.0) ---")
    for N_q in N_list:
        E1 = lowest_E(lambda1, N_q, 6.0)
        E2 = lowest_E(lambda2, N_q, 6.0)
        print(f"N_q={N_q:4d} | Mode1: {E1} | Mode2: {E2}")

    print("\n--- Sweep q_max (fixed N_q = 1200) ---")
    for q_max in qmax_list:
        E1 = lowest_E(lambda1, 1200, q_max)
        E2 = lowest_E(lambda2, 1200, q_max)
        print(f"q_max={q_max:3.1f} | Mode1: {E1} | Mode2: {E2}")