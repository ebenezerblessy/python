#Customize the ticks and axis limits in a plot.
import matplotlib.pyplot as plt

# Data
x = [0.1, 0.2, 0.3, 0.4, 0.5]
y = [10, 20, 25, 30, 35]

# Creating a line plot
plt.plot(x, y)

# Customizing ticks
plt.xticks([0.1, 0.2, 0.3, 0.4, 0.5], ['A', 'B', 'C', 'D', 'E'])
plt.yticks([10, 20, 30, 40], ['Low', 'Medium', 'High', 'Very High'])

# Setting axis limits
plt.xlim([0, 0.6])
plt.ylim([5, 40])

# Adding title and labels
plt.title('Customized Ticks and Axes')
plt.xlabel('Custom X-axis')
plt.ylabel('Custom Y-axis')

# Display the plot
plt.show()
