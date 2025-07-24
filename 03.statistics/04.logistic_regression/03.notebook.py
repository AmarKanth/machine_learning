import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

file_path = "data_science/03.statistics/04.logistic_regression/00.data/01.admittance.csv"
raw_data = pd.read_csv(file_path)

data = raw_data.copy()
data["Admitted"] = data["Admitted"].map({"Yes":1, "No":0})

y = data["Admitted"]
x1 = data["SAT"]

x = sm.add_constant(x1)
reg_log = sm.Logit(y,x)
results_log = reg_log.fit()

print(results_log.summary())

"""
                           Logit Regression Results                           
==============================================================================
Dep. Variable:               Admitted   No. Observations:                  168
Model:                          Logit   Df Residuals:                      166
Method:                           MLE   Df Model:                            1
Date:                Wed, 23 Jul 2025   Pseudo R-squ.:                  0.7992
Time:                        21:16:47   Log-Likelihood:                -23.145
converged:                       True   LL-Null:                       -115.26
Covariance Type:            nonrobust   LLR p-value:                 5.805e-42
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const        -69.9128     15.737     -4.443      0.000    -100.756     -39.070
SAT            0.0420      0.009      4.454      0.000       0.024       0.060
==============================================================================

Possibly complete quasi-separation: A fraction 0.27 of observations can be
perfectly predicted. This might indicate that there is complete
quasi-separation. In this case some parameters will not be identified.
"""

"""
MLE (Maximum likelihood estimation)
A function which estimates how likely it is that the model at hand 
describes the real underlying relationship of the variables.
The bigger the likelihood function, the higher the probability 
that our model is correct.
"""

"""
LLR (Log likelihood Ratio)
measures if our model is statistically different from LL-null, 
a.k.a a useless model
"""

"""
Pseudo R-Squared
"""

"""
Interpreting the odds ratio
"""