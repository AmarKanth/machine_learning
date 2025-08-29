"""
It tries to find the best boundary known as hyperplane that separates different classes in 
the data. 
It is useful when you want to do binary classification like spam vs. not spam or cat vs. dog.
"""

"""
Hyperplane : 
The hyperplane is halfway between these boundaries(support vectors).
Boundaries are closest data points from each class.
"""

"""
Margin : 
The distance between the hyperplane and the support vectors.
"""

"""
How can you conclude about the model's performance using the confusion matrix?

Confusion matrix summarizes the performance of a classification model. In a confusion matrix, 
we get four types of output (in case of a binary classification problem) which are TP, TN, FP, 
and FN. As we know that there are two diagonals possible in a square, and one of these two 
diagonals represents the numbers for which our model's prediction and the true labels are 
the same. Our target is also to maximize the values along these diagonals. From the 
confusion matrix, we can calculate various evaluation metrics like accuracy, precision, 
recall, F1 score, etc.
"""