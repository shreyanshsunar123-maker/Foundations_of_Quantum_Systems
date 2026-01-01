# Numerical Notes – Two-Dimensional Quantum Harmonic Oscillator

This file records observations and checks made during numerical experiments.



## Energy spectrum

- The lowest eigenvalues follow the expected linear spacing.
- Increasing grid size improves convergence of higher excited states.
- Ground-state energy stabilizes rapidly with increasing domain size xₘₐₓ.



## Wavefunctions

- Eigenfunctions show increasing number of nodes with quantum number.
- Ground state is node-free and localized near xₘₐₓ = 0.
- Boundary effects become visible if xₘₐₓ is too small.



## Convergence behavior

- Increasing grid resolution N improves smoothness of wavefunctions.
- Domain truncation error dominates before discretization error.
- eigsh converges reliably for lowest ~10 states.



## Numerical stability

- Sparse representation significantly reduces memory usage.
- Normalization via discrete sum is stable.
- The sparse eigensolver converges reliably for the lowest ~10 states.



## Notes for future work

- Extend to anharmonic potentials using same operator framework.
- Compare numerical spectrum with perturbation theory.
- Investigate basis-expansion methods for efficiency.