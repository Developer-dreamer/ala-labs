import numpy as np
import matplotlib.pyplot as plt
import transfrmProcessor as tp
# Define the matrix and the vector
matrix = np.array([[1, 0], [0, 1]])
vector = np.array([[1, 1], [0, 0]])

# Transpose the vector to the new space
transposed_vector = tp.scale(3, vector)
print(transposed_vector)


# Plot the standard coordinate lines
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)

# Plot the new space defined by the vectors
plt.quiver(*[0, 0], *matrix[0], color=['r'], scale=10)
plt.quiver(*[0, 0], *matrix[1], color=['b'], scale=10)
plt.quiver(*[0, 0], *transposed_vector[0], color=['g'], scale=10)

plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()