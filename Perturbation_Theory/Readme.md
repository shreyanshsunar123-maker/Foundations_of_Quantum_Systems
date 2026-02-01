## Anharmonic Oscillator: Perturbation Theory (Numerical Study)

 This project presents a numerical study of the one-dimensional anharmonic oscillator using first-order perturbation theory. The harmonic oscillator serves as the exactly solvable reference system, while a quartic term is introduced to model real-world deviations from ideal harmonic behavior.

 The goal is to examine how small anharmonic corrections shift energy levels and to understand the limitations of perturbation theory as quantum states extend further in space.

⸻––––––––––––––––––––––––––––––

# Physical Model

 The system consists of a particle in a harmonic potential with an additional quartic contribution. The harmonic part defines the unperturbed Hamiltonian, whose eigenstates and eigenvalues are computed numerically using a finite-difference representation of the kinetic energy operator.

 The quartic term is treated as a perturbation, and first-order energy corrections are obtained from expectation values evaluated using the unperturbed wavefunctions.

⸻––––––––––––––––––––––––––––––

# Methodology
	1.	Discretize the Schrödinger equation on a finite spatial grid.
	2.	Construct the harmonic oscillator Hamiltonian using finite differences.
	3.	Solve the eigenvalue problem numerically.
	4.	Normalize the resulting eigenstates.
	5.	Compute first-order energy corrections using perturbation theory.
	6.	Compare unperturbed and perturbed energy spectra.
	7.	Visualize wavefunctions, probability densities, potentials, and energy shifts.

⸻––––––––––––––––––––––––––––––

# Key Observations
	•	Low-energy states are well described by first-order perturbation theory.
	•	Higher-energy states experience larger corrections due to increased spatial spread.
	•	The expectation value of higher powers of position grows rapidly with the quantum number.
	•	Perturbation theory eventually breaks down when corrections become comparable to the unperturbed energies.

⸻––––––––––––––––––––––––––––––

# Scope and Limitations

 This project focuses on first-order perturbative corrections in one dimension. It does not include higher-order perturbation theory, exact diagonalization of the full anharmonic Hamiltonian, or time-dependent effects. These extensions are natural directions for future work.