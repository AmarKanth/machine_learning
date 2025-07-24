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

file_path = "data_science/03.statistics/04.logistic_regression/00.data/03.test_dataset.csv"
test = pd.read_csv(file_path)

test["Admitted"] = test["Admitted"].map({"Yes": 1, "No": 0})
test["Gender"] = test["Gender"].map({"Female": 1, "Male": 0})

test_actual = test["Admitted"]
test_data = test.drop(["Admitted"], axis=1)
test_data = sm.add_constant(test_data)

def confusion_matrix(data, actual_values, model):
    pred_values = model.predict(data)
    bins = np.array([0,0.5,1])
    cm = np.histogram2d(actual_values, pred_values, bins=bins)[0]
    accuracy = (cm[0,0]+cm[1,1])/cm.sum()
    return cm, accuracy

cm = confusion_matrix(test_data, test_actual, result_log)
cm_df = pd.DataFrame(cm[0])
cm_df.columns = ["Predicted 0", "Predicted 1"]
cm_df = cm_df.rename(index={0: "Actual 0", 1: "Actual 1"})
print(cm_df)