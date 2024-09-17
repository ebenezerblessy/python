import numpy as np
# 1D array and negative index

arr = np.array([23, 53, 67, 89])

print(arr[3])
print(arr[-4])

# 2D array and indexing
arr1 = np.array([[25, 87, 56, 90, 44], [36, 59, 66, 72, 19]])
print("\n2D Array:")
print(arr1)

print('Second element on first row:', arr1[0, 1])
print('Fifth element on second row:', arr1[1, 4])

# 3D array and indexing
arr2 = np.array([[23,45,87,88],[30,55,97,12],[23,94,38,11]])
print("\n3D Array:")
print(arr2)

print('last element from second dim:', arr1[0, 1])
print('second element from  third dim:', arr1[1, 4])
print('element from second index:', arr1[1,1])