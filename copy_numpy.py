import numpy as np
arr1 = np.array([1, 2, 3, 4, 5])

y  = arr1.copy()

arr1[3] = 73

print("View of the array (y):", y)
print("Original array (arr1):", arr1)
