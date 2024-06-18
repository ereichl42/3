from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import array_to_latex
from IPython.display import display, Latex
import numpy as np
import matplotlib.pyplot as plt
# Define the quantum circuit
qc = QuantumCircuit(2)

# Apply CNOT0 (Control: 0, Target: 1)
qc.cx(0, 1)
# Apply SWAP gate
qc.swap(0, 1)

# Get the unitary matrix of the circuit
simulator = Aer.get_backend('unitary_simulator')
compiled_circuit = transpile(qc, simulator)
result = simulator.run(compiled_circuit).result()
unitary_matrix = result.get_unitary(compiled_circuit)

# Print pretext and display the matrix
display(Latex("Matrix of the circuit:"))
display(array_to_latex(unitary_matrix))

# Print the matrix in a more readable format
print("Matrix of the circuit:")
for row in unitary_matrix:
    print(" ".join(f"{elem.real:.2f}{elem.imag:+.2f}j" for elem in row))

# Plot the matrix
# Separate the real and imaginary parts
real_part = np.real(unitary_matrix)
imag_part = np.imag(unitary_matrix)

# Plotting the real part of the matrix
plt.figure(figsize=(8, 6))
plt.imshow(real_part, cmap='viridis', interpolation='none', aspect='auto')
plt.colorbar(label='Real Part')
plt.title('Real Part of Unitary Matrix')
plt.xlabel('Column')
plt.ylabel('Row')
plt.show()

# Plotting the imaginary part of the matrix
plt.figure(figsize=(8, 6))
plt.imshow(imag_part, cmap='viridis', interpolation='none', aspect='auto')
plt.colorbar(label='Imaginary Part')
plt.title('Imaginary Part of Unitary Matrix')
plt.xlabel('Column')
plt.ylabel('Row')
plt.show()



