#"Comparing Memory Usage of Python Range vs. NumPy Array"

import numpy as np
import sys

s = range(1000)
print("Size of range object:", sys.getsizeof(6) * len(s))

D = np.arange(1000)
print("Size of NumPy array:", D.size * D.itemsize)
