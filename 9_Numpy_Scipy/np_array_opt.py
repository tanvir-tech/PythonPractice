import numpy as np

arr2D =  np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]])
print(arr2D)

print("shape is ",arr2D.shape)
# reshape
arr2D = arr2D.reshape(5,2)
print(arr2D)


# linespace(start, end, how_many)
lineSpace_ndArray = np.linspace(1,3,10)
print("lineSpace :",lineSpace_ndArray)
