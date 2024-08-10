"""
Get the maximum value from given matrix 
'[64, 1; 12, 3]'
"""
import numpy as np
          
mx1 = np.matrix('[64, 1; 12, 3]')       
res = mx1.max()
print(res)


"""
Get the minimum value from given matrix
'[64, 1; 12, 3]'
"""
import numpy as np
          
mx1 = np.matrix('[64, 1; 12, 3]')          
res = mx1.min()
print(res)


"""
Fetch the element at index 2 from given matrix
'[4, 1, 12, 3, 4, 6, 7]'
"""
import numpy as np
              
mx1 = np.matrix('[4, 1, 12, 3, 4, 6, 7]')
res = mx1.take(2)    
print(res)


"""
Sum of all elements in matrix
'[4, 1; 12, 3]'
"""
import numpy as np

mx1 = np.matrix('[4, 1; 12, 3]')
res = mx1.sum()   
print(res)


"""
Sum of diagnal elements
[[55, 25, 15],
 [30, 44, 02],
 [11, 45, 77]]
"""
import numpy as np

np1 = np.array([[55, 25, 15],
                [30, 44, 2],
                [11, 45, 77]])  

trace = np.trace(np1)  
print(trace)

array= np.array([[1,2,3],[4,5,6],[7,8,9]])

sum = 0
for i in range(len(myList2D)):
    sum += myList2D[i][i]
print(sum)


"""
Subtract Matrices
[[1, 2], [3, 4]], [[4, 5], [6, 7]]
"""
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[4, 5], [6, 7]])

res = np.subtract(A, B)
print(res)


"""
count the number of occurances of elements
[10, 20, 5, 10, 8, 20, 8, 9]
"""
import numpy as np

np1 = np.array([10, 20, 5, 10, 8, 20, 8, 9])
unique, frequency = np.unique(np1, return_counts = True)

print(unique)  
print(frequency)


"""
Write a program to rotate 90 degrees n*n matrix
[1,2,3], [4,5,6], [7,8,9]]
"""
import numpy as np

myArray = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(myArray)

def rotateMatrix(matrix):
    n = len(matrix)
    for layer in range(n//2):
        first = layer
        last = n - layer - 1
        for rotation in range(first, last):
            top = matrix[layer][rotation]
            matrix[layer][rotation] = matrix[-rotation-1][layer]
            matrix[-rotation-1][layer] = matrix[-layer-1][-rotation-1]
            matrix[-layer-1][-rotation-1] = matrix[rotation][-layer-1]
            matrix[rotation][-layer-1] = top
    return matrix

res = rotateMatrix(myArray)
print(res)
