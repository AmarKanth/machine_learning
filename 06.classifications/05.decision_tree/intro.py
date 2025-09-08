"""
What is a decision tree?
A decision tree maps out decisions and their outcomes. Starts with a root node and branches 
out into decisions.
"""

"""
Gini Impurity: 
-It measures the impurity rate of the class distribution of data points.
-Features(fields) only come into play when we test how well a feature split reduces 
 the impurity.

Gini = 1 - Σ(f_k^2)
-f_k is the fraction(proportion) of samples in class k
-Lower gini = purer node
"""

"""
Information Gain (IG):
---------------------
Information Gain tells us how useful a question (or feature) is for splitting data into 
groups. A good question will create clearer groups and and the feature with the highest 
Information Gain.

Entropy: This measures the amount of uncertainty or disorder in the data. The tree tries 
to reduce the entropy by splitting the data on features that provide the most information 
about the target variable.

Formula:
IG(S, A) = Entropy(S) - Σ_{v ∈ Values(A)} [ (|S_v| / |S|) * Entropy(S_v) ]

S   : The dataset
A   : The feature (attribute) being evaluated
S_v : The subset of S where feature A = v

Interpretation:
If entropy decreases a lot after a split, the feature provides high information gain.
"""

"""
Whether decision tree or random forest is more robust to the outliers.
Decision trees and random forests are both relatively robust to outliers. A random 
forest model is an ensemble of multiple decision trees so, the output of a random forest 
model is an aggregate of multiple decision trees.

So, when we average the results the chances of overfitting get reduced. Hence we can say 
that the random forest models are more robust to outliers.
"""