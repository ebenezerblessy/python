import numpy as np

array1 = np.array(['iphone:', 'price:'])
array2 = np.array(['16', '$700'])

result = np.char.add(array1, array2)

print(result)
