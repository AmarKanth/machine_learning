"""
Cluster Analysis:
Cluster analysis is a method of grouping things(like people, objects, or data points) 
so that observations in the same group are more similar to each other than to items 
in other groups.
"""

"""
1.Specifying k:
- The algorithm needs to know how many clusters to generate as an end result.

2.Initializing centroids:
- The algorithm begins by picking k random points from the data. These points act as the 
  starting centers of the clusters.

3.Assigning clusters:
- Each data point is compared to the k centers(centroids). A data point is placed into the 
  group of the closest center. This way, every point ends up in one of the k clusters.
- Note that closeness is usually measured by the Euclidean distance. Other
  metrics can also be used, such as the Manhattan distance and Chebyshev
  distance

4.Updating centroids:
- After grouping the points, we find the new center of each cluster by taking the average 
  position of all points in that group. These new centers become the updated centroids.
- This is why the algorithm is called k-means.

5.Repeating steps 3 and 4:
- We keep moving points to their closest centers(step 3) and recalculating the new centers(step 4) 
  again and again. This continues until the centers stop changing much.
"""

"""
Manhattan Distance: 
MD = |x1 - x2| + |y1 - y2|

It is calculated as the sum of absolute differences between the coordinates of 
two points along each dimension.
"""

"""
Euclidean Distance:
ED = sqrt((x1 - x2)^2 + (y1 - y2)^2)

It is calculated as the square root of the sum of squared differences between 
the coordinates of two points along each dimension.
"""

"""
Chebyshev Distance:
CD = max(|x1 - x2|, |y1 - y2|)
"""

"""
Cosine Similarity: 
- By considering the two vectors in n - dimension we evaluate the cosine of the angle 
  between the two. 
- The range of this similarity measure varies from [-1, 1] where the value 1 represents 
  that the two vectors are highly similar and -1 represents that the two vectors are 
  completely different from each other.
"""

"""
Jaccard Similarity: 
- It is also known as IoU or Intersection over union it is widely 
  used in the field of object detection to evaluate the overlap between the predicted 
  bounding box and the ground truth bounding box.
"""

"""
Classification vs Clustering:
- Classification means predicting an output category, given input data.
- Grouping data points together based on similarities among them and difference 
  from others.
"""

"""
Similar to SSC, SSR and SSE, WCSS is a measure developed within the ANOVA framework
"""

"""
Elbow Method:
- Minimizing the distance between points in a cluster
- Maximizing the distance between clusters
- Plot the explained variance or within-cluster sum of squares (WCSS) against the number of clusters. 
- The "elbow" point, where the curve starts to flatten, indicates the optimal number of clusters.
"""

"""
Silhouette Score:
- Measures how similar each point is to its own cluster compared to other clusters. 
  A higher silhouette score indicates better-defined clusters. 
- The optimal number of clusters is the one with the highest average silhouette score.
"""

"""
Gap Statistic:
- Compares the clustering result with a random clustering of the same data. 
- A larger gap between the real and random clustering suggests a more appropriate number of clusters.
"""

"""
k-means vs KNN:
- K-means algorithm is one of the popular unsupervised machine learning algorithms which is 
  used for clustering purposes. 
- But, KNN is a model which is generally used for the classification task and is a supervised 
  machine learning algorithm. The k-means algorithm helps us to label the data by forming 
  clusters within the dataset.
"""

"""
K Means:
- The only difference between the two is in the way centroids are initialized.
- In the k-means algorithm, the centroids are initialized randomly from the given points.
- There is a drawback in this method that sometimes this random initialization leads to 
  non-optimized clusters due to maybe initialization of two clusters close to each other.

Assumptions:
Cluster Shape: 
- Assumes clusters are spherical and of similar size, affecting how well 
  it handles non-spherical groups.

Scale of Features: 
- Assumes features are on similar scales; different ranges can distort 
  the distance calculation.

Clusters are Balanced: 
- Assumes clusters have a roughly equal number of observations, which can 
  bias results against smaller clusters.

Similar Density: 
- Assumes all clusters have similar density, impacting the algorithm's 
  effectiveness with clusters of varying densities.
- If these assumptions are not met, the model will perform poorly making difficult to process 
  and select clustering techniques that align with the data characteristics.

Conditions for K-means to Converge:
- Convergence in K-means occurs when the cluster centroids stabilize, and the assignment of 
  data points to clusters no longer changes. This happens when the algorithm has minimized 
  the sum of squared distances between points and their corresponding centroids.

Conditions for K-means to Converge:
Proper Initialization: 
- The initial placement of centroids significantly impacts convergence. 
- Techniques like k-means++ help ensure a better start.

Data Characteristics: 
- The algorithm converges more effectively if the data naturally clusters 
  into well-separated groups. Overlapping or complex cluster shapes can hinder convergence.

Correct Number of Clusters(k): 
- Choosing the right number of clusters is critical; too many or 
  too few can lead to slow convergence or convergence to suboptimal solutions.

Algorithm Parameters: 
- Setting a maximum number of iterations and a small tolerance for 
  centroid change helps prevent infinite loops and determines when the algorithm should stop 
- if centroids move minimally between iterations.
"""

"""
K Means++:
- To overcome this problem k-means++ algorithm was formed. In k-means++, the first centroid is 
  selected randomly from the data points.
- The selection of subsequent centroids is based on their separation from the initial centroids.
- The probability of a point being selected as the next centroid is proportional to the squared 
  distance between the point and the closest centroid that has already been selected.
- This guarantees that the centroids are evenly spread apart and lowers the possibility of 
  convergence to less-than-ideal clusters.
- This helps the algorithm reach the global minima instead of getting stuck at some local minima.
"""