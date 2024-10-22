"""
1) Population And Sample
------------------------
Population : Population is enitre set of individuals, objects, events, or data points that you 
are interested in studying.
Sample : A sample is a subset of the population that is selected for the actual study.
"""

"""
2) Randomness And Representativeness
------------------------------------
Randomness: Selecting samples in a random manner.
Representativeness: Ensuring the sample includes a balanced mix of the population 
(not specific to one type of individual or event).
"""

"""
3) Types of data
----------------
1. categorical : describes categories or groups
2. numerical : represents numbers, these divided into two subsets 
	discrete : can be counted in finite matter(limit or range)
	continuous : infinte and imposible to count(time)

Representation of categorical data
1. bar charts
2. pie charts
3. pareto diagrams
4. Cross Table
"""

"""
4) Bar Chart
------------
"""
categories = ['Audi', 'BMW', 'Mercedes']
frequencies = [124, 98, 113]

"""
5) Pie Chart
------------
"""
categories = ['Audi', 'BMW', 'Mercedes']
frequencies = [124, 98, 113]
total_frequency = sum(frequencies)
relative_frequencies = [freq / total_frequency for freq in frequencies]

"""
6) Pareto diagram
-----------------
X axis represents the brands
Y1 axis represents the comulative frequencies
Y2 axis represents the comulative percentages
Poligonal Line represents (Audi), (Audi, Mercedes), (Audi, Mercedes, BMW) comulative share in toatl sales. 
"""
categories = ['Audi', 'BMW', 'Mercedes']
frequencies = [124, 98, 113]

sorted_indices = sorted(range(len(frequencies)), key=lambda i: frequencies[i], reverse=True)
sorted_categories = [categories[i] for i in sorted_indices]
sorted_frequencies = [frequencies[i] for i in sorted_indices]
total_frequency = sum(sorted_frequencies)

cumulative_frequencies = [sum(sorted_frequencies[:i+1]) for i in range(len(sorted_frequencies))]
cumulative_percentages = [frequency / total_frequency * 100 for frequency in cumulative_frequencies]

"""
7) Cross Table
--------------

       Investor  Invest A  Invest B  Invest C  Total
0        Stocks      96.0     185.0      39.0  320.0
1         Bonds     181.0       3.0      29.0  213.0
2   Real Estate      88.0     152.0     142.0  382.0
3        Total      365.0     340.0     210.0  915.0
"""
import pandas as pd

data = {
    'Invest A': {'Stocks': 96, 'Bonds': 181, 'Real Estate': 88},
    'Invest B': {'Stocks': 185, 'Bonds': 3, 'Real Estate': 152},
    'Invest C': {'Stocks': 39, 'Bonds': 29, 'Real Estate': 142}
}
df = pd.DataFrame(data)
df['Total'] = df.sum(axis=1)
df.loc['Total'] = df.sum()
df = df.reset_index().rename(columns={'index': 'Type Of investment'})
print(df)

"""
8) Levels of measurement
------------------------
1. qualitative :
	nominal : these are like categories, can not be ordered.
	ordinal : oridinal looks same as nominal but categories have order
 		  (Ex: High School, Bachelor's, Master's, Doctorate)
2. quantitative :
	interval : Interval data does not have a true zero point(Ex: temperature 0°C does not mean "no temperature")
	ratio : Ratio data has a true zero point(Ex: income of $0 indicates no income.)
"""

"""
9) Histogram
------------
"""
import math

data_set = [1, 9, 22, 24, 32, 41, 44, 48, 57, 66, 70, 73, 75, 76, 79, 82, 87, 89, 95, 100]
desired_intervals = 5
max_value = max(data_set)
min_value = min(data_set)

range_val = (min_value + max_value)/desired_intervals
intervals = [[] for _ in range(desired_intervals)]
interval_boundaries = [(min_value + i * range_value, min_value + (i + 1) * range_value - 1) for i in range(desired_intervals)]

for j in data_set:
    idx = math.floor((j - min_value) // range_val)
    intervals[idx].append(j)

interval_frequency = [0] * desired_intervals

for idx, interval in enumerate(intervals):
    interval_frequency[idx] = len(interval)

total_frequency = len(data_set)
relative_frequency = [freq / total_frequency for freq in interval_frequency]

print(intervals)
print(interval_frequency)
print(relative_frequency)

"""
10) Scatter Plot
----------------
"""

"""
11) Mean, Median and Mode
-------------------------
Mean : The mean is the average value of a set of numbers.
Median : The median is the middle value when all the numbers are arranged in ascending order.
Mode : The mode is the value that appears most frequently in the dataset.
"""

"""
12) Skewness
------------
Skewness is a measure of the asymmetry in the distribution of data.
It tells us whether the data is skewed to the left (negatively skewed), to the right (positively skewed), 
or is symmetric.

Symmetric (Zero Skewness) : Mean = Median = Mode.
Positive Skewness (Right-Skewed) : Mean > Median > Mode.
Negative Skewness (Left-Skewed) : Mean < Median < Mode.
"""

"""
13) Variance
------------
Variance : Variance is a statistical measure that tells us how many values in a dataset vary from the mean (average).

Variance for a population:    
σ² = Σ (xᵢ - μ)² / N

where:
- σ² is the population variance,
- xᵢ represents each data point,
- μ is the population mean,
- N is the total number of data points in the population.

Variance for a sample:
s² = Σ (xᵢ - x̄)² / (n - 1)

where:
- s² is the sample variance,
- xᵢ represents each data point,
- x̄ is the sample mean,
- n is the number of data points in the sample.
"""

"""
14) Standard Deviation 
----------------------
Standard Deviation for population:
σ = √σ²

Where:
- σ is the standard deviation.
- σ² is the variance.

Standard Deviation for sample:
s = √s²

Where:
- s is the sample standard deviation.
- s² is the sample variance.
"""

"""
15) Coefficient Of Variance(Relative Standard Deviation)
--------------------------------------------------------

Coefficient Of Variance for popultaion
CV = σ / μ

Where:
- CV is the Coefficient of Variation (expressed as a percentage).
- σ is the standard deviation.
- μ is the mean of the dataset.


Coefficient Of Variance for sample
CV = s / x̄

Where:
- CV is the sample Coefficient of Variation (expressed as a percentage).
- s is the sample standard deviation.
- x̄ is the sample mean.
"""

"""
16) Covariance
--------------
Covariance for population:
σₓᵧ = Σ((xᵢ - μₓ) * (yᵢ - μᵧ)) / n

where:
- σₓᵧ is the population covariance between `x` and `y`
- xᵢ and yᵢ are the individual elements of the lists `x` and `y`
- μₓ is the mean of the list `x`
- μᵧ is the mean of the list `y`
- n is the number of elements in `x` and `y` (both must have the same length)

Covariance for sample:
Sₓᵧ = Σ((xᵢ - x̄) * (yᵢ - ȳ)) / (n - 1)

where:
- Sₓᵧ is the covariance between `x` and `y`
- xᵢ and yᵢ are the individual elements of the lists `x` and `y`
- x̄ is the mean of the list `x`
- ȳ is the mean of the list `y`
- n is the number of elements in `x` and `y` (both must have the same length)
"""

"""
17) Correlation Coefficient
---------------------------
"""
