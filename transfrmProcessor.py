import numpy as np

def rotate(degrees, vector):
    theta = np.radians(degrees)
    c, s = np.cos(theta), np.sin(theta)
    R = np.array([[c, -s], [s, c]])
    return np.dot(R, vector)

def scale(scalar, vector):
    return scalar * vector