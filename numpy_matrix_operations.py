# Program: NumPy Matrix Operations
# This program creates a 5x5 matrix with random integers
# and calculates row-wise sum, column-wise sum,
# transpose, and determinant

import numpy as np

# Create a 5x5 matrix with random integers (1 to 10)
matrix = np.random.randint(1, 11, (5, 5))

# Display original matrix
print("Original Matrix:\n", matrix)

# Row-wise sum
row_sum = np.sum(matrix, axis=1)

# Column-wise sum
col_sum = np.sum(matrix, axis=0)

# Transpose of matrix
transpose_matrix = np.transpose(matrix)

# Determinant of matrix
determinant = np.linalg.det(matrix)

# Display results
print("\nRow-wise Sum:", row_sum)
print("Column-wise Sum:", col_sum)
print("\nTranspose of Matrix:\n", transpose_matrix)
print("\nDeterminant of Matrix:", round(determinant, 2))
'''output:
'''
