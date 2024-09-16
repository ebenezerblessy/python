import numpy as np

def calculate_variance(data):
    return np.var(data)

data = np.array([[19, 16, 16, 13], [65, 23, 97, 27]])

variance_value = calculate_variance(data)

print("Variance:", variance_value)
