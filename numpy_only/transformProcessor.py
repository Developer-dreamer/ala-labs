import numpy as np

def rotate(vector, degrees = 0, axis = "none"):
    transposed = []
    if axis == "x":
        R = np.array([[1, 0], [0, -1]])
    elif axis == "y":
        R = np.array([[-1, 0], [0, 1]])
    else:
        theta = np.radians(degrees)
        c, s = np.cos(theta), np.sin(theta)
        R = np.array([[c, -s], [s, c]])
    for i in range(len(vector)):
        transposed.append(np.dot(R, vector[i]))
    return np.array(transposed)

def rotate_3d(vector, degrees = 0, axis = "none"):
    transposed = []
    theta = np.radians(degrees)
    if axis == "x":
        R = np.array([[1, 0, 0],
                      [0, np.cos(theta), -np.sin(theta)],
                      [0, np.sin(theta), np.cos(theta)]])
    elif axis == "y":
        R = np.array([[np.cos(theta), 0, np.sin(theta)],
                      [0, 1, 0],
                      [-np.sin(theta), 0, np.cos(theta)]])
    elif axis == "z":
        R = np.array([[np.cos(theta), -np.sin(theta), 0],
                      [np.sin(theta), np.cos(theta), 0],
                      [0, 0, 1]])
    else:
        raise ValueError("Axis must be 'x', 'y', or 'z'")
    for i in range(len(vector)):
        transposed.append(np.dot(R, vector[i]))
    return np.array(transposed)

def scale(scalar, vector):
    return scalar * vector

def shear(vector, koef, axis):
    transposed = []
    if axis == 'x':
        R = np.array([[1, koef], [0, 1]])
    elif axis == 'y':
        R = np.array([[1, 0], [koef, 1]])
    for i in range(len(vector)):
        transposed.append(np.dot(R, vector[i]))
    return np.array(transposed)

def custom_transformation(vector, matrix):
    transposed = []
    for i in range(len(vector)):
        transposed.append(np.dot(matrix, vector[i]))
    return np.array(transposed)