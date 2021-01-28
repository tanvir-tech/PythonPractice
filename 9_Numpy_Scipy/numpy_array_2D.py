import numpy as np

arr2D = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]])
print("full-array =")
print(arr2D)

print(arr2D[1, 3])         #array[ row, column ]
print(arr2D[1, :])         #full-row
print(arr2D[:, 3])         #full-column

# [ start-from : end-before ]
print(arr2D[1, 1:4])
# [ start-from : end-before : step-size ]
print(arr2D[0, 1:4:2])






