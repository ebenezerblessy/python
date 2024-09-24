#Use fill_between to shade the area between two curves.

import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Creating line plots and filling between
plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)')
plt.fill_between(x, y1, y2, color='gray', alpha=0.3)

# Adding title and labels
plt.title('Fill Between Curves')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

# Display the plot
plt.show()
