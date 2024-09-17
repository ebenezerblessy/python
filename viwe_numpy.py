import numpy as np
arr = np.array([1, 2, 3, 4, 5])

x = arr.view()

arr[1] = 73

print("View of the array (x):", x)
print("Original array (arr):", arr)
