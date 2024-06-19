from qiskit import QuantumCircuit, Aer, transpile, execute
from qiskit.circuit import Gate
import numpy as np

# Create the M3 gate using a QuantumCircuit
def create_M3_gate():
    qc = QuantumCircuit(2, name='M3')  # Initialize a quantum circuit with 2 qubits

    # Implementing the CNOT0 gate
    # A CNOT0 gate can be implemented by flipping the control qubit with X gates
    qc.x(0)  # Apply X gate to flip the control qubit if it's in state |1>
    qc.cx(0, 1)  # Apply CNOT gate where the control is qubit 0 and target is qubit 1
    qc.x(0)  # Apply X gate again to revert the control qubit to its original state

    # Implementing the SWAP gate
    qc.swap(0, 1)  # SWAP gate to exchange the states of qubits 0 and 1

    # Convert the QuantumCircuit to a gate
    return qc.to_gate()

# Create the M3 gate
M3_gate = create_M3_gate()

