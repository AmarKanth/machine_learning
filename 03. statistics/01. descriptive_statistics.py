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
1. bar charts
2. pie charts
3. pareto diagrams
"""

"""
Bar Chart
"""
categories = ['Audi', 'BMW', 'Mercedes']
frequencies = [124, 98, 113]

"""
Pie Chart
"""
categories = ['Audi', 'BMW', 'Mercedes']
frequencies = [124, 98, 113]
total_frequency = sum(frequencies)
relative_frequencies = [freq / total_frequency for freq in frequencies]

"""
Pareto diagram
X axis represents the brands
Y1 axis represents the frequencies
Y2 axis represents the comulative frequencies
Poligonal Line represents (Audi), (Audi, Mercedes), (Audi, Mercedes, BMW) comulative share in toatl sales. 
"""
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
import math

data_set = [1, 9, 22, 24, 32, 41, 44, 48, 57, 66, 70, 73, 75, 76, 79, 82, 87, 89, 95, 100]
desired_intervals = 5
max_value = max(data_set)
min_value = min(data_set)

range_val = (min_value + max_value)/desired_intervals
intervals = [[] for _ in range(desired_intervals)]

for j in data_set:
    idx = math.floor((j - min_value) / range_val)
    intervals[idx].append(j)

interval_frequency = [0] * desired_intervals

for idx, interval in enumerate(intervals):
    interval_frequency[idx] = len(interval)

total_frequency = len(data_set)
relative_frequency = [freq / total_frequency for freq in interval_frequency]

print(intervals)
print(interval_frequency)
print(relative_frequency)
