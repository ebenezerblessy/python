import numpy as np

# Creating two 2D arrays
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
b = np.array([[3, 3, 3, 3], [7, 7, 7, 7]])


print("a + b:\n", a + b)
print("a - b:\n", a - b)
print("a * b:\n", a * b)
print("a / b:\n", a / b)

# arrays vertically and horizontally
print("Vertical Stack:\n", np.vstack((a, b)))
print("Horizontal Stack:\n", np.hstack((a, b)))

