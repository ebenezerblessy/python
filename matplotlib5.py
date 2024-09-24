#Create a histogram to show the distribution of data.

import matplotlib.pyplot as plt

# Data
data = [22, 55, 62, 45, 21, 32, 45, 22, 34, 40, 62, 35, 23, 43, 50, 55, 64, 33]

# Creating a histogram
plt.hist(data, bins=5, color='orange', edgecolor='black')

# Adding title and labels
plt.title('Histogram Example')
plt.xlabel('Value Range')
plt.ylabel('Frequency')

# Display the plot
plt.show()
