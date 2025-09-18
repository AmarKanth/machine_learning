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
n  = number of data points (samples)
p  = number of predictors (independent variables)

-If a new variable improves the model, adjusted R² goes up
-If a new variable is useless, adjusted R² goes down
-Adjusted R² ≤ R² (always less than or equal)
-It helps prevent overfitting by punishing complexity
"""

"""
Overfitting

-Model fits the existing observations too well but fails to predict future new observations.
-Early stopping of the model’s training in case of validation training stops increasing but 
 the training keeps going on.
"""

"""
Underfitting

-It doesn't perform well on the training sets and on the testing sets. 
-It fails to capture the underlying trend of the data.
"""

"""
train and test split

-The main purpose is to keep some data left over on which the model has not been trained so, 
 that we can evaluate the performance of our machine learning model after training.
"""