"""
np.reshape()
"""
import numpy as np
arr = np.arange(12)
reshaped = np.reshape(arr, (3, 4))
print(reshaped)

"""
np.ravel()
"""
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
flat = np.ravel(arr)
print(flat)

"""
flatten()
"""
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
flat = arr.flatten()
print(flat)

"""
astype()
"""
import numpy as np
arr = np.array([1.7, 2.9, 3.2])
int_arr = arr.astype(int)
print(int_arr)

"""
dtype
"""
import numpy as np
arr = np.array([1, 2, 3])
print(arr.dtype)

"""
np.vstack()
"""
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
result = np.vstack((a, b))
print(result)

"""
np.hstack()
"""
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
result = np.hstack((a, b))
print(result)

"""
np.concatenate()
"""
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
result = np.concatenate((a, b))
print(result)

"""
np.meshgrid()
"""
import numpy as np
x = np.array([1, 2, 3])
y = np.array([10, 20])
X, Y = np.meshgrid(x, y)
print("X:\n", X)
print("Y:\n", Y)
