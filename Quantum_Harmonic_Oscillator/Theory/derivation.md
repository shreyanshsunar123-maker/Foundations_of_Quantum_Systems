## Quantum Harmonic Oscillator

The time-independent Schrödinger equation is

Hψ(x) = Eψ(x)

with Hamiltonian

H = - (ħ² / 2m) d²/dx² + ½ mΩ² x²

---

## Discretization

The spatial coordinate x is discretized on a uniform grid

xᵢ = x_min + iΔx ,  i = 1, … , N

The second derivative is approximated using a central finite difference:

d²ψ/dx² ≈ (ψᵢ₊₁ - 2ψᵢ + ψᵢ₋₁) / Δx²

This converts the kinetic energy operator into a tridiagonal matrix.

---

## Matrix Hamiltonian

The Hamiltonian becomes

H = T + V

where
- T is the discrete Laplacian multiplied by -(ħ² / 2m)
- V is a diagonal matrix with elements ½ mΩ² xᵢ²

Diagonalizing H yields approximate energy eigenvalues and eigenstates.

This numerical approach reproduces the analytic spectrum in the continuum limit.xxsx