# function defination

def mathfunction(*numbers):
    sum = 0
    for n in numbers:
        sum = sum+n
    return sum



#function call
result = mathfunction(5,4,8,7)
print(result)


