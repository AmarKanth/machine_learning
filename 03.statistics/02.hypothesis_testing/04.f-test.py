"""
F Test :

Null Hypothesis
H₀ : β₁ = β₂ = ⋯ = βₖ = 0
High F-value and low p-value (typically < 0.05)
F > F-Critical and p < 0.05

Alternative Hypothesis
H₁ : At least one βⱼ ≠ 0
Low F-value and high p-value
F < F-Critical and p >= 0.05
"""

"""
βⱼ ≠ 0 means its not symmetric
F-test in regression = one-tailed test which means it only consider right tail
"""

"""
F = (𝑆𝑆𝑅 / 𝑘) ÷ (𝑆𝑆𝐸 / (𝑛 − 𝑘 − 1))

SSR : Regression Sum of Squares (explained variance)
SSE : Error Sum of Squares (unexplained variance)
n 	: Number of observations
k 	: Number of predictors (excluding intercept)
"""