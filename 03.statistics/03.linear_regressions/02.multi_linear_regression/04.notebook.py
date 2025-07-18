import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

file_path = "data_science/03.statistics/03.linear_regressions/00.data/02.mlr.csv"
data = pd.read_csv(file_path)

x = data[["SAT", "Rand 1,2,3"]]
y = data["GPA"]

scaler = StandardScaler()
scaler.fit(x)
x_scaled = scaler.transform(x)

reg = LinearRegression()
reg.fit(x_scaled,y)

reg_summary = pd.DataFrame([["Bias"], ["SAT"], ["Rand 1,2,3"]], columns=["Features"])
reg_summary["Weights"] = reg.intercept_, reg.coef_[0], reg.coef_[1]
print(reg_summary)

new_data = pd.DataFrame(data=[[1700,2], [1800,1]], columns=["SAT","Rand 1,2,3"])
new_data_scaled = scaler.transform(new_data)
predictions = reg.predict(new_data_scaled)
print(predictions)

reg_simple = LinearRegression()
x_simple_matrix = x_scaled[:,0].reshape(-1,1)
reg_simple.fit(x_simple_matrix,y)
simple_predictions = reg_simple.predict(new_data_scaled[:,0].reshape(-1,1))
print(simple_predictions)