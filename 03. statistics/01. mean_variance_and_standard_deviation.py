"""
1) Find the average of given list
list = [2, 4, 4, 4, 5, 5, 7, 9]
"""
import numpy as np
list = [2, 4, 4, 4, 5, 5, 7, 9]
res = np.average(list)
print(res)

"""
σ² = (1/N) * Σ (xi - μ)²
where:
- N is the number of data points in the population.
- xi is each individual data point.
- μ is the mean (average) of the population.
"""

"""
2) Find the variance of 
list = [2, 4, 4, 4, 5, 5, 7, 9]
"""
import numpy as np

list = [2, 4, 4, 4, 5, 5, 7, 9]
res = np.var(list)
print(res)
