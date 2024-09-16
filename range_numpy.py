import numpy as np

def calculate_range(data):
    return np.max(data) - np.min(data)

data = np.array([[19, 18, 16, 13], [65, 23, 97, 27]])

range_value = calculate_range(data)
max_value = np.max(data)
min_value = np.min(data)

print("Range:", range_value)
print("max:", max_value)
print("min:", min_value)