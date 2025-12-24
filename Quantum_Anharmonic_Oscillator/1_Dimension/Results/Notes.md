# Numerical Results and Observations

This section summarizes the numerical behavior of the one-dimensional
anharmonic oscillator with potential

V(x) = ½ x² + λ x⁴

computed using finite-difference discretization and matrix diagonalization.



## Energy Spectrum

The low-lying energy levels increase nonlinearly with the quantum number n.
Unlike the harmonic oscillator, where energy spacing is uniform, the inclusion of the quartic term (λ x⁴) causes the level spacing to grow
with increasing n.

This reflects the stronger confinement at larger |x| introduced by the
anharmonic term, which raises higher-energy states more rapidly than
lower ones.



## Eigenstate Structure

The computed eigenfunctions exhibit the following features:

- Definite parity due to the even symmetry of the potential.
- The number of nodes increases with the energy level, consistent with
  Sturm–Liouville theory.
- Eigenstates are more localized near the origin compared to the harmonic
  oscillator, reflecting the steeper potential walls at large |x|.

The offset plots help visualize higher excited states without overlap,
while the unshifted plots confirm the relative magnitudes and symmetry.



## Probability Densities

The probability densities |ψₙ(x)|² are sharply peaked near the origin for
low-lying states and broaden for higher-energy states.

Compared to the harmonic oscillator, the densities are more compressed,
indicating stronger spatial confinement due to the quartic term.
This effect becomes more pronounced for increasing λ.



## Numerical Stability and Resolution

The Hamiltonian matrix is considered sufficiently resolved when increasing
the grid size N and/or domain size L no longer produces significant changes
in the low-lying eigenvalues or eigenfunctions.

Convergence tests confirm that the reported results are stable under further refinement, indicating that discretization and boundary effects are under control for the chosen parameters.


## Physical Interpretation

The anharmonic oscillator breaks the exact solvability of the harmonic case, requiring numerical methods to access its spectrum.

The observed deviations from equal energy spacing and Gaussian ground-state
behavior illustrate how even small nonlinear terms qualitatively alter the
quantum dynamics of a system.

These results provide a foundation for further extensions, including:
- Parameter studies in λ
- Comparison with perturbation theory
- Time-dependent evolution
- Higher-dimensional generalizations