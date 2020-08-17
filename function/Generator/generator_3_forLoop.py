def myGenerator(dict):                  # generator
    for x,y in dict.items():
        yield x,y

mydict = {1:"one",2:"tow",3:"three"}     # iterable

gen_object = myGenerator(mydict)         # generator object
print(gen_object)



for x in gen_object:                      # calling next(gen_object) by forloop
    print(x)

