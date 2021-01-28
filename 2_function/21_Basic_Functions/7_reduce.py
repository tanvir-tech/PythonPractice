# Single_vlaue = reduce( reduce_function , iterable)
# 1,2
# 3,3
# 6,4


from functools import reduce

myList=[1,2,3,4,5,6]

def sumFunction(a, b):
    return a+b

sum_result = reduce(sumFunction, myList)
print(sum_result)



#lambda expression
sum_value = reduce(lambda a,b:a+b , myList)
print(sum_value)


