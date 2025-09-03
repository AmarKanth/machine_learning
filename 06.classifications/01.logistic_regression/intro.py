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

"""
Is it always necessary to use an 80:20 ratio for the train test split?

No, there is no such necessary condition that the data must be split into 80:20 ratio. 
The main purpose of the splitting is to have some data which the model has not seen 
previously so, that we can evaluate the performance of the model.

If the dataset contains let’s say 50,000 rows of data then only 1000 or maybe 2000 rows 
of data is enough to evaluate the model’s performance.
"""

"""
5. Why we cannot use linear regression for a classification task?
The main reason why we cannot use linear regression for a classification task is that the output of linear regression is continuous and unbounded, while classification requires discrete and bounded output values. 

If we use linear regression for the classification task the error function graph will not be convex. A convex graph has only one minimum which is also known as the global minima but in the case of the non-convex graph, there are chances of our model getting stuck at some local minima which may not be the global minima. To avoid this situation of getting stuck at the local minima we do not use the linear regression algorithm for a classification task.
"""

"""
10. Explain the classification report and the metrics it includes.
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
26. Does the accuracy score always a good metric to measure the performance of a classification model?
No, there are times when we train our model on an imbalanced dataset the accuracy score is not a good metric to measure the performance of the model. In such cases, we use precision and recall to measure the performance of a classification model.

Also, f1-score is another metric that can be used to measure performance but in the end, f1-score is also calculated using precision and recall as the f1-score is nothing but the harmonic mean of the precision and recall.
"""

"""
29. What is the purpose of splitting a given dataset into training and validation data?
The main purpose is to keep some data left over on which the model has not been trained so, that we can evaluate the performance of our machine learning model after training. Also, sometimes we use the validation dataset to choose among the multiple state-of-the-art machine learning models. Like we first train some models let’s say LogisticRegression, XGBoost, or any other than test their performance using validation data and choose the model which has less difference between the validation and the training accuracy.
"""

"""
30. Explain some methods to handle missing values in that data.
Some of the methods to handle missing values are as follows:

Removing the rows with null values may lead to the loss of some important information.
Removing the column having null values if it has very less valuable information. it may lead to the loss of some important information.
Imputing null values with descriptive statistical measures like mean, mode, and median.
Using methods like KNN Imputer to impute the null values in a more sophisticated way.
"""
