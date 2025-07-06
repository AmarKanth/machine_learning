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
β₀ = 0.2750
β₁ = 0.0017

ŷ = 0.2750 + 0.0017*x1
GPA = 0.2750 + 0.0017*SAT
"""

"""
1. Causal relation is that the higher your SAT score, the higher your GPA.
2. Rverse causal realtion is that the higher your GPA, the more likely it is that you 
had a high SAT score.
3. β₀ and β₁ are the coefficients. β₁ is the coefficient in front of the independent 
variable, and it measures the effect of SAT scores on GPA.
4. β₀ is the minimum GPA.
5. ε is error of estimation, the error is the actual difference between the real 
gpa and the gpa regression predicted.
"""

"""
std err : shows the accuracy of prediction for each variable. The lower the 
standard error, the better the estimate.
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

"""
Sum of squares total : It measures the total variability of the dataset
SST = Σ(yᵢ - ȳ)²
yᵢ = observed dependent value
ȳ  = mean of y value

Sum of squares regression :
SSR = Σ(ŷᵢ - ȳ)²
ŷᵢ = predicted values from the model
ȳ  = mean of actual y values

Sum of squares error :
SSE = Σ(yᵢ - ŷᵢ)²
yᵢ = actual observed values
ŷᵢ = predicted values from the model

SST and SSR is equal, it means your regression model captures all the 
observed variability and is perfect.
SST = SSR + SSE
"""

"""
OLS Ordinary Least Squares
It is most common method to estimate the linear regression equation.
Least squares stands for the minimum squares error or SSE.
Lower error results in a better explanatory power of the regression model.
This method aims to find the line which minimizes the sum of th squared errors.

Other methods performing the regression line
1. Generalized least squares
2. Maximum likelihood estimation
3. Bayesian regression
4. Kernel regression
5. Gaussian process regeression
"""

"""
R² = SSR / SST

It measures how much of the total variability is explained by our model

R² = 0 means your regression line explains none of the variability of the data
R² = 1 means your model explains the entire variability of data

Unfortunately, regressions explaining the entire variability are rare.
What you will usually observe is values ranging from 0.2 to 0.9.
The more factors you include in regression, higher the R².
"""