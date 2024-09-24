#Create a simple pie chart

import matplotlib.pyplot as plt

# Data
labels = ['Python', 'Java', 'C++', 'Php']
sizes = [40, 30, 20, 10]

# Creating a pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

# Adding title
plt.title('Programming Language Usage')

# Display the plot
plt.show()
