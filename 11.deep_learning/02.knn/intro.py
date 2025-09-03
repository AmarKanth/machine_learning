"""
27. What is KNN Imputer and how does it work?
KNN Imputer imputes missing values in a dataset compared to traditional methods like using mean, median, or mode. It is based on the K-Nearest Neighbors (KNN) algorithm, which fills missing values by referencing the values of the nearest neighbors.

Here’s how it works:

Neighborhood-based Imputation: The KNN Imputer identifies the k nearest neighbors to the data point with the missing value, based on a distance metric (e.g., Euclidean distance).
Imputation Process: Once the nearest neighbors are found, the missing value is imputed (filled) using a statistical measure, such as the mean or median, of the values from these neighbors.
Distance Parameter: The k parameter is used to define how many neighbors to consider when imputing a missing value, and the distance metric controls how similarity is measured between data points.
"""

"""
31. What is the difference between k-means and the KNN algorithm?
K-means algorithm is one of the popular unsupervised machine learning algorithms which is used for clustering purposes. But, KNN is a model which is generally used for the classification task and is a supervised machine learning algorithm. The k-means algorithm helps us to label the data by forming clusters within the dataset.
"""

"""
41. Explain the concept of weighting in KNN? What are the different ways to assign weights, and how do they affect the model's predictions?
Weighting in KNN assigns different levels of importance to the neighbors based on their distance from the query point, influencing how each neighbor affects the model's predictions.

The weights can be assigned using:

Uniform Weighting: All neighbors have equal weight regardless of their distance.
Distance Weighting: Weights are inversely proportional to the distance, giving closer neighbors more influence.
User-defined Weights: Weights are assigned based on domain knowledge or specific data characteristics.
Effect on Model's Prediction:

Uniform Weighting: Simple but may not perform well with noisy data or varied distances.
Distance Weighting: Improves accuracy by emphasizing closer neighbors, useful for irregular class boundaries but sensitive to anomalies.
User-defined Weights: Optimizes performance when specific insights about the dataset are applied, though less generalizable.
"""
