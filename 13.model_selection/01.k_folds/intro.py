"""
K-Fold Cross Validation

1.Divide the dataset into K subsets or folds.
2.Use K −1 folds for training the model.
3.Use the remaining fold as the test set to evaluate the model.
"""

"""
What is the bias-variance tradeoff?

Bias(bias refered as accuracy) refers to the difference between the actual values and the 
predicted values by the model.
Low bias means the model has learned the pattern in the data and high bias means 
the model is unable to learn the patterns present in the data i.e the underfitting.

Variance refers to the change in accuracy of the model's prediction on which the model 
has not been trained.
Low variance is a good case but high variance means that the performance of the 
training data and the validation data vary a lot.

If the bias is too low but the variance is too high then that case is known as 
overfitting.

So, finding a balance between these two situations is known as the bias-variance 
trade-off.
"""