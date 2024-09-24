#Add multiple legends to a plot with different data series.

import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4]
y1 = [10, 15, 20, 25]
y2 = [20, 30, 40, 50]

# Creating line plots
line1, = plt.plot(x, y1, label='Series 1', color='blue')
line2, = plt.plot(x, y2, label='Series 2', color='red')

# Adding legends for each line
plt.legend([line1], ['Line 1'], loc='upper left')
plt.legend([line2], ['Line 2'], loc='upper right')

# Adding title and labels
plt.title('Multiple Legends')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Display the plot
plt.show()
