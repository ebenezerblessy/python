#Create a scatter plot with random points.

import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 5, 7, 6, 8, 10, 9, 12, 11]

# Creating a scatter plot
plt.scatter(x, y, color='purple')

# Adding title and labels
plt.title('Simple Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Display the plot
plt.show()
