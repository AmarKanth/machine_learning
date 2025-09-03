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

"""
36. Why removing highly correlated features are considered a good practice?
When two features are highly correlated, they may provide similar information to the model, which may cause overfitting. If there are highly correlated features in the dataset then they unnecessarily increase the dimensionality of the feature space and sometimes create the problem of the curse of dimensionality. If the dimensionality of the feature space is high then the model training may take more time than expected, it will increase the complexity of the model and chances of error. This somehow also helps us to achieve data compression as the features have been removed without much loss of data.
"""

"""
38. How you would assess the goodness-of-fit for a linear regression model? Which metrics would you consider most important and why?
To evaluate the performance of a linear regression model, important key metrics are: R-squared, Adjusted R-squared, RMSE, and F-Statistics. R-squared is particularly important as it reflects the proportion of variance in the dependent variable that can be explained by the independent variables, providing a measure of how well our model fits the data. However, Adjusted R-squared also plays a crucial role, especially when comparing models with different numbers of predictors. It adjusts for the complexity of the model, helping to prevent overfitting and ensuring the robustness of our findings.

To learn more about regression metrics, check out: Regression Metrics
"""