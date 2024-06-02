import cv2 as cv
import numpy as np

def rotateWithCV(vector, degrees = 0):
    rotation_matrix = cv.getRotationMatrix2D((0, 0), degrees, 1.0)
    rotated_object = cv.transform(vector.reshape(-1, 1, 2), rotation_matrix)
    return rotated_object.squeeze()

def mirroring_cv(vector, axis):
    if axis == "x":
        mirroring_matrix = np.float32([
            [1, 0],
            [0, -1]
        ])

    elif axis == "y":
        mirroring_matrix = np.float32([
            [-1, 0],
            [0, 1]
        ])
    else:
        raise ValueError("Axis must be 'x' or 'y'")
    rotated_obj = cv.transform(vector.reshape(-1, 1, 2), mirroring_matrix)
    return rotated_obj.squeeze()

def shear_сv(vector, koef, axis):
    if axis == 'x':
        R = np.float32([
            [1, koef, 0],
            [0, 1, 0]
        ])
    elif axis == 'y':
        R = np.float32([
            [1, 0, 0],
            [koef, 1, 0]
        ])
    sheared_object = cv.transform(vector.reshape(-1, 1, 2), R)
    return sheared_object.squeeze()

def custom_transformation(vector, matrix):
    custom_matrix = np.float32(matrix)
    custom_object = cv.transform(vector.reshape(-1, 1, 2), custom_matrix)
    return custom_object.squeeze()