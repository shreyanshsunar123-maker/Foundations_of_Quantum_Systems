## Assumptions and Validity Regime

This project studies the one-dimensional anharmonic oscillator using first-order perturbation theory. The following assumptions underlie both the analytical framework and the numerical implementation.

#  Small Perturbation Assumption

 The total Hamiltonian is assumed to be decomposable into an exactly solvable part and a small correction term. The quartic contribution to the potential is treated as a perturbation whose effect is assumed to be small compared to the harmonic term in the spatial region where the wavefunction has significant support.

 This assumption is valid only when the anharmonic contribution does not dominate the total energy of the system.

⸻–––––––––––––––––––––––––––––––––

# Validity of First-Order Perturbation Theory

 Only first-order energy corrections are considered. This implicitly assumes that higher-order corrections are negligible, which is generally true for low-energy states and sufficiently small perturbation strength.

 For higher quantum numbers or stronger anharmonicity, first-order perturbation theory is expected to lose accuracy.

⸻–––––––––––––––––––––––––––––––––

# Unperturbed Eigenstates as a Basis

 The unperturbed harmonic oscillator eigenstates are assumed to form a suitable basis for computing perturbative corrections. The wavefunctions are not modified by the perturbation at first order, and only energy shifts are evaluated.

 This assumption breaks down when the perturbation significantly alters the spatial structure of the eigenstates.

⸻–––––––––––––––––––––––––––––––––

# Finite-Difference Approximation

 The kinetic energy operator is discretized using a second-order finite-difference scheme. This approximation assumes that the spatial grid is sufficiently fine and that boundary effects are negligible within the chosen domain.

 Numerical accuracy depends on grid resolution and domain size.

⸻–––––––––––––––––––––––––––––––––

# Boundary Truncation

 The spatial domain is truncated to a finite interval. It is assumed that the wavefunctions decay sufficiently fast near the boundaries so that truncation effects do not significantly influence the computed eigenstates and expectation values.

⸻–––––––––––––––––––––––––––––––––

# One-Dimensional Model

 The system is modeled in one spatial dimension. While this captures essential features of anharmonic behavior, real physical systems may involve higher-dimensional effects not included here.
