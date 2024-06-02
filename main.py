import numpy as np
import transformProcessor as tp
import Presenter as pr
# Define the matrix and the vector
vector_triangle = np.array([[0, 0], [2.5, 5], [7.25, 2.5]])
vector_figure = np.array([[0, 0], [1, 2], [4.4, 1], [1.5, 5.4], [0, -1.8], [-7.5, 6.4], [-3.4, 1], [-1, -5.2]])
vector_figure_3d = np.array([[1, 1, 1], [1, 4, 1], [4, 4, 1], [4, 1, 1], [2.5, 2.5, 5]])
# # Transpose the vector to the new space
# transposed_vector = tp.rotate(vector_figure, 45)
# print(transposed_vector)
#
#
# pr.showResults2D(transposed_vector, vector_figure)

# Transpose the vector to the new space
transposed_vector = tp.rotate_3d(vector_figure_3d, 45, 'y')
print(transposed_vector)
pr.showResults3D(vector_figure_3d, transposed_vector)