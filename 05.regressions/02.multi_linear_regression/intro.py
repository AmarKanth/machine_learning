"""
What is multiple linear regression?
It addresses more complex relationships by including multiple independent variables.
"""

"""
ŷ = β₀ + β₁x₁ + β₂x₂ + ⋯ + βₙxₙ + ε

- ŷ is the predicted value (y-hat)
- β₀ is the intercept
- β₁, β₂, ..., βₙ are the regression coefficients
- x₁, x₂, ..., xₙ are the input(independent) variables
"""

"""
Adjusted R²:

adj_r² = 1 - [(1 - R²) × (n - 1) / (n - p - 1)]
where:
- r² is regular coefficient of determination
- n is number of data points(samples)
- p is number of predictors(independent variables)

- It tells you whether adding a variable actually improves the model or not.
- If a new variable improves the model, adjusted R² goes up
- If a new variable is useless, adjusted R² goes down
- Adj_R² ≤ R² (always less than or equal)
- It helps prevent overfitting by punishing complexity
"""

"""
Overfitting

- Model performs well during training but fails to predict new observations.
- Early stopping of the model's training in case of validation training stops increasing but 
  the training keeps going on.
"""

"""
Underfitting

- It doesn't perform well on the training and on the testing. 
- It fails to capture the underlying trend of the data.
"""

"""
train and test split

- The main purpose of keep some data left over is to evalute the model performance 
  after training.
"""