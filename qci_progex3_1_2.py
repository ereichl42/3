from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.circuit import Gate
import numpy as np
import matplotlib.pyplot as plt
# Given M3 matrix
M3 = np.array([[0, 1, 0, 0],
               [0, 0, 1, 0],
               [1, 0, 0, 0],
               [0, 0, 0, 1]])

def get_gate_matrix(gate):
    """
    Given a gate, return its matrix representation.
    
    Parameters:
    gate (Gate): The quantum gate whose matrix representation is needed.
    num_qubits (int): The number of qubits the gate acts on.
    
    Returns:
    np.ndarray: The matrix representation of the gate.
    """
    # Create a quantum circuit with the specified number of qubits
    qc = QuantumCircuit(2)
    qc.append(gate, [0, 1])  # Append the gate to the circuit
    # Use the unitary simulator to get the matrix representation
    backend = Aer.get_backend('unitary_simulator')
    transpiled_circuit = transpile(qc, backend)
    job = backend.run(transpiled_circuit)
    result = job.result()
    unitary = result.get_unitary(qc)

    return unitary

# Define the M3 gate using a QuantumCircuit
def create_M3_gate():
    qc = QuantumCircuit(2, name='M3')  # Initialize a quantum circuit with 2 qubits

    # Implementing the CNOT0 gate
    qc.x(0)  # Apply X gate to flip the control qubit to |1>
    qc.cx(0, 1)  # Apply CNOT gate where the control is qubit 0 and target is qubit 1
    qc.x(0)  # Apply X gate again to revert the control qubit to its original state

    # Implementing the SWAP gate
    qc.swap(0, 1)  # SWAP gate to exchange the states of qubits 0 and 1
    
    # Convert the QuantumCircuit to a gate
    return qc.to_gate()

# Create the M3 gate
M3_gate = create_M3_gate()
M3_gate_matrix = get_gate_matrix(M3_gate)

print("Matrix form of the M3 gate from the implementation:")
print(M3_gate_matrix)


print("\nGiven M3 matrix:")
print(M3)

# Comparing the matrix representation of the M3 gate with the given matrix
print("M3 Matrix and gate representation are equal: ", np.allclose(M3, M3_gate_matrix))



