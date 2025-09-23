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
n 	= number of observations
xᵢ 	= individual data points
x̄ 	= population mean
s 	= population standard deviation

Skewness for sample:
skewness = (n / ((n - 1)(n - 2))) * Σ[((xᵢ - x̄) / s)³]
where:
n 	= number of observations
xᵢ 	= individual data points
x̄ 	= sample mean
s 	= sample standard deviation
"""

"""
Variance:
Variance is a statistical measure that indicates how much the values in a dataset 
deviate from the mean(average).

Variance for a population:    
σ² 	= (1/N)*Σ (xᵢ - μ)²
where:
σ² 	= population variance
xᵢ 	= represents each data point
μ 	= population mean
N 	= total number of data points in the population

Variance for a sample:
s² = (1/(n-1)Σ (xᵢ - x̄)²
where:
s² 	= sample variance
xᵢ 	= represents each data point
x̄ 	= sample mean
n 	= number of data points in the sample
"""

"""
Standard Deviation:

Standard Deviation for population:
σ = √σ²
where:
σ 	= population standard deviation
σ² 	= population variance

Standard Deviation for sample:
s = √s²
where:
s 	= sample standard deviation
s² 	= sample variance
"""

"""
Coefficient Of Variance(Relative Standard Deviation):
The coefficient of variation tells us what percentage of the mean is made up by 
the standard deviation.

Coefficient Of Variance for popultaion
cv = σ / μ
where:
cv 	= Coefficient of Variation(expressed as a percentage)
σ 	= standard deviation
μ 	= mean of the dataset

Coefficient Of Variance for sample
cv = s / x̄
where:
cv 	= sample Coefficient of Variation(expressed as a percentage)
s 	= sample standard deviation
x̄ 	= sample mean
"""

"""
Covariance:
Covariance measures how much two variables vary together from their respective means.

Covariance for population:
σₓᵧ = Σ((xᵢ - μₓ) * (yᵢ - μᵧ)) / n
where:
σₓᵧ 			= population covariance between 'x' and 'y'
xᵢ and yᵢ 	= individual elements of the lists 'x' and 'y'
μₓ 			= mean of the list 'x'
μᵧ 			= mean of the list 'y'
n 			= number of elements in 'x' and 'y'(both must have the same length)

Covariance for sample:
Sₓᵧ = Σ((xᵢ - x̄) * (yᵢ - ȳ)) / (n - 1)
where:
Sₓᵧ 			= covariance between 'x' and 'y'
xᵢ and yᵢ 	= individual elements of the lists 'x' and 'y'
x̄ 			= mean of the list 'x'
ȳ 			= mean of the list 'y'
n 			= number of elements in 'x' and 'y'(both must have the same length)
"""

"""
Correlation Coefficient:
cc = σₓᵧ / (σₓ * σᵧ)
where:
σₓᵧ 	= covariance of X and Y
σₓ 	= standard deviation of X
σᵧ 	= standard deviation of Y
"""
