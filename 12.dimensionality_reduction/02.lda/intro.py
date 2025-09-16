"""
What is Linear Discriminant Analysis?
-LDA is dimensionality reduction technique.
-It is supervised because of the relation to the dependent variable.
-It uses target variables also for dimensionality reduction.
-It is commonly used for classification problems.

The LDA mainly works on two objectives:
1.Maximize the distance between the means of the two classes.
2.Minimize the variation within each class.
"""

"""
How it works
-Compute the d-dimensional mean vectors for the different classes from the dataset
-Compute the scatter matrices(in-between-class and within-class scatter matrix)
-Compute eigenvectors(e1, e2, e3 ...,ed) and corresponding eigenvalues(λ1, λ2, λ3 ...,λd) 
 for the scatter matrices
-Sort the eigenvectors by decreasing eigenvalues and choose k eigenvectors with the 
 largest eigenvalues to form a d*k dimensional matrix W(where every column represents an 
 eigenvector)
-Use this d*k eigenvector matrix to transform the samples onto the new subspace. This can be 
 summarized by the matrix multiplication: y = X*W
 where x is a n*d dimensional matrix representing the n samples,
 y are the transformed n*k dimensional samples in the new subspace
"""

"""
How can we visualize high-dimensional data in 2-d?
-One of the most common and effective methods is by using the t-SNE algorithm which is a 
 short form for t-Distributed Stochastic Neighbor Embedding. 
-This algorithm uses some non-linear complex methods to reduce the dimensionality of the 
 given data.
-We can also use PCA or LDA to convert n-dimensional data to 2-dimensional so,that 
 we can plot it to get visuals for better analysis. 
-But the difference between the PCA and t-SNE is that the former tries to preserve the 
 variance of the dataset but the t-SNE tries to preserve the local similarities in 
 the dataset.
"""
