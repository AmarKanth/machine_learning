"""
Each tree looks at different random parts of the data and their results are combined by 
voting for classification or averaging for regression.
"""

"""
How does Random Forest ensure diversity among the trees in the model?
Random Forest ensures diversity among the trees in its ensemble through two main mechanisms:

Bootstrap Aggregating (Bagging): Each tree in a Random Forest is trained on a different bootstrap 
sample, a random subset of the data. This sampling with replacement means that each tree sees 
different portions of the data, leading to variations in their learning and 
decision-making processes.

Feature Randomness: When splitting a node during the construction of the tree, Random Forest 
randomly selects a subset of features instead of using all available features. 
This variation in the feature set ensures that trees do not follow the same paths or use the 
same splits, thereby increasing the diversity among the trees.
The diversity among trees reduces the variance of the model without significantly 
increasing the bias.
"""