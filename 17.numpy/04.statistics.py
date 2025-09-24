"""
np.mean()
"""
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(np.mean(arr))

"""
np.var()
"""
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(np.var(arr))

"""
np.min()
"""
import numpy as np
arr = np.array([10, 3, 25, -5, 7])
print(np.min(arr))  

"""
np.max()
"""
import numpy as np
arr = np.array([10, 3, 25, -5, 7])
print(np.max(arr))

"""
np.mod()
"""
import numpy as np
a = np.array([10, 20, 30])
b = np.array([3, 7, 9])
print(np.mod(a, b))

"""
np.round()
"""
import numpy as np
arr = np.array([1.2, 2.5, 3.7, 4.5])
print(np.round(arr))

"""
np.isclose()
"""
import numpy as np
a = 0.3 + 0.6
b = 0.9
print(a == b)
print(np.isclose(a, b))

"""
np.isnan()
"""
import numpy as np
arr = np.array([1.0, np.nan, 2.5, np.nan])
print(np.isnan(arr))
