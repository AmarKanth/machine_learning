"""
Data Preprocessing
------------------
1. Import data
2. Clean the data
3. Split into training and test sets

Modeling
---------
1. Build the model
2. Train the model
3. Make Predictions

Evaluation
----------
1. Calculate the performance metrics
2. Make a verdict
"""

"""
What is feature scaling?

Normalization :
x' = (x - x_min) / (x_max - x_min)

Standardization :
x' = (x - μ) / σ

μ : Mean of the feature
σ : Standard deviation of the feature
"""

"""
SimpleImputer
ColumnTransformer
OneHotEncoder
LabelEncoder
StandardScaler

imputing 
label encoding 
"""

"""
Label encoding
One-hot encoding
Scaling
Feature engineering 
Polynomial features 
Power transformations 
Binning 
Name two feature engineering approaches.
"""

"""
What is z-standardization?

Z-standardization is a statistical procedure used to make data points from different 
datasets comparable. 
In this procedure, each data point is converted into a z-score. 
A z-score indicates how many standard deviations a data point is from the mean of the dataset.
"""

"""
Why do we perform normalization?
To achieve stable and fast training of the model we use normalization techniques to bring 
all the features to a certain scale or range of values. If we do not perform normalization 
then there are chances that the gradient will not converge to the global or local minima and 
end up oscillating back and forth.
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
What is the difference between one hot encoding and ordinal encoding?
One Hot encoding and ordinal encoding both are different methods to convert categorical 
features to numeric ones the difference is in the way they are implemented. In one hot encoding, 
we create a separate column for each category and add 0 or 1 as per the value corresponding 
to that row.

In ordinal encoding, we replace the categories with numbers from 0 to n-1 based on the 
order or rank where n is the number of unique categories present in the dataset. The main 
difference between one-hot encoding and ordinal encoding is that one-hot encoding 
results in a binary matrix representation of the data in the form of 0 and 1, it is 
used when there is no order or ranking between the dataset whereas ordinal encoding 
represents categories as ordinal values.
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