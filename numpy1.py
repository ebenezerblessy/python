#Search Sort
import numpy as np

array13 = np.array([6,7,8,9,7,7])
res10 = np.searchsorted(array13, 7)
print(res10)

#ravel
array14 = np.array([[1, 2, 3], [4, 5, 6], [8, 2, 3]])
print("Flattened array:", array14.ravel())

