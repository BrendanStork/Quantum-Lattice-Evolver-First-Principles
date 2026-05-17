import matplotlib.pyplot as plt
from time_simulation.circuit import Quantum_Circuit
from time_simulation.hamiltonian import general_hamiltonian, squarelattice, transverse_ising_hamiltonian
from time_simulation.expectation_values import observable_vs_time, magnetization
from time_simulation.plotting import (
    	plot_observable
)

  
def main():
	
	bonds = squarelattice(Nx = 3, Ny = 2)
	basis = transverse_ising_hamiltonian(bonds, J = 1, h = 1)

	qc = Quantum_Circuit(6)
	qc.x(0)

	obs1 = magnetization(axis = 'Z')
	obs2 = magnetization(axis = 'Y')
	obs3 = magnetization(axis = 'X')

	t, magZexact = observable_vs_time(qc, basis, time = 15, timesteps = 100, method = 'exact', observable = obs1)
	t, magZtrot10 = observable_vs_time(qc, basis, time = 15, timesteps = 100, trotter_steps=10, method = 'trotter', observable = obs1)
	t, magZtrot20 = observable_vs_time(qc, basis, time = 15, timesteps = 100, trotter_steps=20, method = 'trotter', observable = obs1)
	#t, magZtrot30 = observable_vs_time(qc, basis, time = 15, timesteps = 100, trotter_steps=30, method = 'trotter', observable = obs1)

	t, magYexact = observable_vs_time(qc, basis, time = 15, timesteps = 100, method = 'exact', observable = obs2)
	t, magYtrot10 = observable_vs_time(qc, basis, time = 15, timesteps = 100, trotter_steps=10, method = 'trotter', observable = obs2)
	t, magYtrot20 = observable_vs_time(qc, basis, time = 15, timesteps = 100, trotter_steps=20, method = 'trotter', observable = obs2)
	#t, magYtrot30 = observable_vs_time(qc, basis, time = 15, timesteps = 100, trotter_steps=30, method = 'trotter', observable = obs2)

	t, magXexact = observable_vs_time(qc, basis, time = 15, timesteps = 100, method = 'exact', observable = obs3)
	t, magXtrot10 = observable_vs_time(qc, basis, time = 15, timesteps = 100, trotter_steps=10, method = 'trotter', observable = obs3)
	t, magXtrot20 = observable_vs_time(qc, basis, time = 15, timesteps = 100, trotter_steps=20, method = 'trotter', observable = obs3)
	#t, magXtrot30 = observable_vs_time(qc, basis, time = 15, timesteps = 100, trotter_steps=30, method = 'trotter', observable = obs3)


	fig, axs = plt.subplots(1, 3, figsize = (15, 5))
	ylim = (-0.3, 0.75)

	#fig, ax = plt.subplots()

	plot_observable(t, magXexact, title = 'X-axis', label = 'Exact', ax = axs[0], ylim = ylim)
	plot_observable(t, magXtrot10, linestyle = '-.',  color ='r', label = 'Trotter (10 steps)', ax = axs[0])
	plot_observable(t, magXtrot20, linestyle = '-.', label = 'Trotter (20 steps)', ax = axs[0])
	#plot_observable(t, magXtrot30, linestyle = '-.', label = 'Trotter (30 steps)', ax = axs[0])

	plot_observable(t, magYexact, title = 'Y-axis', label = 'Exact', ax = axs[1], ylim = ylim)
	plot_observable(t, magYtrot10, linestyle = '-.',  color ='r', label = 'Trotter (10 steps)', ax = axs[1])
	plot_observable(t, magYtrot20, linestyle = '-.', label = 'Trotter (20 steps)', ax = axs[1])
	#plot_observable(t, magYtrot30, linestyle = '-.', label = 'Trotter (30 steps)', ax = axs[1])

	plot_observable(t, magZexact, title = 'Z-axis',  label = 'Exact', ax = axs[2], ylim = ylim)
	plot_observable(t, magZtrot10, linestyle = '-.',  color ='r', label = 'Trotter (10 steps)', ax = axs[2])
	plot_observable(t, magZtrot20, linestyle = '-.', label = 'Trotter (20 steps)', ax = axs[2])
	#plot_observable(t, magZtrot30, linestyle = '-.', label = 'Trotter (30 steps)', ax = axs[2])

	plt.suptitle('Magnetization vs Time\n (Square Lattice Transverse Field Ising Model N=6)', fontsize = 18)
	fig.supxlabel('Time', fontsize = 18)
	fig.supylabel('Magnetization', fontsize = 18)
	plt.tight_layout()
	plt.savefig('square_tfim_magnetization_exact_vs_trotter.png')
	plt.show()

if __name__ == '__main__':
    main()


