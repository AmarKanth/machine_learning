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
Regression models are one of the most common ways to make inference and predictions.
"""

"""
Simple Linear Regression:
y = β₀ + β₁X₁ + ε

y  : It is the variable we are trying to predict and is called dependent variable.
β₀ : Intercept(the value of y when x=0)
β₁ : Coeffiecient(slope)
X₁ : Input feature, it is independent variable
ε  : Error term
"""

"""
What is the difference between correlation and regression?

Correlation :
1. Represents the relationship between two variables
2. Shows that two variables move together (no matter in which direction)
3. Symmetrical w.r.t. the two variables: ρ(x,y)=ρ(y,x)
4. A single point (a number)

Regression :
1. Represents the relationship between two or more variables
2. Shows cause and effect (one variable is affected by the other)
3. One way – there is always only one variable that is causally dependent
4. A line (in 2D space)
"""

"""
What is std err?
Shows the accuracy of prediction for each variable. 
The lower the standard error, the better the estimate.
"""

"""
Sum of squares total:
Measures the total variability of the dependent variable y around its mean
SST = Σ(yᵢ - ȳ)²
yᵢ = observed dependent value
ȳ  = mean of y value
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
Least squares stands for the minimum squares error or SSE.
This method aims to find the line which minimizes the sum of the squared errors.
"""

"""
Coefficient of Determination:
R² = SSR / SST

It measures how much of the total variability is explained by model
R² = 0 means your regression line explains none of the variability of the data
R² = 1 means your model explains the entire variability of data

Unfortunately, regressions explaining the entire variability are rare.
What usually you observe is values ranging from 0.2 to 0.9.
The more factors you include in regression, higher the R².
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