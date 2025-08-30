"""
What is multiple linear regression?
Multiple regression addresses more complex relationships by including multiple 
independent variables.
"""

"""
ŷ = β₀ + β₁x₁ + β₂x₂ + ⋯ + βₙxₙ + ε

ŷ 	is the predicted value (y-hat)
β₀ 	is the intercept
β₁, β₂, ..., βₙ are the regression coefficients
x₁, x₂, ..., xₙ are the input(independent) variables
"""

"""
Adjusted R² tells you whether adding a variable actually improves the model or not.

R²_adj = 1 - [(1 - R²) × (n - 1) / (n - p - 1)]

R² = regular coefficient of determination
n = number of data points (samples)
p = number of predictors (independent variables)

If a new variable improves the model, adjusted R² goes up
If a new variable is useless, adjusted R² goes down
Adjusted R² ≤ R² (always less than or equal)
It helps prevent overfitting by punishing complexity
"""

"""
What is overfitting in machine learning and how can it be avoided?
Model fits the existing observations too well but fails to predict future new observations.

1. Early stopping of the model’s training in case of validation training stops increasing but 
the training keeps going on.
2. Using regularization methods like L1 or L2 regularization which is used to penalize the 
model's weights to avoid overfitting.
"""

"""
What is underfitting?
1. It doesn't perform well on the training sets and on the testing sets. 
2. It fails to capture the underlying trend of the data.
"""