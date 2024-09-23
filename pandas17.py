#Dataframe using concatenated method
import pandas as pd

# Create the first DataFrame
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})

# Create the second DataFrame
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})

# Concatenate df1 and df2
df_concatenated = pd.concat([df1, df2], ignore_index=True)

print("Concatenated DataFrame:")
print(df_concatenated)
