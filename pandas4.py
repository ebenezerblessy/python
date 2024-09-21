#Merging

import pandas as pd

df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Ebi', 'blessy', 'angel'],
    'Age': [23, 24, 35]
})

df2 = pd.DataFrame({
    'ID': [1, 2, 4],
    'City': ['New York', 'Los Angeles', 'Chicago'],
    'Salary': [70000, 80000, 75000]
})

merged_df = pd.merge(df1, df2, on='ID')
print(merged_df)
