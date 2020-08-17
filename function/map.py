#map_object = map( apply_function , iterable)

tuple = (1,2,3,4,5,6)
#list is not callable



def square(n):
    return n*n

square_values = list(map(square,tuple))
print(square_values)



#lambda expression
qube_values = list(map(lambda n:n*n*n , tuple))
print(qube_values)

