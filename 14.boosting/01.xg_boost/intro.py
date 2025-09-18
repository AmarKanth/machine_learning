"""
XGBoost:
It builds decision trees sequentially with each tree attempting to correct the mistakes 
made by the previous one.

The process can be broken down as follows:

Start with a base learner: 
The first model decision tree is trained on the data. 
In regression tasks this base model simply predicts the average of the target variable.

Calculate the errors: 
After training the first tree the errors between the predicted and actual values are 
calculated.

Train the next tree: 
The next tree is trained on the errors of the previous tree. 
This step attempts to correct the errors made by the first tree.

Repeat the process: 
This process continues with each new tree trying to correct the errors of the previous 
trees until a stopping criterion is met.

Combine the predictions:
The final prediction is the sum of the predictions from all the trees.
"""


"""
ŷ = Tree₁(x) + η*Tree₂(x) + η*Tree₃(x) + ... + η*Treeₙ(x)

ŷ 		 : Final prediction
Treeᵢ(x) : The i-th decision tree's prediction
η 		 : Learning rate(a small constant, e.g., 0.1)
"""


"""
What is the significance of tree pruning in XGBoost? How does it affect the model?

Tree pruning in XGBoost is used to reduce model complexity and prevent overfitting. 
XGBoost implements a "pruning-as-you-grow" strategy where it starts by growing a full 
tree up to a maximum depth, then prunes back the branches that contribute minimal gains 
in terms of loss reduction. 
This is guided by the gamma parameter, which sets a minimum loss reduction required to make 
further partitions on a leaf node.

Effect on the Model:
Reduces Overfitting: By trimming unnecessary branches, pruning helps in creating simpler 
models that generalize better to unseen data, reducing the likelihood of overfitting.

Improves Performance: 
Pruning helps in removing splits that have little impact, which can enhance the 
model's performance by focusing on more significant attributes.

Optimizes Computational Efficiency: 
It decreases the complexity of the final model, which can lead to faster training and 
prediction times as there are fewer nodes to traverse during decision making.
"""