import numpy as np
from scipy.sparse import diags

def second_derivative_operator(N: int, dq: float):
    """
    Finite-difference second derivative operator d^2/dq^2 on a uniform grid.
    """
    main = -2.0 * np.ones(N)
    off = 1.0 * np.ones(N - 1)
    return diags([off, main, off], offsets=[-1, 0, 1], format="csr") / (dq**2)