"""
1) Mean, Median and Mode
-------------------------
Mean : The mean is the average value of a set of numbers.
Median : The median is the middle value when all the numbers are arranged in ascending order.
Mode : The mode is the value that appears most frequently in the dataset.
"""

"""
2) Skewness
------------
Skewness is a measure of the asymmetry in the distribution of data.
It tells us whether the data is skewed to the left (negatively skewed), to the right (positively skewed), 
or is symmetric.

Symmetric (Zero Skewness) : Mean = Median = Mode.
Positive Skewness (Right-Skewed) : Mean > Median > Mode.
Negative Skewness (Left-Skewed) : Mean < Median < Mode.
"""

"""
3) Variance
------------
Variance : Variance is a statistical measure that tells us how much values in a dataset vary 
from the mean (average).

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
4) Standard Deviation 
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
5) Coefficient Of Variance(Relative Standard Deviation)
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
6) Covariance
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
7) Correlation Coefficient
---------------------------
σₓᵧ / (σₓ * σᵧ)

Where:
- σₓᵧ is the covariance of X and Y.
- σₓ is the standard deviation of X.
- σᵧ is the standard deviation of Y.
"""
