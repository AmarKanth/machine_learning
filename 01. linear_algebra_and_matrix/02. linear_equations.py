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


"""
Solve the 3×3 system:
x + y + z = 6
2x – y + z = 4
x + 2y – z = 3
"""
import numpy as np

# Coefficient matrix
A = np.array([
    [1, 1, 1],
    [2, -1, 1],
    [1, 2, -1]
])

# Constant terms
B = np.array([6, 4, 3])

solution = np.linalg.solve(A, B)
print(solution)


"""
Determine the nature of the system:
2x + 3y = 5
4x + 6y = 11
"""
import numpy as np

A = np.array([[4, 6], [4, 6]])
B = np.array([10, 11])

try:
    solution = np.linalg.solve(A, B)
    print("Solution:", solution)
except np.linalg.LinAlgError:
    print("The system is inconsistent (no solution).")


"""
Solve using Cramer’s Rule:
3x + 2y = 14
x + y = 6
"""
import numpy as np

A = np.array([[3, 2], [1, 1]])
B = np.array([14, 6])

det_A = np.linalg.det(A)

A_x = np.array([[14, 2], [6, 1]])
A_y = np.array([[3, 14], [1, 6]])

det_A_x = np.linalg.det(A_x)
det_A_y = np.linalg.det(A_y)

x = det_A_x / det_A
y = det_A_y / det_A

print((x, y))