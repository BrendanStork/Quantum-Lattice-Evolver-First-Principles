import numpy as np
from .evolution import trotter_evolve, exact_evolve
from .circuit import Quantum_Circuit


def observable_vs_time(qc0, basis, *, time, timesteps=100,  method, observable, trotter_steps = None):
    t = np.linspace(0, time, timesteps)
    vals = np.zeros(timesteps)

    if method == 'trotter':
        for i in range(timesteps):
            qc = qc0.copy()
            psi = trotter_evolve(qc, basis, t[i], trotter_steps=trotter_steps)
            vals[i] = observable(psi)

    elif method == 'exact':
        for i in range(timesteps):
            qc = qc0.copy()
            psi = exact_evolve(qc, basis, t[i])
            vals[i] = observable(psi)

    else:
        raise ValueError("Unknown method")

    return t, vals

def magnetization(axis='Z'):

    def _obs(qc):
        N = int(np.log2(len(qc.state)))  # number of qubits
        total = 0

        for i in range(N):
            pauli_term = ['I'] * N
            pauli_term[i] = axis
            joined_pauli_term = ''.join(pauli_term)

            total += qc.expectation_value(joined_pauli_term)

        return total / N

    return _obs
 

def expectation_value(operator_string):
    def _obs(psi):
        return psi.expectation_value(operator_string)
    return _obs


def correlation(i, j, axis='Z'):

    def _obs(psi):
        N = psi.numqubits
        op = ['I'] * N
        op[i] = axis
        op[j] = axis
        joined_op = ''.join(op)
        return psi.expectation_value(joined_op)

    return _obs
