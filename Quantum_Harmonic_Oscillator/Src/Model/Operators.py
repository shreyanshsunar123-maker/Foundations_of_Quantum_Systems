import numpy as np

def second_derivative_operator(N, dx):
    return (np.eye(N, k=1) + np.eye(N, k=-1) - 2*np.eye(N)) / dx**2

def potential_operator(x, mass=1.0, omega=1.0):
    return 0.5 * mass * omega**2 * np.diag(x**2)
