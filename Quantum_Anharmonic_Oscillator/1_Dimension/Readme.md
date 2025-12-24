## Quantum Anharmonic Oscillator

# Scope

 This repository studies the low-lying bound states of the one-dimensional quantum anharmonic oscillator defined by the Hamiltonian

 H = -\frac{1}{2}\frac{d^2}{dx^2} + \frac{1}{2}x^2 + \lambda x^4,

 using finite-difference discretization and matrix diagonalization.
 Natural units are used throughout (\hbar = m = \omega = 1).

 The goal is not numerical novelty, but controlled investigation of how a quartic perturbation modifies spectral structure and eigenstate localization relative to the harmonic case.



# Method

 The Schrödinger operator is represented on a uniform spatial grid over a finite interval. The kinetic term is approximated by a second-order central difference operator, and the potential is treated exactly in position space. The resulting Hamiltonian matrix is real and symmetric.

 Eigenvalues and eigenfunctions are obtained by direct diagonalization.  Resolution is assessed by verifying stability of low-lying states under refinement of the grid spacing and domain size.



Structure
Quantum_Anharmonic_Oscillation/
├── Src/
│   ├── Model/
│   │   ├── operators.py
│   │   └── hamiltonian.py
│   └── Experiments/
│       ├── spectrum.py
│       ├── wavefunctions.py
│       └── convergence.py
│
├── Theory/
│   ├── assumptions.md
│   └── derivation.md
│
├── Results/
│   ├── figures/
│   └── Notes.md
│
├── explorations.ipynb
├── requirements.txt
└── README.md


# Observations
	•	Energy level spacing increases with quantum number, in contrast to the harmonic oscillator.
	•	Eigenfunctions retain definite parity but exhibit increased localization.
	•	Probability densities reflect stronger confinement due to the quartic term.
	•	Low-lying states converge reliably for sufficiently large domain and grid resolution.

These behaviors follow directly from the altered asymptotic structure of the potential.



# Context

 This project is part of a broader effort to construct a coherent computational framework for quantum systems in which analytical solvability is absent or incomplete. Emphasis is placed on transparency of assumptions and separation of model definition from numerical experimentation.


# Status

Complete.
Stable under refinement.
Structured for extension.