def func(n):
    def func1():
        return "I am Function ONE"
    def func2():
        return "I am Function TWO"

    if n==1:
        return func1()           #returning function1
    elif n==2:
        return func2()           #returning function2



f1 = func(1)           # Assigning function in variable
f2 = func(2)

print(f1)              # Calling function with variable
print(f2)
