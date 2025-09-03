"""
11. What are some of the hyperparameters of the random forest regressor which help to avoid overfitting?
The most important hyperparameters of a Random Forest are:

max_depth: Sometimes the larger depth of the tree can create overfitting. To overcome it, the depth should be limited.
n-estimator: It is the number of decision trees we want in our forest.
min_sample_split: It is the minimum number of samples an internal node must hold in order to split into further nodes.
max_leaf_nodes: It helps the model to control the splitting of the nodes and in turn, the depth of the model is also restricted.
"""
