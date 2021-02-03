import numpy as np
import statistics as st

myTuple = (1,22,2,3,4,55,5,60,6,7,76,80,88,9,0,10,1,43,38,7,7,62,100,99,50,20,30,11,7,4,7,10)
print("Dataset length =",len(myTuple))
print("From these dataset",myTuple)

mean = np.mean(myTuple)
print("Mean is =",mean)


median = np.median(myTuple)
print("Median is =",median)


mode = st.mode(myTuple)
print("Mode is = ",mode)

