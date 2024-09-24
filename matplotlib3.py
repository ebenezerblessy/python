#Create a bar chart to compare categories

import matplotlib.pyplot as plt

# Data
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

# Creating a bar chart
plt.bar(categories, values, color='green')

# Adding title and labels
plt.title('Bar Chart Example')
plt.xlabel('Categories')
plt.ylabel('Values')

# Display the plot
plt.show()
