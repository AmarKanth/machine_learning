"""
Gaussian RBF Kernel

K(x, l_i) = exp( - ||x - l_i||^2 / (2 * sigma^2) )

- x : input vector
- l_i : landmark (or support vector)
- sigma : kernel width parameter (spread of the Gaussian)
"""

"""
Sigmoid Kernel

K(x, y) = tanh(alpha * (x^T y) + c)

- x : input vector
- y : input vector
- alpha : scaling parameter (slope of the sigmoid)
- c : offset parameter (intercept)
"""

"""
Polynomial Kernel

K(x, y) = (x^T y + c)^d

- x : input vector
- y : input vector
- d : degree of the polynomial
- c : offset parameter (also called coef0)
"""

"""
What is a radial basis function?
RBF (radial basis function) is a real-valued function used in machine learning whose 
value only depends upon the input and fixed point called the center.

The formula for the radial basis function is as follows:

K(x, x') = exp( - ||x - x'||^2 / (2 * sigma^2) )

Machine learning systems frequently use the RBF function for a variety of functions, including:

RBF networks can be used to approximate complex functions. By training the network's weights 
to suit a set of input-output pairs, 
RBF networks can be used for unsupervised learning to locate data groups. By treating the RBF 
centers as cluster centers,
RBF networks can be used for classification tasks by training the network's weights to divide 
inputs into groups based on how far from the RBF nodes they are.
It is one of the very famous kernels which is generally used in the SVM algorithm to map 
low dimensional data to a higher dimensional plane so, we can determine a boundary that can 
separate the classes in different regions of those planes with as much margin as possible. 
"""