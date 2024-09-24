#Create a line plot with multiple lines, different colors, and line styles

import matplotlib.pyplot as plt

# Data
x = [0, 1, 2, 3, 4]
y1 = [0, 1, 4, 9, 16]
y2 = [0, 1, 2, 3, 4]

# Plotting two lines with different styles and colors
plt.plot(x, y1, label='y = x^2', color='blue', linestyle='--')
plt.plot(x, y2, label='y = x', color='red', linestyle='-')

# Adding title, labels, and legend
plt.title('Line Plot with Two Functions')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

# Display the plot
plt.show()
