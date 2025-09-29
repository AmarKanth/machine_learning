"""
- Choose the number K of neighbors
- Take the k nearest neighbors of the new data point, according to the euclidean distance
- Among these k neighbors, count the number of data points in the category
- Assign the new data point to the category where you counted the most neighbors
"""

"""
Explain the concept of weighting in KNN? What are the different ways to assign 
weights, and how do they affect the model's predictions?

Weighting in KNN assigns different levels of importance to the neighbors based on their 
distance from the query point, influencing how each neighbor affects the model's predictions.

The weights can be assigned using:

Uniform Weighting: 
- All neighbors have equal weight regardless of their distance.

Distance Weighting: 
- Weights are inversely proportional to the distance, giving closer neighbors more influence.

User-defined Weights: 
- Weights are assigned based on domain knowledge or specific data characteristics.

Effect on Model's Prediction:
- Uniform Weighting: Simple but may not perform well with noisy data or varied distances.

Distance Weighting: 
- Improves accuracy by emphasizing closer neighbors, useful for irregular 
  class boundaries but sensitive to anomalies.

User-defined Weights: 
- Optimizes performance when specific insights about the dataset are 
  applied, though less generalizable.
"""
