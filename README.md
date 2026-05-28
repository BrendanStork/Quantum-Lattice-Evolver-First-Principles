# Quantum Lattice Simulation Framework

A quantum simulation framework built from scratch in Python (NumPy + SciPy) for studying lattice Hamiltonian dynamics using both exact time evolution and digital (Trotterized) quantum simulation.

This project bridges quantum computing and condensed matter physics by providing tools to construct Hamiltonians, simulate time evolution, and compute physical observables on lattice systems such as the transverse-field Ising model.

---

# Overview

This framework implements a Hamiltonian-first approach to quantum simulation. Instead of focusing purely on circuit abstractions, it represents quantum dynamics in terms of physically meaningful Pauli-string Hamiltonians defined on lattice geometries.

The framework supports:

- Exact quantum time evolution via matrix exponentiation
- Digital quantum simulation via Trotter decomposition
- Arbitrary Pauli-string Hamiltonians
- 2D lattice model construction
- Observable tracking (magnetization, correlations)
- Benchmarking of exact vs approximate dynamics

It is fully implemented using NumPy and SciPy without reliance on external quantum SDKs.

---

# Key Features

## Quantum Circuit Simulation
- Statevector-based quantum simulation
- Single-qubit gates: X, Y, Z, H, S, T, rotations
- Multi-qubit CNOT implementation (bitwise optimized)
- Circuit state copying for independent evolution branches

## Hamiltonian Construction
- Arbitrary Pauli-string Hamiltonians
- Automatic validation of operator structure
- Conversion from symbolic operators to matrix form
- Transverse-field Ising Hamiltonian generator

## Lattice Models
- 2D square lattice generator (open boundary conditions)
- Bond-based interaction construction
- Flexible mapping from lattice sites to qubits

## Time Evolution
- Exact evolution:
  \
  U(t) = e^{-iHt}
  \
- Trotterized evolution via operator decomposition
- Configurable Trotter step resolution

## Observables
- Magnetization along X, Y, Z
- Two-point correlation functions
- General expectation value interface
- Time-dependent observable tracking

## Visualization
- Exact vs Trotter comparison plots
- Multi-panel subplot support
- Matplotlib wrapper for consistent scientific visualization

---

# Example: Transverse Field Ising Model (2D)

```python
bonds = squarelattice(Nx=3, Ny=2)

basis = transverse_ising_hamiltonian(
    bonds,
    J=1,
    h=1
)

qc = Quantum_Circuit(6)
qc.x(0)  # initial excitation

obs_z = magnetization(axis='Z')

t, mz_exact = observable_vs_time(
    qc,
    basis,
    time=15,
    timesteps=100,
    method='exact',
    observable=obs_z
)

t, mz_trotter = observable_vs_time(
    qc,
    basis,
    time=15,
    timesteps=100,
    method='trotter',
    trotter_steps=20,
    observable=obs_z
)

```

# Example Output

The framework produces time-dependent quantum dynamics that can be directly compared between exact and approximate evolution methods.

## Magnetization Dynamics (Exact vs Trotter)


![Magnetization Dynamics](figures/square_tfim_magnetization_exact_vs_trotter.png)

Expected results include:

- oscillatory magnetization dynamics
- convergence of Trotter simulation toward the exact solution as the number of Trotter steps increases
- clear separation between approximation regimes

---

# Design Philosophy

This framework is built around a Hamiltonian-centric abstraction rather than a purely circuit-centric model.

Key principles include:

## 1. Physics-first representation

Hamiltonians are represented explicitly as sums of Pauli strings, preserving physical interpretability.

## 2. Dual evolution modes

Both exact and Trotterized evolution are supported within a unified interface for benchmarking and analysis.

## 3. Modular observables

Physical observables are implemented as composable functions acting on quantum states.

## 4. Separation of concerns

- lattices define geometry
- Hamiltonians define physics
- circuits define state evolution
- observables define measurements

## 5. Educational transparency

All operations are implemented explicitly using NumPy and SciPy for clarity rather than black-box optimization.

---

# Limitations

This implementation is educational and exploratory in nature and has several limitations.

## Computational scaling

- statevector simulation scales exponentially with qubit number
- matrix-based Hamiltonian exponentiation becomes expensive beyond approximately 16–20 qubits

## Missing optimizations

- no sparse matrix representations
- no tensor network (MPS) compression
- no GPU acceleration

## Physics extensions not yet implemented

- fermionic Hamiltonians (Hubbard model)
- Jordan-Wigner transformation
- entanglement entropy
- structure factors in momentum space

---

# Future Work

Planned extensions include:

## Physics Models

- Heisenberg spin models
- Fermi-Hubbard model
- fermionic mappings (Jordan-Wigner)

## Advanced Observables

- entanglement entropy
- structure factors
- momentum-space correlations
- fidelity and Loschmidt echo

## Performance Improvements

- sparse operator representations
- cached Hamiltonian exponentiation
- tensor network backend (MPS/DMRG-style simulation)
- GPU acceleration

## Software Architecture

- full package modularization
- testing suite (pytest)
- CI integration
- benchmarking suite

---

# Project Structure (Suggested)

```text
quantum_sim/
├── circuits.py
├── evolution.py
├── hamiltonians.py
├── lattices.py
├── observables.py
├── plotting.py
└── operators.py

examples/
├── tfim_demo.py
└── trotter_comparison.py

figures/
└── square_tfim_magnetization_exact_vs_trotter.png
````

---

# Installation

```bash
git clone <your-repo-url>
cd quantum-lattice-sim
pip install numpy scipy matplotlib
```

---

# Requirements

* Python 3.9+
* NumPy
* SciPy
* Matplotlib

---

# Author Notes

This project was developed as an independent exploration of quantum many-body simulation, combining concepts from quantum computing and condensed matter physics.

It focuses on:

* explicit implementation of quantum evolution algorithms
* physically meaningful observables
* modular scientific computing design
* transparency of numerical methods

---

# Author

Brendan Stork

BS & MS Physics — Quantum Engineering  
San Jose State University

Research areas include:
- Quantum simulation
- Quantum many-body systems
- Condensed matter physics
- Hamiltonian dynamics
- Numerical quantum methods
