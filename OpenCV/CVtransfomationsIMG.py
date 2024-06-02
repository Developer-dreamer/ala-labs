import cv2
import numpy as np

# Load the image
img = cv2.imread('../autism.jpg', 0)
rows, cols = img.shape[:2]

# Define the transformation matrices
rotation_matrix = cv2.getRotationMatrix2D((cols/2,rows/2),100,1)
scaling_matrix = np.float32([[2, 0, 0], [0, 2, 0]])
mirroring_matrix = np.float32([[-1, 0, cols], [0, 1, 0]])
shearing_matrix = np.float32([[1, 0.5, 0], [0, 1, 0]])
custom_matrix = np.float32([[0.4, 0, 0], [0, 2, 0]])  # Replace with your custom matrix

# Apply the transformations
rotated_img = cv2.warpAffine(img, rotation_matrix, (cols, rows))
scaled_img = cv2.warpAffine(img, scaling_matrix, (cols, rows))
mirrored_img = cv2.warpAffine(img, mirroring_matrix, (cols, rows))
sheared_img = cv2.warpAffine(img, shearing_matrix, (cols, rows))
custom_img = cv2.warpAffine(img, custom_matrix, (cols, rows))

# Display the original and transformed images
cv2.imshow('Original Image', img)
cv2.imshow('Rotated Image', rotated_img)
cv2.imshow('Scaled Image', scaled_img)
cv2.imshow('Mirrored Image', mirrored_img)
cv2.imshow('Sheared Image', sheared_img)
cv2.imshow('Custom Transformed Image', custom_img)

cv2.waitKey(0)
cv2.destroyAllWindows()