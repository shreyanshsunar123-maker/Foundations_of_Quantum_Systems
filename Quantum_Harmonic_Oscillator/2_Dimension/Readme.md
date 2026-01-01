# 2D Coupled Harmonic Oscillator (Classical → Normal Modes → Quantum)

This project studies a **2D coupled harmonic oscillator** in two stages:

1) **Classical dynamics (x, y)** using numerical integration  
2) **Normal-mode rotation (Q₁, Q₂)** to decouple the system  
3) **Quantum normal modes** by solving the one-dimensional Schrödinger eigenproblem for each mode (finite-difference + sparse eigensolver)  
4) **2D separable probability density** built from the product of the two 1D eigenstates


## Theory (What’s happening physically)

### 1) Classical coupled oscillator
We model a mass m moving in two dimensions with linear restoring forces and coupling:

 m·ẍ = −kₓ·x − k_xy·y,   m·ẏ̈ = −k_y·y − k_xy·x

This can be written compactly using the stiffness matrix:

 m·r̈ = −K·r,   r = (x, y)ᵀ,   K = ⎡kₓ   k_xy⎤  
                                                  ⎣k_xy  k_y ⎦

### 2) Normal modes (diagonalization)
Normal modes are found by solving the eigenproblem:

K·vᵢ = λᵢ·vᵢ

Let \(R=[\mathbf{v}_1\ \mathbf{v}_2]\). Then the rotation:

Q = Rᵀ·r

produces decoupled coordinates Q₁, Q₂ with independent equations:

 m·Q̈ᵢ = −λᵢ·Qᵢ,   ωᵢ = √(λᵢ / m)

So the energy splits cleanly into two independent mode energies:

Eᵢ = ½·m·Q̇ᵢ² + ½·λᵢ·Qᵢ²

### 3) Quantum normal modes
After rotation, the Hamiltonian separates:

𝐻 = 𝐻₁(Q₁) + 𝐻₂(Q₂)

Each mode is a **1D quantum harmonic oscillator**:

𝐻ᵢ = −(ℏ² / 2m)·d²/dQᵢ² + ½·λᵢ·Qᵢ²

We solve the stationary Schrödinger equation numerically on a grid:

𝐻ᵢ·ψₙ(Qᵢ) = Eₙ·ψₙ(Qᵢ)

using a finite-difference Laplacian and a sparse eigen-solver to obtain the lowest few states.

### 4) 2D separable wavefunction and probability density
Because the Hamiltonian separates, stationary states factorize:

Ψ₍ₙ₁,ₙ₂₎(Q₁, Q₂) = ψₙ₁(Q₁)·ψₙ₂(Q₂)

and the probability density is:

ρ(Q₁, Q₂) = |Ψ(Q₁, Q₂)|²

This project visualizes ρ(Q₁, Q₂) via a heatmap.



## What the script produces

Running explorations.ipynb generates:

- **Classical trajectory** in the x–y plane
- **Time series subplots** for x(t), y(t), Q₁(t), Q₂(t), Q̇₁(t), Q̇₂(t)
- **1D quantum eigenfunctions** for Q1 and Q2 (n=0..3)
- **2D probability density heatmap** for a chosen separable state (default n1=0, n2=1)
- **Classical normal-mode energies** E_{Q₁}(t) and E_{Q₂}(t), which remain constant in time
