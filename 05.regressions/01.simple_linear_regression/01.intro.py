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

y  : It is the variable we are trying to predict and is called dependent variable.
β₀ : Intercept(the value of y when x=0)
β₁ : Coeffiecient(slope)-it tells how much y changes for a one-unit change in X1
X₁ : Input feature, it is independent variable
ε  : Error term
"""

"""
What is the difference between correlation and regression?

Correlation :
1. Represents the relationship between two variables
2. Shows that two variables move together (no matter in which direction)
3. Symmetrical w.r.t. the two variables: ρ(x,y)=ρ(y,x)
4. A single point(a number)

Regression :
1. Represents the relationship between two or more variables
2. Shows cause and effect(one variable is affected by the other)
3. One way – there is always only one variable that is causally dependent
4. A line(in 2D space)
"""

"""
What is std err?

SE = sqrt(SSE / (n - k))
n : Number of observations
k : Number of estimated parameters (including intercept)

-It is measure of prediction accuracy in regression. 
-The lower the standard error, the better the estimate.
"""

"""
Sum of squares total:

SST = Σ(yᵢ - ȳ)²
yᵢ = observed dependent value
ȳ  = mean of y value

-Measures the total variability of the dependent variable y around its mean
"""

"""
Sum of squares regression:

SSR = Σ(ŷᵢ - ȳ)²
ŷᵢ = predicted values from the model
ȳ  = mean of actual y values
"""

"""
Sum of squares error:

SSE = Σ(yᵢ - ŷᵢ)²
yᵢ = actual observed values
ŷᵢ = predicted values from the model

SST = SSR + SSE
"""

"""
OLS Ordinary Least Squares:

-Least squares stands for the minimum squares error or SSE.
-This method aims to find the line which minimizes the sum of the squared errors.
"""

"""
What is the null hypothesis in linear regression problem?
In linear regression, the null hypothesis is that there is no relationship between the 
independent variable(s) and the dependent variable.
H₀ : β₁ = β₂ = ⋯ = βₖ = 0

The alternative hypothesis, denoted as βⱼ ≠ 0, means that changes in the independent 
variable are directly effect the changes in the dependent variable, indicating a meaningful 
relationship.
"""

"""
Coefficient of Determination:

R² = SSR / SST

-It measures how much of the total variability is explained by model
-R² = 0 means your regression line explains none of the variability of the data
-R² = 1 means your model explains the entire variability of data. Unfortunately, regressions 
 explaining the entire variability are rare
-What usually you observe is values ranging from 0.2 to 0.9
-The more factors you include in regression, higher the R²
"""

"""
Mean Square Error(MSE)

MSE = (1/n) * Σ (y_actualᵢ - y_predictedᵢ)²

-When there are outliers, the error is typically large, and squaring it results in 
 even larger error values.
-This causes outliers to disproportionately affect the overall error, leading to 
 misleading results and potentially distorting the model’s performance.
"""

"""
Mean Absolute Error(MAE)

MAE = (1/n) * Σ |y_actualᵢ - y_predictedᵢ|

-It takes the absolute value of the errors. 
-It does not square the error terms, the influence of large errors(outliers) is 
 linear rather than exponential, making MAE less sensitive to outliers.
"""

"""
Root Mean Squared Error(RMSE)

RMSE = sqrt( (1/n) * Σ (y_actualᵢ - y_predictedᵢ)² )

-The square root of the residuals variance is the Root Mean Squared Error.
"""