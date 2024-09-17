import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])

print("Array addition (a + b):")
print(a + b)
print("Array subtraction (a - b):")
print(a - b)
print("Array multiplication (a * b):")
print(a * b)
print("Array division (a / b):")
print(a / b)
print("Vertical stacking (np.vstack((a, b))):")
print(np.vstack((a, b)))
print("Horizontal stacking (np.hstack((a, b))):")
print(np.hstack((a, b)))
