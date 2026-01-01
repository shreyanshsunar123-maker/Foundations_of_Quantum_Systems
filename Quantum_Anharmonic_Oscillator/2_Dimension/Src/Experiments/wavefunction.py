import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse.linalg import eigsh

from Src.Model.operators import second_derivative_operator
from Src.Model.hamiltonian import anharmonic_mode_hamiltonian

FIG_DIR = os.path.join("Results", "figures")
os.makedirs(FIG_DIR, exist_ok=True)

# --- Parameters (mirror exp.py defaults) ---
kx, ky, kxy = 1.0, 1.0, 0.5
m, hbar = 1.0, 1.0
A = 1.0
N_q, q_max = 1200, 6.0
num_states = 4

# Choose separable 2D state (n1, n2)
n1, n2 = 0, 1

# --- Normal modes from stiffness matrix ---
K = np.array([[kx, kxy],
              [kxy, ky]], dtype=float)
lam, R = np.linalg.eigh(K)
lambda1, lambda2 = lam

# --- Grid and operator ---
q = np.linspace(-q_max, q_max, N_q)
dq = q[1] - q[0]
diff = second_derivative_operator(N_q, dq)

def solve_mode(lam_i):
    H = anharmonic_mode_hamiltonian(diff, q, m, hbar, lam_i, A)
    E, psi = eigsh(H, k=num_states, which="SA")
    idx = np.argsort(E)
    E, psi = E[idx], psi[:, idx]
    # normalize each eigenstate
    for j in range(psi.shape[1]):
        psi[:, j] /= np.sqrt(np.sum(np.abs(psi[:, j])**2) * dq)
    return E, psi

def plot_mode_states(psi, title, filename):
    plt.figure(figsize=(6, 4), dpi=120)
    for n in range(psi.shape[1]):
        plt.plot(q, psi[:, n], label=f"n={n}")
    plt.title(title)
    plt.xlabel("q")
    plt.ylabel("psi")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_DIR, filename), dpi=300, bbox_inches="tight")
    plt.show()

if __name__ == "__main__":
    E1, psi1 = solve_mode(lambda1)
    E2, psi2 = solve_mode(lambda2)

    plot_mode_states(psi1, "1D eigenstates in normal mode Q1", "Q1_eigenstates.png")
    plot_mode_states(psi2, "1D eigenstates in normal mode Q2", "Q2_eigenstates.png")

    # 2D separable product state
    Psi2d = np.outer(psi1[:, n1], psi2[:, n2])
    Prob2d = np.abs(Psi2d)**2

    plt.figure(figsize=(6, 5), dpi=120)
    plt.imshow(Prob2d, extent=[-q_max, q_max, -q_max, q_max], origin="lower", aspect="equal")
    plt.colorbar(label=r"$|\psi(Q_1,Q_2)|^2$")
    plt.xlabel(r"$Q_1$")
    plt.ylabel(r"$Q_2$")
    plt.title(f"2D separable state: (n1,n2)=({n1},{n2})")
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_DIR, "2D_probability.png"), dpi=300, bbox_inches="tight")
    plt.show()