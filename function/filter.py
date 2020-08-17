# filter_object = filter( filter_function , iterable)

tuple = (1,2,3,4,5,6)
#list is not callable


def even(n):
    if n%2==0:
        return True

even_list = list(filter(even,tuple))
print(even_list)


# with lambda function
odd_list = list(filter(lambda a:(a%2!=0),tuple))
print(odd_list)

