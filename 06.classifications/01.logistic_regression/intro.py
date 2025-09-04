"""
Logistic Regression:
It predicts the probability of an event occuring (ex spam/not-spam, yes/no, 0/1).
"""

"""
Logistic(sigmoid) function:
ŷ = b₁·x₁ + b₂·x₂ + ... + bₖ·xₖ + a

f(z) = 1 / (1 + e^(−z))
f(z) = e^(z)/(1+e^(z))
z = b₁·x₁ + b₂·x₂ + ... + bₖ·xₖ + a

P(y = 1) = f(z)
P(y = 0) = 1 − f(z)
"""

"""
MLE(Maximum likelihood estimation)
1. It is a method used to estimate the model’s parameters (the coefficients).
2. It produces Standard errors, Log-likelihood values, Pseudo R-Squared as well
"""

"""
LLR(Log likelihood Ratio)
The log-likelihood tells us how well the model explains the data.

The null model(LL-null) is the model with only the intercept (no predictors).
The full model(LL) is your fitted logistic regression with predictors.

LLR = −2×(LLnull−LLmodel)

Interpretation
LLR p-value: This is the probability of seeing such an improvement in log-likelihood 
if the null model were true.

A small p-value(< 0.05) means your predictors significantly improve the model 
compared to the null.
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
1 - (LL_model / LL_null)

Interpretation
- Values closer to 1 indicate a better fit.
- Typical values for real-world logistic regression are between 0.2 and 0.4.
- Much higher values may indicate a very strong predictor or possible overfitting.
"""

"""
Why we cannot use linear regression for a classification task?
The main reason why we cannot use linear regression for a classification task is that the 
output of linear regression is continuous, while classification requires discrete 
output values.
"""

"""
Explain the classification report and the metrics it includes?

Precision: When the model predicts positive, how often is it correct?
Precision = TP / (TP + FP)

Recall: Out of all the actual positive cases, how many did the model find?
Recall = TP / (TP + FN)

F1-Score: The F1-Score is the harmonic mean of Precision and Recall
F1 = 2 * (Precision * Recall) / (Precision + Recall)
- High F1-score indicates a good balance between precision and recall.
- Useful when both false positives and false negatives are important.

Support: The number of true instances for each class in the dataset.

Accuracy: The overall proportion of correct predictions.
Accuracy = (TP + TN) / (TP + TN + FP + FN)

Macro Average: Compute the metric (Precision, Recall, F1-score) for each class individually.

Weighted Average: Compute the metric (Precision, Recall, F1) for each class individually.
Weighted Precision = Σ (Precision_i × Support_i) / Σ (Support_i)
- Precision_i : Precision score for class i
- Support_i   : Number of true instances of class i
- C           : Total number of classes
"""

"""
Does the accuracy score always a good metric to measure the performance of a 
classification model?
No, there are times when we train our model on an imbalanced dataset the accuracy score is 
not a good metric to measure the performance of the model. 

In such cases, we use precision and recall to measure the performance of a 
classification model.

Also, f1-score is another metric that can be used to measure performance but in the end, 
f1-score is also calculated using precision and recall as the f1-score is nothing but 
the harmonic mean of the precision and recall.
"""