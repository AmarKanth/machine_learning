"""
Logistic Regression :
It predicts the probability of an event occuring (ex spam/not-spam, yes/no, 0/1).

ŷ = b₁·x₁ + b₂·x₂ + ... + bₖ·xₖ + a
f(z) = 1 / (1 + e^(−z))
f(z) = 1 / (1 + e^(−(b₁·x₁ + b₂·x₂ + ... + bₖ·xₖ + a)))

P(y = 1) = 1 / (1 + e^(−Z))
P(y = 0) = 1 − 1 / (1 + e^(−Z))
"""

"""
Logistic Regression Assumptions

1. Linearity 
2. No Endogeneity
3. Normality and Homoscedasticity
4. No Autocorrelation
5. No Multilinearity
"""

"""
MLE (Maximum likelihood estimation)
A function which estimates how likely it is that the model at hand 
describes the real underlying relationship of the variables.
The bigger the likelihood function, the higher the probability 
that our model is correct.
"""

"""
LLR (Log likelihood Ratio)
measures if our model is statistically different from LL-null, 
a.k.a a useless model
"""

"""
odds:
The odds of an event represent the ratio of the probability that the event occurs to the 
probability that it does not occur.

odds = P(event) / (1 - P(event))

odds-ratio:
The odds ratio (OR) compares the odds of an event occurring in one group to the odds of 
it occurring in another group.

oddsratio = odds(Group A) / odds(Group B)

Interpretation:
- OR = 1 → No difference in odds between groups.
- OR > 1 → Event is more likely in Group A.
- OR < 1 → Event is more likely in Group B.
"""

"""
Pseudo R-Squared
"""