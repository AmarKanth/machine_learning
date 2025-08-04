import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

file_path = "data_science/03.statistics/04.logistic_regression/00.data/02.binary_predictors.csv"
raw_data = pd.read_csv(file_path)

data = raw_data.copy()
data["Admitted"] = data["Admitted"].map({"Yes": 1, "No": 0})
data["Gender"] = data["Gender"].map({"Female": 1, "Male": 0})

y = data["Admitted"]
x1 = data[["SAT", "Gender"]]

x = sm.add_constant(x1)
reg_log = sm.Logit(y,x)
result_log = reg_log.fit()
# print(result_log.summary())

"""
                           Logit Regression Results                           
==============================================================================
Dep. Variable:               Admitted   No. Observations:                  168
Model:                          Logit   Df Residuals:                      166
Method:                           MLE   Df Model:                            1
Date:                Thu, 24 Jul 2025   Pseudo R-squ.:                  0.1659
Time:                        11:11:48   Log-Likelihood:                -96.140
converged:                       True   LL-Null:                       -115.26
Covariance Type:            nonrobust   LLR p-value:                 6.283e-10
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const         -0.6436      0.222     -2.901      0.004      -1.078      -0.209
Gender         2.0786      0.363      5.727      0.000       1.367       2.790
==============================================================================
"""

"""
Odds interpretation
"""
np.set_printoptions(formatter={"float": lambda x: "{0:0.2f}".format(x)})
# print(result_log.predict())
# print(np.array(data["Admitted"]))
# print(result_log.pred_table())

cm_df = pd.DataFrame(result_log.pred_table())
# cm_df.columns = ["Predicted 0", "Predicted 1"]
# cm_df = cm_df.rename(index={0: "Actual 0", 1: "Actual 1"})
# print(cm_df)

cm = np.array(cm_df)
accuracy_train = (cm[0,0]+cm[1,1])/cm.sum()
print(accuracy_train)

"""
Overfitting : Our training has focused on the particular training set 
so much, it has "missed the points"
Underfitting : The model has not captured the underlying logic of the data
"""