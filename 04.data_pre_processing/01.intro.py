"""
What is feature scaling?
It involves transforming numerical features to a "standard" scale, often leading to better 
model performance.

Methods for Feature Scaling
1. Min-Max Scaling
2. Standardization
3. Robust Scaling
"""

"""
Min-Max Scaling:
It is also called normalization.
x' = (x - x_min) / (x_max - x_min)

To achieve stable and fast training of the model we use normalization techniques to bring 
all the features to a certain scale or range of values.
"""
from sklearn.preprocessing import MinMaxScaler
min_max_scaler = MinMaxScaler()
X_minmax = min_max_scaler.fit_transform(X)

"""
Standardization:
x' = (x - μ) / σ
μ : Mean of the feature
σ : Standard deviation of the feature

It indicates how many standard deviations a data point is from the mean of the dataset.
"""
from sklearn.preprocessing import StandardScaler
std_scaler = StandardScaler()
X_std = std_scaler.fit_transform(X)

"""
Robust Scaling:
(X − Q₁(X)) / (Q₃(X) − Q₁(X))
Q₁(X) = first quartile  
Q₃(X) = third quartile
"""
from sklearn.preprocessing import RobustScaler
robust_scaler = RobustScaler()
X_robust = robust_scaler.fit_transform(X)

"""
How do you handle missing values in a dataset using Scikit-Learn?

SimpleImputer offers several strategies

1. Mean, Median, Most Frequent: Fills in with the mean, median, or mode of the non-missing 
values in the column.
2. Constant: Assigns a fixed value to all missing entries.
3. KNN: Uses the k-Nearest Neighbors algorithm to determine an appropriate value based on other 
instances' known feature values.
"""
from sklearn.impute import SimpleImputer
import numpy as np

X = np.array([[1, 2], [np.nan, 3], [7, 6]])
imp_mean = SimpleImputer()
X_mean = imp_mean.fit_transform(X)
print(X_mean)

"""
How do you encode categorical variables using Scikit-Learn?
1. OneHotEncoder
2. OrdinalEncoder
3. LabelBinarizer
"""

"""
OneHotEncoder: 
Creates Binary columns representing each category to avoid assuming any ordinal 
relationship. Ideal for non-binary categories.
"""
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

data = pd.DataFrame({'Color': ['Red', 'Green', 'Blue', 'Green', 'Red']})
encoder = OneHotEncoder()
encoded_data = encoder.fit_transform(data[['Color']])
columns = encoder.get_feature_names_out(['Color'])
encoded_df = pd.DataFrame(encoded_data.toarray(), columns=columns)
print(encoded_df)

"""
OrdinalEncoder: 
For ordinal categories, assigns a range of numbers to each category. Works 
well when certain categories have an inherent order.
"""

"""
LabelBinarizer: 
A simpler version of OneHotEncoder designed for binary (two-class) categories.
"""

"""
Describe the use of ColumnTransformer in Scikit-Learn
"""
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import Normalizer, StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), ['numerical_feature_1', 'numerical_feature_2']),
        ('num2',Normalizer(),['numerical_feature_3']),
        ('cat', OneHotEncoder(), ['categorical_feature_1', 'categorical_feature_2']),
        ('drop_col', 'drop', ['column_to_drop']),
        ('fill_unk', SimpleImputer(strategy='constant', fill_value='Unknown'), ['categorical_feature_with_nan']),
        ('default', 'passthrough', ['remaining_col_1'])
    ]
)

transformed_data = preprocessor.fit_transform(data)

"""
Feature engineering 
Polynomial features 
Power transformations 
Binning 
Name two feature engineering approaches.
"""

"""
What is feature engineering? How does it affect the model’s performance? 
Feature engineering refers to developing some new features by using existing features. 
Sometimes there is a very subtle mathematical relation between some features which if 
explored properly then the new features can be developed using those mathematical 
operations.

Also, there are times when multiple pieces of information are clubbed and provided 
as a single data column. At those times developing new features and using them help us to 
gain deeper insights into the data as well as if the features derived are significant 
enough helps to improve the model’s performance a lot.
"""

"""
Why do we perform normalization?
To achieve stable and fast training of the model we use normalization techniques to bring 
all the features to a certain scale or range of values. If we do not perform 
normalization then there are chances that the gradient will not converge to the 
global or local minima and end up oscillating back and forth.
"""

"""
What is the difference between precision and recall?
Precision is the ratio between the true positives(TP) and all the positive examples 
(TP+FP) predicted by the model. In other words, precision measures how many of the 
predicted positive examples are actually true positives. It is a measure of the model's 
ability to avoid false positives and make accurate positive predictions.

Precision = TP / (TP + FP)

In recall, we calculate the ratio of true positives (TP) and the total number of examples 
(TP+FN) that actually fall in the positive class. Recall measures how many of the actual 
positive examples are correctly identified by the model. It is a measure of the model's 
ability to avoid false negatives and identify all positive examples correctly.

Recall = TP / (TP + FN)
"""

"""
What is the difference between upsampling and downsampling?
In upsampling method, we increase the number of samples in the minority class by 
randomly selecting some points from the minority class and adding them to the dataset 
repeat this process till the dataset gets balanced for each class. But, here is a 
disadvantage the training accuracy becomes high as in each epoch model trained more 
than once in each epoch but the same high accuracy is not observed in the validation 
accuracy. 

In downsampling, we decrease the number of samples in the majority class by selecting 
some random number of points that are equal to the number of data points in the minority 
class so that the distribution becomes balanced. In this case, we have to suffer from data 
loss which may lead to the loss of some critical information as well. 
"""

"""
What is data leakage and how can we identify it?
If there is a high correlation between the target variable and the input features 
then this situation is referred to as data leakage. This is because when we train our 
model with that highly correlated feature then the model gets most of the target 
variable's information in the training process only and it has to do very little to achieve 
high accuracy. In this situation, the model gives pretty decent performance both on the 
training as well as the validation data but as we use that model to make actual 
predictions then the model’s performance is not up to the mark. This is how we can 
identify data leakage.
"""

"""
What is the bias-variance tradeoff?
First, let’s understand what is bias and variance:

Bias refers to the difference between the actual values and the predicted values by 
the model. Low bias means the model has learned the pattern in the data and high bias means 
the model is unable to learn the patterns present in the data i.e the underfitting.
Variance refers to the change in accuracy of the model's prediction on which the model 
has not been trained. Low variance is a good case but high variance means that the 
performance of the training data and the validation data vary a lot.
If the bias is too low but the variance is too high then that case is known as 
overfitting. So, finding a balance between these two situations is known as the 
bias-variance trade-off.
"""

"""
What is the difference between one hot encoding and ordinal encoding?
One Hot encoding and ordinal encoding both are different methods to convert categorical 
features to numeric ones the difference is in the way they are implemented. In one hot 
encoding, we create a separate column for each category and add 0 or 1 as per the 
value corresponding to that row.

In ordinal encoding, we replace the categories with numbers from 0 to n-1 based on the 
order or rank where n is the number of unique categories present in the dataset. 
The main difference between one-hot encoding and ordinal encoding is that one-hot 
encoding results in a binary matrix representation of the data in the form of 0 and 1, 
it is used when there is no order or ranking between the dataset whereas ordinal encoding 
represents categories as ordinal values.
"""

"""
Explain some measures of similarity which are generally used in Machine learning.
Some of the most commonly used similarity measures are as follows:

Cosine Similarity: By considering the two vectors in n - dimension we evaluate the cosine 
of the angle between the two. The range of this similarity measure varies from [-1, 1] 
where the value 1 represents that the two vectors are highly similar and -1 represents 
that the two vectors are completely different from each other.

Euclidean or Manhattan Distance: These two values represent the distances between the two 
points in an n-dimensional plane. The only difference between the two is in the way the two 
are calculated.

Jaccard Similarity: It is also known as IoU or Intersection over union it is widely 
used in the field of object detection to evaluate the overlap between the predicted 
bounding box and the ground truth bounding box.
"""

"""
What is the difference between L1 and L2 regularization? What is their significance?
L1 regularization (Lasso regularization)adds the sum of the absolute values of the model's 
weights to the loss function. This penalty encourages sparsity in the model by pushing 
the weights of less important features to exactly zero. As a result, L1 regularization 
automatically performs feature selection, removing irrelevant or redundant features 
from the model, which can improve interpretability and reduce overfitting.

L2 regularization (Ridge regularization) in which we add the square of the weights to the 
loss function. In both of these regularization methods, weights are penalized but 
there is a subtle difference between the objective they help to achieve. 

In L2 regularization the weights are not penalized to 0 but they are near zero for 
irrelevant features. It is often used to prevent overfitting by shrinking the weights 
towards zero, especially when there are many features and the data is noisy.
"""

"""
What is a radial basis function?
RBF (radial basis function) is a real-valued function used in machine learning whose 
value only depends upon the input and fixed point called the center.

The formula for the radial basis function is as follows:

K(x, x') = exp( - ||x - x'||^2 / (2 * sigma^2) )

Machine learning systems frequently use the RBF function for a variety of functions, including:

RBF networks can be used to approximate complex functions. By training the network's weights 
to suit a set of input-output pairs, 
RBF networks can be used for unsupervised learning to locate data groups. By treating the RBF 
centers as cluster centers,
RBF networks can be used for classification tasks by training the network's weights to divide 
inputs into groups based on how far from the RBF nodes they are.
It is one of the very famous kernels which is generally used in the SVM algorithm to map 
low dimensional data to a higher dimensional plane so, we can determine a boundary that can 
separate the classes in different regions of those planes with as much margin as possible. 
"""

"""
Explain SMOTE method used to handle data imbalance.
In SMOTE, we synthesize new data points using the existing ones from the minority 
classes by using linear interpolation. The advantage of using this method is that the model 
does not get trained on the same data. But the disadvantage of using this method is that 
it adds undesired noise to the dataset and can lead to a negative effect on the model’s 
performance.
"""

"""
Which metric is more robust to outliers: MAE, MSE, or RMSE?
Out of the three metrics—Mean Absolute Error (MAE), Mean Squared Error (MSE), and 
Root Mean Squared Error (RMSE)—MAE is more robust to outliers.

The reason behind this is the way each metric handles error values:

MSE and RMSE both square the error values. When there are outliers, the error is typically 
large, and squaring it results in even larger error values. This causes outliers to 
disproportionately affect the overall error, leading to misleading results and potentially 
distorting the model’s performance.

MAE, on the other hand, takes the absolute value of the errors. Since it does not square 
the error terms, the influence of large errors (outliers) is linear rather than exponential, 
making MAE less sensitive to outliers.
"""

"""
How do you evaluate the effectiveness of a machine learning model in an imbalanced dataset 
scenario? What metrics would you use instead of accuracy?
We can use Precision, Recall, F1 score and ROC-AUC to evaluate the effectiveness of 
machine learning model in imbalanced dataset scenario. The best metric is F1 score as it 
combines both precision and recall into single metric that is important in imbalanced 
datasets where a high number of true negatives can skew accuracy. By focusing on both false 
positives and false negatives, the F1-score ensures that both the positive class detection 
and false positives are accounted for.

If the cost of false positives (Type I errors) and false negatives (Type II errors) is similar, 
F1-Score strikes a good balance.
It is especially useful when you need to prioritize performance in detecting the minority 
class (positive class).
However, if you are more concerned about false positives or false negatives specifically, 
you may opt for:

Precision (if false positives are more costly) or
Recall (if false negatives are more costly).
"""

"""
Explain some methods to handle missing values in that data.
Some of the methods to handle missing values are as follows:

Removing the rows with null values may lead to the loss of some important information.
Removing the column having null values if it has very less valuable information. it may 
lead to the loss of some important information.
Imputing null values with descriptive statistical measures like mean, mode, and median.
Using methods like KNN Imputer to impute the null values in a more sophisticated way.
"""