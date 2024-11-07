from qiskit import QuantumCircuit
from qiskit.circuit.library import HGate, MCXGate
import matplotlib.pyplot as plt

# Define gates
mcx_gate = MCXGate(3)
hadamard_gate = HGate()

# Create quantum circuit
qc = QuantumCircuit(4)
qc.append(hadamard_gate, [0])
qc.append(mcx_gate, [0,1,2,3])

# Draw and display the circuit
qc.draw('mpl')
plt.show()
