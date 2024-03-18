import numpy as np

# Coefficients matrix
A = np.array([[2, 1, -1],
              [3, 4, 2],
              [1, -5, 3]])

# Constants vector
b = np.array([8, 35, 1])

# Solve the system of linear equations
solution = np.linalg.solve(A, b)
print("Solution to the system of linear equations:", solution)
