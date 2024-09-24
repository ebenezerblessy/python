#Create a figure with multiple subplots to show different plots side by side
import matplotlib.pyplot as plt

# Data
x = [0, 1, 2, 3, 4]
y1 = [0, 1, 4, 9, 16]
y2 = [0, -1, -4, -9, -16]

# Creating subplots
plt.figure(figsize=(10,5))

# First subplot
plt.subplot(1, 2, 1)
plt.plot(x, y1, 'b--')
plt.title('y = x^2')

# Second subplot
plt.subplot(1, 2, 2)
plt.plot(x, y2, 'r-.')
plt.title('y = -x^2')

# Display the plots
plt.tight_layout()  # Automatically adjust layout
plt.show()
