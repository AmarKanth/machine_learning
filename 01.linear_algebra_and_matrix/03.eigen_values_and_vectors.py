"""
Eigenvectors are special vectors that, when a matrix(or transformation) is applied to them, 
don’t change their direction. 
They might stretch, shrink, or stay the same size, but their direction remains unchanged.
"""

"""
Eigenvalues are the scaling factors that tell you how much the eigenvector is stretched or 
shrunk during the transformation. Is also knows as scalar value.
"""

"""
Av = λv

A is the matrix
v is associated eigenvector
λ is scaler eigenvalue
"""

"""
Find the eigenvalues and the eigenvectors for the matrix 
A = [[1, 5],
     [2, 4]]
"""
import numpy as np

A = np.array([[1, 5],
              [2, 4]])

eigenvalues, eigenvectors = np.linalg.eig(A)
for i, val in enumerate(eigenvalues, start=1):
    print(f"λ{i} = {val:.0f}")

for i in range(len(eigenvalues)):
    v = eigenvectors[:, i]
    print(f"v{i+1} = {v}")

for i in range(len(eigenvalues)):
    lam = eigenvalues[i]
    v = eigenvectors[:, i]
    left = A @ v
    right = lam * v
    print(f"\nCheck for λ = {lam:.0f}:")
    print("A v =", left)
    print("λ v =", right)
    print("Verification:", np.allclose(left, right))