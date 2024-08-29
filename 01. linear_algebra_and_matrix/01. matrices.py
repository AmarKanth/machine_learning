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
[a 	b] [i  j] [a*i+b*k 	a*j+b*l]
[c 	d] [k  l] [c*i+d*k  c*j+d*l]
"""
import numpy as np
a = np.array([[1, 2], [4, 5]])
b = np.array([[2, 3], [6, 7]])
res = np.dot(a, b)
print(res)


"""
4) Inverse Of the matrix
A = [['a', 'b'],
     ['c', 'd']]
A_inverse = (1/det(A)) * [['d', '-b'],
                          ['-c', 'a']]
det(A) = ad - bc
"""
import numpy as np 
arr = np.array([[1, 2], [5, 6]]) 
res = np.linalg.inv(arr)
print(res)

"""
5) Transpose the given array.
[[1,2,3],
 [4,5,6]]
"""
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
res = np.transpose(arr)
print(res)

"""
6) Normal : square root of sum of squares of matrix elements.
Trace : sum of diagonal elements
"""
from math import sqrt
mat = [[7, 8, 9],
       [6, 1, 2],
       [5, 4, 3]]
normal = sqrt(7*7+8*8+9*9+6*6+1*1+2*2+5*5+4*4+3*3)
trace = 7+1+3
print(normal)
print(trace)
