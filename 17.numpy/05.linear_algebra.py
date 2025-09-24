"""
np.dot()
"""
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.dot(a, b))

"""
np.linalg.inv(A)
"""
import numpy as np
A = np.array([[1, 2], [3, 4]])
A_inv = np.linalg.inv(A)
print(A_inv)

"""
np.eigvals()
"""
import numpy as np
A = np.array([[1, 2], [4, 3]])
eigvals = np.linalg.eigvals(A)
print(eigvals)

"""
np.linalg.det()
"""
import numpy as np
A = np.array([[1, 2], [3, 4]])
print(np.linalg.det(A))

"""
np.linalg.norm()
"""
import numpy as np
v = np.array([3, 4])
print(np.linalg.norm(v))
print(np.linalg.norm(v, 1))
print(np.linalg.norm(v, np.inf))

"""
np.linalg.qr()
"""
import numpy as np
A = np.array([[1, 2], [3, 4], [5, 6]])
Q, R = np.linalg.qr(A)
print("Q:\n", Q)
print("R:\n", R)
