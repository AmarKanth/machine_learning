"""
ŷ  : y hat
β₀ : beta zero
β₁ : beta one
ε  : epsilon
"""

"""
Linear Regression:
A linear regression is a linear approximation of a causal relationship between two or 
more variables.
"""

"""
Simple Linear Regression:
y = β₀ + β₁X₁ + ε

- y is the variable we are trying to predict and is called dependent variable.
- β₀ is intercept(the value of y when x=0)
- β₁ is coeffiecient(slope)-it tells how much y changes for a one-unit change in X1
- X₁ is input feature, it is independent variable
- ε is error term
"""

"""
What is the difference between correlation and regression?

Correlation:
- Represents the relationship between two variables
- Shows that two variables move together, no matter in which direction
- Symmetrical w.r.t. the two variables: ρ(x,y)=ρ(y,x)
- A single point(a number)

Regression:
- Represents the relationship between two or more variables
- Shows cause and effect(one variable is affected by the other)
- One way – there is always only one variable that is causally dependent
- A line(in 2D space)
"""

"""
What is std err?

SE = sqrt(SSE / (n - k))
where:
- n is number of observations
- k is Number of estimated parameters(including intercept)

- It is measure of prediction accuracy in regression. 
- A lower standard error indicates a better estimate.
"""

"""
Sum of squares total:

SST = Σ(yᵢ - ȳ)²
where:
- yᵢ is observed dependent value
- ȳ is mean of y value

- Measures the total variability of the dependent variable y around its mean
"""

"""
Sum of squares regression:

SSR = Σ(ŷᵢ - ȳ)²
where:
- ŷᵢ is predicted values from the model
- ȳ is mean of actual y values
"""

"""
Sum of squares error:

SSE = Σ(yᵢ - ŷᵢ)²
where:
- yᵢ is actual observed values
- ŷᵢ is predicted values from the model

SST = SSR + SSE
"""

"""
OLS Ordinary Least Squares:
- Least squares stands for the minimum squares error(MSE) or SSE.
- This method aims to find the line which minimizes the sum of the squared errors.
"""

"""
What is the null hypothesis in linear regression problem?
- In linear regression, the null hypothesis is that there is no relationship between the 
  independent variable(s) and the dependent variable.
- H₀ : β₁ = β₂ = ⋯ = βₖ = 0

- The alternative hypothesis, denoted as βⱼ ≠ 0 
- Means that changes in the independent variable are directly effect the changes in the 
  dependent variable, indicating a meaningful relationship.
"""

"""
Coefficient of Determination:
R² = SSR / SST

- It measures how much of the total variability is explained by model
- R² = 0 means your regression line explains none of the variability of the data
- R² = 1 means your model explains the entire variability of data. Unfortunately, regressions 
  explaining the entire variability are rare
- What usually you observe is values ranging from 0.2 to 0.9
- The more factors you include in regression, higher the R²
"""

"""
Mean Square Error(MSE)
MSE = (1/n) * Σ (yᵢ - ŷᵢ)²

- When outliers are present, the error is typically large, and squaring it makes the 
  error values even larger.
- This causes outliers to disproportionately influence the overall error, which can lead to 
  misleading results.
"""

"""
Mean Absolute Error(MAE)
MAE = (1/n) * Σ |yᵢ - ŷᵢ|

- It takes the absolute value of the errors. 
- It does not square the error terms, the influence of large errors(outliers) is 
  linear rather than exponential, making MAE less sensitive to outliers.
"""

"""
Root Mean Squared Error(RMSE)
RMSE = sqrt( (1/n) * Σ (yᵢ - ŷᵢ)² )

- The square root of the residuals variance is the Root Mean Squared Error.
"""