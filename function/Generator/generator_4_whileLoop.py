def myGenerator(n):                 # generator
    while n<=3:
        yield n
        n+=1


obj = myGenerator(1)                # generator object
print(obj)


for x in obj:                       # calling next(obj) by forloop
    print(x)


