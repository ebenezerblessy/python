'''Comparison of List Comprehension vs. NumPy Arrays
  Timing List Comprehension with Zip
  Speed Test: Creating Tuples from Ranges'''

import numpy as np
import time
import sys

SIZE = int(input("Enter a size"))
l1 = range(SIZE)
l2 = range(SIZE)
A1 = np.arange(SIZE)
A2 = np.arange(SIZE)

start = time.time()
result = [(x, y) for x, y in zip(l1, l2)]
print("Time taken for list comprehension (ms):", (time.time() - start) * 1000)
