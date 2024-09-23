#DataFrame using joined method

import pandas as pd

# Create the first DataFrame with custom index
df1 = pd.DataFrame({'A': [1, 2]}, index=['a', 'b'])

# Create the second DataFrame with the same index
df2 = pd.DataFrame({'B': [3, 4]}, index=['a', 'b'])

# Join df2 to df1
df_joined = df1.join(df2)

print("Joined DataFrame:")
print(df_joined)
