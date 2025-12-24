import numpy as np
from Src.model.operators import second_derivative_operator

def anharmonic_hamiltonian(x, dx, mass=1.0, hbar=1.0, omega=1.0, Lambda=1.0):
    """
    Constructs the Hamiltonian matrix for the anharmonic oscillator:
    with V(x) = 1/2 m ω^2 x^2 + λ x^4
    """
    N = len(x)

    T = -(hbar**2 / (2*mass)) * second_derivative_operator(N, dx)
    V = np.diag(0.5 * mass * omega**2 * x**2 + Lambda * x**4)

    return T + V