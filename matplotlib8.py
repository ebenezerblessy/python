#Create a stacked bar chart to compare parts of a whole.

import matplotlib.pyplot as plt

# Data
categories = ['A', 'B', 'C', 'D']
values1 = [3, 2, 5, 7]
values2 = [2, 3, 6, 8]

# Creating a stacked bar chart
plt.bar(categories, values1, color='blue', label='Category 1')
plt.bar(categories, values2, bottom=values1, color='orange', label='Category 2')

# Adding title and labels
plt.title('Stacked Bar Chart Example')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.legend()

# Display the plot
plt.show()
