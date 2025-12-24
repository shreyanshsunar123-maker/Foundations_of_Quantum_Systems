import numpy as np
from .Operators import second_derivative_operator, potential_operator

def hamiltonian(x, dx, hbar=1.0, mass=1.0, omega=1.0):
    N = len(x)
    T = -(hbar**2 / (2*mass)) * second_derivative_operator(N, dx)
    V = potential_operator(x, mass, omega)
    return T + V
