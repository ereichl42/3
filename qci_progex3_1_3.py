from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
import numpy as np
import math

# Define the M3 gate
def create_M3_gate():
    qc = QuantumCircuit(2, name='M3')
    qc.x(0)  # Flip control qubit to |1>
    qc.cx(0, 1)  # Apply CNOT gate
    qc.x(0)  # Revert control qubit to original state
    qc.swap(0, 1)  # SWAP gate to exchange states of qubits
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
        # Apply controlled-M3 gates controlled by the negation of the input qubits
        qc.x(i)
        qc.append(cM3_gate, [i, n, n + 1])
        qc.x(i)
    
    # Implement the OR gate using ancillary qubits
    qc.ccx(n, n + 1, n + 2)
    
    # Negate the result and measure
    qc.x(n + 2)
    qc.measure(n + 2, 0)

    # Uncompute the negation
    qc.x(n + 2)

    return qc

# Create the mod[3] gate
mod3_circuit = create_mod3_gate()

# Function to initialize a quantum circuit with a specific state
def initialize_circuit_with_state(circuit, state, num_qubits):
    # Create a state vector with the desired state having amplitude 1 and others having amplitude 0
    state_vector = np.zeros(2**num_qubits)
    state_vector[int(state, 2)] = 1
    circuit.initialize(state_vector, list(range(num_qubits)))

# Test the implementation of the mod[3] gate
def test_mod3_gate():
    backend = Aer.get_backend('qasm_simulator')
    test_results = []

    # Test all possible 16 values for the 4 input qubits
    for i in range(16):
        input_state = f"{i:04b}"  # Convert to binary
        test_circuit = mod3_circuit.copy()
        initialize_circuit_with_state(test_circuit, input_state, test_circuit.num_qubits)
        transpiled_circuit = transpile(test_circuit, backend)
        job = backend.run(transpiled_circuit)
        result = job.result()
        counts = result.get_counts()
        test_results.append((input_state, counts))
    
    # Print the test results with expected output
    for input_state, counts in test_results:
        expected_output = str(int(int(input_state, 2) % 3 == 0))
        print(f"Input: {input_state}, Output: {counts}, Expected Output: {expected_output}")

# Execute the test
test_mod3_gate()
