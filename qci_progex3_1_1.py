import numpy as np
import matplotlib.pyplot as plt

# Function to plot a matrix
def plot_matrix(matrix, title):
    fig, ax = plt.subplots()
    cax = ax.matshow(matrix, cmap='viridis')
    plt.title(title)
    fig.colorbar(cax)
    for (i, j), val in np.ndenumerate(matrix):
        ax.text(j, i, f'{val:.2f}', ha='center', va='center', color='white')
    plt.show()

# Given M3 matrix
M3 = np.array([[0, 1, 0, 0],
               [0, 0, 1, 0],
               [1, 0, 0, 0],
               [0, 0, 0, 1]])

# Compute M3^3
M3_cubed = np.linalg.matrix_power(M3, 3)

# Identity matrix for comparison with the eye function
identity_matrix = np.eye(4)

# Check if M3^3 is the identity matrix using np.allclose function, 
# which checks if two arrays are element-wise equal, a tolerance can be applied
is_identity = np.allclose(M3_cubed, identity_matrix)

# Display M3 cubed and if it is the identity matrix
print("M3^3:")
print(M3_cubed)
print("M3^3 is identity:", is_identity)

#plot_matrix(M3_cubed, 'M3^3')

