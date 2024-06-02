import numpy as np

def rotate(vector, degrees = 0, axis = "none"):
    transposed = []
    if axis == "x":
        R = np.array([[1, 0], [0, -1]])
        for i in range(len(vector)):
            transposed.append(np.dot(R, vector[i]))
        return np.array(transposed)
    if axis == "y":
        R = np.array([[-1, 0], [0, 1]])
        for i in range(len(vector)):
            transposed.append(np.dot(R, vector[i]))
        return np.array(transposed)
    theta = np.radians(degrees)
    c, s = np.cos(theta), np.sin(theta)
    R = np.array([[c, -s], [s, c]])
    for i in range(len(vector)):
        transposed.append(np.dot(R, vector[i]))
    return np.array(transposed)

def scale(scalar, vector):
    return scalar * vector

def shear_matrix(theta, axis):
    theta = np.radians(theta)  # Convert the angle to radians
    if axis == 'x':
        return np.array([[1, np.tan(theta)], [0, 1]])
    elif axis == 'y':
        return np.array([[1, 0], [np.tan(theta), 1]])
    else:
        raise ValueError("Axis must be 'x' or 'y'")

def shear(vector, theta, axis):
    theta = np.radians(theta)
    transposed = []
    if axis == 'x':
        R = np.array([[1, np.tan(theta)], [0, 1]])
    elif axis == 'y':
        R = np.array([[1, 0], [np.tan(theta), 1]])
    for i in range(len(vector)):
        transposed.append(np.dot(R, vector[i]))
    return np.array(transposed)

def castom_transformation(vector, matrix):
    transposed = []
    for i in range(len(vector)):
        transposed.append(np.dot(matrix, vector[i]))
    return np.array(transposed)