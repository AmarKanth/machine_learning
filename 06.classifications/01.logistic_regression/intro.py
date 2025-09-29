"""
Logistic Regression:
- It predicts the probability of an event occuring (ex spam/not-spam, yes/no, 0/1).
- The main reason why we cannot use linear regression for a classification task is that the 
  output of linear regression is continuous, while classification requires discrete 
  output values.
"""

"""
Logistic(sigmoid) function:
z = b₁·x₁ + b₂·x₂ + ... + bₖ·xₖ + a

f(z) = 1 / (1 + e^(−z))
f(z) = e^(z)/(1+e^(z))

P(y = 1) = f(z)
P(y = 0) = 1 − f(z)
"""

"""
MLE(Maximum likelihood estimation):
- It is a method used to estimate the model’s parameters (the coefficients).
- It produces Standard errors, Log-likelihood values, Pseudo R-Squared as well
"""

"""
LLR(Log likelihood Ratio):
LLR = −2×(LLnull−LLmodel)
- The log-likelihood tells us how well the model explains the data.
- The null model(LL-null) is the model with only the intercept(no predictors).
- The full model(LL) is your fitted logistic regression with predictors.

Interpretation
LLR p-value: This is the probability of seeing such an improvement in log-likelihood 
if the null model were true.

A small p-value(< 0.05) means your predictors significantly improve the model 
compared to the null.
"""

"""
odds:
odds = P(event) / (1 - P(event))
- The odds of an event represent the ratio of the probability that the event occurs to the 
  probability that it does not occur.
"""

"""
odds-ratio:
oddsratio = odds(Group A) / odds(Group B)
- The odds ratio (OR) compares the odds of an event occurring in one group to the odds of 
  it occurring in another group.
Interpretation:
- OR = 1 → No difference in odds between groups.
- OR > 1 → Event is more likely in Group A.
- OR < 1 → Event is more likely in Group B.
"""

"""
Pseudo R²:
1 - (LL_model / LL_null)
Interpretation
- Values closer to 1 indicate a better fit.
- Typical values for real-world logistic regression are between 0.2 and 0.4.
- Much higher values may indicate a very strong predictor or possible overfitting.
"""

"""
                        Actual Positive   Actual Negative
Predicted Positive      TP(True Pos)      FP(False Pos)
Predicted Negative      FN(False Neg)     TN(True Neg)
"""

"""
Accuracy:
(TP + TN) / (TP + TN + FP + FN)
- The overall proportion of correct predictions.
- There are times when we train our model on an imbalanced dataset the accuracy score is 
  not a good metric to measure the performance of the model. In such cases, we use precision and 
  recall to measure the performance of a classification model.
"""

"""
Precision:
TP / (TP + FP)
- When the model predicts positive, how often is it correct?
- Precision is the ratio between the true positives(TP) and all the positive examples 
  (TP+FP) predicted by the model. 
- In other words, precision measures how many of the predicted positive examples are actually 
  true positives. 
- It is a measure of the model's ability to avoid false positives and make accurate positive 
  predictions.
- However, if you are more concerned about false positives or false negatives specifically, 
  you may opt for:Precision(if false positives are more costly) or Recall(if false negatives are 
  more costly).
"""

"""
Recall:
TP / (TP + FN)
- Out of all the actual positive cases, how many did the model find?
- In recall, we calculate the ratio of true positives (TP) and the total number of examples 
  (TP+FN) that actually fall in the positive class. 
- Recall measures how many of the actual positive examples are correctly identified by the model. 
- It is a measure of the model's ability to avoid false negatives and identify all positive 
  examples correctly.
"""

"""
F1 Score:
2 * (Precision * Recall) / (Precision + Recall)
- The F1-Score is the harmonic mean of Precision and Recall
- High F1-score indicates a good balance between precision and recall.
- Useful when both false positives and false negatives are important.
- Also, f1-score is another metric that can be used to measure performance but in the end, 
  f1-score is also calculated using precision and recall as the f1-score is nothing but 
  the harmonic mean of the precision and recall.
- We can use Precision, Recall, F1 score and ROC-AUC to evaluate the effectiveness of 
  machine learning model in imbalanced dataset scenario. 
- The best metric is F1 score as it combines both precision and recall into single metric that is 
  important in imbalanced datasets where a high number of true negatives can skew accuracy. 
- By focusing on both false positives and false negatives, the F1-score ensures that both the positive 
  class detection and false positives are accounted for.
- If the cost of false positives(Type I errors) and false negatives(Type II errors) is similar, 
  F1-Score strikes a good balance.
- It is especially useful when you need to prioritize performance in detecting the minority 
  class(positive class).
"""

"""
Macro Average: 
- Compute the metric(Precision, Recall, F1-score) for each class individually.
"""

"""
Weighted Average:
wp = Σ (Precision_i × Support_i) / Σ (Support_i)
where:
- Precision_i is Precision score for class i
- Support_i is Number of true instances of class i
- C is Total number of classes

- Compute the metric(Precision, Recall, F1) for each class individually.
"""