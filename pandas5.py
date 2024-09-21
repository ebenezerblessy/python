# Compare the elements of the two Series

import pandas as pd
ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 9])

print("Series1: ")
print(ds1)

print("Series2: ")
print(ds2)

print("Compare the elements of the said series: ")

print("Equals: ")
print(ds1 == ds2)

print("Greater than: ")
print(ds1 > ds2)

print("Less than: ")
print(ds1 < ds2)
