"""
H₀ : Null Hypothesis
H₁ : Alternative Hypothesis
α  : Alpha
"""

"""
Null Hypothesis :
A default assumption that there is no effect, no difference, or no relationship 
between variables.

Example: The new product performs the same as the old one.
"""

"""
Alternative Hypothesis :
A statement that there is an effect, a difference, or a relationship — it's 
what you're trying to prove.

Example: The new product performs better than the old one.
"""

"""
Important Notes :
- In hypothesis testing, we either reject the null hypothesis or fail to reject it — we 
  never accept it as absolutely true.
- If the test results are unclear, we say:
  “We fail to reject the null hypothesis due to insufficient evidence.”
- If we reject H₀, we have sufficient evidence to support H₁, but we do not 
  ‘accept’ H₁ as absolutely true.
"""

"""
Significance Level :
The significance level (denoted by α, "alpha") is a threshold used in hypothesis 
testing to determine whether to reject the null hypothesis.
"""

"""
Rejection Region :
The rejection region (also called the critical region) in hypothesis testing is 
the range of values for the test statistic (like a z-score or t-score) that leads to 
rejection of the null hypothesis (H₀).
"""

"""
One-Sided Test :
A one-sided test (also called a one-tailed test) is a hypothesis test where the 
alternative hypothesis (H₁) states that the effect or difference exists in only one 
direction.
"""

"""
Type I Error:
A Type I error occurs in hypothesis testing when you reject the null hypothesis (H₀) 
even though it is actually true.

Type II Error:
A Type II error occurs when you fail to reject the null hypothesis (H₀) even 
though it is actually false.

Summary of Type I and Type II Errors in Hypothesis Testing:

| Error Type | What Happened          | Real Situation | Your Conclusion   | Also Called        |
|------------|------------------------|----------------|-------------------|--------------------|
| Type I     | Rejected H₀            | H₀ is true     | False positive    | False alarm        |
| Type II    | Failed to reject H₀    | H₀ is false    | False negative    | Missed detection   |

Notes:
- Type I error (α): Incorrectly rejecting a true null hypothesis.
- Type II error (β): Failing to reject a false null hypothesis.
"""

"""
What is the null hypothesis in linear regression problem?
In linear regression, the null hypothesis id that there is no relationship between the 
independent variable(s) and the dependent variable. This is formally represented as 
H₀ : β₁ = 0, where β₁ is the coefficient of the independent variable.

Essentially, the null hypothesis suggests that the predictor variable does not contribute 
to predicting the outcome. For instance, if the null hypothesis states that the slope of 
the regression line is zero, then a student's score in an English class would not be a 
useful predictor of their overall grade-point average.

The alternative hypothesis, denoted as βⱼ ≠ 0, proposes that changes in the independent 
variable are indeed associated with changes in the dependent variable, indicating a meaningful 
relationship.
"""