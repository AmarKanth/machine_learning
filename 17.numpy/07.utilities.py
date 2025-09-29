"""
np.array_equal()
"""
import numpy as np
a = np.array([1, 2, 3])
b = np.array([1, 2, 3])
print(np.array_equal(a, b))

"""
np.diag()
"""
import numpy as np
v = np.array([1, 2, 3])
D = np.diag(v)
print(D)
