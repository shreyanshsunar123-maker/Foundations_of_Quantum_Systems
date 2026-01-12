# Hydrogen Orbital Derivations
This document outlines the mathematical derivation behind the orbital cloud visualizations in this project.



## 1. Schrodinger Equation (Hydrogen Atom)
We begin with the time-independent Schrodinger equation for a hydrogen atom in spherical coordinates:

    [-ħ² / (2μ)] ∇²ψ(r, θ, φ) - [e² / (4πε₀r)] ψ(r, θ, φ) = Eψ(r, θ, φ)

After separation of variables, the wavefunction becomes:

    ψ(r, θ, φ) = Rₙₗ(r) · Yₗᵐ(θ, φ)

Where:
- Rₙₗ(r) is the radial part
- Yₗᵐ(θ, φ) is the spherical harmonic (angular part)



## 2. Radial Solution
The radial part of the hydrogenic wavefunction is given by:

    Rₙₗ(r) = Nₙₗ · ρˡ · e^(-ρ/2) · L⁽²ˡ⁺¹⁾ₙ₋ₗ₋₁(ρ)

Where:
- ρ = (2r) / (n · a₀)
- L⁽²ˡ⁺¹⁾ₖ(ρ) is the associated Laguerre polynomial
- a₀ is the Bohr radius
- Nₙₗ is a normalization constant

The normalization constant is:

    Nₙₗ = sqrt[(2 / (n · a₀))³ · k! / (2n · (n + l)!)]
    where k = n - l - 1



## 3. Angular Solution (Spherical Harmonics)
The angular part is given by the spherical harmonics:

    Yₗᵐ(θ, φ) = Normalization · Pₗᵐ(cosθ) · e^(i·m·φ)

To visualize real orbitals like px, py, dxy, etc., we form linear combinations such as:

- px = (Y₁⁻¹ - Y₁¹) / √2
- py = (Y₁⁻¹ + Y₁¹) / (i√2)
- pz = Y₁⁰
- dz² = Y₂⁰
- dxz = (Y₂⁻¹ - Y₂¹) / √2
- dxy = (Y₂⁻² - Y₂²) / √2



## 4. Probability Cloud Visualization

To create the 3D visualization:
- We sample many random points (r, θ, φ) in spherical space.
- Compute the wavefunction ψ(r, θ, φ) at each point.
- Weight each point by |ψ|² (probability density).
- Resample based on probability and convert to (x, y, z).
- Plot with color intensity based on |ψ|².

This yields a realistic visual representation of the electron cloud for any (n, l, m).