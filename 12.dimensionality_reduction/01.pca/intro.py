"""
PCA:
-It helps you to reduce the number of features in a dataset while keeping the most 
 important information.
-PCA is commonly used for data preprocessing for use with machine learning algorithms.
-It uses eigenvectors (directions) and eigenvalues (importance) from the covariance matrix.
"""

"""
How PCA works?
-Standardize the data
-Calculate covariance matrix
"""

"""
Why does PCA maximize the variance in the data?
-PCA aims to maximize the variance because variance represents how much information is 
 spread out in a given direction. 
-The higher the variance along a direction, the more information that direction holds 
 about the data. 

By focusing on the directions of highest variance, PCA helps us:
-Preserve information while reducing the dimensionality.
-Simplify the data by eliminating less important features(those with low variance)
"""