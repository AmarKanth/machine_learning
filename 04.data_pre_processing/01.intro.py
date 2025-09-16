"""
What is feature scaling?
It involves transforming numerical features into a "standard" scale, often leading to 
better model performance.

Methods for feature scaling
1.Min-Max Scaling
2.Standardization
3.Robust Scaling

Algorithms that benefit from feature scaling
1.k-Nearest Neighbors(KNN)
2.k-Means Clustering
3.Logistic Regression
"""


"""
Min-Max Scaling:
x' = (x - x_min) / (x_max - x_min)

-It is also called normalization.
-It brings all the features to a certain scale or range of values.
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
x' = (X − Q₁(X)) / (Q₃(X) − Q₁(X))
Q₁(X) = first quartile  
Q₃(X) = third quartile
"""
from sklearn.preprocessing import RobustScaler
robust_scaler = RobustScaler()
X_robust = robust_scaler.fit_transform(X)


"""
How do you handle missing values in a dataset using Scikit-Learn?

Mean, Median, Median:
Fills in with the mean, median, or mode of the non-missing values in the column.

Constant:
Assigns a fixed value to all missing entries.

KNN:
Uses the k-Nearest Neighbors algorithm to determine an appropriate value based on other 
instances known feature values.
"""
import numpy as np
from sklearn.impute import SimpleImputer

X = np.array([[1, 2], [np.nan, 3], [7, 6]])
imp_mean = SimpleImputer()
X_mean = imp_mean.fit_transform(X)
print(X_mean)


"""
How do you encode categorical variables using Scikit-Learn?
1.OneHotEncoder
2.OrdinalEncoder
3.LabelBinarizer
"""


"""
OneHotEncoder:
In one hot encoding, we create a separate column for each category and add 0 or 1 as per 
the value corresponding to that row.
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
In ordinal encoding, we replace the categories with numbers from 0 to n-1 based on the 
order or rank where n is the number of unique categories present in the dataset.
"""


"""
LabelBinarizer: 
A simpler version of OneHotEncoder designed for binary(two-class) categories.
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
Polynomial features 
Power transformations 
Binning
"""


"""
What is feature engineering? How does it affect the model’s performance? 
-Feature engineering refers to developing some new features by using existing features.
-Sometimes there is a very subtle mathematical relation between some features which if 
 explored properly then the new features can be developed using those mathematical 
 operations.
-Also, there are times when multiple pieces of information are clubbed and provided 
 as a single data column.
"""


"""
Correlation:
Correlation is a statistical measure that shows how strongly two variables are related 
to each other — in other words, how much one changes when the other changes.
"""


"""
What is data leakage and how can we identify it?
-If there is a high correlation between the target variable and the input features 
 then this situation is referred to as data leakage.
-This is because when we train our model with that highly correlated feature then the model gets 
 most of the target variable's information and show artificially high accuracy during 
 training and validation.
-But in real-world predictions(where the leakage feature is not available), performance will 
 drop badly
"""


"""
What is the difference between upsampling and downsampling?
In upsampling method, we increase the number of samples in the minority class by 
randomly selecting some points from the minority class and adding them to the dataset 
repeat this process till the dataset gets balanced for each class.

But, here is a disadvantage the training accuracy becomes high as in each epoch model 
trained more than once in each epoch but the same high accuracy is not observed in 
the validation accuracy. 

In downsampling, we decrease the number of samples in the majority class by selecting 
some random number of points that are equal to the number of data points in the minority 
class so that the distribution becomes balanced.

In this case, we have to suffer from data loss which may lead to the loss of some 
critical information as well. 
"""


"""
Explain SMOTE method used to handle data imbalance.
In SMOTE, we synthesize new data points using the existing ones from the minority 
classes by using linear interpolation.

The advantage of using this method is that the model does not get trained on the same data. 

But the disadvantage of using this method is that it adds undesired noise to the dataset and 
can lead to a negative effect on the model’s performance.
"""