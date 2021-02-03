import numpy as np

myTuple = (1,22,2,3,4,55,5,60,6,7,76,80,88,9,0,10,1,43,38,7,7,62,100,99,50,20,30,11,7,4,7,10)
print("Dataset length =",len(myTuple))
print("From these dataset",myTuple)


variance = np.var(myTuple)
print("Variance is =",variance)



standard_Dev = np.std(myTuple)
print("Standard deviation is =",standard_Dev)