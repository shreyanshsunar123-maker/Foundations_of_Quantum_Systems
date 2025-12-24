# Physical and Numerical Assumptions

This project computes low lying bound state eigenvalues and eigenfunctions of a one-dimensional anharmonic oscillator by discretizing the time-independent Schrödinger equation on a finite spatial grid and diagonalizing the resulting Hamiltonian matrix.



## Physical Assumptions

1. **Non-relativistic quantum mechanics**
   The system is governed by the time-independent Schrödinger equation.

2. **One-dimensional motion**
   The particle is restricted to a single spatial coordinate x.

3. **Anharmonic confining potential**
   The potential is taken to be
   \[
   V(x) = \frac{1}{2}m\omega^2 x^2 + \lambda x^4,
   \]
   which is even in x and therefore implies eigenstates of definite parity (even/odd).

4. **Natural (dimensionless) units**
   In the numerical implementation we choose
   \[
   \hbar = m = \omega = 1,
   \]
   so the Hamiltonian is dimensionless and λ controls the strength of the anharmonicity.

5. **Bound states**
   The potential grows rapidly for large |x| (∝ x^4), so the low-lying states are localized near x = 0.



## Numerical Assumptions

1. **Finite domain truncation**
   The infinite domain is approximated by a finite interval:
   \[
   x \in [-L, L].
   \]
   We assume the low-lying wavefunctions satisfy
   \[
   \psi(\pm L) \approx 0,
   \]
   so boundary effects are negligible.

2. **Uniform grid**
   The interval [-L, L] is discretized using N equally spaced points with spacing
   \[
   \Delta x = \frac{2L}{N-1}.
   \]

3. **Finite-difference approximation**
   The second derivative is approximated by a central finite difference stencil, introducing discretization error that decreases as Δx → 0.

4. **Matrix eigenvalue formulation**
   The discretized Hamiltonian is real and symmetric, so its eigenvalues are real and eigenvectors can be chosen real.

5. **Normalization**
   The wavefunction is normalized using the discrete approximation to the continuum norm:
   \[
   \sum_{i=0}^{N-1} |\psi(x_i)|^2 \,\Delta x = 1.
   \]

6. **Convergence criterion (resolution sufficiency)**
   We consider the computation sufficiently resolved when increasing N (refining Δx) and/or increasing L does not materially change the low-lying eigenvalues and eigenfunctions. In other words, the results are stable under further refinement of the grid and domain.