"""
t test :
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

Decision rules for one-tailed and two-tailed t-tests using p-values.
┌──────────────────────┬────────────────────┬────────────────────┬────────────────────────┬─────────────────────────────┐
│ Test Type            │ H₀                 │ H₁                 │ Compare p-value to α   │ Reject H₀ if...             │
├──────────────────────┼────────────────────┼────────────────────┼────────────────────────┼─────────────────────────────┤
│ One-Tailed (Left)    │ μ ≥ μ₀             │ μ < μ₀             │ p < α                  │ t is in the left tail       │
│ One-Tailed (Right)   │ μ ≤ μ₀             │ μ > μ₀             │ p < α                  │ t is in the right tail      │
│ Two-Tailed           │ μ = μ₀             │ μ ≠ μ₀             │ p < α                  │ t is in either tail         │
└──────────────────────┴────────────────────┴────────────────────┴────────────────────────┴─────────────────────────────┘

Notes:
- μ₀ is the hypothesized population mean.
- t is the test statistic computed from the sample.
- α is the significance level (commonly 0.05).
- In two-tailed tests, p-value is doubled: p = 2 × P(T ≥ |t|).
"""
