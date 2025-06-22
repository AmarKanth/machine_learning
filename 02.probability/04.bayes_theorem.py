"""
Bayes Theorem : 
It is enables us to calculate the probability of a hypothesis being true given observed evidence.
P(A∣B) = (P(B∣A) × P(A))​ / P(B)

Mathematical Formulation :
To derive Bayes’s Theorem, we start with the definition of conditional probability:
P(A∣B)=P(A∩B)/P(B)
P(B∣A)=P(A∩B)/P(A)

Rearranging the second equation to express P(A∩B):
P(A∩B)=P(B∣A)*P(A)

Substitute this into the first equation:
P(A∣B)=P(B∣A)*P(A)/P(B)​
"""

"""
1) A disease affects 1% of the population. A test is 95% accurate for both positive and negative results. 
If a person tests positive, what’s the probability they have the disease?
"""
from fractions import Fraction

# Given data
prevalence = 0.01  # 1% of the population has the disease
sensitivity = 0.95  # True positive rate
specificity = 0.95  # True negative rate

# Calculating the probability of a positive test result
# P(Positive Test) = P(Positive Test | Disease) * P(Disease) + P(Positive Test | No Disease) * P(No Disease)
p_positive_given_disease = sensitivity
p_positive_given_no_disease = 1 - specificity

p_disease = prevalence
p_no_disease = 1 - p_disease

p_positive_test = (p_positive_given_disease * p_disease) + (p_positive_given_no_disease * p_no_disease)

# Applying Bayes' Theorem to find P(Disease | Positive Test)
# P(Disease | Positive Test) = (P(Positive Test | Disease) * P(Disease)) / P(Positive Test)
p_disease_given_positive = (p_positive_given_disease * p_disease) / p_positive_test

# Output the result
print(f"The probability of having the disease given a positive test result is: {p_disease_given_positive:.4f}")
