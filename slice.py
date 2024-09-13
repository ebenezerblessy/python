my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get the first three items
slice1 = my_list[:3]
print(slice1)  # Output: [1, 2, 3]

# Get the last three items
slice2 = my_list[-3:]
print(slice2)  # Output: [8, 9, 10]

# Get every other item starting from the second item
slice3 = my_list[1::2]
print(slice3)  # Output: [2, 4, 6, 8, 10]

# Reverse the list
slice4 = my_list[::-1]
print(slice4)  # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]