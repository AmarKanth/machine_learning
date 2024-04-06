"""
Levels of measurement
1. qualitative :
	nominal : these are like categories, can not be ordered.
	ordinal : consist of groups and categories, which can follow the order.
2. quantitative :
	interval : has true zero
	ratio : has no true zero
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