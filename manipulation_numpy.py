import numpy as np

# Original array
array1 = np.array([1, 3, 5, 7, 9, 11])
print("Original array:\n", array1)

# Reshape the array
array2 = np.reshape(array1, (2, 3))
print("\nReshaped array:\n", array2)

#transposed array
array3 = np.transpose(array2)
print("\nTransposed array:\n", array3)