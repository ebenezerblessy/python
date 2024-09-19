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

# Series example: Create a Series from the 'Name' column
name_series = df['Name']
print("\nName Series:")
print(name_series)

# Series functions
print("\nSeries Functions:")
print("Index of Series:")
print(name_series.index)  # Get the index of the Series

print("\nValues of Series:")
print(name_series.values)  # Get the values of the Series

print("\nLength of Series:")
print(len(name_series))  # Get the length of the Series

print("\nFirst 3 elements of Series:")
print(name_series.head(3))  # Get the first 3 elements

print("\nElement at index 1:")
print(name_series[1])  # Access the element at index 1

print("\nCheck if 'angel' is in the Series:")
print('angel' in name_series.values)  # Check for a value

print("\nConvert Series to list:")
print(name_series.tolist())  # Convert Series to a list

# Display the 'Age' column as a Series
age_series = df['Age']
print("\nAge Series:")
print(age_series)

# Perform operations on the Age Series
print("\nAge + 5:")
print(age_series + 5)  # Add 5 to each element

print("\nAge greater than 22:")
print(age_series[age_series > 22])  # Filter values greater than 22


df.to_csv('output.csv', index=False)
print("\nDataFrame saved to 'output.csv'.")
