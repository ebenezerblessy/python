#save and load, read data with numpy

import numpy as np

array17 = np.array([[3, 7, 9], [2, 4, 6]])

np.savetxt(fname='data.txt', X=array17)

loaded_data = np.loadtxt('data.txt')

print(loaded_data)
