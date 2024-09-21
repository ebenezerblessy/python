#Pandas programs to arithmetic operations

import pandas as pd
ds1 = pd.Series([2,4,6,8,10])
ds2 = pd.Series([1,3,5,7,9])
print("Add two Series: ")
ds = ds1+ds2
print(ds)

print("Subtract two series: ")
ds = ds1-ds2
print(ds)

print("Multiply two series: ")
ds = ds1*ds2
print(ds)

print("Divide two series: ")
ds = ds1/ds2
print(ds)