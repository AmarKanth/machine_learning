"""
t test :

The t-test is one of the most common hypothesis tests in statistics. 
The t-test determines either whether the sample mean and the mean of the population differ 
or if two sample means differ statistically.
"""

"""
1.one sample t-test
2.independent sample t-test
3.paired samples t-test
"""

"""
One-sample t-test : 
Is there a difference between a group and the population

t = (x̄ - μ₀) / (s / √n)

x̄   = sample mean
μ₀   = population mean
s    = sample standard deviation
n    = sample size
"""

"""
one tailed Test

Use Case:
As an example for the t-test for one sample, we examine whether an online statistics tutorial 
newly introduced at the university has an effect on the students' examination results.

The average score in the statistics test at a university has been 28 points for years. 
This semester a new online statistics tutorial was introduced. Now the course management 
would like to know whether the success of the studies has changed since the introduction of 
the statistics tutorial: Does the online statistics tutorial have a positive effect on 
exam results?

The population considered is all students who have written the statistics exam since the new 
statistics tutorial was introduced. The reference value to be compared is 28.
"""

import pandas as pd
import numpy as np

from scipy.stats import t

student = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
score = [28, 29, 35, 37, 32, 26, 37, 39, 22, 29, 36, 38]
data = list(zip(student, score))

df = pd.DataFrame(data, columns=["student", "score"])
df = df.astype({'student': 'int64', 'score': 'int64'})

alpha = 0.025
n = len(df)
dfree = n - 1

sample_mean = df['score'].mean()
mu_0 = 28
sem = df['score'].std(ddof=1) / np.sqrt(n)

t_value = (sample_mean-mu_0)/sem
t_critical = t.ppf(1 - alpha, dfree)
print((t_value, t_critical))

"""
If the calculated t value is below the critical t value, there is no significant 
difference between the sample and the population; if it is above the critical t value, 
there is a significant difference.
"""

"""
Interpret t-value
The t-value is calculated by dividing the measured difference by the scatter in the 
sample data. The larger the magnitude of t, the more this argues against the null 
hypothesis. If the calculated t-value is larger than the critical t-value, the null 
hypothesis is rejected.
"""

"""
Number of degrees of freedom - df
The number of degrees of freedom indicates how many values are allowed to vary freely. 
The degrees of freedom are therefore the number of independent individual pieces 
of information.
"""

"""
Null hypothesis H0
The mean value from the sample and the predefined value does not differ significantly.  
The online statistics tutorial has no significant effect on exam results.
"""

"""
Independent Samples t-test :
Is there a difference between two groups
"""

"""
Paired Samples t-test :
Is there a difference in a group between two points in time
"""