import pandas as pd

# Create a DataFrame with two columns
data_info = {
    'first': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
    'second': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
}

df = pd.DataFrame(data_info)

# To add a new column 'third'
df['third'] = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print("DataFrame after adding 'third':")
print(df)

# To add a new column 'fourth' by adding 'first' and 'third'
df['fourth'] = df['first'] + df['third']
print("\nDataFrame after adding 'fourth':")
print(df)
