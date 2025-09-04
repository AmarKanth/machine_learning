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

"""
Why we cannot use linear regression for a classification task?
The main reason why we cannot use linear regression for a classification task is that the 
output of linear regression is continuous and unbounded, while classification requires 
discrete and bounded output values. 

If we use linear regression for the classification task the error function graph will not 
be convex. A convex graph has only one minimum which is also known as the global minima 
but in the case of the non-convex graph, there are chances of our model getting stuck at 
some local minima which may not be the global minima. To avoid this situation of getting 
stuck at the local minima we do not use the linear regression algorithm for a 
classification task.
"""

"""
Explain the classification report and the metrics it includes?
The classification report provides key metrics to evaluate a model’s performance, including:

Precision: The proportion of true positives to all predicted positives, measuring accuracy of positive predictions.
Recall: The proportion of true positives to all actual positives, indicating how well the model finds positive instances.
F1-Score: The harmonic mean of precision and recall, balancing the two metrics.
Support: The number of true instances for each class in the dataset.
Accuracy: The overall proportion of correct predictions.
Macro Average: The average of precision, recall, and F1-score across all classes, treating them equally.
Weighted Average: The average of metrics, weighted by class support, giving more importance to frequent classes.
"""

"""
Does the accuracy score always a good metric to measure the performance of a 
classification model?
No, there are times when we train our model on an imbalanced dataset the accuracy score is 
not a good metric to measure the performance of the model. In such cases, we use precision 
and recall to measure the performance of a classification model.

Also, f1-score is another metric that can be used to measure performance but in the end, 
f1-score is also calculated using precision and recall as the f1-score is nothing but 
the harmonic mean of the precision and recall.
"""
