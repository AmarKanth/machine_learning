"""
x + y = 5
2x – y = 1

Substitute into equation 2:
2x – (5 – x) = 1
3x – 5 = 1
3x = 6
x = 2

Substitute back to find y:
y = 5 – 2 = 3
Answer: (2, 3)

It represents the system of equations in matrix form Ax=b.
Here A is coefficient
b is constant

Let's convert them to matrix form
x + y = 5
2x - y = 1
"""
import numpy as np

A = np.array([[1, 1], [2, -1]])
b = np.array([5, 1])
solution = np.linalg.solve(A, b)
x, y = solution
print((x, y))