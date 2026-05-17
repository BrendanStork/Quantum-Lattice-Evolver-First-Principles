from .gates import GATES
import numpy as np

def string_to_operator(pauli_string):
    operator = GATES[pauli_string[0]] # Builds operator
    for p in pauli_string[1:]:
        operator = np.kron(operator, GATES[p])
    return operator


def general_hamiltonian(**pauli_terms): ##basically checks for errors then turns input into hamiltonian dict

    if not pauli_terms:
        raise ValueError('Hamiltonian cannot be empty')
        
    pauli_ops = ['I', 'X', 'Y', 'Z']
    lengths = {len(term) for term in pauli_terms} # If all the terms have the same length, set length = 1

    for term in pauli_terms:
        for char in term:
            if char not in pauli_ops:
                raise ValueError(f'Unknown operator {char}')
    
    if len(lengths) != 1:
        raise ValueError('All Pauli strings must have the same length')

    for term, coeff in pauli_terms.items():
        if not isinstance(term, str):
            raise TypeError(f'{term} is not a string')
            
        if not isinstance(coeff, (int, float, complex)):
            raise TypeError(f'Coefficient for "{term}" must be a real number')

    return pauli_terms


def squarelattice(Nx, Ny, y_periodic = False, full_periodic = False):
    bonds = []
    for i in range(Nx * Ny):
        if (i+1) % Nx != 0: # Connects right up until boundary
            bonds.append([i, i+1])
        if i < Nx*(Ny-1): # Connects down up until boundary
            bonds.append([i, i+Nx])
    return bonds


def transverse_ising_hamiltonian(bonds, J, h, transverse = True):
    ising_hamil = {}
    sites = {site for bond in bonds for site in bond}
    site_num = max(sites) + 1
    #print(bonds, site_num)
    for bond_i, bond_j in bonds:
        pauli_term = ['I'] * site_num # Initializes Pauli string to all 'I'
        pauli_term[bond_i] = 'Z'
        pauli_term[bond_j] = 'Z'
        joined_pauli_term = ''.join(pauli_term) # Joins characters into one Pauli string
        #print(''.join(pauli_term), -J)
        ising_hamil[joined_pauli_term] = -J
    if transverse:
        for i in range(site_num):
            pauli_term = ['I'] * site_num
            pauli_term[i] = 'X'
            joined_pauli_term = ''.join(pauli_term)
            #print(''.join(pauli_term), -h)
            ising_hamil[joined_pauli_term] = -h
    return ising_hamil
