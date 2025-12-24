import numpy as np

def second_derivative_operator(N, dx):
    """
    central finite-difference second derivative operator.
    """
    return (np.eye(N, k=1) + np.eye(N, k=-1) - 2 * np.eye(N)) / (dx ** 2)