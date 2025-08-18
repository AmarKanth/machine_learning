"""
What is a decision tree?
A decision tree maps out decisions and their outcomes. Starts with a root node and branches 
out into decisions.
"""

"""
Splitting criteria in decision tree

Gini Index :
----------
Gini Impurity: This criterion measures how "impure" a node is. The lower the Gini Impurity 
the better the feature splits the data into distinct categories.

Formula:
Gini(S) = 1 - Σ_{i=1}^C (p_i^2)
C   : Number of classes
p_i : Probability of class i in dataset S

Interpretation:
Lower Gini = purer node

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