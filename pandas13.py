#Delete rows by index

import pandas as pd

# Sample DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# Delete the row with index 1
df = df.drop(index=1)
print(df)

#delete multiple rows
# Delete rows with indices 0 and 2
df = df.drop(index=[0, 2])
print(df)

# Delete column 'B'
df = df.drop(columns=['B'])
print(df)

# Delete rows where values in column 'A' are less than 3
df = df[df['A'] >= 3]
print(df)
