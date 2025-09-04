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
1) get_label_indices(labels)
Goal: Know which rows belong to each class.
How: Iterate with enumerate(labels) and append indices into a defaultdict(list).
Why: Later steps (priors/likelihoods) need to look at class-specific subsets.

2) get_prior(label_indices)
Goal: Estimate the prior P(class).
How: Count samples per class and divide by total.
Why: Priors capture class imbalance and are multiplied into the posterior.

3) get_likelihood(features, label_indices, smoothing=1)
Setting: Bernoulli NB (binary features 0/1).
Goal: For each class 'c' and feature 'j', estimates p_jc = P(x_j = 1 | c)
How: Count 1s for feature j among rows of class c
Laplace smoothing (add-s):
p̂_jc = (#ones + s) / (#class_samples + 2s)
2s because feature can be 0 or 1.
Why: Avoid zero probabilities and get stable estimates.

4) get_posterior(X, prior, likelihood)
Goal: Compute P(c∣x) for each test sample x.
How:
Start with prior[c].

For each feature j:
If x_j = 1, multiply by  p_jc
If x_j = 0, multiply by  1-p_jc

Normalize so the probabilities across classes sum to 1.
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