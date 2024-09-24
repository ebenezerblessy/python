#Plot multiple mathematical functions (e.g., sine, cosine, tangent) on the same graph
import matplotlib.pyplot as plt
import numpy as np

# Data: x values from 0 to 2*pi
x = np.linspace(0, 2 * np.pi, 100)

# Plotting mathematical functions
plt.plot(x, np.sin(x), label='sin(x)')
plt.plot(x, np.cos(x), label='cos(x)')
plt.plot(x, np.tan(x), label='tan(x)', color='red')

# Limiting the y-axis for tangent to avoid infinite values
plt.ylim(-5, 5)

# Adding title, labels, and legend
plt.title('Sine, Cosine, and Tangent Functions')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

# Display the plot
plt.show()
