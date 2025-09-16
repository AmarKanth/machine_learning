"""
SVM finds the best boundary known as hyperplane that separates different classes in 
the data.
"""

"""
In 2D space, this boundary is a line
In 3D space, it’s a plane
In higher dimensions, it’s called a hyperplane(surface)
"""

"""
Hyperplane:
The hyperplane is halfway between these boundaries(support vectors).
Boundaries are closest data points from each class.
"""

"""
Support Vectors:
The closest data points to the hyperplane, crucial for determining the hyperplane and 
margin in SVM.
"""

"""
Margin:
- Distance between the hyperplane and the nearest data points from each class.
- The data points that lie closest to the boundary are called support vectors.
"""

"""
Kernel:
A function that maps data to a higher-dimensional space enabling SVM to handle non-linearly 
separable data.
"""

"""
Hard Margin:
A maximum-margin hyperplane that perfectly separates the data without misclassifications.
"""

"""
Soft Margin: 
Allows some misclassifications by introducing slack variables, balancing margin maximization 
and misclassification penalties when data is not perfectly separable.
"""

"""
C: A regularization term balancing margin maximization and misclassification penalties. 
A higher C value forces stricter penalty for misclassifications.
"""

"""
Outlier:
An outlier is a data point that is significantly different from the other data points in 
the dataset.
"""

"""
Hinge Loss:
A loss function penalizing misclassified points or margin violations and is combined with 
regularization in SVM.
"""

"""
Can SVMs be used for both classification and regression tasks?
Yes, Support Vector Machines (SVMs) can be used for both classification and regression. 
For classification, SVMs work by finding a hyperplane that separates different classes in 
the data with the largest gap possible.

For regression, which involves predicting a continuous number, SVMs are adapted into a 
version called Support Vector Regression (SVR). SVR tries to fit as many data points 
as possible within a certain range of the predicted line, allowing some errors but 
penalizing those that are too large. This makes it useful for predicting values in 
situations where the data shows complex patterns.

To learn how to implement Support Vector Regression, you can refer to: 
Support Vector Regression (SVR) using Linear and Non-Linear Kernels in Scikit Learn
"""

"""
How the One-Class SVM algorithm works for anomaly detection?
One-Class SVM is an unsupervised anomaly detection algorithm. It is often used 
when only normal data is available. The model learns a decision boundary around normal data 
points using a kernel, typically an RBF, to map the data into a higher-dimensional 
space. The algorithm identifies support vectors—data points closest to the boundary—and 
any new data point outside this boundary is flagged as an anomaly. Key parameters like 'nu' 
control the fraction of outliers allowed, while the kernel defines the boundary shape.
"""

"""
Explain the concept of "concept drift" in anomaly detection.
Concept driftrefers to the change in the underlying distribution or patterns in the data 
over time, which can make previously normal data points appear as anomalies. 
In anomaly detection, this is particularly challenging because a model trained on old 
data may not recognize new, evolving patterns as part of the normal data distribution. 
Concept drift can occur suddenly or gradually and needs to be monitored closely. 
To address this, models can be adapted through periodic retraining with new data or by 
using adaptive anomaly detection algorithms.
"""