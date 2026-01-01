import numpy as np
from scipy.sparse import diags

def second_derivative_operator(N, dx):
    """
    Construct finite-difference second derivative operator.
    """
    main = -2.0 * np.ones(N)
    off = 1.0 * np.ones(N - 1)
    return diags([off, main, off], [-1, 0, 1], format="csr") / (dx**2)