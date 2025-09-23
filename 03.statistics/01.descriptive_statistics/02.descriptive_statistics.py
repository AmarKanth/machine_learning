"""
σ : Sigma(Lower Case)
Σ : Sigma(Capital)
μ : mu
"""

"""
mean:
The mean is the average value of a set of numbers.
"""

"""
median:
The median is the middle value when all the numbers are arranged in ascending order.
"""

"""
mode:
The mode is the value that appears most frequently in the dataset.
"""

"""
Skewness:
- Skewness is a measure of the asymmetry in the distribution of data.
- It tells us whether the data is skewed to the left(negatively skewed), to the 
  right(positively skewed), or is symmetric.

- Symmetric (Zero Skewness) : Mean = Median = Mode
- Positive Skewness (Right-Skewed) : Mean > Median > Mode
- Negative Skewness (Left-Skewed) : Mean < Median < Mode

Skewness for population:
skewness = (1 / n) * Σⁿᵢ₌₁ [ (xᵢ - x̄) / s ]³
where:
- n is the number of observations
- xᵢ is individual data points
- x̄ is population mean
- s is population standard deviation

Skewness for sample:
skewness = (n / ((n - 1)(n - 2))) * Σ[((xᵢ - x̄) / s)³]
where:
- n is number of observations
- xᵢ is individual data points
- x̄ is sample mean
- s is sample standard deviation
"""

"""
Variance:
Variance is a statistical measure that indicates how much the values in a dataset 
deviate from the mean(average).

Variance for a population:    
σ²  = (1/N)*Σ (xᵢ - μ)²
where:
- σ² is population variance
- xᵢ is represents each data point
- μ is population mean
- N is total number of data points in the population

Variance for a sample:
s² = (1/(n-1)Σ (xᵢ - x̄)²
where:
- s² is sample variance
- xᵢ is represents each data point
- x̄ is sample mean
- n is number of data points in the sample
"""

"""
Standard Deviation:

Standard Deviation for population:
σ = √σ²
where:
- σ is population standard deviation
- σ² is population variance

Standard Deviation for sample:
s = √s²
where:
- s is sample standard deviation
- s² is sample variance
"""

"""
Coefficient Of Variance(Relative Standard Deviation):
The coefficient of variation tells us what percentage of the mean is made up by 
the standard deviation.

Coefficient Of Variance for popultaion
cv = σ / μ
where:
- cv is Coefficient of Variation(expressed as a percentage)
- σ is standard deviation
- μ is mean of the dataset

Coefficient Of Variance for sample
cv = s / x̄
where:
- cv is sample Coefficient of Variation(expressed as a percentage)
- s is sample standard deviation
- x̄ is sample mean
"""

"""
Covariance:
Covariance measures how much two variables vary together from their respective means.

Covariance for population:
σₓᵧ = Σ((xᵢ - μₓ) * (yᵢ - μᵧ)) / n
where:
- σₓᵧ is population covariance between 'x' and 'y'
- xᵢ, yᵢ is individual elements of the lists 'x' and 'y'
- μₓ is mean of the list 'x'
- μᵧ is mean of the list 'y'
- n is number of elements in 'x' and 'y' (both must have the same length)

Covariance for sample:
Sₓᵧ = Σ((xᵢ - x̄) * (yᵢ - ȳ)) / (n - 1)
where:
- Sₓᵧ is covariance between 'x' and 'y'
- xᵢ, yᵢ is individual elements of the lists 'x' and 'y'
- x̄ is mean of the list 'x'
- ȳ is mean of the list 'y'
- n is number of elements in 'x' and 'y'(both must have the same length)
"""

"""
Correlation Coefficient:
cc = σₓᵧ / (σₓ * σᵧ)
where:
- σₓᵧ is covariance of X and Y
- σₓ is standard deviation of X
- σᵧ is standard deviation of Y
"""
