#create and manipulate a DataFrame

import numpy as np
import pandas as pd

dates = pd.date_range(start='2024-07-20', periods=7)

df = pd.DataFrame(np.random.randn(7, 4), index=dates, columns=list('EBIH'))

print(df)
print(df.index)
print(df.to_numpy())
print(df.describe())
print(df.T)
print(df.sort_values("E"))
