# 2D Anharmonic Oscillator (Normal-Mode Quantum Model)

This project studies a **2D coupled harmonic oscillator**, transforms it into **normal modes**, and
extends the system into a **separable quantum anharmonic oscillator** by adding quartic corrections
to each normal mode.

The implementation includes:
- Classical dynamics in (x, y)
- Normal-mode diagonalization
- Classical energy conservation checks
- Quantum eigenstates for each anharmonic normal mode
- Construction and visualization of a separable 2D quantum state



## Physical Model

### Classical potential (in x,y)
V(x, y) = ½·kₓ·x² + ½·k_y·y² + k_xy·x·y

The system is diagonalized into normal coordinates:
(x, y) → (Q₁, Q₂)



### Quantum potential (in normal modes)
Each normal mode is treated independently with an anharmonic correction:
V(Qᵢ) = ½·λᵢ·Qᵢ² + A·Qᵢ⁴

This leads to **two independent 1D quantum anharmonic oscillators**.

The full 2D quantum state is constructed as a product:
Ψ(Q₁, Q₂) = ψₙ₁(Q₁) · ψₙ₂(Q₂)



## What This Project Demonstrates

✔ Normal-mode physics  
✔ Anharmonic quantum corrections  
✔ Energy conservation diagnostics  
✔ Numerical eigenvalue methods (sparse eigensolvers)  
✔ Separable 2D wavefunctions  
✔ Scientific visualization



## What This Project Does NOT Do

- It does **not** include cross-anharmonic coupling terms such as Q₁²·Q₂²
- The anharmonicity is **separable**, not fully coupled
- A full 2D anharmonic Hamiltonian is left as future work



## Generated Figures (auto-saved)

All figures are saved to `Results/figures/`:

1. `xy_trajectory.png`
2. `Total_Energy_Of_Normal_Modes.png`
3. `Time_series_and_normal_modes.png`
4. `Q1_eigenstates.png`
5. `Q2_eigenstates.png`
6. `2D_probability.png`