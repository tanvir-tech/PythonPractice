# filter_Object = filter( filter_function , iterable)

# only "true" will be enlisted
#

tuple = (1,2,3,4,5,6)               # list is not callable

def evenCheck_Function(n):
    if n%2==0:
        return True

even_list = list(filter(evenCheck_Function, tuple))              # filterring and typeCasting
print(even_list)


# with lambda function
odd_list = list(filter(lambda a:(a%2!=0),tuple))
print(odd_list)

