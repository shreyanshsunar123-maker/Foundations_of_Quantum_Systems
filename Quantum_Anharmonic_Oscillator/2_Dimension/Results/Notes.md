# Results & Observations

## Classical
- Linear coupling in (x, y) is removed by diagonalization into normal modes
- Motion in Q₁ and Q₂ evolves independently after rotation
- Total energy in each normal mode remains conserved, validating the numerical integration
- x–y trajectories depend sensitively on initial conditions but are fully explained by normal-mode dynamics

## Quantum
- Each normal mode is treated as an independent one-dimensional anharmonic oscillator
- Quartic anharmonicity breaks the equal energy spacing of the harmonic spectrum
- Eigenstates exhibit increasing node count with excitation number
- The full two-dimensional quantum state is constructed as a separable product of normal-mode eigenfunctions
- the resulting probability density ρ(Q₁, Q₂) reflects this separability rather than a fully coupled 2D quantum Hamiltonian

## Numerical
- Accurate representation of excited states requires increasing the domain size qₘₐₓ
- Finite-difference discretization converges systematically with increasing grid resolution
- Sparse eigensolvers efficiently compute the lowest-energy states of each normal-mode Hamiltonian
- Convergence tests confirm numerical stability of the reported spectra and wavefunctions