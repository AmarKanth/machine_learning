"""
np.sort()
"""
import numpy as np
arr = np.array([3, 1, 4, 1, 5, 9])
print(np.sort(arr))

"""
np.argsort()
"""
import numpy as np
arr = np.array([3, 1, 4, 1, 5, 9])
idx = np.argsort(arr)
print(idx)

"""
np.unique()
"""
import numpy as np
arr = np.array([1, 2, 2, 3, 1, 4])
print(np.unique(arr))

"""
How to filter the elements in array
"""
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
condition = (arr > 25)
result = arr[condition]
print(result)