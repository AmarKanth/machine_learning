"""
Create linear regression which predicts GPA based on the SAT score obtained
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

file_path = "data_science/03.statistics/03.linear_regressions/00.data/01.slr.csv"
df = pd.read_csv(file_path)

y = df["GPA"]
x = df["SAT"]

x_with_const = sm.add_constant(x)
model = sm.OLS(y, x_with_const).fit()

plt.scatter(x, y, label="Data")
b0, b1 = model.params
y_hat = b0 + b1 * x

plt.plot(x, y_hat, lw=4, c="orange", label="Regression Line")
plt.xlabel("SAT", fontsize=20)
plt.ylabel("GPA", fontsize=20)
plt.legend()
plt.title("SAT vs GPA Regression")
plt.show()

"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                    GPA   R-squared:                       0.406
Model:                            OLS   Adj. R-squared:                  0.399
Method:                 Least Squares   F-statistic:                     56.05
Date:                Tue, 24 Jun 2025   Prob (F-statistic):           7.20e-11
Time:                        14:37:16   Log-Likelihood:                 12.672
No. Observations:                  84   AIC:                            -21.34
Df Residuals:                      82   BIC:                            -16.48
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.2750      0.409      0.673      0.503      -0.538       1.088
SAT            0.0017      0.000      7.487      0.000       0.001       0.002
==============================================================================
Omnibus:                       12.839   Durbin-Watson:                   0.950
Prob(Omnibus):                  0.002   Jarque-Bera (JB):               16.155
Skew:                          -0.722   Prob(JB):                     0.000310
Kurtosis:                       4.590   Cond. No.                     3.29e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 3.29e+04. This might indicate that there are
strong multicollinearity or other numerical problems.
"""

"""
Hypothesis

For the SAT coefficient:
-----------------------
Null Hypothesis(H₀): The SAT score has no effect on GPA(i.e. the coefficient=0).
Alternative Hypothesis(H₁): The SAT score does have an effect on GPA(i.e. the coefficient≠0).
p-value for SAT is extremely small (p < 0.05), we reject the null hypothesis.
This means there is statistically significant evidence that SAT score does affect GPA.

For the Intercept (const):
-------------------------
Null Hypothesis: The intercept is zero (no GPA when SAT = 0).
p-value = 0.503, which is not significant (p > 0.05).
This tells us the intercept isn't statistically significant — but in practical terms, 
this is often less important than the slope (SAT’s effect on GPA).
"""
