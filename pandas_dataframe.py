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

# Display DataFrame info
print("\nDataFrame Info:")
print(df.info())

# Display summary statistics for numerical columns
print("\nSummary Statistics:")
print(df.describe())

# Adding a new column
df['Country'] = ['USA', 'USA', 'USA', 'UK', 'USA', 'USA']
print("\nDataFrame after adding 'Country' column:")
print(df)

# Dropping a column
df_dropped = df.drop('Country', axis=1)
print("\nDataFrame after dropping 'Country' column:")
print(df_dropped)

# Filtering: Get rows where Age is greater than 22
filtered_df = df[df['Age'] > 22]
print("\nRows where Age > 22:")
print(filtered_df)

# Sorting the DataFrame by Age
sorted_df = df.sort_values(by='Age', ascending=False)
print("\nDataFrame sorted by Age (descending):")
print(sorted_df)

# Resetting the index
reset_index_df = df.reset_index(drop=True)
print("\nDataFrame after resetting index:")
print(reset_index_df)

# Grouping: Group by 'City' and count the number of occurrences
grouped_df = df.groupby('City').count()
print("\nGrouped DataFrame by City:")
print(grouped_df)

# Saving the DataFrame to a new CSV file
df.to_csv('output.csv', index=False)
print("\nDataFrame saved to 'output.csv'.")
