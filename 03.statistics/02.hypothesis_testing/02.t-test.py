"""
t test 
It follows the students distribution.
"""

"""
1. One-sample t-test

t = (x̄ - μ₀) / (s / √n)

x̄   = sample mean
μ₀   = population mean
s    = sample standard deviation
n    = sample size
"""

import pandas as pd
import numpy as np

from scipy.stats import t

student = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
score = [28, 29, 35, 37, 32, 26, 37, 39, 22, 29, 36, 38]
data = list(zip(student, score))

df = pd.DataFrame(data, columns=["student", "score"])
df = df.astype({'student': 'int64', 'score': 'int64'})

alpha = 0.05
n = len(df)
dfree = n - 1

sample_mean = df['score'].mean()
mu_0 = 28
sem = df['score'].std(ddof=1) / np.sqrt(n)

t_value = (sample_mean-mu_0)/sem
t_critical = t.ppf(1 - alpha, dfree)
print((t_value, t_critical))