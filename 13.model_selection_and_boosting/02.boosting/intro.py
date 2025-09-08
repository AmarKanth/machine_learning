"""
Explain the working procedure of the XGBoost model?
XGBoost model is an ensemble technique of machine learning in this method weights are 
optimized in a sequential manner by passing them to the decision trees. After each pass, 
the weights become better and better as each tree tries to optimize the weights, and finally, 
we obtain the best weights for the problem at hand. Techniques like regularized gradient 
and mini-batch gradient descent have been used to implement this algorithm so, that it 
works in a very fast and optimized manner.
"""

"""
Explain the working procedure of the XGBoost model?
XGBoost model is an ensemble technique of machine learning in this method weights 
are optimized in a sequential manner by passing them to the decision trees. 

After each pass, the weights become better and better as each tree tries to optimize 
the weights, and finally, we obtain the best weights for the problem at hand. 

Techniques like regularized gradient and mini-batch gradient descent have been used 
to implement this algorithm so, that it works in a very fast and optimized manner.
"""

"""
What is the significance of tree pruning in XGBoost? How does it affect the model?
Tree pruning in XGBoost is used to reduce model complexity and prevent overfitting. 
XGBoost implements a "pruning-as-you-grow" strategy where it starts by growing a full 
tree up to a maximum depth, then prunes back the branches that contribute minimal gains 
in terms of loss reduction. This is guided by the gamma parameter, which sets a 
minimum loss reduction required to make further partitions on a leaf node.

Effect on the Model:
Reduces Overfitting: By trimming unnecessary branches, pruning helps in creating simpler 
models that generalize better to unseen data, reducing the likelihood of overfitting.

Improves Performance: Pruning helps in removing splits that have little impact, which can 
enhance the model's performance by focusing on more significant attributes.

Optimizes Computational Efficiency: It decreases the complexity of the final model, which can 
lead to faster training and prediction times as there are fewer nodes to traverse 
during decision making.
"""