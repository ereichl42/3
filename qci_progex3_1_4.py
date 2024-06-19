from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
import numpy as np
import math

# Step 1: Define the M3 gate using a QuantumCircuit
def create_M3_gate():
    qc = QuantumCircuit(2, name='M3')  # Initialize a quantum circuit with 2 qubits

    # Implementing the CNOT0 gate
    qc.x(0)  # Apply X gate to flip the control qubit to |1>
    qc.cx(0, 1)  # Apply standard CNOT gate
    qc.x(0)  # Apply X gate again to revert the control qubit to its original state

    # Implementing the SWAP gate
    qc.swap(0, 1)  # SWAP gate to exchange the states of qubits 0 and 1

    # Convert the QuantumCircuit to a gate
    return qc.to_gate()

# Create the M3 gate
M3_gate = create_M3_gate()

# Define the controlled version of the M3 gate (cM3)
cM3_gate = M3_gate.control(1)

# Function to create the mod[3] gate
def create_mod3_gate():
    n = 4  # Number of input qubits
    q = 3  # Value of q
    k = math.ceil(math.log2(q))  # Number of ancillary qubits
    
    # Create a quantum circuit with n input qubits, k ancillary qubits, and 1 output qubit
    qc = QuantumCircuit(n + k + 1, 1)

    # Apply controlled M3 gates
    for i in range(n):
        qc.append(cM3_gate, [i, n, n + 1])

    # Implement the OR gate using ancillary qubits
    qc.cx(n, n + 2)
    qc.cx(n + 1, n + 2)
    
    # Negate the result and measure
    qc.x(n + 2)
    qc.measure(n + 2, 0)

    # Uncompute the negation
    qc.x(n + 2)

    return qc

# Create the mod[3] gate
mod3_circuit = create_mod3_gate()

# Test the implementation of the mod[3] gate
def test_mod3_gate():
    backend = Aer.get_backend('qasm_simulator')
    test_results = []

    # Test all possible 16 values for the 4 input qubits
    for i in range(16):
        input_state = f"{i:04b}"[::-1]  # Convert to binary and reverse for little-endian order
        test_circuit = mod3_circuit.copy()
        test_circuit.initialize([1 if x == '1' else 0 for x in input_state] + [0] * (test_circuit.num_qubits - len(input_state)), list(range(test_circuit.num_qubits)))
        transpiled_circuit = transpile(test_circuit, backend)
        job = transpile(transpiled_circuit, backend, shots=1024)
        result = job.result()
        counts = result.get_counts()
        test_results.append((input_state[::-1], counts))
    
    # Print the test results
    for input_state, counts in test_results:
        print(f"Input: {input_state}, Output: {counts}")

# Execute the test
test_mod3_gate()
