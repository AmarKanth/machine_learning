"""
Logistic Regression :
It predicts the probability of an event occuring (ex spam/not-spam, yes/no, 0/1).

p(X) = e^(β₀ + β₁x₁ + ⋯ + βₖxₖ) / (1 + e^(β₀ + β₁x₁ + ⋯ + βₖxₖ))

- p(X) is the probability that the output is 1 given input X
- β₀ is the intercept (bias)
- β₁, ..., βₖ are the coefficients
- x₁, ..., xₖ are the input features
"""

"""
Logistic Regression Assumptions

1. Linearity 
2. No Endogeneity
3. Normality and Homoscedasticity
4. No Autocorrelation
5. No Multilinearity
"""