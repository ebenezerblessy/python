# Filter

import numpy as np
array15 = np.array([41, 42, 43, 44, 45])
res11 = [True, True, False, False, True]
new_arr = array15[res11]
print("Filtered array:", new_arr)