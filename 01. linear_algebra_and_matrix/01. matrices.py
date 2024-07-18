"""
1) Find sum of two matrices
a = [[1,2], [4,5]]
b = [[2,3], [6,7]]
"""
import numpy as np

a = np.array([[1, 2], [4, 5]])
b = np.array([[2, 3], [6, 7]])
res = np.add(a, b)
print(res)


"""
2) Subtract a from b
"""
import numpy as np

a = np.array([[2, 3], [6, 7]])
b = np.array([[1, 2], [4, 5]])
res = a - b
print(res)


"""
3) Mlutiple a and b
[a 	b] [i  j] [a*i+b*k 	a*j+b*i]
[c 	d] [k  l] [c*i+d*k  c*j+d*i]
"""
import numpy as np

a = np.array([[1, 2], [4, 5]])
b = np.array([[2, 3], [6, 7]])
res = np.dot(a, b)
print(res)