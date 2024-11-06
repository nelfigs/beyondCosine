from qiskit import QuantumCircuit, transpile, assemble, Aer, execute
from qiskit.providers.aer import PulseSimulator
from qiskit.pulse import Play, Schedule, Waveform, DriveChannel
from qiskit.visualization import plot_bloch_multivector, plot_histogram
import numpy as np
import matplotlib.pyplot as plt

# Initialize a Quantum Circuit for two qubits
qc = QuantumCircuit(2)

# Apply gates for the setup
qc.x(0)           # X Gate on qubit 0
qc.sx(0)          # SX Gate on qubit 0
qc.cx(0, 1)       # CNOT Gate with qubit 0 as control and qubit 1 as target

# Draw the circuit
qc.draw(output='mpl')
plt.show()

# Set up backend simulator
backend = Aer.get_backend('statevector_simulator')

# Compile and simulate the circuit
transpiled_circuit = transpile(qc, backend)
qobj = assemble(transpiled_circuit)
job = backend.run(qobj)
result = job.result()

# Extract and visualize the results
statevector = result.get_statevector()
plot_bloch_multivector(statevector)
plt.show()

# Measurement simulation to see counts
qc.measure_all()
backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend, shots=1024)
result = job.result()
counts = result.get_counts()
plot_histogram(counts)
plt.show()
