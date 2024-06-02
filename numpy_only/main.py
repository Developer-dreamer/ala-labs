import numpy as np
import transformProcessor as tp
import Presenter as pr
import OpenCV.CVtransformationsMatrix as cvt

# Define the vectors
vector_triangle = np.array([[0, 0], [2.5, 5], [7.25, 2.5], [0, 0]])
vector_figure = np.array([[0, 0],
                          [5, 1],
                          [2, 5],
                          [2.5, 2],
                          [0, 4],
                          [-2.5, 2],
                          [-2, 5],
                          [-5, 1],
                          [0, 0]]
                         )
vector_figure_3d = np.array(
    [[1, 1, 1], [1, 4, 1], [4, 4, 1], [4, 1, 1], [1, 1, 1], [2.5, 2.5, 5], [1, 1, 1], [2.5, 2.5, 5], [1, 4, 1],
     [2.5, 2.5, 5], [4, 4, 1], [2.5, 2.5, 5], [4, 1, 1]])

# Transpose the vector to the new space
transposed_vector = tp.rotate(vector_figure, axis='x')
print(transposed_vector)
pr.showResults2D(transposed_vector, vector_figure)

transposed_vector = cvt.shear_сv(vector_triangle, 0.2, 'x')
print(transposed_vector)
pr.showResults2D(transposed_vector, vector_triangle)

# Transpose the vector to the new space
transposed_vector = tp.custom_transformation(vector_figure_3d, [[2, 0, 0], [0, 1, 0], [0, 0, 1]])
print(transposed_vector)
pr.showResults3D(vector_figure_3d, transposed_vector)
