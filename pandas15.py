import pandas as pd

# Original DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data, index=['a', 'b', 'c'])

# Reindexing
new_index = ['c', 'b', 'd']  # 'd' is a new index
reindexed_df = df.reindex(new_index)
