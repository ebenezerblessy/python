#Numpy array to pandas series

import numpy as np
import pandas as pd
arr1 = np.array([10,20,30,40,50])
print("Numpy array: ")
print(arr1)
new_series = pd.Series(arr1)
print("Converted pandas services: ")
print(new_series)