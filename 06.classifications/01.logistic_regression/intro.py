"""
Logistic Regression:
- It predicts the probability of an event occuring(ex spam/not-spam, yes/no, 0/1).
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
MLE(Maximum Likelihood Estimation) Method:
- It is a method used to estimate the model's parameters(the coefficients)
- It produces standard errors, log-likelihood values, pseudo r-squared as well
"""

"""
LLR(Log Likelihood Ratio) Test:
LLR = −2×(LLnull−LLmodel)
- The log-likelihood tells us how well the model explains the data
- The null model(LL-null) is the model with only the intercept(no predictors)
- The full model(LL-model) is fitted logistic regression that includes the predictors

- Null Hypothesis : null model is correct. Adding the predictors does not improve the fit.
  β₁ = β₂ = ⋯ = βₖ = 0
- Alternative Hypothesis: full model fits significantly better than the null model.
  β₁,β₂,βₖ != 0
- LLR p-value = 0 then we reject the null hypothesis.
- LLR p-value > 0.05 then we failed to reject the null hypothesis.
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
- OR = 1 → No difference in odds between groups.
- OR > 1 → Event is more likely in Group A.
- OR < 1 → Event is more likely in Group B.
"""

"""
Pseudo R²:
1 - (LL_model / LL_null)
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
- The percentage of total predictions that the model got correct.
- There are times when we train our model on an imbalanced dataset the accuracy score is 
  not a good metric to measure the performance of the model. 
- In such cases, we use precision and recall to measure the performance of a classification 
  model.
"""

"""
Precision:
TP / (TP + FP)
- Precision is the ratio between the true positives(TP) and all the positive examples 
  (TP+FP) predicted by the model.
- However, if you are more concerned about false positives or false negatives specifically, 
  you may opt for:Precision(if false positives are more costly) or Recall(if false negatives are 
  more costly).
"""

"""
Recall:
TP / (TP + FN)
- In recall, we calculate the ratio of true positives(TP) and the total number of examples 
  (TP+FN) that actually fall in the positive class.
"""

"""
F1 Score:
2 * (Precision * Recall) / (Precision + Recall)
- The F1-Score is the harmonic mean of Precision and Recall
- High F1-score indicates a good balance between precision and recall.
- Useful when both false positives and false negatives are important.
- We can use Precision, Recall, F1 score and ROC-AUC to evaluate the effectiveness of 
  machine learning model in imbalanced dataset scenario.
"""

"""
Macro Average:
ma = (1 / 𝐶) × ∑ᶦ⁼¹ ᶜ Precisionᵢ
where:
C = total number of classes
Precisionᵢ = precision for class i

- Compute the metric(Precision, Recall, F1-score) for each class individually.
- Take the unweighted mean across all classes.
- Every class contributes equally, regardless of how many samples it has.
"""

"""
Weighted Average:
wp = ( Σᶦ⁼¹ ᶜ (Precisionᵢ × Supportᵢ) ) / ( Σᶦ⁼¹ ᶜ Supportᵢ )

where:
- Precisionᵢ is Precision score for class i
- Supportᵢ is number of true instances of class i
- C is total number of classes

- Compute the metric(Precision, Recall, F1) for each class individually.
- Take the support-weighted mean across classes.
- Classes with more samples (higher support) have more influence.
"""