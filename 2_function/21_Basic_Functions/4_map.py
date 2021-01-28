#  map_Object = map( apply_function , iterable)

myTuple = (1,2,3,4,5,6)
#.......................................list is not callable!



def square_Func(n):
    return n*n

map_obj=map(square_Func, myTuple)                 # mapping with function and tuple
print(map_obj)                                    # map_Object

square_values = list(map_obj)                     # typeCasting map_Object to list
print(square_values)



#lambda expression
qube_values = list(map(lambda n:n*n*n, myTuple))
print(qube_values)

