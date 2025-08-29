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