# Hydrogen Orbital Theory (Concise)

The hydrogen atom is described by the time‑independent Schrödinger equation with a Coulomb potential, assuming a single electron bound to a proton. In spherical coordinates, the equation is separable, allowing the total wavefunction to be written as a product of radial and angular components:

 ψ(r, θ, φ) = Rₙₗ(r) · Yₗᵐ(θ, φ)

Here, n is the principal quantum number, l the orbital angular momentum quantum number, and m the magnetic quantum number.

# The radial coordinate is rescaled using
 ρ = 2r / (n·a₀),
 where a₀ is the Bohr radius. The radial wavefunction then takes the  form:

 Rₙₗ(r) = N · exp(−ρ/2) · ρˡ · L(ρ)

 where L(ρ) is the generalized Laguerre polynomial of order (n − l − 1) with parameter (2l + 1), and N is a normalization constant ensuring ∫|ψ|² dV = 1.

# The angular dependence is encoded in the spherical harmonics:

 Yₗᵐ(θ, φ) = normalization · Pₗᵐ(cos θ) · exp(i m φ)

 where Pₗᵐ are the associated Legendre polynomials. While these harmonics are complex-valued, physically meaningful orbital shapes are obtained by taking real linear combinations. For example:

 px = (Y₁⁻¹ − Y₁¹) / √2
 py = (Y₁⁻¹ + Y₁¹) / (i√2)
 pz = Y₁⁰

 and for d orbitals:

 dz² = Y₂⁰
 dxz = (Y₂⁻¹ − Y₂¹) / √2
 dyz = (Y₂⁻¹ + Y₂¹) / (i√2)
 dxy = (Y₂⁻² − Y₂²) / √2
 dx²−y² = (Y₂² + Y₂⁻²) / √2

# The physically observable quantity is the probability density:

 |ψ(r, θ, φ)|² = |Rₙₗ(r)|² · |Yₗᵐ(θ, φ)|²

 In this project, the orbital cloud is constructed using Monte Carlo sampling. A large number of candidate points are drawn uniformly in spherical volume, converted to Cartesian coordinates, and assigned weights proportional to |ψ|². A weighted resampling step then produces a point cloud whose spatial density directly reflects the quantum probability distribution of the electron.

 The resulting 3D visualization represents the stationary electron probability cloud for a given hydrogen orbital, rather than a classical trajectory.

# How To Run:
 In terminal: 
 python3 main.py --n (value of n) --l (value of l) --m (value of m) or
 python3 main.py --n (value of n) --l (value of l) --orbital (orbital you want)

 To see the default n=2, l=1, px, py, pz orbitals:
 python3 main.py