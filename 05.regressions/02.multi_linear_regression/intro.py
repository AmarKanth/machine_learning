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

"""
What is overfitting in machine learning and how can it be avoided?
Overfitting happens when the model learns patterns as well as the noises present in the 
data this leads to high performance on the training data but very low performance for data 
that the model has not seen earlier.

To avoid overfitting there are multiple methods that we can use:

Early stopping of the model’s training in case of validation training stops increasing but the 
training keeps going on.

Using regularization methods like L1 or L2 regularization which is used to penalize the model's 
weights to avoid overfitting.
"""

"""
Is it always necessary to use an 80:20 ratio for the train test split?
No, there is no such necessary condition that the data must be split into 80:20 ratio. 
The main purpose of the splitting is to have some data which the model has not seen previously so, 
that we can evaluate the performance of the model.

If the dataset contains let’s say 50,000 rows of data then only 1000 or maybe 2000 rows of 
data is enough to evaluate the model’s performance.
"""

"""
What is the purpose of splitting a given dataset into training and validation data?
The main purpose is to keep some data left over on which the model has not been trained so, 
that we can evaluate the performance of our machine learning model after training.

Also, sometimes we use the validation dataset to choose among the multiple state-of-the-art 
machine learning models. 

Like we first train some models let’s say LogisticRegression, XGBoost, 
or any other than test their performance using validation data and choose the model which has 
less difference between the validation and the training accuracy.
"""