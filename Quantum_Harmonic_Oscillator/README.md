## Quantum Harmonic Oscillator

A numerical and theoretical exploration

# Overview

This project implements a numerical solution to the one-dimensional quantum harmonic oscillator using finite-difference discretization of the time-independent Schrödinger equation. The goal is not only to reproduce known analytic results, but to study convergence, structure, and limitations of numerical quantum methods in a controlled setting.

The project is structured to reflect how a theorist approaches computation:
assumptions → operators → models → experiments → results.

# Physical Model

The Hamiltonian of the quantum harmonic oscillator is

𝐻 = (−ℏ^2/2𝑚).𝑑^2/𝑑𝑥^2 + 1/2𝑚Ω^2𝑥^2

with units chosen such that

ℏ=𝑚=Ω=1.

The continuous operator is approximated on a finite spatial grid, converting the Schrödinger equation into a matrix eigenvalue problem.

# Numerical Method

Spatial domain truncated to [−L,L]

Central finite-difference approximation for the second derivative

Hamiltonian constructed as a sparse tridiagonal matrix

Eigenvalue problem solved using scipy.linalg.eigh

Convergence is examined by varying grid resolution N and domain size L.