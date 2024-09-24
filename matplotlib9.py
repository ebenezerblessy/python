#Add a grid and annotations to a plot.

import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]

# Creating a plot
plt.plot(x, y, marker='o', color='green')

# Adding grid
plt.grid(True)

# Annotating specific points
plt.annotate('Highest Point', xy=(5, 35), xytext=(3, 30),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Adding title and labels
plt.title('Line Plot with Annotations and Grid')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Display the plot
plt.show()
