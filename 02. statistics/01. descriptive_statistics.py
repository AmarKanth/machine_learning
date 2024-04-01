"""
Types of data
1. categorical : describes categories or groups
2. numerical : represents numbers, these divided into two subsets 
	discrete : can be counted in finite matter(limit or range)
	continuous : infinte and imposible to count(time)

Representation of categorical data
1. frequency distribution tables
2. bar charts
3. pie charts
4. pareto diagrams
"""

"""
Frequency distribution
"""
import matplotlib.pyplot as plt

categories = ['Audi', 'BMW', 'Mercedes']
frequencies = [124, 98, 113]

plt.bar(categories, frequencies, color='skyblue')
plt.xlabel('Car Brands')
plt.ylabel('Frequency')
plt.title('Frequency Distribution of Car Brands')
plt.show()

"""
Pie chart
"""
import matplotlib.pyplot as plt

categories = ['Audi', 'BMW', 'Mercedes']
frequencies = [124, 98, 113]
total_frequency = sum(frequencies)
relative_frequencies = [freq / total_frequency for freq in frequencies]

plt.figure(figsize=(6, 6))
plt.pie(relative_frequencies, labels=categories, autopct='%1.1f%%', startangle=140)
plt.title('Relative Frequency Distribution of Car Brands')
plt.axis('equal')
plt.show()

"""
Pareto diagram
"""
import matplotlib.pyplot as plt
import numpy as np

categories = ['Audi', 'BMW', 'Mercedes']
frequencies = [124, 98, 113]

sorted_indices = np.argsort(frequencies)[::-1]
sorted_categories = [categories[i] for i in sorted_indices]
sorted_frequencies = [frequencies[i] for i in sorted_indices]

total_frequency = sum(sorted_frequencies)

# cumulative_frequencies = np.cumsum(sorted_frequencies)
# cumulative_percentages = cumulative_frequencies / total_frequency * 100

cumulative_frequencies = [sum(sorted_frequencies[:i+1]) for i in range(len(sorted_frequencies))]
cumulative_percentages = [frequency / total_frequency * 100 for frequency in cumulative_frequencies]

fig, ax1 = plt.subplots()

ax1.bar(sorted_categories, sorted_frequencies, color='b')
ax1.set_xlabel('Car Brands')
ax1.set_ylabel('Frequency', color='b')

ax2 = ax1.twinx()
ax2.plot(sorted_categories, cumulative_percentages, color='r', marker='o')
ax2.set_ylabel('Cumulative Percentage (%)', color='r')
ax2.set_ylim([0, 100])

plt.title('Pareto Diagram for Car Brands')
plt.xticks(rotation=45)
plt.show()

"""
Levels of measurement
1. qualitative :
	nominal : these are like categories, can not be ordered.
	ordinal : consist of groups and categories, which can follow the order.
2. quantitative :
	interval : has true zero
	ratio : has no true zero
"""