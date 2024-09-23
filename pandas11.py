# Get items of series A that are not available in series B:

import pandas as pd

A = pd.Series([1, 2, 3, 4])
B = pd.Series([3, 4, 5, 6])
result = A[~A.isin(B)]
print(result)
