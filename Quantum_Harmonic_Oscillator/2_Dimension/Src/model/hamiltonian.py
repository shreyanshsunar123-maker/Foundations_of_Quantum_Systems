from scipy.sparse import diags

def harmonic_hamiltonian(D2, x, m, omega, hbar):
    """
    Construct the Hamiltonian matrix for the 1D harmonic oscillator.
    """
    T = -(hbar**2) / (2*m) * D2
    V = 0.5 * m * omega**2 * x**2
    Vop = diags(V, 0, format="csr")
    return T + Vop