"""
Naive Bayes is a classification algorithm that uses probability to predict which 
category a data point belongs to.
"""

"""
𝑃(𝐴|𝐵) = (𝑃(𝐵|𝐴) × 𝑃(𝐴))/𝑃(𝐵)

𝑃(𝐴) 	: Prior Probability
𝑃(𝐵) 	: Marginal Liklihood
𝑃(𝐵|𝐴) 	: Liklihood
𝑃(𝐴|𝐵) 	: Posterior Probability
"""

"""
What is the difference between the content-based and collaborative filtering algorithms 
of recommendation systems?
In a content-based recommendation system, similarities in the content and services are 
evaluated, and then by using these similarity measures from past data we recommend products 
to the user. But on the other hand in collaborative filtering, we recommend content and 
services based on the preferences of similar users.

For example, if one user has taken A and B services in past and a new user has taken 
service A then service A will be recommended to him based on the other user's preferences.
"""

"""
How does the independence assumption affect the accuracy of a Naive Bayes classifier?
Naive Bayes classifier operates under the assumption that all features in the dataset 
are independent of each other given the class label. This assumption simplifies the 
computation of the classifier's probability model, as it allows the conditional probability 
of the class given multiple features to be calculated as the product of the 
individual probabilities for each feature.

Affect of accuracy on a Naive Bayes classifier:

Strengths in High-Dimensional Data: In practice, the independence assumption can sometimes 
lead to good performance, especially in high-dimensional settings like text classification, 
despite the interdependencies among features. This is because the errors in probability 
estimates may cancel out across the large number of features.

Limitations Due to Feature Dependency: The accuracy of Naive Bayes can be adversely affected 
when features are not independent, particularly if the dependencies between features are 
strong and critical to predicting the class. The model may underperform in such scenarios 
because it fails to capture the interactions between features.

Generalization Capability: The simplistic nature of the independence assumption often 
allows Naive Bayes to perform well on smaller datasets or in cases where data for 
training is limited, as it does not require as complex a model as other classifiers.
"""