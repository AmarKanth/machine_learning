"""
Cluster Analysis :
Cluster analysis is a multivariate statistical technique that groups observations 
on the basis some of their features or variables they are described by.
"""

"""
-After you’ve chosen K (number of clusters), k-means tries to find K centroids.
-A centroid is just the “center point” of a cluster. It’s not necessarily one of the 
 data points—it’s the mean position of all the points in that cluster.
"""

"""
Classification vs Clustering
-Classification means predicting an output category, given input data.
-Grouping data points together based on similarities among them and difference 
 from others.
"""

"""
Elbow Method
-Minimizing the distance between points in a cluster
-Maximizing the distance between clusters
"""

"""
Similar to SSC, SSR and SSE, WCSS is a measure developed within the ANOVA framework
"""

"""
Manhattan Distance: 
It is calculated as the sum of absolute differences between the coordinates of 
two points along each dimension. 
MD = |x1 - x2| + |y1 - y2|

Euclidean Distance:
It is calculated as the square root of the sum of squared differences between 
the coordinates of two points along each dimension.
ED = sqrt((x1 - x2)^2 + (y1 - y2)^2)

Chebyshev Distance:
CD = max(|x1 - x2|, |y1 - y2|)
"""

"""
How to choose an optimal number of clusters?
Elbow Method: 
Plot the explained variance or within-cluster sum of squares (WCSS) against 
the number of clusters. The "elbow" point, where the curve starts to flatten, indicates the 
optimal number of clusters.

Silhouette Score: 
Measures how similar each point is to its own cluster compared to 
other clusters. A higher silhouette score indicates better-defined clusters. The optimal 
number of clusters is the one with the highest average silhouette score.

Gap Statistic: 
Compares the clustering result with a random clustering of the same data. 
A larger gap between the real and random clustering suggests a more appropriate 
number of clusters.
"""

"""
What is the difference between the k-means and k-means++ algorithms?
The only difference between the two is in the way centroids are initialized. In the 
k-means algorithm, the centroids are initialized randomly from the given points. 
There is a drawback in this method that sometimes this random initialization leads to 
non-optimized clusters due to maybe initialization of two clusters close to each other. 

To overcome this problem k-means++ algorithm was formed. In k-means++, 
the first centroid is selected randomly from the data points. The selection of subsequent 
centroids is based on their separation from the initial centroids. The probability of a 
point being selected as the next centroid is proportional to the squared distance between 
the point and the closest centroid that has already been selected. This guarantees that 
the centroids are evenly spread apart and lowers the possibility of convergence to 
less-than-ideal clusters. This helps the algorithm reach the global minima instead of 
getting stuck at some local minima.
"""

"""
What are the assumptions behind the K-means algorithm? How do these assumptions affect 
the results?
The assumptions of K-Means algorithm include:

Cluster Shape: 
Assumes clusters are spherical and of similar size, affecting how well 
it handles non-spherical groups.

Scale of Features: 
Assumes features are on similar scales; different ranges can distort 
the distance calculation.

Clusters are Balanced: 
Assumes clusters have a roughly equal number of observations, which can 
bias results against smaller clusters.

Similar Density: 
Assumes all clusters have similar density, impacting the algorithm's 
effectiveness with clusters of varying densities.
If these assumptions are not met, the model will perform poorly making difficult to process 
and select clustering techniques that align with the data characteristics.
"""

"""
Can you explain the concept of convergence in K-means? What conditions must be met for 
K-means to converge?

Convergence in K-means occurs when the cluster centroids stabilize, and the assignment of 
data points to clusters no longer changes. This happens when the algorithm has minimized 
the sum of squared distances between points and their corresponding centroids.

Conditions for K-means to Converge:

Proper Initialization: 
The initial placement of centroids significantly impacts convergence. 
Techniques like k-means++ help ensure a better start.

Data Characteristics: 
The algorithm converges more effectively if the data naturally clusters 
into well-separated groups. Overlapping or complex cluster shapes can hinder convergence.

Correct Number of Clusters(k): 
Choosing the right number of clusters is critical; too many or 
too few can lead to slow convergence or convergence to suboptimal solutions.

Algorithm Parameters: 
Setting a maximum number of iterations and a small tolerance for 
centroid change helps prevent infinite loops and determines when the algorithm should stop 
if centroids move minimally between iterations.
"""
