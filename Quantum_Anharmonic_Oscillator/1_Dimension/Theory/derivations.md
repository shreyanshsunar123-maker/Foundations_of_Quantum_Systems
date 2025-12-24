# Derivation of the Discrete Hamiltonian


## 1. Continuous Problem

The one-dimensional time-independent Schrödinger equation is
\[
H\psi(x) = E\psi(x),
\]
with Hamiltonian
\[
H = -\frac{\hbar^2}{2m}\frac{d^2}{dx^2} + V(x).
\]

For the anharmonic oscillator used here,
\[
V(x) = \frac{1}{2}m\omega^2 x^2 + \lambda x^4.
\]

In the implementation we use natural units ℏ = m = ω = 1, giving
\[
H = -\frac{1}{2}\frac{d^2}{dx^2} + \frac{1}{2}x^2 + \lambda x^4.
\]



## 2. Discretization of Space

We truncate the domain to x ∈ [-L, L] and sample it on a uniform grid:
\[
x_i = -L + i\Delta x,\quad i=0,1,\dots,N-1,
\]
where
\[
\Delta x = \frac{2L}{N-1}.
\]

The wavefunction is represented by its values on the grid:
\[
\psi \;\to\; (\psi_0,\psi_1,\dots,\psi_{N-1})^T,
\quad \psi_i = \psi(x_i).
\]



## 3. Finite-Difference Second Derivative

Using a central finite difference approximation,
\[
\frac{d^2\psi}{dx^2}\Big|_{x_i}
\approx
\frac{\psi_{i+1} - 2\psi_i + \psi_{i-1}}{\Delta x^2}.
\]

This corresponds to a discrete second-derivative operator (a tridiagonal matrix) acting on the vector ψ:
\[
D_2 = \frac{1}{\Delta x^2}
\begin{pmatrix}
-2 & 1  & 0  & \cdots & 0 \\
 1 &-2  & 1  & \cdots & 0 \\
 0 & 1  &-2  & \ddots & 0 \\
\vdots & \vdots & \ddots & \ddots & 1 \\
 0 & 0 & 0 & 1 & -2
\end{pmatrix}.
\]



## 4. Discrete Kinetic and Potential Operators

The kinetic operator becomes
\[
T = -\frac{\hbar^2}{2m} D_2.
\]

The potential operator is diagonal in position space:
\[
V_{ij} = V(x_i)\delta_{ij},
\]
so
\[
V =
\mathrm{diag}\big(V(x_0),V(x_1),\dots,V(x_{N-1})\big).
\]

In natural units:
\[
V(x_i) = \frac{1}{2}x_i^2 + \lambda x_i^4.
\]



## 5. Matrix Hamiltonian and Eigenvalue Problem

The discrete Hamiltonian is
\[
H = T + V.
\]

We then solve the symmetric matrix eigenvalue problem
\[
H\psi_n = E_n\psi_n,
\]
where:
- \(E_n\) are approximate energy eigenvalues,
- \(\psi_n\) are approximate eigenfunctions sampled on the grid.



## 6. Normalization in the Discrete Setting

Continuum normalization is
\[
\int_{-\infty}^{\infty} |\psi(x)|^2\,dx = 1.
\]

On the grid this is approximated by
\[
\sum_{i=0}^{N-1} |\psi_i|^2\,\Delta x = 1,
\]
and we normalize each eigenvector accordingly.



## 7. Continuum Limit and Convergence

In the limits:
\[
\Delta x \to 0,\qquad L \to \infty,
\]
the discrete formulation approaches the continuum Schrödinger problem.

Practically, we verify convergence by checking that low-lying eigenvalues and eigenfunctions are stable under increasing N and/or L.