import numpy as np
from scipy.sparse.linalg import eigsh

from Src.Model.operators import second_derivative_operator
from Src.Model.hamiltonian import anharmonic_mode_hamiltonian

# --- Parameters (mirror exp.py defaults) ---
kx, ky, kxy = 1.0, 1.0, 0.5
m, hbar = 1.0, 1.0
A = 1.0
N_q, q_max = 1200, 6.0
num_states = 6

# --- Normal modes from stiffness matrix ---
K = np.array([[kx, kxy],
              [kxy, ky]], dtype=float)
lam, R = np.linalg.eigh(K)          # lam = [lambda1, lambda2]
lambda1, lambda2 = lam

# --- Grid and operator ---
q = np.linspace(-q_max, q_max, N_q)
dq = q[1] - q[0]
diff = second_derivative_operator(N_q, dq)

def mode_energies(lam_i):
    H = anharmonic_mode_hamiltonian(diff, q, m, hbar, lam_i, A)
    E, _ = eigsh(H, k=num_states, which="SA")
    return np.sort(E)

if __name__ == "__main__":
    print("Normal-mode lambdas:", lam)
    print("Normal-mode omegas:", np.sqrt(lam / m))
    print(f"Anharmonic strength A = {A}")

    E1 = mode_energies(lambda1)
    E2 = mode_energies(lambda2)

    print("\nMode1 energies:", np.array2string(E1, precision=6))
    print("Mode2 energies:", np.array2string(E2, precision=6))