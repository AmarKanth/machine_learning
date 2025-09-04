"""
It tries to find the best boundary known as hyperplane that separates different classes in 
the data. 
It is useful when you want to do binary classification like spam vs. not spam or cat vs. dog.
"""

"""
Hyperplane : 
The hyperplane is halfway between these boundaries(support vectors).
Boundaries are closest data points from each class.
"""

"""
Margin : 
The distance between the hyperplane and the support vectors.
"""

"""
Explain the working principle of SVM.
A data set that is not separable in different classes in one plane may be separable 
in another plane. This is exactly the idea behind the SVMin this a low dimensional 
data is mapped to high dimensional data so, that it becomes separable in the 
different classes. A hyperplane is determined after mapping the data into a higher 
dimension which can separate the data into categories.

SVM model can even learn non-linear boundaries with the objective that there should be 
as much margin as possible between the categories in which the data has been categorized. 
To perform this mapping different types of kernels are used like radial basis kernel, 
gaussian kernel, polynomial kernel, and many others.
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