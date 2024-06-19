from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator
import numpy as np
import matplotlib.pyplot as plt

def create_CNOT0_gate():
    """
    Create a CNOT0 gate (acts on |0⟩ control state) as a custom gate.
    
    Returns:
    Gate: Custom CNOT0 gate.
    """
    qc = QuantumCircuit(2, name='CNOT0')  # Initialize a quantum circuit with 2 qubits

    # Implementing the CNOT0 gate
    qc.x(0)  # Apply X gate to flip the control qubit to |1>
    qc.cx(0, 1)  # Apply standard CNOT gate
    qc.x(0)  # Apply X gate again to revert the control qubit to its original state

    # Convert the QuantumCircuit to a gate
    return qc.to_gate()

def plot_matrix(matrix, title):
    """
    Plot the magnitude of a complex matrix using matplotlib.
    
    Parameters:
    matrix (np.ndarray): The matrix to be plotted.
    title (str): The title of the plot.
    """
    magnitude_matrix = np.abs(matrix)
    fig, ax = plt.subplots()
    cax = ax.matshow(magnitude_matrix, cmap='viridis')
    plt.title(title)
    fig.colorbar(cax)
    for (i, j), val in np.ndenumerate(magnitude_matrix):
        ax.text(j, i, f'{val:.2f}', ha='center', va='center', color='white')
    plt.show()

# Create the CNOT0 gate
CNOT0_gate = create_CNOT0_gate()

# Use the Operator class to get the matrix representation
CNOT0_matrix = Operator(CNOT0_gate).data

print("Matrix form of the CNOT0 gate:")
print(np.round(CNOT0_matrix, 2))

# Plot the matrix of the CNOT0 gate
plot_matrix(np.round(CNOT0_matrix, 2), "CNOT0 Gate Matrix")

# Define the standard CNOT gate
standard_cnot = QuantumCircuit(2)
standard_cnot.cx(0, 1)
CNOT_matrix = Operator(standard_cnot).data

print("\nMatrix form of the standard CNOT gate:")
print(np.round(CNOT_matrix, 2))

# Plot the matrix of the standard CNOT gate
plot_matrix(np.round(CNOT_matrix, 2), "Standard CNOT Gate Matrix")

# Define the CZ gate
cz_gate = QuantumCircuit(2)
cz_gate.cz(0, 1)
CZ_matrix = Operator(cz_gate).data

print("\nMatrix form of the CZ gate:")
print(np.round(CZ_matrix, 2))

# Plot the matrix of the CZ gate
plot_matrix(np.round(CZ_matrix, 2), "CZ Gate Matrix")
