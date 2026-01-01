Assumptions for the 1D Quantum Harmonic Oscillator model.

This file documents the physical, mathematical, and numerical assumptions
used throughout the simulations in this directory.


ASSUMPTIONS =

   
# Physical assumptions
    
- The particle is modeled as a point particle.
- It has one degree of freedom in the 1D model.
- The particle mass m is constant.

## Potential

The system assumes a harmonic (quadratic) potential.  
The potential energy is:

V(x) = ½·m·ω²·x²

- The potential is time-independent.
- No anharmonic or external driving terms are included.

- No dissipation or damping is included; the system is energy‑conserving.


# Quantum assumptions

- The system is treated using the time‑independent Schrödinger equation.
- Relativistic effects are neglected.
- Spin degrees of freedom are not included.
- States are stationary energy eigenstates.
- Superpositions of eigenstates are allowed, though time evolution is not studied.


# Numerical assumptions

- The spatial domain is truncated such that the wavefunction is negligible at boundaries.
- A uniform grid is used with second‑order finite‑difference derivatives.
- Operators are represented as sparse matrices derived from local finite‑difference stencils.
- Only the lowest‑energy eigenstates are needed, so sparse eigensolvers (e.g., eigsh) are used.

# Assumptions — Two-Dimensional Quantum Harmonic Oscillator

This document summarizes the physical, mathematical, and numerical assumptions
used in the simulations and analyses contained in this directory.

---

## 1. Physical Assumptions

- The system consists of a single point particle.
- The particle moves in two spatial dimensions.
- The particle mass m is constant in time.
- The potential energy is harmonic and quadratic in displacement.

The harmonic potential is given by V(x, y) = ½·m·ω²·(x² + y²)

- The potential is time-independent.
- No dissipative effects (such as friction or damping) are included.
- The system is energy conserving.

---

## 2. Quantum Mechanical Assumptions

- The system is treated within non-relativistic quantum mechanics.
- Dynamics are governed by the time-independent Schrödinger equation.
- Relativistic effects are neglected.
- Spin degrees of freedom are not included.
- Physical states are stationary energy eigenstates.
- Superpositions of eigenstates are allowed, but explicit time evolution is not studied.

---

## 3. Numerical Assumptions

- The spatial domain is truncated to a finite interval.
- The truncation is chosen such that the wavefunction is negligible at the boundaries.
- Spatial derivatives are approximated using a second-order finite-difference scheme.
- The computational grid is uniform.
- Operators are represented as sparse matrices derived from local finite-difference stencils.
- Only the lowest-energy eigenstates are required for analysis.
- Eigenvalue problems are solved using sparse eigensolvers.

---

## 4. Scope

- The model focuses on low-energy properties of the quantum harmonic oscillator.
- Higher-dimensional effects beyond two spatial degrees of freedom are not considered.
- Extensions to time-dependent dynamics or anharmonic potentials are outside the scope of this section.