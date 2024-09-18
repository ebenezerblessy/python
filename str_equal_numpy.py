import numpy as np

array8 = np.array(['C', 'Python', 'Numpy', 'c sharp'])
array9 = np.array(['C++', 'Python', 'numpy', 'c#'])

res6 = np.char.equal(array8, array9)

print(res6)
