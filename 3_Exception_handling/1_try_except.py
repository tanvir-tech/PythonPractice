a,b = map(int,input("Enter 2 Integer with space :").split())
div = 0

try:
    div = a/b
    print("Division is ", div)
except :
    print("Can not divide by Zero")


