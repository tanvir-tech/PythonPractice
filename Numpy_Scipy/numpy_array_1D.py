import numpy as np

arr1D = np.array([2, 3, 4, 5, 6], dtype='int16')
print(arr1D)


print("DataType        : ", arr1D.dtype)
print("full array size : ", arr1D.size)
print("each item size in byte : ", arr1D.itemsize)
print("full array size in byte: ", arr1D.nbytes)

print("Dimension : ", arr1D.ndim)
print("Array shape : ", arr1D.shape)




