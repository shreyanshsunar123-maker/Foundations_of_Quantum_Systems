# Assumptions — 2D Anharmonic Oscillator (Separable Normal-Mode Model)

This document lists all physical, mathematical, and numerical assumptions underlying the implementation and results presented in the `Src/experiments` scripts (`convergence.py`, `spectrum.py`, and `wavefunctions.py`) and discussed in the Results and Theory sections of this project.


## 1. Classical System Assumptions

- The system consists of a single particle of mass m moving in two dimensions.
- The restoring forces are linear in displacement, leading to harmonic motion at the classical level.
- Coupling between x and y is linear and symmetric.
- No damping, friction, or external driving forces are present.
- All parameters are time-independent.

The classical equations of motion are:
m·ẍ = −kₓ·x − k_xy·y,   m·ÿ = −k_y·y − k_xy·x



## 2. Normal Mode Assumptions

- The stiffness matrix
K = ⎡kₓ   k_xy⎤  
    ⎣k_xy  k_y ⎦
is real and symmetric.
- Therefore, it admits an orthonormal eigenbasis.
- A single orthogonal rotation diagonalizes the equations of motion.
- The resulting normal-mode coordinates represent the physically independent directions of oscillation.
- The same rotation is applied to both positions and velocities:
Q = Rᵀ·r,   Q̇ = Rᵀ·ṙ



## 3. Quantum Model Assumptions

- The system is treated within non-relativistic quantum mechanics.
- After classical diagonalization, each normal mode is quantized and treated as an independent one-dimensional quantum system.
- The quantum Hamiltonian is not solved as a full 2D eigenvalue problem; instead, two independent 1D Hamiltonians are constructed in normal-mode coordinates.
- Anharmonicity is introduced as a quartic correction in each normal mode:
V(Qᵢ) = ½·λᵢ·Qᵢ² + A·Qᵢ⁴
- No cross-anharmonic terms (e.g. Q₁²·Q₂²) are included.
- The full 2D wavefunction is assumed separable:
Ψ(Q₁, Q₂) = ψₙ₁(Q₁)·ψₙ₂(Q₂)

### Scope and Limitations of the Quantum Model

- The anharmonicity is applied only in the normal-mode coordinates.
- Cross-anharmonic coupling terms such as Q₁²·Q₂² are intentionally excluded.
- As a result, the quantum problem remains separable and admits product eigenstates.
- A fully coupled 2D anharmonic Schrödinger equation is beyond the scope of the present implementation.



## 4. Numerical Assumptions

- Continuous coordinates are truncated to a finite domain [-q_max, q_max].
- A uniform spatial grid is used.
- Second derivatives are approximated using a second-order finite-difference scheme.
- The Hamiltonian matrix is sparse.
- Only the lowest-energy eigenstates are computed using sparse eigensolvers, consistent with the low-energy focus of the analysis.
- Wavefunctions are normalized using discrete integration on the truncated spatial grid.