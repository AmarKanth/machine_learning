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

# plt.scatter(x1, y, color='C0')
# plt.xlabel("SAT", fontsize=20)
# plt.ylabel("Admitted", fontsize=20)
# plt.show()

"""
Why the data is non linear
"""
x = sm.add_constant(x1)
reg_lin = sm.OLS(y,x)
results_lin = reg_lin.fit()

# plt.scatter(x1, y, color='C0')
# y_hat = x1 * results_lin.params["SAT"] + results_lin.params["const"]

# plt.plot(x1, y_hat, lw=2.5, color='C8')
# plt.xlabel("SAT", fontsize=20)
# plt.ylabel("Admitted", fontsize=20)
# plt.show()

"""
Logistic Regression Curve
"""
reg_log = sm.Logit(y, x)
results_log = reg_log.fit()

def f(x, b0, b1):
    return np.exp(b0 + x * b1) / (1 + np.exp(b0 + x * b1))

f_sorted = np.sort(f(x1, results_log.params["const"], results_log.params["SAT"]))
x_sorted = np.sort(np.array(x1))

plt.scatter(x1, y, color='C0')
plt.xlabel("SAT", fontsize=20)
plt.ylabel("Admitted", fontsize=20)
plt.plot(x_sorted, f_sorted, color='C8')
plt.show()