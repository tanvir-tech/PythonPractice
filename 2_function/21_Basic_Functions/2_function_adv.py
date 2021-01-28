def mainfunc(n):
    def func1():
        return "I am Function_01"
    def func2():
        return "I am Function_02"

    if n==1:
        return func1()           #returning function1..........................(python_Special)
    elif n==2:
        return func2()           #returning function2..........................(python_Special)
    else:
        print("Function not available")


f1 = mainfunc(1)           # Assigning RETURNED function in variable..........................(python_Special)
f2 = mainfunc(2)

print(f1)              # Calling function with variable
print(f2)
