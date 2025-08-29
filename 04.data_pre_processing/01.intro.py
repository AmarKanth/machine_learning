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