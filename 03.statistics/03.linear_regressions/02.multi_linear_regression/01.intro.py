"""
Multiple regressions, address the higher complexity of problems. The more variables 
you have more factors you are considering in a model.
"""

"""
ŷ = β₀ + β₁x₁ + β₂x₂ + ⋯ + βₙxₙ + ε

ŷ 	is the predicted value (y-hat)
β₀ 	is the intercept
β₁, β₂, ..., βₙ are the regression coefficients
x₁, x₂, ..., xₙ are the input (independent) variables
"""

"""
Adjusted R² penalizes unnecessary complexity and tells you whether adding a variable 
actually improves the model.

R²_adj = 1 - [(1 - R²) × (n - 1) / (n - p - 1)]

R² = regular coefficient of determination
n = number of data points (samples)
p = number of predictors (independent variables)

If a new variable improves the model, adjusted R² goes up
If a new variable is useless, adjusted R² goes down
Adjusted R² ≤ R² (always less than or equal)
"""