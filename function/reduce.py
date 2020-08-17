from functools import reduce

# Single_vlaue = reduce( reduce_function , iterable)

list=[1,2,3,4,5,6]

def sum(a,b):
    return a+b

sum_result = reduce(sum,list)
print(sum_result)



#lambda expression
sum_value = reduce(lambda a,b:a+b , list)
print(sum_value)
