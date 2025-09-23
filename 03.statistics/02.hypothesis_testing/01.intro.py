"""
H₀ : Null Hypothesis
H₁ : Alternative Hypothesis
α  : Alpha
"""

"""
What is Null Hypothesis?
- If there is no effect, no difference, or no relationship between variables.
- Example: The new product performs the same as the old one.
- We either reject the null hypothesis or fail to reject it — we never accept it as absolutely true.
- If the test results are unclear, we say: 'We fail to reject, due to insufficient evidence.'
"""

"""
What is Alternative Hypothesis?
- If there is an effect, a difference, or a relationship — it's what we're trying to prove.
- Example: The new product performs better than the old one.
- If we reject H₀, we have sufficient evidence to support H₁, but we do not 'accept' H₁ as 
  absolutely true.
"""

"""
Significance Level:
The significance level(denoted by α, "alpha") is a threshold used in hypothesis testing 
to determine whether to reject the null hypothesis.
"""

"""
Rejection Region:
- The rejection region is also called the critical region in hypothesis testing.
- If your test statistic(z, t, etc.) falls into that region, you reject H₀
- If it falls outside that region, you fail to reject H₀
"""

"""
One-Sided Test:
- A one-sided test(also called a one-tailed test) is a hypothesis test. 
- Where the alternative hypothesis(H₁) states that the effect or difference exists in only one 
  direction.
"""

"""
Explain about type 1 and type 2 error?

Type I Error:
When you reject the null hypothesis(H₀) even though it is actually true.

Type II Error:
When you fail to reject the null hypothesis(H₀) even though it is actually false.

Summary of Type I and Type II Errors in Hypothesis Testing:

| Error Type | What Happened          | Real Situation | Your Conclusion   | Also Called        |
|------------|------------------------|----------------|-------------------|--------------------|
| Type I     | Rejected H₀            | H₀ is true     | False positive    | False alarm        |
| Type II    | Failed to reject H₀    | H₀ is false    | False negative    | Missed detection   |

Notes:
- Type I error (α): Incorrectly rejecting a true null hypothesis.
- Type II error (β): Failing to reject a false null hypothesis.
"""