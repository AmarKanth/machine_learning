"""
Population : Population is enitre set of individuals, objects, events, or data points that you 
are interested in studying.

Sample : A sample is a subset of the population that is selected for the actual study.
"""

"""
Randomness: Selecting samples in a random manner.

Representativeness: Ensuring the sample includes a balanced mix of the population 
(not specific to one type of individual or event).
"""

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
	ordinal : oridinal looks same as nominal but categories have order
 		  (Ex: High School, Bachelor's, Master's, Doctorate)
2. quantitative :
	interval : Interval data does not have a true zero point(Ex: temperature 0°C does not mean "no temperature")
	ratio : Ratio data has a true zero point(Ex: income of $0 indicates no income.)
"""

"""
Histogram
"""
import matplotlib.pyplot as plt
import numpy as np

data_set = [1, 9, 22, 24, 32, 41, 44, 48, 57, 66, 70, 73, 75, 76, 79, 82, 87, 89, 95, 100]
frequency = [1]*20
desired_intervals = 5
max_num = max(data_set)
min_num = min(data_set)
interval_width = max_num - min_num / desired_intervals
intervals = np.linspace(min_num, max_num, num=desired_intervals+1)
interval_bounds = [(intervals[i], intervals[i+1]) for i in range(len(intervals)-1)]

interval_frequency = [0] * desired_intervals

for data_point in data_set:
    for i, (lower_bound, upper_bound) in enumerate(interval_bounds):
        if lower_bound <= data_point <= upper_bound:
            interval_frequency[i] += 1
            break

plt.bar(range(len(interval_frequency)), interval_frequency, align='center')
plt.xlabel('Intervals')
plt.ylabel('Frequency')
plt.title('Histogram Table')
plt.xticks(range(len(interval_frequency)), [f'{int(lower)}-{int(upper)}' for lower, upper in interval_bounds])
plt.show()

total_frequency = sum(frequency)
relative_frequency = [freq/total_frequency for freq in interval_frequency]

fig, ax = plt.subplots()
ax.bar(range(len(interval_frequency)), relative_frequency, align='center')
ax.set_xlabel('Intervals')
ax.set_ylabel('Relative Frequency')
ax.set_title('Histogram Table with Intervals and Relative Frequency')
ax.set_xticks(range(len(interval_frequency)))
ax.set_xticklabels([f'{int(lower)}-{int(upper)}' for lower, upper in interval_bounds])
plt.show()
