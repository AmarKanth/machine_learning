"""
OverFitting : Our training has focused on the particular training set so much, 
it has "missed the point".
UnderFitting : The model has not captured the underlying logic of the data.
"""
import numpy as np
from sklearn.model_selection import train_test_split

a = np.arange(1,101)
b = np.arange(501, 601)
a_train, a_test, b_train, b_test = train_test_split(a, b, test_size=0.2, random_state=365)
print(a_train)
print(a_test)
print("------------")
print(b_train)
print(b_test)