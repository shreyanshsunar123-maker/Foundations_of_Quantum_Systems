# ---------------------------
# Importing Necessary Libraries
# ---------------------------
import os
import numpy as np
from scipy.linalg import eigh
import matplotlib.pyplot as plt

if not os.path.exists("Results"):
    os.makedirs("Results")


# ---------------------------
# Defining Constants
# ---------------------------
Lambda = 0.5
m = 1
h_bar = 1
w = 1
x_max = 5
n_states = 5

N = 1000
x = np.linspace(-x_max, x_max, N)
dx = x[1] - x[0]


# ----------------------------
# Kinetic, potential and Hamiltonian
# ----------------------------
D2 = (np.eye(N, k=1) - 2*np.eye(N) + np.eye(N, k=-1)) / dx**2
KE = -(h_bar**2 / (2*m)) * D2

PE = 0.5 * m * w**2 * x**2
PE_real = PE + Lambda * x**4

H = KE + np.diag(PE)

energy, wavefunction = eigh(H)


# ----------------------------
# Perturbation Theory (First Order)
# ----------------------------
E_unperturbed = energy[:n_states]
E_perturbed = []

Psis = wavefunction.copy()

for n in range(n_states):
    # Normalize
    Psis[:, n] /= np.sqrt(np.sum(Psis[:, n]**2) * dx)

    # Expectation value ⟨x⁴⟩
    pert = np.sum(Psis[:, n]**2 * x**4) * dx
    Delta_E = Lambda * pert
    total_energy = energy[n] + Delta_E

    print(f"n = {n}")
    print(f"E₀ = {energy[n]:.6f}")
    print(f"ΔE = {Delta_E:.6f}")
    print(f"E_total = {total_energy:.6f}\n")

    E_perturbed.append(total_energy)


# -----------------------------
# Plotting
# -----------------------------
plt.figure(figsize=(10, 8))

# Wavefunctions
plt.subplot(2, 2, 1)
for n in range(4):
    plt.plot(x, Psis[:, n], label=f"n={n}")
plt.title("Wavefunctions ψₙ(x)")
plt.xlabel("x")
plt.ylabel("ψ")
plt.grid()
plt.legend()

# Probability density
plt.subplot(2, 2, 2)
for n in range(4):
    plt.plot(x, Psis[:, n]**2, label=f"n={n}")
plt.title("Probability Density |ψₙ(x)|²")
plt.xlabel("x")
plt.ylabel("|ψ|²")
plt.grid()
plt.legend()

# Potentials
plt.subplot(2, 2, 3)
plt.plot(x, PE, label="Harmonic")
plt.plot(x, PE_real, label="Anharmonic")
plt.title("Potential Comparison")
plt.xlabel("x")
plt.ylabel("V(x)")
plt.grid()
plt.legend()

# Energies vs n
plt.subplot(2, 2, 4)
n_idx = np.arange(n_states)
plt.plot(n_idx, E_unperturbed, 'o-', label="Unperturbed")
plt.plot(n_idx, E_perturbed, 'o-', label="Perturbed")
plt.title("Energy Spectrum")
plt.xlabel("n")
plt.ylabel("Energy")
plt.grid()
plt.legend()

plt.tight_layout()
plt.savefig("Results/Figures.png",dpi=500)
plt.show()

