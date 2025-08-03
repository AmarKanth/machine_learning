import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import f_regression
from sklearn.preprocessing import StandardScaler

file_path = "data_science/03.statistics/03.linear_regressions/00.data/02.mlr.csv"
data = pd.read_csv(file_path)

x = data[["SAT", "Rand 1,2,3"]]
y = data["GPA"]

reg = LinearRegression()
reg.fit(x,y)

print("Intercept:", reg.intercept_)
print("Coefficient:", reg.coef_)

r2 = reg.score(x,y)
n = x.shape[0]
p = x.shape[1]
adj_r2 = 1-(1-r2)*(n-1)/(n-p-1)
print("R2:", r2)
print("Adjusted R2:", adj_r2)

"""
e⁻¹¹ = 1/10¹¹
0.000 represents the p value of SAT
0.676 represents the p value of Rand 1,2,3
Why p value(or field) of Rand 1,2,3 not useful
"""
f_reg = f_regression(x,y)
f_stastistics = f_reg[0]
p_values = f_reg[1].round(3)
print("F Statistics:", f_stastistics)
print("P Values:", p_values)

reg_summary = pd.DataFrame(data=x.columns.values, columns=["Features"])
reg_summary["Coefficients"] = reg.coef_
reg_summary["p-values"] = p_values
print(reg_summary)