import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

file_path = "data_science/03.statistics/03.linear_regressions/00.data/01.slr.csv"
data = pd.read_csv(file_path)

x = data["SAT"]
y = data["GPA"]

x_matrix = x.values.reshape(-1,1)
reg = LinearRegression()
reg.fit(x_matrix,y)
print("Intercept:", reg.intercept_)
print("Coefficient:", reg.coef_[0])

r_squared = reg.score(x_matrix,y)
print("R Squared:", r_squared)

predicted_gpa = reg.predict([[1700]])
print("Predicted GPA:", predicted_gpa[0])

plt.scatter(x,y)
yhat = reg.coef_*x_matrix + reg.intercept_
fig = plt.plot(x, yhat, lw=4, c="orange", label="regression line")
plt.xlabel("SAT", fontsize=20)
plt.ylabel("GPA", fontsize=20)
plt.show()