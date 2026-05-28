oimport numpy as np


GATES = {
    'I' : np.array([[1,0], [0,1]]),
    'X' : np.array([[0, 1], [1, 0]]),
    'Y' : np.array([[0, -1j], [1j, 0]]),
    'Z' : np.array([[1, 0], [0,-1]]),
    'H' : 1/np.sqrt(2) * np.array([[1, 1], [1,-1]]),
    'S' : np.array([[1,0], [0, 1j]]),
    'Sdag' : np.array([[1,0], [0, -1j]]),
    'T' : np.array([[1,0], [0, np.exp(1j*np.pi/4)]]),
    'P' : lambda theta : np.array([[1, 0],[0, np.e**(1j*theta)]]),
    'RX': lambda theta : np.array([[np.cos(theta/2),-1j*np.sin(theta/2)], [-1j*np.sin(theta/2),np.cos(theta/2)]]),
    'RY': lambda theta : np.array([[np.cos(theta/2),-np.sin(theta/2)], [np.sin(theta/2),np.cos(theta/2)]]),
    'RZ': lambda theta : np.array([[np.exp(-1j*theta/2),0], [0,np.exp(1j*theta/2)]])
}

