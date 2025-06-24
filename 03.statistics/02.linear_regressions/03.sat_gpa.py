"""
We will create linear regression which predicts GPA based on the 
SAT score obtained
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

file_path = "data_science/03.statistics/02.linear_regressions/data/01.simple_linear_regression.csv"
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
std err shows the accuracy of prediction for each variable. The lower the 
standard error, the better the estimate.
"""

"""
1. There is hypothesis involved.
2. The null hypothesis of this test is H₀: β = 0, in other words is the coefficient 
equals to zero.
3. ŷ = 0 + 0.0017*x1 then line crosses the y axis at the origin.
4. if β₁ = 0, ŷ will be zero, so the variable will not be for the model.
5. P < 0.05 means that the variable is significant. Therefore co-efficient is most 
probably different from zero.
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
"""

"""
SST and SSR is equal, it means your regression model captures all the 
observed variability and is perfect.
"""