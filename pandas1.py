import pandas as pd

# Create a DataFrame
data = {
    'Name': ['ebi', 'blessy', 'ebin', 'angel', 'Eva', 'ancy'],
    'Age': [20, 21, 22, 23, 24, 25],
    'City': ['New York', 'Los Angeles', 'Chicago', 'London', 'USA', 'Philadelphia']
}
df = pd.DataFrame(data)

# Display the first 5 rows of the DataFrame
print("First 5 rows:")
print(df.head())

# Display the first 3 rows of the DataFrame
print("\nFirst 3 rows:")
print(df.head(3))

# Display the 'Name' column
print("\nName column:")
print(df['Name'])

# Access the first row using .loc
print("\nFirst row using loc:")
print(df.loc[0])

# Access the first row using .iloc (by position)
print("\nFirst row using iloc:")
print(df.iloc[0])

# Filtering: Get all rows where Age is greater than 22
print("\nRows where Age > 22:")
print(df[df['Age'] > 22])

# Adding a new column
df['Country'] = ['USA', 'USA', 'USA', 'UK', 'USA', 'USA']
print("\nDataFrame after adding 'Country' column:")
print(df)

# Dropping a column
df_dropped = df.drop('Country', axis=1)
print("\nDataFrame after dropping 'Country' column:")
print(df_dropped)

df.to_csv('output.csv', index=False)
print("\nDataFrame saved to 'output.csv'.")
