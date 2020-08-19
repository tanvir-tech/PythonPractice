import numpy as np

arr2D =  np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]])
print(arr2D)

#sum
print("Sum of arr2D =",arr2D.sum())
#axis
print("Sum of axis ZERO =",arr2D.sum(axis=0))
print("Sum of axis ONE =",arr2D.sum(axis=1))
#sqrt
print("Sqrt =",np.sqrt(arr2D))
#standard deviation
print("standard deviation =",np.std(arr2D))






