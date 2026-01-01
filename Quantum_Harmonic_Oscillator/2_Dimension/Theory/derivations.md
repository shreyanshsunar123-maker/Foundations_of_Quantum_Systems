# Derivations — One-Dimensional Quantum Harmonic Oscillator

This document derives the equations used in the numerical implementation
from first principles.


## 1. Classical Hamiltonian

The classical energy is:

𝐻 = (p² / 2m) + ½·m·ω²·x²



## 2. Quantization

Canonical quantization replaces momentum:

p → −i·ℏ·d/dx

Yielding the quantum Hamiltonian operator:

𝐻 = −(ℏ² / 2m)·d²/dx² + ½·m·ω²·x²



## 3. Stationary Schrödinger equation

𝐻·ψ(x) = E·ψ(x)

This is an eigenvalue problem for energy eigenstates.



## 4. Spatial discretization

Define a grid:

xⱼ = x_min + j·Δx

Second derivative approximation:

ψ″(x) ≈ (ψⱼ₊₁ − 2ψⱼ + ψⱼ₋₁) / (Δx)²



## 5. Operator matrix form

The Hamiltonian becomes:

𝐻 = 𝐓 + 𝐕

Where:
- 𝐓 is tridiagonal (kinetic)
- 𝐕 is diagonal (potential)



## 6. Eigenvalue problem

𝐻·ψₙ = Eₙ·ψₙ

Solved numerically using sparse eigensolvers.



## 7. Normalization

Discrete normalization condition:

∑ⱼ |ψⱼ|² · Δx = 1



## 8. Physical interpretation

- Each eigenvector corresponds to a quantum state.
- Each eigenvalue corresponds to an allowed energy.
- Nodes increase with quantum number.



## 9. Connection to higher dimensions

The 1D harmonic oscillator serves as the building block for:
- separable multidimensional systems,
- normal-mode decompositions,
- field-theoretic oscillators.