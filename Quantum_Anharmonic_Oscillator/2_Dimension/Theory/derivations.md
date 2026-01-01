# Derivations — 2D Anharmonic Oscillator

This document outlines the analytical steps leading from the classical coupled oscillator to the separable quantum normal-mode formulation implemented in the source code.



## 1. Classical Equations of Motion

The system consists of a particle of mass m moving in two dimensions under linear restoring forces:

`m·ẍ = −kₓ·x − k_xy·y`
`m·ÿ = −k_y·y − k_xy·x`

These equations can be written compactly in vector form as

`m·r̈ = −K·r,   r = (x, y)ᵀ`

where the stiffness matrix is

`K = ⎡kₓ   k_xy⎤  
    ⎣k_xy  k_y ⎦`



## 2. Normal-Mode Decomposition

Since \(K\) is real and symmetric, it admits an orthonormal eigenbasis. The normal modes are obtained by solving the eigenvalue problem

`K·vᵢ = λᵢ·vᵢ`

Let \(R\) be the orthogonal matrix whose columns are the normalized eigenvectors of \(K\). Introducing rotated coordinates

`Q = Rᵀ·r,   Q̇ = Rᵀ·ṙ`

the equations of motion decouple into independent normal modes:

`m·Q̈ᵢ = −λᵢ·Qᵢ`

i = 1, 2

`ωᵢ = √(λᵢ / m)`

Each normal mode represents an independent direction of oscillation.



## 3. Classical Energy in Normal Modes

In normal-mode coordinates, the total classical energy separates as a sum of mode energies:

`E = E₁ + E₂`

with

`Eᵢ = ½·m·Q̇ᵢ² + ½·λᵢ·Qᵢ²`

Energy conservation in each mode provides a consistency check for the numerical time integration.



## 4. Quantization and Anharmonic Extension

Each normal mode is quantized independently. The corresponding harmonic Hamiltonian for each normal mode is
`Hᵢ⁽⁰⁾ = −(ℏ² / 2m)·d²/dQᵢ² + ½·λᵢ·Qᵢ²`
The harmonic potential is augmented by a quartic anharmonic term, yielding the 1D Hamiltonian

`Hᵢ = −(ℏ² / 2m)·d²/dQᵢ² + ½·λᵢ·Qᵢ² + A·Qᵢ⁴`

The Schrödinger equation for each mode is solved numerically using finite-difference discretization and sparse eigensolvers.



## 5. Construction of the 2D Quantum State

Because the Hamiltonian is separable, the full 2D quantum eigenstates are constructed as products of 1D normal-mode eigenfunctions:

`Ψ₍ₙ₁,ₙ₂₎(Q₁, Q₂) = ψₙ₁(Q₁)·ψₙ₂(Q₂)`

\n
The corresponding probability density associated with this eigenstate is

`ρ(Q₁, Q₂) = |Ψ₍ₙ₁,ₙ₂₎(Q₁, Q₂)|²`

This separable construction matches the implementation in `wavefunctions.py` and avoids solving a fully coupled 2D anharmonic eigenvalue problem.



## 6. Scope of the Derivation

The derivation assumes that anharmonicity acts independently in each normal mode. Cross-mode anharmonic coupling terms are not included. Extending the model to a fully coupled 2D anharmonic Hamiltonian would require solving a true 2D Schrödinger equation and is left for future work.