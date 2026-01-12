# Assumptions in Hydrogen Orbital Visualization
The simulation is based on these simplifications and assumptions:

1. **Single Electron System**:
   - Only hydrogen (or hydrogen-like ions) are modeled — no electron-electron repulsion.

2. **Stationary States**:
   - Orbitals are stationary solutions (energy eigenstates) of the time-independent Schrodinger equation.

3. **Non-Relativistic Quantum Mechanics**:
   - We ignore relativistic effects and fine structure.

4. **Bohr Radius Normalization**:
   - All lengths are expressed in units of the Bohr radius (a0 = 1.0).

5. **Radial Cutoff**:
   - The maximum radial extent is set to r_max = 8n^2*a0 to ensure 99% of the probability cloud is captured.

6. **Monte Carlo Sampling**:
   - Points are uniformly sampled in spherical volume and then reweighted based on probability density.

7. **Real Spherical Harmonics**:
   - Real-valued combinations of Yₗᵐ are used (e.g., px, py, dz²) for easier interpretation and aesthetic visual clarity.

8. **Opacity & Color**:
   - Color scale is based on |ψ|² with Plotly’s "plasma" theme; opacity fixed for visual coherence.

9. **Quantum Numbers Validity**:
   - Inputs are validated to satisfy:
        - n > 0
        - 0 ≤ l < n
        - -l ≤ m ≤ l